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
import time

import charts
import flows as flowlog
import retries
import urllib.error
import urllib.request
from datetime import datetime, timezone

API = "https://api.github.com"
TOKEN = os.environ.get("GH_TOKEN", "")
RUNS = int(os.environ.get("RUNS_PER_SOURCE", "15"))
RESULTS = os.environ.get("RESULTS_DIR", "results")
# The bench started with the scheduled runs on the night of 2026-10-02; our
# runs before that were setup and development builds and are not counted.
# Upstream's history is kept as the baseline.
OURS_SINCE = os.environ.get("OURS_SINCE", "2026-10-02T20:00:00Z")


def counted(rec):
    return rec["side"] != "ours" or rec["created_at"] >= OURS_SINCE

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
    """GET an API path, trying again on GitHub's passing 5xx errors."""
    for attempt in range(4):
        try:
            return _api(path, raw)
        except urllib.error.HTTPError as e:
            if e.code < 500 or attempt == 3:
                raise
        except urllib.error.URLError:
            if attempt == 3:
                raise
        time.sleep(5 * (attempt + 1))


def _api(path, raw=False):
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
            return _api(loc, raw=raw)
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


def timing(run, job):
    """Wall-clock times kept on every record: the whole run and the job."""
    return dict(run_started_at=run.get("run_started_at"),
                run_seconds=seconds(run.get("run_started_at"), run.get("updated_at")),
                job_seconds=seconds(job.get("started_at"), job.get("completed_at")))


def job_record(src, run, job):
    step = next((s for s in job.get("steps", []) if E2E_STEP.search(s["name"])), None)
    reached_tests = step is not None and step.get("conclusion") not in (None, "skipped")
    # Our job that stopped before its tests (a build or emulator failure, or
    # cut off at the time limit) is kept, so the per-repo report shows every
    # run; upstream's are left out.
    if not reached_tests and src["side"] != "ours":
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
        e2e_seconds=seconds(step.get("started_at"), step.get("completed_at")) if reached_tests else None,
        queue_seconds=seconds(job.get("created_at"), job.get("started_at")),
        stage="tests" if reached_tests else "setup",
        **timing(run, job),
    )
    if rec["flavor"].isdigit():  # "android-test-e2e (36)" is an API level
        rec["flavor"] = ""
    lines = job_log(src["repo"], job["id"])
    h = src["harness"]
    if src["side"] == "ours":
        rec["runner_commit"] = runner_commit(lines)
    if not reached_tests:
        return rec
    rec["_flows"] = flowlog.parse(h, src["side"], lines) if lines else None
    if h == "maestro-runner":
        rec.update(parse_maestro_runner(lines))
    elif h == "rn-maestro":
        rec.update(parse_rn_maestro(lines))
    elif h == "agent-device":
        rec.update(parse_agent_device(lines))
    elif h == "expo":
        rec.update(parse_expo(src["repo"], job["id"], lines))
    return rec


def job_log(repo, job_id):
    try:
        return clean(api(f"/repos/{repo}/actions/jobs/{job_id}/logs", raw=True))
    except Exception as e:  # logs expire or are not ready yet
        print(f"  logs unavailable for {job_id}: {e}", file=sys.stderr)
        return []


def flow_entry(rec, flows):
    """One line of results/flows.jsonl: a job's flows and their attempts."""
    return dict(job_id=rec["job_id"], run_id=rec["run_id"], created_at=rec["created_at"],
                project=rec["project"], side=rec["side"], repo=rec["repo"], workflow=rec["workflow"],
                platform=rec["platform"], flavor=rec["flavor"], job=rec["job"], retry_round=rec["retry_round"],
                runner_commit=rec.get("runner_commit"), status="ok" if flows is not None else "no-log",
                v=flowlog.VERSION,
                flows=flows or [])


def backfill_flows(records, entries, limit):
    """Read the flows of jobs collected before flows were recorded (or whose
    log was not ready), newest first, up to limit logs per run."""
    harness = {(s["repo"], s["workflow"]): s["harness"] for s in SOURCES}
    todo = [r for r in records.values() if r.get("stage", "tests") == "tests"
            and (r["job_id"] not in entries or entries[r["job_id"]].get("v") != flowlog.VERSION)
            and (r["repo"], r["workflow"]) in harness]
    todo.sort(key=lambda r: r["created_at"], reverse=True)
    for r in todo[:limit]:
        lines = job_log(r["repo"], r["job_id"])
        flows = flowlog.parse(harness[(r["repo"], r["workflow"])], r["side"], lines) if lines else None
        entries[r["job_id"]] = flow_entry(r, flows)
    return min(len(todo), limit)


