#!/usr/bin/env bash
# Characterisation tests for behaviours the book must understand before teaching them.
# These record what the tested Git version DOES; they do not assert what it SHOULD do.
set -u
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null GIT_AUTHOR_NAME=T GIT_AUTHOR_EMAIL=t@example.invalid GIT_COMMITTER_NAME=T GIT_COMMITTER_EMAIL=t@example.invalid
W=$(mktemp -d); cd "$W"; git init -q -b main r && cd r
echo "git version: $(git --version)"
echo one > f; git add f; git commit -qm base
echo two > f; git commit -qam real
git commit -q --allow-empty -m empty
show(){ echo "OBSERVED  $1"; }
git revert --no-edit HEAD~1 >/dev/null 2>&1; show "revert of a NON-empty commit: exit=$?"
git revert --no-edit HEAD~2 >/tmp/rev.out 2>&1; rc=$?; show "revert of an EMPTY commit (auto-commit): exit=$rc; output: $(tr '\n' '|' </tmp/rev.out)"
git status --short | wc -l | sed 's/^/OBSERVED  working-tree changes left after failed empty revert: /'
git revert --no-commit HEAD~2 >/dev/null 2>&1; show "revert --no-commit of the EMPTY commit: exit=$?"
git status --short | wc -l | sed 's/^/OBSERVED  changes staged by that no-commit revert: /'
git commit -q --allow-empty -m "manual commit after no-commit revert" >/dev/null 2>&1; show "manual 'git commit --allow-empty' afterwards: exit=$?"
git switch -q -c side HEAD~4 2>/dev/null || git switch -q -c side "$(git rev-list --max-parents=0 HEAD)"
E=$(git log --format=%H --grep='^empty$' main | head -1)
git cherry-pick "$E" >/tmp/cp.out 2>&1; show "cherry-pick of an EMPTY commit: exit=$?; output: $(head -3 /tmp/cp.out | tr '\n' '|')"
git cherry-pick --abort >/dev/null 2>&1
git cherry-pick --allow-empty "$E" >/dev/null 2>&1; show "cherry-pick --allow-empty of the same commit: exit=$?"
git revert -h 2>&1 | grep -qiE 'allow-empty|keep-redundant' && show "git revert usage lists an empty-commit option" || show "git revert usage lists NO empty-commit option (allow-empty/keep-redundant-commits)"
git cherry-pick -h 2>&1 | grep -qiE 'allow-empty' && show "git cherry-pick usage lists --allow-empty" || show "git cherry-pick usage lists NO --allow-empty"
cd /; rm -rf "$W"
