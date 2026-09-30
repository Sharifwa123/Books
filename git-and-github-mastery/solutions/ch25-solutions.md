# Chapter 25 solutions

## Level 1
**1.1** `git status --short` is empty and `cat menu.md` shows the committed content. The edit is gone for good.

**1.2** After `git add`, the status shows `M ` (first column). After `restore --staged`, it shows ` M` (second column): the edit is still in the file, no longer staged.

## Level 2
**2.1** The file shows the older, shorter content; the status shows ` M`. `git restore menu.md` returns it to the latest commit.

**2.2** After `--soft`, the change is staged (`M `) and the commit is gone from the log. `git commit -m "..."` creates the new commit.

## Level 3
**3.1** `--soft`: log loses the commit, change staged. Default: log loses the commit, change in the file but unstaged. `--hard`: log loses the commit and the change is gone from the file.

**3.2** `git reflog` lists the moves, with the lost commit at `HEAD@{1}`; `git reset --hard HEAD@{1}` restores both the commit and the file content.

## Level 4
**4.1** `git revert --no-edit <commit>` adds a new commit that cancels the pie line. `reset` would remove the commit from the branch, but the colleague already has it, so the histories would diverge and force a messy repair (Chapter 23<!--ref:remotes-->).

## Level 5
**5.1** No. The edit was never committed, so Git holds no copy, and the reflog records only moves of `HEAD`. They should have committed the work to a branch or run `git stash` first.

**5.2** Git cannot recover it: `restore` overwrote the file and the edit was never committed. Look outside Git (an editor's undo history or backups).

**5.3** `git reflog`, to find the commit `HEAD` pointed to before the reset; then `git reset --hard <that commit>` (or `HEAD@{1}`).
