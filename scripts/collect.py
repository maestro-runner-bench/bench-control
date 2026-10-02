#!/usr/bin/env python3
"""Collect e2e results from the bench forks (maestro-runner) and from upstream
(Maestro / agent-device) into results/jobs.jsonl, then write results/SUMMARY.md.

One record per e2e job: its duration, conclusion, how many flows failed on
their first attempt, how many failed in the end, and job-level retry rounds.
Records are keyed by job id, so a job is collected once. Standard library only.

Env: GH_TOKEN (any token that can read public Actions logs), RUNS_PER_SOURCE
(default 15), RESULTS_DIR (default results).
"""
import json
import os
import re
import statistics
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

API = "https://api.github.com"
TOKEN = os.environ.get("GH_TOKEN", "")
RUNS = int(os.environ.get("RUNS_PER_SOURCE", "15"))
RESULTS = os.environ.get("RESULTS_DIR", "results")

# Each source: repo, workflow file, branch, side ("ours"/"upstream"), the
# harness that ran the flows, and which jobs are e2e test jobs.
SOURCES = [
    # React Native: Test All. Upstream runs Maestro per flow (iOS, up to 5
    # attempts) or once per job (Android, failures go to retry jobs).
    dict(repo="maestro-runner-bench/react-native", workflow="test-all.yml", branch="maestro-runner-e2e-batch",
         side="ours", project="react-native", harness="maestro-runner"),
    dict(repo="react/react-native", workflow="test-all.yml", branch="main",
         side="upstream", project="react-native", harness="rn-maestro"),
    # React Navigation: upstream runs agent-device.
    dict(repo="maestro-runner-bench/react-navigation", workflow="e2e-ios.yml", branch="maestro-runner-e2e",
         side="ours", project="react-navigation", harness="maestro-runner"),
    dict(repo="maestro-runner-bench/react-navigation", workflow="e2e-android.yml", branch="maestro-runner-e2e",
         side="ours", project="react-navigation", harness="maestro-runner"),
    dict(repo="react-navigation/react-navigation", workflow="e2e-ios.yml", branch="main",
         side="upstream", project="react-navigation", harness="agent-device"),
    dict(repo="react-navigation/react-navigation", workflow="e2e-android.yml", branch="main",
         side="upstream", project="react-navigation", harness="agent-device"),
    # Expo: the same harness on both sides (per-flow attempts as annotations).
    dict(repo="maestro-runner-bench/expo", workflow="test-suite.yml", branch="maestro-runner-e2e",
         side="ours", project="expo", harness="expo"),
    dict(repo="expo/expo", workflow="test-suite.yml", branch="main",
         side="upstream", project="expo", harness="expo"),
    # No upstream e2e CI to compare against: ours only.
    dict(repo="maestro-runner-bench/react-native-enriched-html", workflow="maestro-runner-e2e.yml",
         branch="maestro-runner-e2e", side="ours", project="enriched-html", harness="maestro-runner"),
    dict(repo="maestro-runner-bench/react-native-pager-view", workflow="maestro-runner-e2e.yml",
         branch="maestro-runner-e2e", side="ours", project="pager-view", harness="maestro-runner"),
]

E2E_JOB = re.compile(r"(?i)e2e")
E2E_STEP = re.compile(r"(?i)run e2e|build and run e2e")


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


_opener = urllib.request.build_opener(_NoRedirect)


def api(path, raw=False):
    """GET an API path; for log downloads, follow the redirect without auth."""
    req = urllib.request.Request(path if path.startswith("http") else API + path)
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    try:
        with _opener.open(req, timeout=60) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        loc = e.headers.get("Location") if e.code in (301, 302, 303, 307, 308) else None
        if not loc:
            raise
        if loc.startswith(API):
            # A renamed repository: the API answers at its new address.
            return api(loc, raw=raw)
        # A log download: a pre-signed URL that takes no auth.
        with urllib.request.urlopen(loc, timeout=120) as resp:
            data = resp.read()
    return data.decode("utf-8", "replace") if raw else json.loads(data)