def collect(records):
    """Add new e2e jobs to records (by job id); fill in the timing of known ones."""
    new = []
    for src in SOURCES:
        try:
            # Up to 300 recent runs, of which the newest RUNS that ran e2e
            # jobs are used: many upstream runs skip e2e (change detection).
            runs = []
            for page in (1, 2, 3):
                batch = api(f"/repos/{src['repo']}/actions/workflows/{src['workflow']}/runs"
                            f"?branch={src['branch']}&status=completed&per_page=100&page={page}")["workflow_runs"]
                runs += batch
                if len(batch) < 100:
                    break
        except urllib.error.HTTPError as e:
            print(f"{src['repo']} {src['workflow']}: {e}", file=sys.stderr)
            continue
        used = 0
        for run in runs:
            if used >= RUNS:
                break
            ours = src["side"] == "ours"
            if ours and run["created_at"] < OURS_SINCE:
                continue
            # Upstream cancels superseded runs; ours are cancelled only by
            # the time limit, which is a result.
            if run.get("conclusion") == "skipped" or (run.get("conclusion") == "cancelled" and not ours):
                continue
            jobs = api(f"/repos/{src['repo']}/actions/runs/{run['id']}/jobs?per_page=100")["jobs"]
            skip = (None, "skipped") if ours else (None, "skipped", "cancelled")
            ran_e2e = any(E2E_JOB.search(j["name"]) and j.get("conclusion") not in skip
                          and j.get("started_at") and not re.search(r"/ (report|build)\b", j["name"]) for j in jobs)
            if not ran_e2e:
                continue
            used += 1
            for job in jobs:
                if not E2E_JOB.search(job["name"]) or job.get("conclusion") in skip or not job.get("started_at"):
                    continue
                if re.search(r"/ (report|build)\b", job["name"]):
                    continue
                if job["id"] in records:
                    if records[job["id"]].get("job_seconds") is None:
                        records[job["id"]].update(timing(run, job))
                    continue
                rec = job_record(src, run, job)
                if rec:
                    records[job["id"]] = rec
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
           "agent-device for React Navigation); ours one line per maestro-runner build, newest first "
           "(\"older\" = before builds were recorded). Times are the e2e test step only (no builds, no queue). "
           "First-attempt failures count flows that failed at least once before passing or failing for good; "
           "job retry rounds are React Native's retry_1/retry_2 jobs.", ""]
    hdr = ("| Project | Platform | Flavour | Side | Build | Runs | Median e2e (min) | Green runs | "
           "Runs with no first-attempt failure | First-attempt failures / run | Final failures / run | "
           "Runs needing a retry job | Runner |")
    out += [hdr, "|" + "---|" * 13]
    # Ours is split by maestro-runner build, newest first, so a fix does not
    # carry the failures of the builds before it.
    groups = {}
    for r in records:
        build = (r.get("runner_commit") or "older") if r["side"] == "ours" else ""
        flav = r["flavor"] + (" (template app)" if "templateapp" in r["job"] else "")
        groups.setdefault((r["project"], r["platform"], flav, r["side"], build), []).append(r)
    def order(item):
        (proj, plat, flav, side, build), rs = item
        return (proj, plat, flav, side, -max(datetime.strptime(r["created_at"], "%Y-%m-%dT%H:%M:%SZ").timestamp() for r in rs))
    for (proj, plat, flav, side, build), rs in sorted(groups.items(), key=order):
        if not any(r.get("stage", "tests") == "tests" for r in rs):
            continue
        first_round = [r for r in rs if r["retry_round"] == 0 and r.get("stage", "tests") == "tests"]
        run_ids = {r["run_id"] for r in rs}
        retried_runs = {r["run_id"] for r in rs if r["retry_round"] > 0}
        green = [r for r in first_round if r["conclusion"] == "success" and r["run_id"] not in retried_runs]
        ff = [r.get("first_attempt_failures") for r in first_round if r.get("first_attempt_failures") is not None]
        fin = [r.get("final_failures") for r in first_round if r.get("final_failures") is not None]
        clean_runs = sum(1 for x in ff if x == 0)
        med = median([r["e2e_seconds"] for r in first_round if r["conclusion"] != "cancelled"])
        out.append("| {} | {} | {} | {} | {} | {} | {} | {}/{} | {} | {} | {} | {}/{} | {} |".format(
            proj, plat, flav or "-", side, build or "-", len(run_ids),
            f"{med / 60:.1f}" if med else "-",
            len(green), len(first_round),
            f"{clean_runs}/{len(ff)}" if ff else "-",
            f"{statistics.mean(ff):.2f}" if ff else "-",
            f"{statistics.mean(fin):.2f}" if fin else "-",
            len(retried_runs), len(run_ids),
            ", ".join(sorted({r["runner"] for r in first_round})) or "-"))
    out += ["", "Upstream React Native runs its e2e jobs on larger runners (macos-*-large, 8-core-ubuntu); "
            "the bench fork uses the standard ones (macos-*-intel, ubuntu-latest).", ""]
    return "\n".join(out) + "\n"


PROJECT_NOTES = {
    "react-native": "Upstream runs Maestro on larger runners (macos-*-large, 8-core-ubuntu); "
                    "the bench fork uses the standard ones.",
    "react-navigation": "Upstream runs agent-device.",
    "expo": "Both sides use Expo's own harness; upstream with Maestro.",
    "enriched-html": "Upstream has no e2e CI to compare against.",
    "pager-view": "Upstream has no e2e CI to compare against.",
}


