"""Retried test cases per run, from results/flows.jsonl.

A run's flows are joined across its jobs for one platform, flavour and app:
the first job's flows, and the flows React Native's retry_1/retry_2 jobs run
again. What counts is failed attempts: a flow that failed at least once and
then passed *passed on retry*; one whose last run failed *failed*. Runs that
did not fail (a retry job rerunning a whole suite) only add extra runs.
"""
import collections
import re


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


def _aggregate(rows):
    out = ["| Platform | Side | Build | Runs | Runs where every flow passed first time | "
           "Flows that failed at least once / run (avg, max) | Flows passed only on retry / run | "
           "Runs ending with a failed flow | Extra flow runs / run | Runs needing a retry job | Flows / run | "
           "Most often failing flows |", "|" + "---|" * 12]
    groups = collections.defaultdict(list)
    for r in rows:
        if r["complete"]:
            groups[(_label(r), r["side"], r["build"] if r["side"] == "ours" else "")].append(r)
    for (label, side, build), rs in sorted(groups.items()):
        n = len(rs)
        once = [r["failed_once"] for r in rs]
        top = collections.Counter(name for r in rs for name in list(r["retried"]) + r["failed"]).most_common(3)
        out.append("| {} | {} | {} | {} | {}/{} | {:.2f}, {} | {:.2f} | {}/{} | {:.2f} | {}/{} | {} | {} |".format(
            label, side, build or "-", n, sum(1 for c in once if c == 0), n,
            sum(once) / n, max(once), sum(len(r["retried"]) for r in rs) / n,
            sum(1 for r in rs if r["failed"]), n, sum(r["extra_attempts"] for r in rs) / n,
            sum(1 for r in rs if r["retry_jobs"]), n, round(sum(r["flows"] for r in rs) / n),
            ", ".join(f"{name} ×{c}" for name, c in top) or "-"))
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


INTRO = ("Per run, from each job's log: a flow *failed at least once* if any of its attempts failed, inside "
         "its job (maestro-runner `--retries`, React Native's iOS per-flow attempts, agent-device, Expo's "
         "rounds) or in a retry job (React Native's retry_1/retry_2); it *passed on retry* if it then passed. "
         "*Extra flow runs* counts every run of a flow beyond its first, including whole-suite reruns of "
         "flows that had passed. Runs whose logs had expired are left out.")


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
