#!/usr/bin/env python3
"""Decide which benches to start on this tick; prints one repo name per line.

GitHub starts scheduled workflows late, by hours and by a different amount
each time, so a fixed cron per slot let React Native (all 5 macOS runners for
~2.5h) overlap the others and their jobs waited for a Mac. Instead a tick
runs every 15 minutes and starts a repo when:

  - its latest slot (repos.json slotsUTC) has passed and no run of it has
    started since that slot,
  - no run of it is still going, and
  - the macOS runners it needs (macRunners) are free: the repos with a run
    going hold theirs until it ends.

Repos go in slot order; one that has to wait for Macs holds back the repos
due after it, so the order stays React Native, then Expo, React Navigation
and enriched-html, then pager-view, however late a tick fires.

Needs GH_TOKEN (Actions read). NOW=2026-10-03T05:00 overrides the clock.
"""
import datetime as dt
import json
import os
import sys
import urllib.request

MAC_RUNNERS = int(os.environ.get("MAC_RUNNERS", "5"))  # free org limit
UTC = dt.timezone.utc


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


def latest_slot(slots, now):
    """The latest slot time at or before now (today's or yesterday's)."""
    best = None
    for day in (now.date(), now.date() - dt.timedelta(days=1)):
        for s in slots:
            h, m = map(int, s.split(":"))
            t = dt.datetime(day.year, day.month, day.day, h, m, tzinfo=UTC)
            if t <= now and (best is None or t > best):
                best = t
    return best


def runs_of(repo):
    runs = []
    for wf in repo["workflows"]:
        data = api(
            f"repos/{repo['fork']}/actions/workflows/{wf}/runs"
            f"?branch={repo['branch']}&per_page=20"
        )
        runs += data.get("workflow_runs", [])
    return runs


def main():
    now = parse(os.environ["NOW"]) if os.environ.get("NOW") else dt.datetime.now(UTC)
    if now.tzinfo is None:
        now = now.replace(tzinfo=UTC)
    repos = json.load(open("repos.json"))

    busy = 0
    waiting = []
    for repo in repos:
        slot = latest_slot(repo["slotsUTC"], now)
        runs = runs_of(repo)
        going = [r for r in runs if r["status"] != "completed"]
        started = any(
            r["event"] == "workflow_dispatch" and parse(r["created_at"]) >= slot
            for r in runs
        )
        macs = repo.get("macRunners", 1)
        if going:
            busy += macs
        state = "running" if going else "done" if started else "due"
        print(f"{repo['name']}: slot {slot:%H:%M}, {state}, needs {macs} Mac(s)", file=sys.stderr)
        if state == "due":
            waiting.append((slot, repo["name"], macs))

    free = MAC_RUNNERS - busy
    print(f"Macs: {busy} held, {free} free", file=sys.stderr)
    for slot, name, macs in sorted(waiting, key=lambda w: w[0]):
        if macs > free:
            print(f"{name}: waits for {macs} Mac(s); later repos wait behind it", file=sys.stderr)
            break
        free -= macs
        print(name)


if __name__ == "__main__":
    main()
