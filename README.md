# bench-control

Keeps the maestro-runner bench forks on the latest upstream code and runs
them on a schedule.

`repos.json` lists each fork, its upstream branch, our bench branch (which
holds only CI changes: Maestro swapped for maestro-runner) and the workflows
to start. `.github/workflows/sync-and-run.yml` runs nightly, each repo at its own UTC hour (`hourUTC`; add a matching cron line for a new hour), and on demand:
for each repo it rebases the bench branch onto upstream, force-pushes it and
starts the workflows. A rebase that conflicts skips that repo and opens an
issue here.

Setup: add a `BENCH_TOKEN` secret, a fine-grained token for the
`maestro-runner-bench` org with Contents, Workflows and Actions read/write
(GitHub's built-in token cannot push commits that change workflow files).

Run by hand: Actions → Sync and run benches → Run workflow (`only` picks one
repo, `dry_run` rebases without pushing or starting anything).
