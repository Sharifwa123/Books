---
key: reflog
number: 26
tag: Core
first_read: full
status: draft
requires: [undo]
ledger: [R187, R188, R189]
---
# Chapter 26 — Recovery with the Reflog [Core]

**In this chapter**

- what the reflog is, and why it exists
- reading `git reflog`
- recovering a deleted branch
- what a *detached HEAD* is, and how to save work made in one
- a decision tree for "I think I lost my work"

**Before you start.** Chapter 25<!--ref:undo--> (especially `git reset --hard`) and Chapter 20<!--ref:branching-->. The recordings use the `bakery-menu` repository and were run in Bash and zsh on Git 2.43.0, then re-run in CI on Git 2.55.0.

The most useful thing to know about losing work in Git is that you usually have not. Git rarely deletes a commit when you move away from it. It only stops pointing at it. The reflog remembers where you were.

---

## 26.1 What the reflog is

> **New term: reflog.** A private, local log of where `HEAD` (and each branch) has pointed, kept by Git for you. Every commit, switch, reset, merge and rebase adds a line.

The ordinary log (Chapter 17<!--ref:history_view-->) shows the history of *commits* reachable from a branch. The reflog shows the history of *your movements*. It is different in three ways:

- It is **local**: it is not pushed, and a fresh clone starts with a single `clone:` entry and none of the original repository's history.
- It is **temporary**: Git eventually removes old entries.
- It records **every move**, including moves that left commits unreachable.

```text
$ git reflog
81f772e (HEAD -> main) HEAD@{0}: commit: Add coconut cake
9f10b43 HEAD@{1}: commit: Raise the price of the white loaf
8a52ffe HEAD@{2}: commit (initial): Add the menu
```

*Recorded in Bash; `ch26-reflog/expected-deleted-branch.bash.txt`.*

Read one line: `81f772e HEAD@{0}: commit: Add coconut cake`.

| Part | Meaning |
|---|---|
| `81f772e` | the commit `HEAD` pointed to after the event |
| `HEAD@{0}` | how many moves ago (0 is now, 1 is one move ago) |
| `commit: Add coconut cake` | what happened |

The list is newest first. `HEAD@{1}` is where you were one step earlier.

> **Checked against the documentation (Git 2.56.0, R189).** Two settings control how long the reflog keeps entries: `gc.reflogExpire`, which "defaults to 90 days", applies to entries whose commits are still reachable from a branch; `gc.reflogExpireUnreachable`, "defaults to 30 days", applies to entries whose commits are **not** reachable from the current tip (as after a `git reset --hard`, or a deleted branch). Separately, `git gc` prunes unreachable *objects* only after a grace period, `gc.pruneExpire`, which is **two weeks** by default. The documentation explains why the unreachable period is shorter: such entries are "generally created as a result of using `git commit --amend` or `git rebase`" and are the commits from *before* the amend or rebase, which most users want to expire sooner. In practice: treat a lost commit as recoverable for **about a month**, but not for anything old, and remember that these are *defaults* that a system or a team can change (Chapter 14<!--ref:config-->).

---

## 26.2 Recovering a deleted branch

You start an experiment on a branch and commit some work:

```text
$ git switch -c experiment
Switched to a new branch 'experiment'
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[experiment 1493bc1] Add tea
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch26-reflog/expected-deleted-branch.bash.txt`.*

Then you switch back and delete the branch, believing that the experiment is finished:

```text
$ git switch main
Switched to branch 'main'
$ git branch -D experiment
Deleted branch experiment (was 1493bc1).
$ git branch
* main
```

*Recorded in Bash; `ch26-reflog/expected-deleted-branch.bash.txt`.*

Git deleted it with `-D` (force, Chapter 20<!--ref:branching-->) and told you the last commit, `1493bc1`. The branch name is gone. The commit is not. To find it again, ask the reflog:

```text
$ git reflog -4
81f772e (HEAD -> main) HEAD@{0}: checkout: moving from experiment to main
1493bc1 HEAD@{1}: commit: Add tea
81f772e (HEAD -> main) HEAD@{2}: checkout: moving from main to experiment
81f772e (HEAD -> main) HEAD@{3}: commit: Add coconut cake
```