def seconds(start, end):
    if not start or not end:
        return None
    f = "%Y-%m-%dT%H:%M:%SZ"
    return (datetime.strptime(end, f) - datetime.strptime(start, f)).total_seconds()


ANSI = re.compile(r"\x1b\[[0-9;]*m|\x1b\]8;;[^\x1b]*\x1b\\")
STAMP = re.compile(r"^\d{4}-\d\d-\d\dT[\d:.]+Z ")


def clean(log):
    return [ANSI.sub("", STAMP.sub("", line)) for line in log.splitlines()]


def parse_maestro_runner(lines):
    """maestro-runner output: TOTAL lines per run, and in-run retries."""
    totals = [(int(m.group(1)), int(m.group(2))) for m in
              (re.search(r"^\s*TOTAL\s+(\d+)/(\d+)\s", l) for l in lines) if m]
    first_retry = [int(m.group(1)) for m in
                   (re.search(r"Retrying (\d+) failed flow\(s\) \(retry 1 of", l) for l in lines) if m]
    if not totals:
        # The final table is missing (output cut short): count flows from
        # the per-flow result lines, the latest status of each winning.
        status = {}
        for l in lines:
            m = re.match(r"^(✓|✗) (\S+) [\dm. ]+s\b", l)
            if m:
                status[m.group(2)] = m.group(1)
        if not status:
            return {}
        failed = sum(1 for v in status.values() if v == "✗")
        return dict(flows=len(status), first_attempt_failures=sum(first_retry) if first_retry else failed,
                    final_failures=failed, tool="maestro-runner", summary_missing=True)
    version = next((m.group(1) for m in (re.search(r"maestro-runner (\d+\.\d+\.\d+(?:\.\d+)?)\b", l)
                                          for l in lines) if m), None)
    if first_retry:
        # One run with --retries: TOTAL is final, the retry line counts the
        # first-attempt failures.
        total = sum(t for _, t in totals)
        final_fail = sum(t - p for p, t in totals)
        first_fail = sum(first_retry)
    else:
        # The harness ran failed flows again in another run (React
        # Navigation): the first TOTAL is the first attempt, the rest retries.
        p0, t0 = totals[0]
        total, first_fail = t0, t0 - p0
        rerun_pass = sum(p for p, _ in totals[1:])
        final_fail = max(first_fail - rerun_pass, 0) if len(totals) > 1 else first_fail
    return dict(flows=total, first_attempt_failures=first_fail, final_failures=final_fail,
                tool="maestro-runner " + (version or "?"))


def parse_rn_maestro(lines):
    """Upstream React Native: iOS logs every attempt, Android one per job."""
    attempts = {}
    for l in lines:
        m = re.search(r"Executing flow: (\S+)(?: \(attempt (\d+)\))?", l)
        if m:
            n = int(m.group(2) or 1)
            attempts[m.group(1)] = max(attempts.get(m.group(1), 0), n)
    summary = next((m for m in (re.search(r"Passed: (\d+) · Failed: (\d+)", l) for l in lines) if m), None)
    if summary and not any(n > 1 for n in attempts.values()):
        passed, failed = int(summary.group(1)), int(summary.group(2))
        return dict(flows=passed + failed, first_attempt_failures=failed, final_failures=failed, tool="maestro")
    if not attempts:
        return {}
    final = sum(1 for l in lines if re.search(r"Failed to execute flow .* after \d+ attempts", l))
    return dict(flows=len(attempts), first_attempt_failures=sum(1 for n in attempts.values() if n > 1),
                final_failures=final, tool="maestro")


def parse_agent_device(lines):
    m = next((m for m in (re.search(r"Test summary: (\d+) passed \((\d+)\)(?:, (\d+) failed)?(?:, (\d+) flaky)?", l)
                          for l in lines) if m), None)
    if not m:
        return {}
    failed, flaky = int(m.group(3) or 0), int(m.group(4) or 0)
    return dict(flows=int(m.group(2)), first_attempt_failures=failed + flaky, final_failures=failed,
                tool="agent-device")


