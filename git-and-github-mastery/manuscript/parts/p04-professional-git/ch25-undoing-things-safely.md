---
key: undo
number: 25
tag: Core
first_read: full
status: draft
requires: [commits, merging]
ledger: [R184, R185, R186, R355]
---
# Chapter 25 — Undoing Things Safely [Core]

**In this chapter**

- how to tell *what* you want to undo before you type anything
- `git restore`: discard an edit, or unstage a file
- `git reset`: move a branch back, in three strengths (`--soft`, default, `--hard`)
- `git revert`: undo a commit by adding a new one
- which of these can lose work, and which cannot

**Before you start.** Chapter 19<!--ref:commits-->, Chapter 17<!--ref:history_view--> and Chapter 20<!--ref:branching-->. The recordings use the `bakery-menu` repository and were run in Bash and zsh on Git 2.43.0, then re-run in CI on Git 2.55.0.

Everyone makes mistakes with Git. Almost all of them can be undone, but *which* command is right depends on where the mistake is. So the first skill is diagnosis.

---

## 25.1 First, find where the mistake is

Chapter 15<!--ref:model--> described three places where your work lives: the **working tree** (your files), the **index** (what you have staged) and the **repository** (the commits). An undo command works on one or more of them.

| The mistake is... | You want to... | Use |
|---|---|---|
| an edit in a file, not yet staged | throw the edit away | `git restore <file>` |
| a file staged by mistake | unstage it, keep the edit | `git restore --staged <file>` |
| the last commit(s), not yet shared | move the branch back | `git reset` |
| a commit that is already shared | add a new commit that cancels it | `git revert` |

Before any undo, run `git status` and `git log --oneline`. Read them. Then choose.

> **⚠️ CAUTION.** Some undo commands are safe and some destroy work. This chapter marks them. The rule: a command that *discards uncommitted changes* is permanent, because Git never saw those changes.

---

## 25.2 `git restore`: discard an edit

You changed the white loaf price to 9.99 by mistake:

```text
$ printf '# Sunrise Bakery menu\n\n- White loaf: 9.99\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git status --short
 M menu.md
```

*Recorded in Bash; `ch25-undo/expected-restore.bash.txt`.*

`git diff` shows the change:

```text
$ git diff
diff --git a/menu.md b/menu.md
index 97e3bea..d71ff95 100644
--- a/menu.md
+++ b/menu.md
@@ -1,5 +1,5 @@
 # Sunrise Bakery menu

-- White loaf: 2.80
+- White loaf: 9.99
 - Rolls (six): 3.00
 - Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch25-undo/expected-restore.bash.txt`.*

To bring the file back to how it was at the last commit:

```text
$ git restore menu.md
$ git status --short
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.80
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch25-undo/expected-restore.bash.txt`.*

> **New term: git restore.** Restores files from the index or from a commit into your working tree, or (with `--staged`) into the index.

The file is back and `git status --short` is empty. The edit is **gone for good**: it was never committed, so Git kept no copy.

> **⚠️ CAUTION.** `git restore <file>` throws away uncommitted edits permanently. Run `git diff <file>` first if you are not sure that you want that.

---

## 25.3 `git restore --staged`: unstage

You staged a change (a tea line) and realised it does not belong in the next commit:

```text
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n- Tea: 1.50\n' > menu.md
$ git add menu.md
$ git status --short
M  menu.md
```

*Recorded in Bash; `ch25-undo/expected-restore.bash.txt`.*

`M ` (the first column) means the change is staged. To take it out of the index, without touching the file:

```text
$ git restore --staged menu.md
$ git status --short
 M menu.md
```

*Recorded in Bash; `ch25-undo/expected-restore.bash.txt`.*

Now the status shows ` M` (the second column): still modified, no longer staged. The edit is safe in the file. If you also want to discard the edit:

```text
$ git restore menu.md
$ git status --short
```

*Recorded in Bash; `ch25-undo/expected-restore.bash.txt`.*

The two columns of `git status --short` are worth remembering: the **first** is the index, the **second** is the working tree.

---

## 25.4 Restoring from an older commit

`git restore` can also fetch a file from **any commit**. Here `--source=HEAD~2` takes `menu.md` from two commits back:

```text
$ git restore --source=HEAD~2 menu.md
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.50
- Rolls (six): 3.00
```

*Recorded in Bash; `ch25-undo/expected-restore.bash.txt`.*

The file now shows the old content (`2.50`, only two lines). Git reports it as modified, as any change from the last commit would be:

```text
$ git status --short
 M menu.md
$ git restore menu.md
$ git status --short
```