*Recorded in Bash; `ch26-reflog/expected-deleted-branch.bash.txt`.*

The line `1493bc1 HEAD@{1}: commit: Add tea` is the commit you made on `experiment`. Now give it a branch name again:

```text
$ git branch experiment-restored HEAD@{1}
$ git branch
  experiment-restored
* main
```

*Recorded in Bash; `ch26-reflog/expected-deleted-branch.bash.txt`.*

`git branch experiment-restored HEAD@{1}` creates a branch at the commit that `HEAD@{1}` names. The log shows the recovered work:

```text
$ git log --oneline experiment-restored
1493bc1 (experiment-restored) Add tea
81f772e (HEAD -> main) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch26-reflog/expected-deleted-branch.bash.txt`.*

The commit "Add tea" is back, on a new branch. **Notice what saved the work:** the hash printed by `git branch -D` (`1493bc1`) would also have worked, with `git branch experiment-restored 1493bc1`. Reading the output of destructive commands is a recovery technique.

---

## 26.3 Detached HEAD

Normally `HEAD` points to a **branch**, and the branch points to a commit. Sometimes you check out a *commit* directly: to look at old code, or by accident. Then `HEAD` points straight at the commit.

(Chapter 20<!--ref:branching--> named this state; here it matters for recovery.)

```text
$ git switch --detach HEAD~1
HEAD is now at 9f10b43 Raise the price of the white loaf
$ git status
HEAD detached at 9f10b43
nothing to commit, working tree clean
```

*Recorded in Bash; `ch26-reflog/expected-detached.bash.txt`.*

`HEAD detached at 9f10b43` says it. This is a legitimate place to look around. The danger is that **commits made here belong to no branch**:

```text
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea on a detached HEAD"
[detached HEAD fae405d] Add tea on a detached HEAD
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch26-reflog/expected-detached.bash.txt`.*

The commit has been made, and Git says `[detached HEAD fae405d]`. Now you leave:

```text
$ git switch main
Warning: you are leaving 1 commit behind, not connected to
any of your branches:

  fae405d Add tea on a detached HEAD

If you want to keep it by creating a new branch, this may be a good time
to do so with:

 git branch <new-branch-name> fae405d

Switched to branch 'main'
```

*Recorded in Bash; `ch26-reflog/expected-detached.bash.txt`.*

Read the warning. Git tells you that one commit is left behind, *not connected to any of your branches*, and it even prints the command to save it: `git branch <new-branch-name> fae405d`. If you close the window without reading it, the commit is no longer visible:

```text
$ git log --oneline --all
81f772e (HEAD -> main) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch26-reflog/expected-detached.bash.txt`.*

`git log --all` shows only the three original commits; the tea commit is gone from view. But the reflog remembers:

```text
$ git reflog -3
81f772e (HEAD -> main) HEAD@{0}: checkout: moving from fae405dddf099cd51e07afda8545230358e7aa2e to main
fae405d HEAD@{1}: commit: Add tea on a detached HEAD
9f10b43 HEAD@{2}: checkout: moving from main to HEAD~1
```

*Recorded in Bash; `ch26-reflog/expected-detached.bash.txt`.*

The line `fae405d HEAD@{1}: commit: Add tea on a detached HEAD` gives you the hash. Save it on a branch:

```text
$ git branch rescued fae405d
$ git branch
* main
  rescued
$ git log --oneline rescued
fae405d (rescued) Add tea on a detached HEAD
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch26-reflog/expected-detached.bash.txt`.*

The commit is safe on `rescued`.

**The rule.** If Git says `HEAD detached` and you want to keep any work: create a branch first (`git switch -c <name>`). If you only looked around, `git switch main` is all you need.

---

## 26.4 A bad reset

