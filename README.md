# bench-control

Keeps the maestro-runner bench forks on the latest upstream code and runs
them back to back.

`repos.json` lists each fork, its upstream branch, our bench branch (which
holds only CI changes: Maestro swapped for maestro-runner), the workflows to
start and how many macOS runners it needs at once (`macRunners`). Starting a
repo rebases its bench branch onto upstream, force-pushes it and starts the
workflows (`scripts/sync-and-run.sh`); a rebase that conflicts skips that
repo and opens an issue here.

`.github/workflows/bench-loop.yml` runs the benches in cycles. A cycle starts
with React Native (first in `repos.json`); the others start beside it as
macOS runners come free, counted live from the running and queued macOS jobs
(the free org runs 5 at once); when all have run, the next cycle starts.
Nothing starts while a macOS job is queued, so no bench waits for a Mac
because of another. The loop checks every 5 minutes (`scripts/plan.py`
decides), runs for about 5h40m and then starts a new copy of itself; an
hourly cron only restarts it if that chain breaks.

Setup: add a `BENCH_TOKEN` secret, a fine-grained token for the
`maestro-runner-bench` org with Contents, Workflows and Actions read/write
(GitHub's built-in token cannot push commits that change workflow files).

Run by hand: Actions → Sync and run benches → Run workflow (`only` picks one
repo, `dry_run` rebases without pushing or starting anything).

## Results

`.github/workflows/collect.yml` runs daily (23:30 UTC, or by hand) and reads
the e2e jobs of the bench forks and of upstream (Maestro, or agent-device for
React Navigation): `scripts/collect.py` appends one record per job to
`results/jobs.jsonl` (e2e step time, conclusion, flows, first-attempt
failures, final failures, retry round, runner) and rewrites
`results/SUMMARY.md`, the side-by-side comparison per project, platform and
flavour.
