"""Per-flow attempts from an e2e job's log, for every harness the bench reads.

Each parser takes the job's cleaned log lines and returns a list of
{"name", "attempts", "fails", "passed"}: how many times the flow ran in this
job, how many of those runs failed, and whether its last run passed. A flow that a later job runs again (React
Native's retry_1/retry_2 jobs) is joined up per run in retries.py.

Formats:
- maestro-runner: a line per flow as it runs ("✓ name 12.3s"), and with
  --retries a final listing whose line for a retried flow ends "(passed on
  attempt N)" or "(failed all N attempts)". Several runner invocations in one
  job (a harness that runs the failed flows again) each count.
- Maestro, React Native's scripts: "Executing flow: path[ (attempt N)]" then
  "[Passed] name" or "[Failed] name".
- agent-device (React Navigation upstream): "✓ Name 12.3s" per flow, and for a
  retried one an indented "✓ Name after N attempts".
- Expo's harness: "Custom e2e flows attempt N of M: a.yaml, b.yaml" per
  round, with the Maestro "[Passed]/[Failed]" lines (upstream) or
  maestro-runner lines (ours) inside it.
"""
import re

VERSION = 2  # bump when parsing changes; older entries are read again

MR_BANNER = re.compile(r"maestro-runner \d+\.\d+\.\d+(?:\.\d+)? - by DeviceLab")
MR_FLOW = re.compile(r"^(✓|✗) (.+?) (?:\d+h )?(?:\d+m )?[\d.]+m?s"
                     r"(?: \((?:passed on attempt (\d+)|failed all (\d+) attempts)\))?\s*$")


def maestro_runner(lines):
    flows = []
    chunks, cur = [], []
    for l in lines:
        if MR_BANNER.search(l) and cur:
            chunks.append(cur)
            cur = []
        cur.append(l)
    chunks.append(cur)
    for chunk in chunks:
        last = {}
        order = []
        for l in chunk:
            m = MR_FLOW.match(l)
            if not m:
                continue
            name = m.group(2)
            if name not in last:
                order.append(name)
            passed = m.group(1) == "✓"
            attempts = int(m.group(3) or m.group(4) or 1)
            # The final listing repeats every flow; its line is the last one.
            last[name] = dict(name=name, attempts=attempts, fails=attempts - 1 if passed else attempts,
                              passed=passed)
        flows += [last[n] for n in order]
    return _join_reruns(flows)


def _join_reruns(flows):
    """A flow run again by a later invocation in the same job (a failed flow
    re-run by the harness) is one flow with the attempts added up."""
    out = {}
    order = []
    for f in flows:
        prev = out.get(f["name"])
        if prev and not prev["passed"]:
            prev["attempts"] += f["attempts"]
            prev["fails"] += f["fails"]
            prev["passed"] = f["passed"]
        elif prev:
            # The same name passed already: a different flow of that name.
            key = f["name"] + "#" + str(len(order))
            out[key] = dict(f)
            order.append(key)
        else:
            out[f["name"]] = dict(f)
            order.append(f["name"])
    return [out[k] for k in order]


MAESTRO_EXEC = re.compile(r"Executing flow: (\S+?)(?:\.ya?ml)?(?: \(attempt (\d+)\))?\s*$")
MAESTRO_RESULT = re.compile(r"^\[(Passed|Failed)\] (\S+)")


def maestro(lines):
    """Maestro's per-flow lines; attempts counted from repeats of a flow."""
    flows = {}
    order = []
    for l in lines:
        m = MAESTRO_RESULT.match(l)
        if not m:
            continue
        name = m.group(2)
        f = flows.get(name)
        if f is None:
            f = flows[name] = dict(name=name, attempts=0, fails=0, passed=False)
            order.append(name)
        f["attempts"] += 1
        f["passed"] = m.group(1) == "Passed"
        f["fails"] += 0 if f["passed"] else 1
    return [flows[n] for n in order]


AD_FLOW = re.compile(r"^(✓|✗) (.+?) [\d.]+s\s*$")
AD_RETRIED = re.compile(r"^\s+(✓|✗) (.+?) after (\d+) attempts")


def agent_device(lines):
    flows = {}
    order = []
    for l in lines:
        m = AD_FLOW.match(l)
        if m and not l.startswith(("✓ Lockfile",)):
            name = m.group(2)
            if name not in flows:
                order.append(name)
            if name in flows:  # the summary line after its "after N attempts" detail
                flows[name]["passed"] = m.group(1) == "✓"
            else:
                ok = m.group(1) == "✓"
                flows[name] = dict(name=name, attempts=1, fails=0 if ok else 1, passed=ok)
            continue
        m = AD_RETRIED.match(l)
        if m:
            name = m.group(2)
            if name not in flows:
                order.append(name)
            ok, n = m.group(1) == "✓", int(m.group(3))
            flows[name] = dict(name=name, attempts=n, fails=n - 1 if ok else n, passed=ok)
    return [flows[n] for n in order]


EXPO_ROUND = re.compile(r"(?:Custom e2e flows|Native modules test suite) attempt (\d+) of \d+(?:: (.+))?$")


def expo(lines):
    """Expo's harness runs rounds: "Custom e2e flows attempt N of M: a.yaml,
    ..." and "Native modules test suite attempt N of M". A flow counts one
    attempt per round it runs in (the tools print a flow more than once); a
    whole-step rerun starts again at attempt 1 and adds to the count."""
    flows = {}
    order = []
    seen = set()  # flows counted in the current round
    failed = set()  # flows whose run failed in the current round
    for l in lines:
        m = EXPO_ROUND.search(l)
        if m:
            seen, failed = set(), set()
            for p in (m.group(2) or "").split(","):
                name = re.sub(r"\.ya?ml$", "", p.strip().split("/")[-1])
                if name:
                    _expo_attempt(flows, order, seen, name)
            continue
        m = MAESTRO_RESULT.match(l) or MR_FLOW.match(l)
        if m:
            name = m.group(2)
            _expo_attempt(flows, order, seen, name)
            ok = m.group(1) in ("Passed", "✓")
            flows[name]["passed"] = ok
            if not ok and name not in failed:
                failed.add(name)
                flows[name]["fails"] += 1
    return [flows[n] for n in order]


def _expo_attempt(flows, order, seen, name):
    if name not in flows:
        flows[name] = dict(name=name, attempts=0, fails=0, passed=False)
        order.append(name)
    if name not in seen:
        seen.add(name)
        flows[name]["attempts"] += 1


PARSERS = {"maestro-runner": maestro_runner, "rn-maestro": maestro, "agent-device": agent_device}


def parse(harness, side, lines):
    if harness == "expo":
        return expo(lines)
    return PARSERS[harness](lines)