Chapter 25<!--ref:undo--> showed the same technique for `git reset --hard`: `git reflog` finds the commit that `HEAD` pointed to before the reset, and `git reset --hard HEAD@{1}` (or the hash) brings it back. That example is the one to reread if you have just run a reset you regret.

---

## 26.5 What the reflog cannot save

- **Uncommitted changes.** Work that was never committed was never recorded (Chapter 25<!--ref:undo-->, section on `--hard`).
- **Old work,** once entries have expired and garbage collection has run (see the defaults in section 26.1).
- **Work in a different clone.** The reflog is per repository.
- **A repository you deleted.**

The habit that avoids all of these: **commit early, on a branch.** A commit you made an hour ago is almost always recoverable. An edit you never committed is not.

---

## 26.6 "I think I lost my work": a decision tree

1. **Stop.** Do not run more commands that move things around, and do not delete the folder.
2. **`git status`.** Is the work sitting there, uncommitted? Then it is not lost.
3. **`git branch --all` and `git stash list`.** Is it on another branch, or in a stash?
4. **`git log --oneline --all`.** Is it in a commit you cannot see from the current branch?
5. **`git reflog`.** Look for the last commit that had your work. Note the hash.
6. **Recover it:** `git branch <name> <hash>` (safe, adds a branch), or `git reset --hard <hash>` (moves the current branch; check `git status` first).
7. **If it was never committed** and is not in a stash, Git cannot help. Look in your editor's undo history and in backups (Chapter 3<!--ref:editors-->).

---

## Checkpoint

## What You Learned

- The reflog is a local, temporary record of where `HEAD` has been; `HEAD@{n}` names a position in it.
- A deleted branch's commits survive; find them in the reflog (or in the hash printed by `git branch -D`) and give them a new branch.
- A detached `HEAD` points at a commit rather than a branch; commits made there need a branch to be kept.
- Git warns when you leave commits behind, and prints the command to save them.
- The reflog cannot recover uncommitted work, or old entries that have expired.

## New Vocabulary

- **Reflog**: Git's local log of where `HEAD` and branches have pointed.

## Commands Learned

`git reflog`, `git reflog -n`, `HEAD@{n}`, `git branch <name> <commit>`, `git switch --detach`, `git log --all`.

## Common Mistakes

1. **Committing on a detached `HEAD`** without creating a branch.
2. **Ignoring the "leaving 1 commit behind" warning.**
3. **Deleting a branch with `-D` without noting the hash.**
4. **Assuming the reflog is permanent, or shared.**
5. **Running more commands before looking at the reflog.**

## Practice

Do the exercises in [`exercises/ch26-exercises.md`](../../../exercises/ch26-exercises.md).

## Self-Test

1. What does `HEAD@{1}` mean?
2. After `git branch -D experiment`, how can you find the deleted commit?
3. What does `HEAD detached at 9f10b43` tell you?
4. What did Git print when you left the detached `HEAD` with a commit, and why does it matter?
5. Name two things the reflog cannot recover.

## Before Moving On

You are ready for Chapter 27<!--ref:rebase--> if you can:

- [ ] read a reflog line
- [ ] recover a deleted branch
- [ ] rescue a commit made on a detached `HEAD`
- [ ] work through the "lost work" decision tree

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Reflog lines and `HEAD@{n}`; deleted-branch recovery | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0. Concept and option statements also checked in the Git 2.56.0 manual (git-reflog). | R187 |
| Detached `HEAD`, the leaving-commits warning, rescue with `git branch` | Locally tested (as above). Concept and option statements also checked in the Git 2.56.0 manual (git-switch, glossary-content). | R188 |
| Reflog expiry defaults (90 days, 30 days) and the `gc.pruneExpire` grace period (two weeks) | Checked against the Git 2.56.0 documentation (`config/gc`); not measured by test | R189 |

## Where this leads

Chapter 27<!--ref:rebase--> rewrites history on purpose; the reflog is what makes that safe to try. Chapter 28<!--ref:tools--> uses `git switch --detach` for bisecting, and Chapter 33<!--ref:gitsec--> explains why a leaked secret in old history cannot be fixed by these tools alone.
