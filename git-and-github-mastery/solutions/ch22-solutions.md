# Chapter 22 solutions

## Level 1
**1.1** Git prints `Auto-merging menu.md`, `CONFLICT (content): Merge conflict in menu.md` and `Automatic merge failed; fix conflicts and then commit the result.`

**1.2** `You have unmerged paths` and `both modified: menu.md`. The second command prints `menu.md`.

## Level 2
**2.1** `HEAD` (between `<<<<<<<` and `=======`) holds 2.90; the `raise-bread` side holds 3.00.

**2.2** Replace the whole conflicted block with `- White loaf: 2.95`, run `git add menu.md`, then `git commit -m "Merge raise-bread, settling on 2.95"`. The graph shows a merge commit with two parents.

## Level 3
**3.1** After `--abort`, `git status` says the working tree is clean, `menu.md` shows 2.90, and the graph shows two diverged branches.

**3.2** With `diff3`, a `|||||||` line begins a section that holds the ancestor's line, `White loaf: 2.80`.

## Level 4
**4.1** After resolving and staging one file, `git status` still lists the other under `Unmerged paths`. Only when every file is resolved and staged does Git say `All conflicts fixed but you are still merging`; then `git commit` concludes.

## Level 5
**5.1** The marker lines were staged and committed because Git does not check for them. Edit the file to remove the markers and make a new commit, for example `git commit -am "Remove leftover conflict markers"`. Do not rewrite shared history.

**5.2** Either no merge was in progress (it was already committed or aborted), or the conflict came from another operation such as a rebase or cherry-pick, which has its own abort command.
