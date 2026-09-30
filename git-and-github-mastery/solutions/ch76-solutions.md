# Chapter 76 solutions

## Level 1
**1.1** (a) amend; (b) revert; (c) squash with `git reset --soft main` and one new commit; (d) cherry-pick (with `-x`).

**1.2** `git status`, `git log` (with a format such as `--format=%s`) and `git diff`.

## Level 2
**2.1** As in the recording: `git switch -c`, edit, `git commit -am`, `git push -u origin BRANCH`, then in a second clone `git merge --no-ff origin/BRANCH` and push; in yours `git fetch`, `git switch main`, `git merge --ff-only origin/main`, `git branch -d BRANCH`, `git push origin --delete BRANCH`.

**2.2** The reflog entry expires after some time (Chapter 26<!--ref:reflog-->), and unreferenced commits may be removed by garbage collection, so the recovery would no longer be possible.

## Level 3
**3.1** Answers vary. A good scenario states who else has the commits, chooses a tool accordingly, and shows the output before and after.

**3.2** After the resolution the history has a merge commit with two parents; after the abort the history and working tree are as before the merge attempt.

## Level 4
**4.1** Revoke or rotate the key first, because anyone who saw the repository may have it; then remove the file from tracking and add it to `.gitignore`; explain that the key is still in earlier commits and in clones and forks; rewrite history only if needed, with the team informed; check where else the key was used.

## Level 5
**5.1** Check with `git log main..branch` (no output means everything is in `main`) or `git branch --merged main`. `-D` is acceptable only when you have confirmed that you do not need the unmerged commits, or that they exist elsewhere.

**5.2** The cherry-pick was made on another branch; it conflicted and was left unfinished; the wrong commit was picked; or the local `main` was not pushed or updated.
