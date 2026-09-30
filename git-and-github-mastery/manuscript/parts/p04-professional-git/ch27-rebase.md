---
key: rebase
number: 27
tag: Deep
first_read: later
status: draft
requires: [conflicts, reflog, remotes]
ledger: [R190, R191, R192]
---
# Chapter 27 — Rebase [Deep]

**In this chapter**

- what rebase does, and how it differs from merge
- `git rebase <branch>`: replay your commits on a new base
- rebase conflicts, and `--abort` and `--continue`
- `git rebase -i`: combining commits
- the golden rule: never rebase commits that others already have

> **Deep.** This chapter is marked **[Deep]**. You can skip it on a first read and return after Chapter 34<!--ref:workflows-->. Merge (Chapter 21<!--ref:merging-->) is enough to work with Git.

**Before you start.** Chapter 21<!--ref:merging-->, Chapter 22<!--ref:conflicts-->, Chapter 26<!--ref:reflog--> and Chapter 23<!--ref:remotes-->. The recordings use `bakery-menu` and were run in Bash and zsh on Git 2.43.0, then re-run in CI on Git 2.55.0.

---

## 27.1 The problem rebase solves

Chapter 21<!--ref:merging--> joined two diverged branches with a **merge commit**. That is honest, and it leaves a history with many small merges. Some teams prefer a **straight line**, where the work of a branch appears *after* the work that was already on `main`. **Rebase** does that.

> **New term: rebase.** Take the commits of one branch and replay them, one by one, on top of another commit. The replayed commits are **new commits**, with new hashes.

---

## 27.2 Rebase a branch onto `main`

The same starting situation as the three-way merge: `main` got "Add opening hours", `add-tea` got "Add tea". They have diverged:

```text
$ git switch -c add-tea
Switched to a new branch 'add-tea'
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[add-tea 73ad7ed] Add tea
 1 file changed, 1 insertion(+)
$ git switch main
Switched to branch 'main'
$ printf 'Open Monday to Saturday.\n' > hours.md
$ git add hours.md
$ git commit -m "Add opening hours"
[main 1e5eef8] Add opening hours
 1 file changed, 1 insertion(+)
 create mode 100644 hours.md
$ git log --oneline --all --graph
* 1e5eef8 (HEAD -> main) Add opening hours
| * 73ad7ed (add-tea) Add tea
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase.bash.txt`.*

Now, standing on `add-tea`, rebase it onto `main`:

```text
$ git switch add-tea
Switched to branch 'add-tea'
$ git rebase main
Successfully rebased and updated refs/heads/add-tea.
```

*Recorded in Bash; `ch27-rebase/expected-rebase.bash.txt`.*

Read what happened. Git took the commit "Add tea", set it aside, moved to the tip of `main`, and applied it there again. The graph is now a straight line:

```text
$ git log --oneline --all --graph
* 2cc423d (HEAD -> add-tea) Add tea
* 1e5eef8 (main) Add opening hours
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase.bash.txt`.*

Look at the hash. Before: `73ad7ed Add tea`. After: `2cc423d Add tea`. **The commit was not moved; it was copied.** The content of the change is the same, but its parent is different, so it is a different commit, with a different hash. The old commit still exists (Chapter 26<!--ref:reflog-->), but no branch points to it.

Now `main` can absorb the branch with a plain fast-forward (Chapter 21<!--ref:merging-->):

```text
$ git switch main
Switched to branch 'main'
$ git merge add-tea
Updating 1e5eef8..2cc423d
Fast-forward
 menu.md | 1 +
 1 file changed, 1 insertion(+)
$ git log --oneline --graph
* 2cc423d (HEAD -> main, add-tea) Add tea
* 1e5eef8 Add opening hours
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase.bash.txt`.*

There is no merge commit: the history reads as if the tea had been added after the opening hours.

**Merge or rebase?** They produce the same *content*. Merge keeps the true shape of the work, including the fork; rebase gives a tidy line but *rewrites* the branch's commits. Chapter 34<!--ref:workflows--> compares the styles.

---

## 27.3 When rebase hits a conflict

Both branches changed the same line, as in Chapter 22<!--ref:conflicts-->:

```text
$ git switch -c raise-bread
Switched to a new branch 'raise-bread'
$ printf '# Sunrise Bakery menu\n\n- White loaf: 3.00\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git commit -am "Raise the white loaf to 3.00"
[raise-bread 73e14f7] Raise the white loaf to 3.00
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git switch main
Switched to branch 'main'
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.90\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git commit -am "Raise the white loaf to 2.90"
[main 4afeda6] Raise the white loaf to 2.90
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git switch raise-bread
Switched to branch 'raise-bread'
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

Rebase applies your commits **one at a time**, and each may conflict:

```text
$ git rebase main
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
error: could not apply 73e14f7... Raise the white loaf to 3.00
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 73e14f7... Raise the white loaf to 3.00
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

