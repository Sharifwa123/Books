# Chapter 21 solutions

## Level 1
**1.1** The output shows `Updating <old>..<new>` and `Fast-forward`; the history stays a straight line.

**1.2** `main` moved forward to the tea commit; `add-tea` did not move. Both now point to the same commit.

## Level 2
**2.1** `git switch -c add-tea`, edit and commit, `git switch main`, add `hours.md` and commit, then `git merge --no-edit add-tea`. `git log --merges` lists one commit, `Merge branch 'add-tea'`.

**2.2** Two parents: the previous tip of `main` and the tip of `add-tea`. Note that `git show --stat` on a merge commit lists the changes brought in from the other branch.

## Level 3
**3.1** With `--no-ff` the graph joins two lines even though a fast-forward was possible, whereas 1.2 showed a straight line.

**3.2** `git merge --squash <branch>`, `git status --short` shows the new file staged, `git commit -m "..."`. The squash commit has one parent only, so nothing in the history refers to the branch.

## Level 4
**4.1** Squash merge: one commit per feature, straight history. Lost: the individual commits and the record that a branch existed. Commands: `git switch main`, `git merge --squash feature`, `git commit -m "Add feature"`.

## Level 5
**5.1** The work is in `main`, but Git cannot see the branch's commits there because the squash created a new commit. Check with `git diff main feature` (no output means the content matches) or `git log --oneline main`; then `git branch -D feature`.

**5.2** The merge went the wrong way: `git merge main` on `add-tea` brought `main` into `add-tea`, which changed `add-tea` and left `main` alone. Switch to `main` and run `git merge add-tea`.
