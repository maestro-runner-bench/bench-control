#!/usr/bin/env bash
# For each repo in repos.json (or only $ONLY): rebase our bench branch, which
# holds only CI changes, onto the latest upstream branch, push it, and start
# its test workflows. A rebase that conflicts (upstream changed the same CI
# files) skips that repo and opens an issue here instead of running stale code.
#
# Needs GH_TOKEN: a token that can push workflow files and start workflows in
# the forks (fine-grained: Contents, Workflows and Actions read/write).
set -uo pipefail

ONLY="${ONLY:-}"
DRY_RUN="${DRY_RUN:-false}"
WORK="${RUNNER_TEMP:-/tmp}/bench-sync"
CONTROL_REPO="${GITHUB_REPOSITORY:-maestro-runner-bench/bench-control}"
status=0

note() { echo "$*"; }

sync_repo() {
  local name=$1 fork=$2 upstream=$3 upstream_branch=$4 branch=$5 workflows=$6
  local dir="$WORK/$name"
  rm -rf "$dir"
  git clone -q --filter=blob:none --single-branch --branch "$branch" \
    "https://x-access-token:${GH_TOKEN}@github.com/${fork}.git" "$dir" || { note "❌ $name: clone failed"; return 1; }
  cd "$dir" || return 1
  git config user.name "maestro-runner-bench"
  git config user.email "bench@devicelab.dev"
  git remote add upstream "https://github.com/${upstream}.git"
  git fetch -q --filter=blob:none upstream "$upstream_branch" || { note "❌ $name: fetch upstream failed"; return 1; }

  local before after behind
  before=$(git rev-parse HEAD)
  behind=$(git rev-list --count HEAD..upstream/"$upstream_branch")
  if [ "$behind" -gt 0 ]; then
    if ! git rebase -q upstream/"$upstream_branch"; then
      local files
      files=$(git diff --name-only --diff-filter=U | tr '\n' ' ')
      git rebase --abort
      note "❌ $name: rebase onto $upstream@$(git rev-parse --short upstream/"$upstream_branch") conflicts in: $files"
      gh issue create -R "$CONTROL_REPO" \
        --title "$name: bench branch no longer rebases onto upstream" \
        --body "Rebasing \`$branch\` of $fork onto $upstream \`$upstream_branch\` conflicts in: $files. The run was skipped; resolve by hand." >/dev/null || true
      return 1
    fi
  fi
  after=$(git rev-parse HEAD)
  if [ "$DRY_RUN" = "true" ]; then
    note "🔍 $name: $behind upstream commit(s) behind; dry run, nothing pushed or started"
    return 0
  fi
  if [ "$before" != "$after" ]; then
    git push -q --force-with-lease="$branch:$before" origin "$branch" || { note "❌ $name: push failed"; return 1; }
  fi
  for wf in $workflows; do
    gh workflow run "$wf" -R "$fork" --ref "$branch" || { note "❌ $name: could not start $wf"; return 1; }
  done
  note "✅ $name: on $upstream@$(git rev-parse --short upstream/"$upstream_branch") ($behind new upstream commit(s)); started $workflows"
}

mkdir -p "$WORK"
count=$(jq length repos.json)
for i in $(seq 0 $((count - 1))); do
  name=$(jq -r ".[$i].name" repos.json)
  if [ -n "$ONLY" ] && [ "$ONLY" != "$name" ]; then continue; fi
  # A scheduled run ("0 <hour> * * *") takes only the repos set to that hour.
  if [ -n "${SCHEDULED_HOUR:-}" ]; then
    hour=$(echo "$SCHEDULED_HOUR" | awk '{print $2}')
    [ "$(jq -r ".[$i].hourUTC" repos.json)" = "$hour" ] || continue
  fi
  ( sync_repo "$name" \
      "$(jq -r ".[$i].fork" repos.json)" \
      "$(jq -r ".[$i].upstream" repos.json)" \
      "$(jq -r ".[$i].upstreamBranch" repos.json)" \
      "$(jq -r ".[$i].branch" repos.json)" \
      "$(jq -r ".[$i].workflows | join(\" \")" repos.json)" ) | tee -a "$WORK/summary.txt" || status=1
  [ "${PIPESTATUS[0]}" -eq 0 ] || status=1
done

if [ -n "${GITHUB_STEP_SUMMARY:-}" ] && [ -f "$WORK/summary.txt" ]; then
  { echo "## Bench sync"; echo; sed 's/^/- /' "$WORK/summary.txt"; } >> "$GITHUB_STEP_SUMMARY"
fi
exit $status