Git stops in the middle and says which commit it could not apply, and it lists the ways out. *(On newer Git versions, 2.55.0 was tested, the output has one more hint line about `advice.mergeConflict`, and the commit subject is shown with a `# ` before it, as in `Could not apply 73e14f7... # Raise the white loaf to 3.00`. The meaning is the same.)* Ask for the state:

```text
$ git status
interactive rebase in progress; onto 4afeda6
Last command done (1 command done):
   pick 73e14f7 Raise the white loaf to 3.00
No commands remaining.
You are currently rebasing branch 'raise-bread' on '4afeda6'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
	both modified:   menu.md

no changes added to commit (use "git add" and/or "git commit -a")
$ git diff --name-only --diff-filter=U
menu.md
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

Two details differ from a merge conflict. The status says `interactive rebase in progress` (even though this rebase was not interactive; the name is Git's), and it names the commit being replayed. And, confusingly, which side is which is **reversed**: the "current" side (`HEAD`) is `main` (the base you are rebasing onto), and the side being applied is *your* commit.

You can walk away:

```text
$ git rebase --abort
$ git status
On branch raise-bread
nothing to commit, working tree clean
$ git log --oneline --all --graph
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

`git rebase --abort` puts the branch back as it was before you started:

```text
* 4afeda6 (main) Raise the white loaf to 2.90
| * 73e14f7 (HEAD -> raise-bread) Raise the white loaf to 3.00
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

Or you can resolve it. Start again, and this time fix the file, stage it, and continue:

```text
$ git rebase main
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
error: could not apply 73e14f7... Raise the white loaf to 3.00
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 73e14f7... Raise the white loaf to 3.00
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.95\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git add menu.md
$ git rebase --continue
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

