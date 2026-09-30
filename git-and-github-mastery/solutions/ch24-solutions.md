# Chapter 24 solutions

## Level 1
**1.1** After `git stash`, the status is empty (for tracked files) and the list shows `stash@{0}: WIP on main: ...`. `git stash pop` restores the edit and drops the entry.

**1.2** The log shows `tag: v1.0, tag: v0.1` beside the commit.

## Level 2
**2.1** With plain `git stash`, `ideas.txt` stays because it is untracked. With `git stash -u` it is shelved too, and the tree is completely clean.

**2.2** `git clean -n` lists only files; `git clean -n -d` also lists untracked folders.

## Level 3
**3.1** `git grep -n "Rolls"` gives `menu.md:4:...`; `git grep "loaf" HEAD~2` shows the older price with the `HEAD~2:` prefix.

**3.2** The hash on line 3 names the commit that last changed that line; `git show <hash>` shows that change.

## Level 4
**4.1** `git stash -u`, `git switch other-branch`, make the fix, `git switch main`, `git stash pop`.

## Level 5
**5.1** `git stash list` shows entries; `git stash show -p stash@{0}` shows the content. (The `show` form was not recorded for this book; check it with your own Git before relying on it.)

**5.2** No. Untracked files were never committed, so Git holds no copy. This is why `-n` comes first.

**5.3** No. Deleting a tag removes only the name; the commit remains and can be found through the branch history, and the tag can be recreated on it.