def parse_expo(repo, job_id, lines):
    """Expo's harness reports each failed attempt as an annotation."""
    notes = [a.get("message", "") for a in api(f"/repos/{repo}/check-runs/{job_id}/annotations?per_page=100")]
    first = {m.group(1) for m in (re.search(r"^(\S+) failed on attempt 1 of", n) for n in notes) if m}
    first |= {"native-modules-suite" for n in notes if re.search(r"^attempt 1 of \d+ failed", n)}
    final = {m.group(1) for m in (re.search(r"^(\S+) kept failing after", n) for n in notes) if m}
    tool = parse_maestro_runner(lines).get("tool") or "maestro"
    return dict(flows=None, first_attempt_failures=len(first), final_failures=len(final), tool=tool)


def runner_commit(lines):
    """The maestro-runner build: `--version` prints its version, then
    "Commit:  <sha>". Other steps (checkout) print a Commit line too, so only
    the one right after the version line counts."""
    for i, l in enumerate(lines):
        if re.match(r"^\s*maestro-runner \d+\.\d+\.\d+", l):
            for nxt in lines[i + 1:i + 3]:
                m = re.search(r"^\s*Commit:\s+([0-9a-f]{7,40})\s*$", nxt)
                if m:
                    return m.group(1)[:7]
    return None


def job_record(src, run, job):
    step = next((s for s in job.get("steps", []) if E2E_STEP.search(s["name"])), None)
    if step is None or step.get("conclusion") in (None, "skipped"):
        return None
    name = job["name"]
    m = re.search(r"_retry_(\d)", name)
    rec = dict(
        side=src["side"], project=src["project"], repo=src["repo"], workflow=src["workflow"],
        run_id=run["id"], run_url=run["html_url"], created_at=run["created_at"], head_sha=run["head_sha"][:10],
        job_id=job["id"], job=name, retry_round=int(m.group(1)) if m else 0,
        platform="ios" if re.search(r"(?i)ios", name + src["workflow"]) else "android",
        flavor=(re.search(r"\((\w+)", name).group(1).lower() if re.search(r"\((\w+)", name) else ""),
        runner=",".join(job.get("labels", [])), conclusion=job.get("conclusion"),
        e2e_seconds=seconds(step.get("started_at"), step.get("completed_at")),
        queue_seconds=seconds(job.get("created_at"), job.get("started_at")),
    )
    if rec["flavor"].isdigit():  # "android-test-e2e (36)" is an API level
        rec["flavor"] = ""
    try:
        lines = clean(api(f"/repos/{src['repo']}/actions/jobs/{job['id']}/logs", raw=True))
    except Exception as e:  # logs expire or are not ready yet
        print(f"  logs unavailable for {job['id']}: {e}", file=sys.stderr)
        lines = []
    h = src["harness"]
    if src["side"] == "ours":
        rec["runner_commit"] = runner_commit(lines)
    if h == "maestro-runner":
        rec.update(parse_maestro_runner(lines))
    elif h == "rn-maestro":
        rec.update(parse_rn_maestro(lines))
    elif h == "agent-device":
        rec.update(parse_agent_device(lines))
    elif h == "expo":
        rec.update(parse_expo(src["repo"], job["id"], lines))
    return rec