(`hint: Waiting for your editor to close the file...` appears because Git opens an editor for the commit message; the recording's editor closes at once. In your own terminal you would see your editor open, and you would save and close it.)

```text
hint: Waiting for your editor to close the file...
[detached HEAD 608311e] Raise the white loaf to 3.00
 1 file changed, 1 insertion(+), 1 deletion(-)
Successfully rebased and updated refs/heads/raise-bread.
$ git log --oneline --all --graph
* 608311e (HEAD -> raise-bread) Raise the white loaf to 3.00
* 4afeda6 (main) Raise the white loaf to 2.90
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

The result is a straight line again: "Raise the white loaf to 3.00" now sits on top of `main`, and its content is the resolution you chose (2.95).

**The rebase checklist for conflicts:**

1. Read `git status`.
2. Edit the file; remove the markers (Chapter 22<!--ref:conflicts-->).
3. `git add <file>`.
4. `git rebase --continue`.
5. Repeat for each commit that conflicts, or `git rebase --abort` to stop.

---

## 27.4 Interactive rebase: combining commits

`git rebase -i` (interactive) lets you edit a list of commits before they are replayed: keep, combine, reword, reorder or drop. A common use is to tidy several small commits into one before sharing them.

In a rebase, to **squash** a commit is to combine it into the one before it. (Chapter 21<!--ref:merging--> used the word for `git merge --squash`; the effect is similar, the mechanism different.)

Three small commits were made:

```text
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[main 60cb0bb] Add tea
 1 file changed, 1 insertion(+)
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -am "Add coffee"
[main bf6d066] Add coffee
 1 file changed, 1 insertion(+)
$ printf -- '- Juice: 2.20\n' >> menu.md
$ git commit -am "Add juice"
[main bde8e38] Add juice
 1 file changed, 1 insertion(+)
$ git log --oneline
bde8e38 (HEAD -> main) Add juice
bf6d066 Add coffee
60cb0bb Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-squash.bash.txt`.*

Normally, `git rebase -i HEAD~3` opens your editor with a list such as `pick <hash> Add tea`, one line per commit. You change `pick` to `squash` on the lines that should be folded into the first. The recording cannot open an editor, so it does the same edit with a program (`sed`), through the variable `GIT_SEQUENCE_EDITOR`. In your own work you edit the list by hand.

```text
$ GIT_SEQUENCE_EDITOR="sed -i -e '2s/^pick/squash/' -e '3s/^pick/squash/'" git rebase -i HEAD~3
hint: Waiting for your editor to close the file...
hint: Waiting for your editor to close the file...
[detached HEAD 69d6e2b] Add tea
 Date: Mon Jan 5 09:09:00 2026 +0000
 1 file changed, 3 insertions(+)
Successfully rebased and updated refs/heads/main.
```

*Recorded in Bash; `ch27-rebase/expected-squash.bash.txt`.*

The recorded run changed the second and third lines from `pick` to `squash`. Git combined all three commits into one. It also gave you a chance to edit the combined message (the editor was closed at once here):

```text
$ git log --oneline
69d6e2b (HEAD -> main) Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
$ git log -1 --format=%B
Add tea

Add coffee

Add juice

```

*Recorded in Bash; `ch27-rebase/expected-squash.bash.txt`.*

```text
$ git show --stat --oneline HEAD
69d6e2b (HEAD -> main) Add tea
 menu.md | 3 +++
 1 file changed, 3 insertions(+)
```

*Recorded in Bash; `ch27-rebase/expected-squash.bash.txt`.*

The three commits are now one, and the message shows all three original messages.

> **Verification pending [R192].** Only the `squash` action of `git rebase -i` was run, with the list edited by a program. The other actions (`reword`, `edit`, `drop`, reorder) and the real interactive editor flow were not run and are not described here. The official documentation could not be reached to check the current list of actions.

---

## 27.5 The golden rule

Because rebase **replaces commits with new ones**, it is safe only for commits that nobody else has.

> **⚠️ CAUTION. Never rebase commits that you have already shared** (pushed to a place where others may have pulled them). Rebasing them creates *different* commits with the same content. Your colleagues still have the old ones; the two versions of history then have to be reconciled, and that is painful and easy to get wrong. Rebase your **own, local, unpublished** work. For shared work, use merge or `git revert` (Chapter 25<!--ref:undo-->).

A rebased branch that was already pushed can only be pushed again by **forcing** the push, which overwrites the remote's branch. Chapter 33<!--ref:gitsec--> returns to the dangers of forced pushes.

> **Verification pending [R191].** Two options are commonly used with rebase and are *not* demonstrated here: `git pull --rebase` (fetch, then rebase instead of merge) and `git push --force-with-lease` (a safer forced push). Their exact behaviour was not tested for this chapter and must be checked before the book relies on them.

If a rebase goes wrong and you have already finished it, the reflog (Chapter 26<!--ref:reflog-->) still holds the state from before: find the entry from before `rebase (start)` and reset to it.

---

## Checkpoint

## What You Learned

- Rebase replays a branch's commits on top of another commit, giving a straight history.
- The replayed commits are *new* commits with new hashes; the originals remain until they expire.
- A rebase can conflict once per commit; resolve, `git add`, `git rebase --continue`, or `git rebase --abort`.
- `git rebase -i` edits the list of commits; `squash` combines them.
- Never rebase commits that others already have.

## New Vocabulary

- **Rebase**: replay commits on top of another commit, producing new commits.

## Commands Learned

`git rebase <branch>`, `git rebase --abort`, `git rebase --continue`, `git rebase -i`.

## Common Mistakes

1. **Rebasing shared commits.**
2. **Confusing which side is which in a rebase conflict.**
3. **Forgetting `git rebase --continue` after resolving.**
4. **Being surprised that hashes change.**
5. **Rebasing with uncommitted work in the tree.**

## Practice

Do the exercises in [`exercises/ch27-exercises.md`](../../../exercises/ch27-exercises.md).

## Self-Test

1. What happens to the hash of a commit when it is rebased, and why?
2. Which branch do you stand on when you run `git rebase main` to bring `add-tea` up to date?
3. What are the three ways out of a rebase conflict?
4. What does `squash` do in an interactive rebase?
5. State the golden rule of rebase.

## Before Moving On

You are ready for Chapter 28<!--ref:tools--> if you can:

- [ ] rebase a local branch onto `main`
- [ ] abort a rebase and resolve one
- [ ] explain why rebasing shared commits is dangerous
- [ ] combine commits with a squash

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Rebase of a diverged branch, new hashes, fast-forward afterwards | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R190 |
| Rebase conflict, `--abort`, `--continue` | Locally tested (as above) | R190 |
| Interactive `squash` (list edited by a program) | Locally tested (as above); other actions and the real editor flow not run | R192 |
| `pull --rebase`, `--force-with-lease` | **Not tested** | R191 |

## Where this leads

Chapter 28<!--ref:tools--> adds cherry-pick, bisect and patches, which also copy commits. Chapter 34<!--ref:workflows--> compares merge-based and rebase-based team workflows, and Chapter 33<!--ref:gitsec--> returns to forced pushes.
