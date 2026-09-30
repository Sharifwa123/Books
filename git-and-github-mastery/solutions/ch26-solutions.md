# Chapter 26 solutions

## Level 1
**1.1** `HEAD@{0}` is the newest entry: the current position of `HEAD`. The text describes the event, for example `commit: Add coconut cake`.

**1.2** `git branch -D experiment` prints `Deleted branch experiment (was <hash>).`

## Level 2
**2.1** `git branch experiment-restored <hash>`; `git log --oneline experiment-restored` shows the commit.

**2.2** `git reflog` shows a `commit:` line for the experiment commit; `git branch experiment-restored HEAD@{1}` (or the appropriate `HEAD@{n}`).

## Level 3
**3.1** Git says it is leaving one commit behind, connected to none of your branches, and prints `git branch <new-branch-name> <hash>`.

**3.2** Find the `commit:` line in the reflog, note the hash, and run `git branch rescued <hash>`.

## Level 4
**4.1** `git reflog` to find the commit `HEAD` pointed to before the reset (often `HEAD@{1}`), then `git reset --hard HEAD@{1}` (or the hash). Check `git status` first, because `--hard` discards uncommitted changes.

## Level 5
**5.1** The reflog is local and is not copied by cloning. A fresh clone starts with just a `clone:` entry, and the colleague's branch was never in it.

**5.2** Git cannot help: the reflog records commits and moves, not uncommitted edits. Try the editor's undo history or a backup.

**5.3** `git switch -c <new-name>` from the detached state (or `git branch <new-name>` and then switch); the new branch points at the current commit and keeps all five.
