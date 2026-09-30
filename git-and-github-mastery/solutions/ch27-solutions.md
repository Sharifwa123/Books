# Chapter 27 solutions

## Level 1
**1.1** The graph shows two lines splitting from the same commit: `main` with "Add opening hours" and `add-tea` with "Add tea".

**1.2** The graph becomes a straight line: "Add tea" now sits on top of "Add opening hours".

## Level 2
**2.1** The commit's parent changed, and a commit's hash covers its parent, so the replayed commit is a new commit with a new hash.

**2.2** A fast-forward: `main` had not moved, so Git only moves the pointer.

## Level 3
**3.1** After `git rebase --abort`, `git status` says the working tree is clean, and the graph shows the original fork.

**3.2** Edit the file to remove the markers, `git add menu.md`, `git rebase --continue`, and read the graph: a straight line with your resolution.

## Level 4
**4.1** In the list, leave line 1 as `pick` and change lines 2 and 3 to `squash`. After the rebase, `git log --oneline` shows one commit, whose message contains all three original messages.

## Level 5
**5.1** The colleague still has the old commits, and the learner's branch now has different commits with the same content; the two histories diverge and merging them produces duplicates and conflicts. The learner should have used `git merge` or `git revert` for shared work.

**5.2** In the reflog (Chapter 26<!--ref:reflog-->): find the entry from before `rebase (start)`, and reset the branch to it.

**5.3** They did not stage the resolved file: run `git add menu.md` first, then `git rebase --continue`.