def collect(known):
    new = []
    for src in SOURCES:
        try:
            # Up to 100 recent runs, of which the newest RUNS that ran e2e
            # jobs are used: many upstream runs skip e2e (change detection).
            runs = api(f"/repos/{src['repo']}/actions/workflows/{src['workflow']}/runs"
                       f"?branch={src['branch']}&status=completed&per_page=100")["workflow_runs"]
        except urllib.error.HTTPError as e:
            print(f"{src['repo']} {src['workflow']}: {e}", file=sys.stderr)
            continue
        used = 0
        for run in runs:
            if used >= RUNS:
                break
            if run.get("conclusion") in ("cancelled", "skipped"):
                continue
            jobs = api(f"/repos/{src['repo']}/actions/runs/{run['id']}/jobs?per_page=100")["jobs"]
            ran_e2e = any(E2E_JOB.search(j["name"]) and j.get("conclusion") not in (None, "skipped", "cancelled")
                          and not re.search(r"/ (report|build)\b", j["name"]) for j in jobs)
            if not ran_e2e:
                continue
            used += 1
            for job in jobs:
                if job["id"] in known or not E2E_JOB.search(job["name"]) or job.get("conclusion") in (None, "skipped", "cancelled"):
                    continue
                if re.search(r"/ (report|build)\b", job["name"]):
                    continue
                rec = job_record(src, run, job)
                if rec:
                    known.add(job["id"])
                    new.append(rec)
        print(f"{src['side']:8} {src['repo']} {src['workflow']}: {used} runs with e2e")
    return new


def median(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def summary(records):
    out = ["# Bench results", "",
           f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} from {len(records)} e2e jobs.",
           "", "Per project, platform and flavour: ours (maestro-runner) against upstream (Maestro, or "
           "agent-device for React Navigation). Times are the e2e test step only (no builds, no queue). "
           "First-attempt failures count flows that failed at least once before passing or failing for good; "
           "job retry rounds are React Native's retry_1/retry_2 jobs.", ""]
    hdr = ("| Project | Platform | Flavour | Side | Runs | Median e2e (min) | Green runs | "
           "Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | "
           "Runs needing a retry job | Runner |")
    out += [hdr, "|" + "---|" * 12]
    groups = {}
    for r in records:
        groups.setdefault((r["project"], r["platform"], r["flavor"], r["side"]), []).append(r)
    for (proj, plat, flav, side), rs in sorted(groups.items()):
        first_round = [r for r in rs if r["retry_round"] == 0]
        run_ids = {r["run_id"] for r in rs}
        retried_runs = {r["run_id"] for r in rs if r["retry_round"] > 0}
        green = [r for r in first_round if r["conclusion"] == "success" and r["run_id"] not in retried_runs]
        ff = [r.get("first_attempt_failures") for r in first_round if r.get("first_attempt_failures") is not None]
        fin = [r.get("final_failures") for r in first_round if r.get("final_failures") is not None]
        clean_runs = sum(1 for x in ff if x == 0)
        med = median([r["e2e_seconds"] for r in first_round])
        out.append("| {} | {} | {} | {} | {} | {} | {}/{} | {} | {} | {} | {}/{} | {} |".format(
            proj, plat, flav or "-", side, len(run_ids),
            f"{med / 60:.1f}" if med else "-",
            len(green), len(first_round),
            f"{clean_runs}/{len(ff)}" if ff else "-",
            f"{statistics.mean(ff):.2f}" if ff else "-",
            f"{statistics.mean(fin):.2f}" if fin else "-",
            len(retried_runs), len(run_ids),
            ", ".join(sorted({r["runner"] for r in first_round})) or "-")
            + (" (builds: " + ", ".join(sorted({r.get("runner_commit") or "?" for r in first_round})) + ")"
               if side == "ours" else ""))
    out += ["", "Upstream React Native runs its e2e jobs on larger runners (macos-*-large, 8-core-ubuntu); "
            "the bench fork uses the standard ones (macos-*-intel, ubuntu-latest).", ""]
    return "\n".join(out) + "\n"


def main():
    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, "jobs.jsonl")
    records = []
    if os.path.exists(path):
        with open(path) as f:
            records = [json.loads(l) for l in f if l.strip()]
    known = {r["job_id"] for r in records}
    new = collect(known)
    with open(path, "a") as f:
        for r in new:
            f.write(json.dumps(r, sort_keys=True) + "\n")
    records += new
    with open(os.path.join(RESULTS, "SUMMARY.md"), "w") as f:
        f.write(summary(records))
    print(f"{len(new)} new e2e jobs, {len(records)} in total")


if __name__ == "__main__":
    main()
