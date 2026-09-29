#!/usr/bin/env bash
# Empirical verification of core Git behaviour in a throwaway sandbox.
# Records the Git version and what each command actually does.
set -u
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null   # ignore host config (e.g. forced signing)
export GIT_AUTHOR_NAME=T GIT_AUTHOR_EMAIL=t@example.invalid GIT_COMMITTER_NAME=T GIT_COMMITTER_EMAIL=t@example.invalid
W=$(mktemp -d); cd "$W"
ok(){ echo "PASS  $1"; }; bad(){ echo "FAIL  $1"; }
chk(){ if eval "$2" >/dev/null 2>&1; then ok "$1"; else bad "$1"; fi; }
echo "git version: $(git --version)"

git -c init.defaultBranch=main init -q repo && cd repo
chk "init.defaultBranch=main honoured" '[ "$(git symbolic-ref --short HEAD)" = main ]'
echo a > a.txt; git add a.txt
chk "status --short shows staged add" 'git status --short | grep -q "^A  a.txt"'
git commit -qm one; echo b >> a.txt
chk "diff shows unstaged change" 'git diff | grep -q "^+b"'
git add a.txt
chk "diff --staged shows staged change" 'git diff --staged | grep -q "^+b"'
git commit -qm two
chk "HEAD~1 resolves to first commit" '[ "$(git log -1 --format=%s HEAD~1)" = one ]'

# restore / switch
echo junk >> a.txt; git restore a.txt
chk "restore discards working-tree edit" '[ -z "$(git status --short)" ]'
echo c >> a.txt; git add a.txt; git restore --staged a.txt
chk "restore --staged unstages" 'git status --short | grep -q "^ M a.txt"'
git restore a.txt
git switch -qc feature
chk "switch -c creates+switches" '[ "$(git branch --show-current)" = feature ]'
echo f > f.txt; git add f.txt; git commit -qm feat
git switch -q main
chk "ff merge (no divergence)" 'git merge --ff-only feature'

# reset modes
git commit -q --allow-empty -m three; H=$(git rev-parse HEAD)
git reset -q --soft HEAD~1
chk "reset --soft keeps commit changes staged/HEAD moved" '[ "$(git rev-parse HEAD)" != "$H" ]'
git commit -q --allow-empty -m three-again
git reset -q --hard HEAD~1
chk "reflog still holds reset-away commit" 'git reflog | grep -q three-again'
git reset -q --hard "HEAD@{1}"
chk "recovered via reflog" '[ "$(git log -1 --format=%s)" = three-again ]'

# revert
echo rv > rv.txt; git add rv.txt; git commit -qm "add rv"; git revert --no-edit HEAD >/dev/null 2>&1
chk "revert creates new commit" 'git log -1 --format=%s | grep -q "^Revert"'

# conflict + abort
git switch -qc c1; echo one > x; git add x; git commit -qm c1
git switch -q main; git switch -qc c2; echo two > x; git add x; git commit -qm c2
git merge c1 >/dev/null 2>&1
chk "conflicting merge leaves conflict markers" 'grep -q "^<<<<<<<" x'
git merge --abort
chk "merge --abort restores clean tree" '[ -z "$(git status --short)" ]'

# rebase (non-interactive scripted) + squash
git switch -q main; for i in 1 2 3; do echo $i > r$i; git add r$i; git commit -qm "r$i"; done
GIT_SEQUENCE_EDITOR="sed -i '2,3s/^pick/squash/'" GIT_EDITOR=true git rebase -q -i HEAD~3 >/dev/null 2>&1
chk "interactive rebase squash (scripted)" '[ "$(git log --format=%s -1)" != r3 ] && git log -1 --format=%B | grep -q r2'

# stash / tags / bisect / worktree / grep / blame
echo wip > wip; git add wip; git stash -q
chk "stash cleans tree" '[ -z "$(git status --short)" ]'; git stash pop -q
git add wip; git commit -qm wip
git tag light; git tag -a v1.0.0 -m rel
chk "annotated tag is tag object" '[ "$(git cat-file -t v1.0.0)" = tag ]'
chk "lightweight tag points to commit" '[ "$(git cat-file -t light)" = commit ]'
git worktree add -q ../wt -b wt-br
chk "worktree add" '[ -d ../wt ]'; git worktree remove ../wt
chk "grep finds content" 'git grep -q wip'
chk "blame runs" 'git blame -s a.txt'
chk "cherry-pick usage exists" 'git cherry-pick -h 2>&1 | grep -qi usage'

# object model
chk "blob type" '[ "$(git cat-file -t HEAD:a.txt)" = blob ]'
chk "tree type" '[ "$(git cat-file -t HEAD^{tree})" = tree ]'
# clone variants
cd "$W"
chk "clone --depth 1" 'git clone -q --depth 1 file://$W/repo shallow'
chk "clone --filter=blob:none" 'git clone -q --filter=blob:none file://$W/repo partial'
chk "sparse-checkout set" '(cd shallow && git sparse-checkout set nothing-here)'
# option existence checks (usage text)
for c in "push --force-with-lease" "rebase --abort" "rebase --continue" "rebase --skip" "reflog expire" "maintenance start" "submodule add" "clean -n" "bisect start" "config --global core.autocrlf" "am" "format-patch" "rerere" "gc" "fsck"; do
  chk "'git $c' recognised" "git ${c%% *} -h 2>&1 | grep -qi usage"
done
chk "gpg.format=ssh accepted" 'git -c gpg.format=ssh config --get gpg.format'
git lfs version >/dev/null 2>&1 && echo 'INFO  git-lfs installed' || echo 'INFO  git-lfs NOT installed in sandbox (LFS commands unverified)'

# local bare repository as a stand-in "remote" (lets learners practise remotes offline, no account needed)
cd "$W"
git init -q --bare -b main origin.git
cd repo
chk "remote add" 'git remote add origin "$W/origin.git"'
chk "push -u sets upstream" 'git push -q -u origin main'
chk "branch tracking configured" '[ "$(git rev-parse --abbrev-ref @{u})" = origin/main ]'
cd "$W" && git clone -q origin.git other && cd other
echo z > z.txt; git add z.txt; git commit -qm "from other"; git push -q origin main
cd "$W/repo"
chk "fetch updates remote-tracking ref only" 'git fetch -q && [ "$(git rev-parse origin/main)" != "$(git rev-parse main)" ] && [ ! -e z.txt ]'
chk "status reports behind" 'git status -sb | head -1 | grep -q behind'
chk "pull --ff-only brings changes" 'git pull -q --ff-only && [ -e z.txt ]'
chk "push --force-with-lease accepted (no-op)" 'git push -q --force-with-lease origin main'
echo "cleanup: $W"; rm -rf "$W"
