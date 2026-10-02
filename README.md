# bench-control

Keeps the maestro-runner bench forks on the latest upstream code and runs
them on a schedule.

`repos.json` lists each fork, its upstream branch, our bench branch (which
holds only CI changes: Maestro swapped for maestro-runner) and the workflows
to start. `.github/workflows/sync-and-run.yml` runs five 4.5-hour cycles a day, each repo in its slots (`slotsUTC`; add a matching cron line for a new slot), and on demand:
for each repo it rebases the bench branch onto upstream, force-pushes it and
starts the workflows. A rebase that conflicts skips that repo and opens an
issue here.

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
