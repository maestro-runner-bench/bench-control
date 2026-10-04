#!/usr/bin/env python3
"""Decide which benches to start now; prints one repo name per line.

The benches run in back-to-back cycles. A cycle starts with React Native
(the first repo in repos.json); the others start during it as macOS runners
come free, and when every repo has run in the cycle and nothing is still
running, the next cycle starts with React Native again.

Macs are counted live: the macOS jobs running or queued in the bench forks
right now (the free org runs 5 at a time). React Native needs all of them
only for its first ~25 minutes, so the others fit in beside it. Nothing is
started while any macOS job is queued, so a bench never makes React Native
(or another bench) wait for a Mac.

A cycle older than CYCLE_HOURS starts over even if a repo never ran in it
(its sync failed, say), so one broken repo does not stop the others.

Needs GH_TOKEN (Actions read). NOW=2026-10-04T05:00 overrides the clock.
"""
import datetime as dt
import json
import os
import sys
import urllib.request

MAC_RUNNERS = int(os.environ.get("MAC_RUNNERS", "5"))  # free org limit
CYCLE_HOURS = float(os.environ.get("CYCLE_HOURS", "8"))
# React Native's macOS jobs appear a few minutes after it starts; until then
# the Macs look free, so the others wait this long after it starts.
LEAD_GRACE_MIN = float(os.environ.get("LEAD_GRACE_MIN", "10"))
UTC = dt.timezone.utc
NEVER = dt.datetime.min.replace(tzinfo=UTC)


def api(path):
    req = urllib.request.Request(
        "https://api.github.com/" + path,
        headers={
            "Authorization": "Bearer " + os.environ["GH_TOKEN"],
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def parse(ts):
    return dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))


def runs_of(repo):
    runs = []
    for wf in repo["workflows"]:
        data = api(
            f"repos/{repo['fork']}/actions/workflows/{wf}/runs"
            f"?branch={repo['branch']}&per_page=20"
        )
        runs += data.get("workflow_runs", [])
    return runs


def mac_jobs(repo, run):
    """(running, queued) macOS jobs of a run that is not finished."""
    jobs = api(f"repos/{repo['fork']}/actions/runs/{run['id']}/jobs?per_page=100").get("jobs", [])
    mac = [j for j in jobs if any("macos" in label for label in j.get("labels", []))]
    return (sum(1 for j in mac if j["status"] == "in_progress"),
            sum(1 for j in mac if j["status"] in ("queued", "waiting", "pending")))


def main():
    now = parse(os.environ["NOW"]) if os.environ.get("NOW") else dt.datetime.now(UTC)
    if now.tzinfo is None:
        now = now.replace(tzinfo=UTC)
    # A repo with "paused" set stays out of the cycles (it can still be
    # started by hand from sync-and-run.yml).
    repos = [r for r in json.load(open("repos.json")) if not r.get("paused")]

    state = {}
    running = queued = 0
    for repo in repos:
        runs = runs_of(repo)
        going = [r for r in runs if r["status"] != "completed"]
        dispatched = [parse(r["created_at"]) for r in runs if r["event"] == "workflow_dispatch"]
        for r in going:
            a, b = mac_jobs(repo, r)
            running, queued = running + a, queued + b
        state[repo["name"]] = dict(repo=repo, going=bool(going), last=max(dispatched, default=NEVER))

    lead = repos[0]["name"]
    cycle_start = state[lead]["last"]
    others = [r["name"] for r in repos[1:]]
    for name, s in state.items():
        s["ran"] = s["last"] >= cycle_start
        print(f"{name}: {'running' if s['going'] else 'idle'}, last started "
              f"{s['last']:%m-%d %H:%M}{'' if s['last'] != NEVER else ' (never)'}, "
              f"{'ran' if s['ran'] else 'not yet run'} this cycle", file=sys.stderr)
    free = MAC_RUNNERS - running - queued
    print(f"Macs: {running} running, {queued} queued, {free} free; cycle started "
          f"{cycle_start:%m-%d %H:%M}", file=sys.stderr)

    if queued:
        print("A macOS job is waiting for a runner: start nothing.", file=sys.stderr)
        return

    cycle_done = all(state[n]["ran"] and not state[n]["going"] for n in others)
    stale = now - cycle_start > dt.timedelta(hours=CYCLE_HOURS)
    if not state[lead]["going"] and (cycle_done or stale):
        # A new cycle: React Native first, on its own.
        if running == 0 and not any(s["going"] for s in state.values()):
            print(lead)
        else:
            print(f"New cycle waits for the running benches to finish.", file=sys.stderr)
        return

    if now - cycle_start < dt.timedelta(minutes=LEAD_GRACE_MIN):
        print(f"{lead} started under {LEAD_GRACE_MIN:.0f} minutes ago: wait for its jobs.", file=sys.stderr)
        return

    # During a cycle: the repos that have not run in it, least recently run
    # first, while their Macs fit.
    todo = sorted((n for n in others if not state[n]["ran"] and not state[n]["going"]),
                  key=lambda n: state[n]["last"])
    for name in todo:
        macs = state[name]["repo"].get("macRunners", 1)
        if macs > free:
            print(f"{name}: waits for {macs} Mac(s)", file=sys.stderr)
            break
        free -= macs
        print(name)


if __name__ == "__main__":
    main()