def minutes(sec):
    return f"{sec / 60:.1f}" if sec is not None else "-"


def job_label(r):
    name = re.sub(r"^test_e2e_", "", r["job"])
    return name.replace(" / test ", " ").replace("android-test-e2e (36)", "android").replace("-test-e2e", "")


def job_result(r):
    if r.get("stage") == "setup":
        return "cancelled before tests" if r["conclusion"] == "cancelled" else "failed before tests"
    if r["conclusion"] == "cancelled":
        return "cancelled during tests (time limit or by hand)"
    flows, final = r.get("flows"), r.get("final_failures")
    if flows:
        res = f"{flows - (final or 0)}/{flows}"
    elif final is not None:
        res = "all passed" if final == 0 else f"{final} failed"
    else:
        res = r["conclusion"]
    retried = (r.get("first_attempt_failures") or 0) - (final or 0)
    return res + (f", {retried} passed on retry" if retried > 0 else "")


def project_report(project, rs, summary_rows):
    out = [f"# {project}", "", PROJECT_NOTES.get(project, ""), "",
           "Times in minutes. *Run* is the whole workflow run (builds included); *job* is one job; "
           "*tests* is its test step only; *queue* is the wait for a runner.", "",
           "## Summary", ""] + summary_rows
    for side, title in (("ours", "maestro-runner (bench fork)"), ("upstream", "upstream")):
        mine = [r for r in rs if r["side"] == side]
        if not mine:
            continue
        out += ["", f"## Runs: {title}", "",
                "| Started (UTC) | Run | Build | Run time | Job | Job time | Tests | Queue | Result |",
                "|---|---|---|---|---|---|---|---|---|"]
        by_run = {}
        for r in mine:
            by_run.setdefault(r["run_id"], []).append(r)
        for run_id, jobs in sorted(by_run.items(), key=lambda kv: kv[1][0]["created_at"], reverse=True):
            first = jobs[0]
            started = (first.get("run_started_at") or first["created_at"])[:16].replace("T", " ")
            build = first.get("runner_commit") or (first.get("tool") or "-")
            for i, r in enumerate(sorted(jobs, key=lambda j: (j["platform"], j["job"]))):
                head = (f"{started} | [{run_id}]({first['run_url']}) | {build} | {minutes(first.get('run_seconds'))}"
                        if i == 0 else " | | | ")
                out.append(f"| {head} | {job_label(r)} | {minutes(r.get('job_seconds'))} | "
                           f"{minutes(r.get('e2e_seconds'))} | {minutes(r.get('queue_seconds'))} | {job_result(r)} |")
    return "\n".join(out) + "\n"


def main():
    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, "jobs.jsonl")
    records = {}
    if os.path.exists(path):
        with open(path) as f:
            for l in f:
                if l.strip():
                    r = json.loads(l)
                    records[r["job_id"]] = r
    new = collect(records)
    records = {k: r for k, r in records.items() if counted(r)}
    flows_path = os.path.join(RESULTS, "flows.jsonl")
    entries = {}
    if os.path.exists(flows_path):
        with open(flows_path) as f:
            for l in f:
                if l.strip():
                    e = json.loads(l)
                    entries[e["job_id"]] = e
    entries = {k: e for k, e in entries.items() if counted(e)}
    for r in records.values():
        if "_flows" in r:
            entries[r["job_id"]] = flow_entry(r, r.pop("_flows"))
    filled = backfill_flows(records, entries, int(os.environ.get("FLOW_BACKFILL", "400")))
    with open(flows_path, "w") as f:
        for e in sorted(entries.values(), key=lambda e: (e["created_at"], e["job_id"])):
            f.write(json.dumps(e, sort_keys=True) + "\n")
    rows = sorted(records.values(), key=lambda r: (r["created_at"], r["job_id"]))
    run_rows = retries.rollup(entries.values())
    retries.add_times(run_rows, rows)
    with open(os.path.join(RESULTS, "RETRIES.md"), "w") as f:
        f.write(retries.render_all(run_rows))
    made = charts.write(RESULTS, rows, run_rows)
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r, sort_keys=True) + "\n")
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(os.path.join(RESULTS, "SUMMARY.md"), "w") as f:
        f.write(retries.render_summary(run_rows, generated, made))
    text = summary(rows)
    projects = sorted({r["project"] for r in rows})
    lines = text.splitlines()
    head = [l for l in lines if l.startswith("| Project") or l.startswith("|---")]
    for p in projects:
        mine = [l for l in lines if l.startswith(f"| {p} |")]
        with open(os.path.join(RESULTS, f"{p}.md"), "w") as f:
            f.write(project_report(p, [r for r in rows if r["project"] == p], head + mine))
            f.write("\n## Trend\n\n" + charts.markdown(p, made.get(p, [])))
            f.write(retries.render_project(p, run_rows))
    print(f"{len(new)} new e2e jobs, {len(rows)} in total; flows read for {filled} more jobs")


if __name__ == "__main__":
    main()
