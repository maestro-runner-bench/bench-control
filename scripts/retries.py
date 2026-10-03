"""Retried test cases per run, from results/flows.jsonl.

A run's flows are joined across its jobs for one platform, flavour and app:
the first job's flows, and the flows React Native's retry_1/retry_2 jobs run
again. What counts is failed attempts: a flow that failed at least once and
then passed *passed on retry*; one whose last run failed *failed*. Runs that
did not fail (a retry job rerunning a whole suite) only add extra runs.
"""
import collections
import re
import statistics


def _app(job):
    m = re.search(r"test_e2e_\w+?_(rntester|templateapp)", job)
    return m.group(1) if m else ""


def rollup(entries):
    groups = collections.defaultdict(list)
    for e in entries:
        key = (e["project"], e["side"], e["run_id"], e["platform"], e["flavor"], _app(e["job"]))
        groups[key].append(e)
    rows = []
    for (project, side, run_id, platform, flavor, app), es in groups.items():
        es.sort(key=lambda e: e["retry_round"])
        first = es[0]
        if first["retry_round"] != 0:
            continue  # the first job of the run was not collected
        flows = collections.OrderedDict()
        for e in es:
            for f in e["flows"]:
                cur = flows.setdefault(f["name"], dict(attempts=0, fails=0, passed=False))
                cur["attempts"] += f["attempts"]
                cur["fails"] += f.get("fails", 0)
                cur["passed"] = f["passed"]
        retried = {n: f["fails"] for n, f in flows.items() if f["fails"] and f["passed"]}
        rows.append(dict(
            project=project, side=side, run_id=run_id, platform=platform, flavor=flavor, app=app,
            created_at=first["created_at"], build=first.get("runner_commit") or "",
            complete=all(e["status"] == "ok" for e in es) and bool(flows),
            flows=len(flows), retried=retried,
            failed_once=sum(1 for f in flows.values() if f["fails"]),
            extra_attempts=sum(f["attempts"] - 1 for f in flows.values()),
            failed=[n for n, f in flows.items() if not f["passed"]],
            retry_jobs=max(e["retry_round"] for e in es),
            url=f"https://github.com/{first['repo']}/actions/runs/{run_id}",
        ))
    rows.sort(key=lambda r: r["created_at"], reverse=True)
    return rows


def _label(r):
    return " ".join(x for x in (r["platform"], r["flavor"], r["app"]) if x)


def _stats(rs):
    n = len(rs)
    times = [r["test_min"] for r in rs if r.get("test_min")]
    return dict(
        runs=n,
        test_min=statistics.median(times) if times else None,
        first_time=sum(1 for r in rs if r["failed_once"] == 0) / n,
        failed_once=sum(r["failed_once"] for r in rs) / n,
        retry_job=sum(1 for r in rs if r["retry_jobs"]) / n,
        extra=sum(r["extra_attempts"] for r in rs) / n,
        failed_end=sum(1 for r in rs if r["failed"]) / n,
        top=collections.Counter(name for r in rs for name in list(r["retried"]) + r["failed"]).most_common(3))


# (key, header, format, True when higher is better)
COLUMNS = [
    ("test_min", "Test time / run (min)", lambda v: f"{v:.1f}" if v is not None else "-", False),
    ("first_time", "Every flow passed first time", lambda v: f"{v:.0%}", True),
    ("failed_once", "Flows that failed at least once / run", lambda v: f"{v:.2f}", False),
    ("retry_job", "Runs needing a retry job", lambda v: f"{v:.0%}", False),
    ("extra", "Extra flow runs / run", lambda v: f"{v:.1f}", False),
    ("failed_end", "Runs ending with a failed flow", lambda v: f"{v:.0%}", False),
]


def _vs(ours, up, fmt, higher_better):
    if ours is None or up is None:
        return f"{fmt(ours)} vs {fmt(up)}"
    a, b = fmt(ours), fmt(up)
    if a != b and (ours > up) == higher_better:
        a = f"**{a}**"
    elif a != b:
        b = f"**{b}**"
    return f"{a} vs {b}"