*Recorded in Bash; `ch25-undo/expected-restore.bash.txt`.*

The last `git restore menu.md` brings the file back to the latest commit. Nothing was committed by the experiment. This is a safe way to look at, or take back, an old version of a single file.

---

## 25.5 `git reset`: move the branch back

`git restore` deals with files. `git reset` moves **the branch** (and `HEAD`) to a different commit. It has three strengths. To show them, two commits are added:

```text
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[main 60cb0bb] Add tea
 1 file changed, 1 insertion(+)
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -am "Add coffee"
[main bf6d066] Add coffee
 1 file changed, 1 insertion(+)
$ git log --oneline
bf6d066 (HEAD -> main) Add coffee
60cb0bb Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch25-undo/expected-reset.bash.txt`.*

### `--soft`: undo the commit, keep everything staged

```text
$ git reset --soft HEAD~1
$ git status --short
M  menu.md
$ git log --oneline
60cb0bb (HEAD -> main) Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch25-undo/expected-reset.bash.txt`.*

The commit "Add coffee" is gone from the log, but the change is still **staged** (`M `). It is as if you had run `git add` but not `git commit`. Use this to redo a commit, for instance to combine it with the next one.

```text
$ git commit -m "Add coffee"
[main 1558157] Add coffee
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch25-undo/expected-reset.bash.txt`.*

### Default (`--mixed`): undo the commit, keep the changes unstaged

```text
$ git reset HEAD~1
Unstaged changes after reset:
M	menu.md
$ git status --short
 M menu.md
$ git log --oneline
60cb0bb (HEAD -> main) Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch25-undo/expected-reset.bash.txt`.*

The commit is gone, and the change is still in the file (` M`), but no longer staged. Git prints `Unstaged changes after reset:` to list what it left in your files. (The wording of that message may differ in other Git versions.) This is the default: `git reset HEAD~1` with no option.

### `--hard`: undo the commit and discard the change

```text
$ git commit -am "Add coffee"
[main df83910] Add coffee
 1 file changed, 1 insertion(+)
$ git reset --hard HEAD~1
HEAD is now at 60cb0bb Add tea
$ git status --short
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.80
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
- Tea: 1.50
```

*Recorded in Bash; `ch25-undo/expected-reset.bash.txt`.*

`HEAD is now at 60cb0bb Add tea` says the branch moved. The file no longer has the coffee line. `--hard` also reset your **working tree** to match.

> **New term: git reset.** Moves the current branch to another commit. `--soft` leaves the index and working tree alone; the default also resets the index; `--hard` resets the index **and** the working tree.

| Option | Branch moves | Index reset | Working tree reset | Can lose uncommitted work? |
|---|---|---|---|---|
| `--soft` | yes | no | no | no |
| (default) | yes | yes | no | no |
| `--hard` | yes | yes | yes | **yes** |

### After a `--hard` reset, the commit is not lost

The "Add coffee" commit was **committed**, so Git can still find it. The **reflog** is Git's private diary of where `HEAD` has been:

```text
$ git reflog -4
60cb0bb (HEAD -> main) HEAD@{0}: reset: moving to HEAD~1
df83910 HEAD@{1}: commit: Add coffee
60cb0bb (HEAD -> main) HEAD@{2}: reset: moving to HEAD~1
1558157 HEAD@{3}: commit: Add coffee
$ git reset --hard HEAD@{1}
HEAD is now at df83910 Add coffee
```

*Recorded in Bash; `ch25-undo/expected-reset.bash.txt`.*

`HEAD@{1}` is where `HEAD` was one step ago: the commit `df83910 Add coffee`. Resetting to it brings the commit back:

```text
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.80
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
- Tea: 1.50
- Coffee: 2.00
$ git log --oneline
df83910 (HEAD -> main) Add coffee
60cb0bb Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch25-undo/expected-reset.bash.txt`.*

The coffee line and the commit are both back. This is the safety net for *committed* work. Chapter 26<!--ref:reflog--> teaches it fully.

### But uncommitted work is different

```text
$ printf -- '- Precious draft: 5.00\n' >> menu.md
$ git status --short
 M menu.md
$ git reset --hard
HEAD is now at 81f772e Add coconut cake
$ git status --short
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.80
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch25-undo/expected-lost.bash.txt`.*

The line "Precious draft" was never committed. `git reset --hard` discarded it, and the reflog has nothing about it:

```text
$ git reflog -2
81f772e (HEAD -> main) HEAD@{0}: reset: moving to HEAD
81f772e (HEAD -> main) HEAD@{1}: commit: Add coconut cake
```