def _aggregate(rows):
    """One row per job: ours (the newest maestro-runner build) against
    upstream in the same cell; older builds of ours in a second table."""
    groups = collections.defaultdict(list)
    for r in rows:
        if r["complete"]:
            groups[(_label(r), r["side"], r["build"] if r["side"] == "ours" else "")].append(r)
    labels = sorted({k[0] for k in groups})
    out = ["Each cell: **ours vs upstream**; the better one in bold. Ours is the newest maestro-runner build.", "",
           "| Job | Build | Runs | " + " | ".join(c[1] for c in COLUMNS) + " | Most often failing (ours / upstream) |",
           "|" + "---|" * (len(COLUMNS) + 4)]
    older = []
    for label in labels:
        builds = sorted(((k[2], rs) for k, rs in groups.items() if k[0] == label and k[1] == "ours"),
                        key=lambda b: max(r["created_at"] for r in b[1]), reverse=True)
        up_rs = groups.get((label, "upstream", ""))
        ours = _stats(builds[0][1]) if builds else None
        up = _stats(up_rs) if up_rs else None
        cells = [_vs(ours and ours[k], up and up[k], fmt, hb) if up else (fmt(ours[k]) if ours else "-")
                 for k, _, fmt, hb in COLUMNS]
        top = lambda st: ", ".join(f"{n} ×{c}" for n, c in st["top"]) if st and st["top"] else "-"
        runs = f"{ours['runs'] if ours else 0} vs {up['runs']}" if up else str(ours["runs"])
        out.append(f"| {label} | {builds[0][0] or '-' if builds else '-'} | {runs} | " + " | ".join(cells)
                   + f" | {top(ours)} / {top(up)} |")
        for build, rs in builds[1:]:
            st = _stats(rs)
            older.append(f"| {label} | {build or 'older'} | {st['runs']} | "
                         + " | ".join(fmt(st[k]) for k, _, fmt, _ in COLUMNS) + f" | {top(st)} |")
    if older:
        out += ["", "Ours on earlier maestro-runner builds:", "",
                "| Job | Build | Runs | " + " | ".join(c[1] for c in COLUMNS) + " | Most often failing |",
                "|" + "---|" * (len(COLUMNS) + 4)] + older
    return out


def _runs(rows):
    out = ["| Started (UTC) | Run | Platform | Side | Build | Flows | Failed at least once | "
           "Passed on retry (failed attempts) | Failed at the end | Extra flow runs | Retry jobs |",
           "|" + "---|" * 11]
    for r in rows:
        if not r["complete"]:
            continue
        retried = ", ".join(f"{n} ({a})" for n, a in r["retried"].items()) or "-"
        out.append(f"| {r['created_at'][:16].replace('T', ' ')} | [{r['run_id']}]({r['url']}) | {_label(r)} | "
                   f"{r['side']} | {r['build'] or '-'} | {r['flows']} | {r['failed_once']} | {retried} | "
                   f"{', '.join(r['failed']) or '-'} | {r['extra_attempts']} | {r['retry_jobs']} |")
    return out


def add_times(rows, records):
    """Each run's test time: its jobs' test steps added up, retry jobs
    included (the time the run took to go green or give up)."""
    minutes = collections.defaultdict(float)
    for r in records:
        if r.get("e2e_seconds") and r.get("stage", "tests") == "tests":
            minutes[(r["run_id"], r["project"], r["platform"], r["flavor"], _app(r["job"]))] += r["e2e_seconds"] / 60
    for row in rows:
        row["test_min"] = minutes.get((row["run_id"], row["project"], row["platform"], row["flavor"], row["app"]))


INTRO = ("Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside "
         "its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's "
         "rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. "
         "*Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of "
         "flows that had passed. Runs whose logs had expired are left out.")


def render_summary(rows, generated, charts):
    out = ["# Bench results: maestro-runner against upstream", "", f"Generated {generated}.", "",
           "*Test time* is a run's test steps added up, retry jobs included (no builds, no queue). "
           "The other columns are read per flow from the job logs; see [RETRIES.md](RETRIES.md). "
           "Upstream React Navigation runs agent-device; React Native and Expo run Maestro. Upstream "
           "React Native uses larger runners (macos-*-large, 8-core-ubuntu) than the bench fork. "
           "enriched-html and pager-view run no e2e upstream, so they show ours only."]
    for project in sorted({r["project"] for r in rows}):
        out += ["", f"## [{project}]({project}.md)", ""] + _aggregate([r for r in rows if r["project"] == project])
        out += [""] + [f"![{n[:-4]}](charts/{n})" for n in charts.get(project, [])]
    return "\n".join(out) + "\n"


def render_all(rows):
    out = ["# Retried test cases", "", INTRO]
    for project in sorted({r["project"] for r in rows}):
        mine = [r for r in rows if r["project"] == project]
        out += ["", f"## {project}", ""] + _aggregate(mine)
    return "\n".join(out) + "\n"


def render_project(project, rows):
    mine = [r for r in rows if r["project"] == project]
    if not mine:
        return ""
    out = ["", "## Retried test cases", "", INTRO, ""] + _aggregate(mine)
    out += ["", "### Per run", ""] + _runs(mine)
    return "\n".join(out) + "\n"