*Recorded in Bash; `ch25-undo/expected-lost.bash.txt`.*

Both entries describe commits and moves; neither mentions your edit. Because the edit was never even staged (never passed to `git add`), **there is no way to get the draft back with Git.**

> **Deep.** Staging changes this. If the edit had been staged with `git add` before the reset, Git would already have stored its contents as an object, and `git fsck --lost-found` would list it as a *dangling blob* that you could read and save. Staging before a risky command is therefore a cheap safety net. This was tried once on Git 2.43.0 and is not part of the recorded sessions; Chapter 80<!--ref:challenges--> uses `git fsck --lost-found` for a lost commit.

> **⚠️ CAUTION.** `git reset --hard` is the most dangerous everyday command. Before you run it, run `git status` and `git stash` (Chapter 24<!--ref:stash-->) if there is anything you want to keep. Commits can be recovered from the reflog. Uncommitted changes cannot.

> **⚠️ CAUTION.** Do not reset commits that you have already **pushed** and that others may have pulled. Moving a shared branch back rewrites history that other people already have, and causes the problems described in Chapter 23<!--ref:remotes-->. For shared commits, use `git revert`.

---

## 25.6 `git revert`: undo by adding a commit

`git revert` does not remove history. It creates a **new commit that does the opposite** of an earlier one. Someone committed a bad line:

```text
$ printf -- '- Mystery pie: 0.01\n' >> menu.md
$ git commit -am "Add a mystery pie"
[main 1080a4c] Add a mystery pie
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch25-undo/expected-revert.bash.txt`.*

Revert it:

```text
$ git revert --no-edit HEAD
[main 3075407] Revert "Add a mystery pie"
 Date: Mon Jan 5 09:10:00 2026 +0000
 1 file changed, 1 deletion(-)
```

*Recorded in Bash; `ch25-undo/expected-revert.bash.txt`.*

`--no-edit` accepts Git's suggested message, `Revert "Add a mystery pie"`. Without it, Git opens your editor. The history now has both commits:

```text
$ git log --oneline
3075407 (HEAD -> main) Revert "Add a mystery pie"
1080a4c Add a mystery pie
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch25-undo/expected-revert.bash.txt`.*

The original commit is still there, followed by its reversal. The file is back to normal:

```text
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.80
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch25-undo/expected-revert.bash.txt`.*

```text
$ git show --stat --oneline HEAD
3075407 (HEAD -> main) Revert "Add a mystery pie"
 menu.md | 1 -
 1 file changed, 1 deletion(-)
```

*Recorded in Bash; `ch25-undo/expected-revert.bash.txt`.*

The revert commit removes one line, exactly what the original added.

> **New term: git revert.** Creates a new commit that undoes the changes of an earlier commit, leaving history intact.

Because it only *adds* to history, `git revert` is the safe choice for anything already shared. Anyone who pulls receives the correction like any other commit.

### Reverting a merge commit

A merge commit has **two parents** (Chapter 21<!--ref:merging-->), so "undo this commit" is ambiguous: undo the changes relative to which parent? Git refuses to guess. Here a branch `add-tea` was merged into `main` with a merge commit, and the first attempt to revert it fails:

```text
$ git switch -q -c add-tea
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -qam "Add tea"
$ git switch -q main
$ printf 'Open Monday to Saturday.\n' > hours.md
$ git add hours.md
$ git commit -qm "Add opening hours"
$ git merge -q --no-ff --no-edit add-tea
$ git revert --no-edit HEAD
error: commit 0f412999532a95752723706687e3813749d8e86b is a merge but no -m option was given.
fatal: revert failed
```

*Recorded in Bash; `ch25-undo/expected-revert-merge.bash.txt`.*

`is a merge but no -m option was given`. The option `-m` (`--mainline`) names the parent that counts as the **mainline**, numbered from 1. For a merge made *on `main`*, parent 1 is the side you were on (`main`), so `-m 1` means "go back to how `main` was before the merge":

```text
$ git revert --no-edit -m 1 HEAD
[main f999f2d] Revert "Merge branch 'add-tea'"
 Date: Mon Jan 5 09:16:00 2026 +0000
 1 file changed, 1 deletion(-)
```

*Recorded in Bash; `ch25-undo/expected-revert-merge.bash.txt`.*

The result:

```text
$ git log --oneline
f999f2d (HEAD -> main) Revert "Merge branch 'add-tea'"
0f41299 Merge branch 'add-tea'
1e5eef8 Add opening hours
73ad7ed (add-tea) Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.80
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch25-undo/expected-revert-merge.bash.txt`.*

The tea line is gone from `menu.md`, and the history shows both the merge and its reversal.

> **⚠️ CAUTION.** Git's documentation warns that reverting a merge "declares that you will never want the tree changes brought in by the merge": later merges of the same branch will only bring in commits that are not ancestors of the reverted merge. That may or may not be what you want, and it is a good reason to think before you revert a merge.

**Reverting an empty commit** (a commit that changes nothing) is not covered. The official `git revert` documentation says nothing about it, its behaviour was characterised locally in this book's research (Git 2.43.0 and 2.55.0, see the research folder), and there is no documented intent to teach from. The exercise stays blocked, as agreed.

---

## 25.7 Reset or revert?

| | `git reset` | `git revert` |
|---|---|---|
| What happens to history | commits are removed from the branch | a new commit is added |
| Safe after pushing? | **no** | yes |
| Leaves a record of the mistake? | no | yes |
| Best for | local commits you have not shared | shared commits |

---

## 25.8 An undo checklist

1. **Look:** `git status`, `git log --oneline`.
2. **Decide where the mistake is:** working tree, index, or commits.
3. **Prefer the safe option:** `restore --staged` and `revert` lose nothing.
4. **Before a destructive one** (`restore <file>`, `reset --hard`): `git diff`, and stash anything you want.
5. **Never reset shared history.**
6. **If it went wrong:** stop, run `git reflog` (Chapter 26<!--ref:reflog-->).

---

## Checkpoint

## What You Learned

- Diagnose first: where is the mistake (files, index or commits)?
- `git restore <file>` discards an uncommitted edit permanently; `git restore --staged <file>` unstages and keeps it.
- `git restore --source=<commit> <file>` takes a file from an older commit.
- `git reset` moves the branch: `--soft` keeps the staged change, the default keeps the file change, `--hard` discards it.
- After a reset, committed work is recoverable via the reflog; uncommitted work is not.
- `git revert` adds a commit that cancels an earlier one, and is the safe choice for shared history.

## New Vocabulary

- **git restore**: bring file content from the index or a commit into the working tree or index.
- **git reset**: move the current branch to another commit, with three strengths.
- **git revert**: add a commit that undoes an earlier commit.

## Commands Learned

`git restore`, `git restore --staged`, `git restore --source`, `git reset --soft`, `git reset`, `git reset --hard`, `git reflog`, `git revert --no-edit`.

## Common Mistakes

1. **Running `git reset --hard` with uncommitted work.**
2. **Resetting a branch that has been pushed.**
3. **Using `git restore <file>` before checking `git diff`.**
4. **Forgetting which column of `git status --short` is the index.**
5. **Panicking after a reset instead of reading the reflog.**

## Practice

Do the exercises in [`exercises/ch25-exercises.md`](../../../exercises/ch25-exercises.md).

## Self-Test

1. Which command unstages a file without losing the edit?
2. What is the difference between `reset --soft` and `reset --hard`?
3. Why can the "Add coffee" commit be recovered but the "Precious draft" cannot?
4. Which of `reset` and `revert` is safe after pushing, and why?
5. What does `git restore --source=HEAD~2 menu.md` do?

## Before Moving On

You are ready for Chapter 26<!--ref:reflog--> if you can:

- [ ] undo an unstaged edit, and a staged one
- [ ] explain the three `git reset` options
- [ ] revert a commit
- [ ] say which undo commands can lose work

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `restore`, `restore --staged`, `restore --source` | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R184 |
| `reset --soft/--mixed/--hard`, reflog recovery, loss of uncommitted work | Locally tested (as above); wording of the `Unstaged changes after reset` message may vary | R185 |
| `revert` of an ordinary commit, and of a merge commit with `-m 1` | Locally tested (as above), and checked against the `git revert` documentation (Git 2.56.0) for `-m` and its warning | R186 |
| A staged edit survives `reset --hard` as a dangling blob (`git fsck --lost-found`); an unstaged edit does not | Locally tested once on Git 2.43.0; not a recorded session; documentation not yet consulted | R355 |
| `revert` of an empty commit | Behaviour characterised in the research folder; **documentation is silent**; deliberately not taught | R186 |

## Where this leads

Chapter 26<!--ref:reflog--> turns the reflog into a full recovery toolkit. Chapter 27<!--ref:rebase--> rewrites history in a more controlled way, and Chapter 33<!--ref:gitsec--> shows why removing a committed secret needs more than a revert.
