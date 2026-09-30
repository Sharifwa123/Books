---
key: tools
number: 28
tag: Deep
first_read: later
status: draft
requires: [merging, undo]
ledger: [R193, R194, R195]
---
# Chapter 28 — Cherry-pick, Bisect and Patches [Deep]

**In this chapter**

- `git cherry-pick`: copy one commit to another branch
- `git bisect`: find the commit that introduced a bug, by halving
- `git format-patch`, `git apply` and `git am`: share a change as a file

> **Deep.** This chapter is marked **[Deep]**. You can skip it on a first read. Each tool here solves a specific problem that you may not meet for a while.

**Before you start.** Chapter 21<!--ref:merging-->, Chapter 25<!--ref:undo--> and Chapter 17<!--ref:history_view-->. The recordings use `bakery-menu` and were run in Bash and zsh on Git 2.43.0, then re-run in CI on Git 2.55.0.

---

## 28.1 Cherry-pick: copy one commit

Merging brings *all* the work of a branch. Sometimes you want **one commit** from another branch, without the rest: a bug fix made on a feature branch that `main` needs now.

> **New term: cherry-pick.** Copy the change made by one commit onto the current branch, as a new commit.

A branch `drinks` has two commits, tea and coffee:

```text
$ git switch -c drinks
Switched to a new branch 'drinks'
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[drinks 73ad7ed] Add tea
 1 file changed, 1 insertion(+)
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -am "Add coffee"
[drinks 398a33e] Add coffee
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch28-tools/expected-cherry-pick.bash.txt`.*

Back on `main`, the history looks like this:

```text
$ git switch main
Switched to branch 'main'
$ git log --oneline --all --graph
* 398a33e (drinks) Add coffee
* 73ad7ed Add tea
* 81f772e (HEAD -> main) Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch28-tools/expected-cherry-pick.bash.txt`.*

Cherry-pick the **first** of the two, tea. `drinks~1` means "one commit before the tip of `drinks`" (Chapter 17<!--ref:history_view-->):

```text
$ git cherry-pick drinks~1
[main eb86246] Add tea
 Date: Mon Jan 5 09:10:00 2026 +0000
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch28-tools/expected-cherry-pick.bash.txt`.*

The result is a **new commit** on `main`: hash `eb86246`, where the original was `73ad7ed`. As with a rebase (Chapter 27<!--ref:rebase-->), the change is copied and the copy gets a new identity because its parent is different. The `Date:` line shows that Git kept the original *author date*.

```text
$ git log --oneline --all --graph
* eb86246 (HEAD -> main) Add tea
| * 398a33e (drinks) Add coffee
| * 73ad7ed Add tea
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
$ git status --short
```

*Recorded in Bash; `ch28-tools/expected-cherry-pick.bash.txt`.*

The graph shows the copy on `main` and the original still on `drinks`; they are not linked in any way. Now the second one:

```text
$ git cherry-pick drinks
[main 8b679d1] Add coffee
 Date: Mon Jan 5 09:11:00 2026 +0000
 1 file changed, 1 insertion(+)
$ git log --oneline
8b679d1 (HEAD -> main) Add coffee
eb86246 Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch28-tools/expected-cherry-pick.bash.txt`.*

**Two cautions.**

- A copied commit can **conflict**, just as in Chapter 22<!--ref:conflicts-->, if the code around it differs. Git then stops; you resolve, `git add`, and `git cherry-pick --continue`, or you give up with `git cherry-pick --abort`. (The recordings in this chapter did not conflict, and these three commands were not run.)
- Because the copy is a different commit, merging `drinks` into `main` later will not know that the changes are already there. Usually Git handles that well, but the history contains the same change twice.

---

## 28.2 Bisect: find where a bug came in

You notice something wrong, and you know that it was fine last week. Somewhere among the commits since then, one broke it. Instead of reading them all, you can search by **halving**.

> **New term: bisect.** A search through history that finds the commit that introduced a change, by repeatedly testing the commit in the middle of the remaining range.

Five commits are added to the menu. The third one adds a bad line, a "Mystery pie" at 0.01:

```text
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[main 60cb0bb] Add tea
 1 file changed, 1 insertion(+)
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -am "Add coffee"
[main bf6d066] Add coffee
 1 file changed, 1 insertion(+)
$ printf -- '- Mystery pie: 0.01\n' >> menu.md
$ git commit -am "Add a mystery pie"
[main 7a5ee8a] Add a mystery pie
 1 file changed, 1 insertion(+)
$ printf -- '- Juice: 2.20\n' >> menu.md
$ git commit -am "Add juice"
[main 59d1a45] Add juice
 1 file changed, 1 insertion(+)
$ printf -- '- Scones: 1.80\n' >> menu.md
$ git commit -am "Add scones"
[main 2862c91] Add scones
 1 file changed, 1 insertion(+)
$ git log --oneline
2862c91 (HEAD -> main) Add scones
59d1a45 Add juice
7a5ee8a Add a mystery pie
bf6d066 Add coffee
60cb0bb Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch28-tools/expected-bisect.bash.txt`.*

(The commits are listed with the newest at the top; "Add a mystery pie" is the third one after "Add coconut cake".) You tell Git one commit that is *bad* (the current one) and one that is *good* (five commits back):

```text
$ git bisect start
status: waiting for both good and bad commits
$ git bisect bad HEAD
status: waiting for good commit(s), bad commit known
$ git bisect good HEAD~5
Bisecting: 2 revisions left to test after this (roughly 1 step)
[bf6d06696d870f97a07b7fc658a78580e0976059] Add coffee
```

*Recorded in Bash; `ch28-tools/expected-bisect.bash.txt`.*

Git checks out the commit **in the middle**, `bf6d066 Add coffee`, and asks you to test it. You would run your program or read the file, and then say `git bisect good` or `git bisect bad`, and Git would pick the next middle. With *n* commits, this takes about log₂(*n*) steps: 1000 commits need only about 10 tests.

You can let Git do the testing if you can write a command that succeeds (exit status 0) when a commit is good and fails when it is bad. `git bisect run` runs it at each step. Here the test is "the file does **not** contain the word Mystery":

```text
$ git bisect run sh -c '! grep -q Mystery menu.md'
running 'sh' '-c' ''\!' grep -q Mystery menu.md'
Bisecting: 0 revisions left to test after this (roughly 1 step)
[59d1a45ac75c3ce66c8226746cdb12c9cf8f311a] Add juice
running 'sh' '-c' ''\!' grep -q Mystery menu.md'
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[7a5ee8a1ad6ad0d61d041c66d9346164b5a51b96] Add a mystery pie
running 'sh' '-c' ''\!' grep -q Mystery menu.md'
7a5ee8a1ad6ad0d61d041c66d9346164b5a51b96 is the first bad commit
commit 7a5ee8a1ad6ad0d61d041c66d9346164b5a51b96
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:11:00 2026 +0000

    Add a mystery pie

 menu.md | 1 +
 1 file changed, 1 insertion(+)
bisect found first bad commit
```

*Recorded in Bash; `ch28-tools/expected-bisect.bash.txt`.*

Read the end: `7a5ee8a... is the first bad commit`, followed by the commit's details. Git narrowed five commits down to one in three steps, without help.

When you are done, **always** return to where you were:

```text
$ git bisect reset
Previous HEAD position was 7a5ee8a Add a mystery pie
Switched to branch 'main'
$ git status --short
```

*Recorded in Bash; `ch28-tools/expected-bisect.bash.txt`.*

`git bisect reset` leaves the bisect and returns you to your branch. While bisecting, your repository sits at a detached `HEAD` (Chapter 26<!--ref:reflog-->); reset takes you back.

> **⚠️ CAUTION.** Do not commit or change files in the middle of a bisect. And write down the good and bad commits before you start, so that you can restart.

> *On Git 2.55.0, bisect puts quotes around the words: `waiting for both 'good' and 'bad' commits` and `is the first 'bad' commit`.*

> **Verification pending [R195].** The exact wording of bisect's messages (for instance the `running` line, and the "roughly N steps" estimate) may differ between Git versions. Manual bisecting (`git bisect good` and `git bisect bad` typed by hand) was not run for this chapter.

---

## 28.3 Patches: share a change as a file

Sometimes you cannot push to a shared place: the receiver is offline, or an open-source project asks for changes by email. A **patch** is a file that describes a change.

> **New term: patch.** A text file that describes changes to files, so that they can be applied elsewhere.

`git format-patch` turns commits into patch files. Here, the tea commit on a new branch `tea`:

```text
$ git switch -c tea
Switched to a new branch 'tea'
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[tea 73ad7ed] Add tea
 1 file changed, 1 insertion(+)
$ git format-patch -1 HEAD
0001-Add-tea.patch
```

*Recorded in Bash; `ch28-tools/expected-patch.bash.txt`.*

Git wrote a file named `0001-Add-tea.patch`. The start of the file:

```text
$ head -n 8 0001-Add-tea.patch
From 73ad7ed97c9b9d17ef5c51e3e0f15a8e9e8a0638 Mon Sep 17 00:00:00 2001
From: Ada Learner <ada@example.org>
Date: Mon, 5 Jan 2026 09:10:00 +0000
Subject: [PATCH] Add tea

---
 menu.md | 1 +
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch28-tools/expected-patch.bash.txt`.*

It looks like an email: who wrote it, when, and the subject (`[PATCH] Add tea`), followed by a summary and, further down (not shown), the change itself. It keeps the author and message. Now switch to `main`, which does not have the tea yet. First **check** that the patch applies cleanly:

```text
$ git switch main
Switched to branch 'main'
$ git apply --check 0001-Add-tea.patch
```

*Recorded in Bash; `ch28-tools/expected-patch.bash.txt`.*

No output means that it would apply without problems. `git am` then applies it *and* records it as a commit, keeping the author and message:

```text
$ git am 0001-Add-tea.patch
Applying: Add tea
$ git log --oneline
eb86246 (HEAD -> main) Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch28-tools/expected-patch.bash.txt`.*

The commit has a new hash (`eb86246`) because its parent is different, as with cherry-pick.

There is also a plain `git apply`, which changes the files but does **not** commit. Use `git apply --check` first, as above. In this chapter, only the `--check` form was run.

> **Verification pending [R194].** `git apply` without `--check`, `git am` with a conflict (`--continue`, `--abort`, `--skip`), and sending patches by email were not run. The chapter describes only what was recorded.

---

## 28.4 Which tool for which job?

| You want to... | Use |
|---|---|
| bring *one* commit to the current branch | `git cherry-pick <commit>` |
| bring *all* of a branch | `git merge` or `git rebase` (Chapters 21<!--ref:merging-->, 27<!--ref:rebase-->) |
| find which commit broke something | `git bisect` |
| send a change without a shared repository | `git format-patch`, then `git am` on the other side |

---

## Checkpoint

## What You Learned

- `git cherry-pick <commit>` copies one commit onto the current branch as a new commit.
- `git bisect` halves the range of commits until it finds the first bad one; `bisect run` automates the test; `bisect reset` returns to your branch.
- `git format-patch` writes commits as patch files; `git apply --check` tests one; `git am` applies it and keeps the author and message.

## New Vocabulary

- **Cherry-pick**: copy the change of one commit onto the current branch.
- **Bisect**: find the commit that introduced a change by halving the range.
- **Patch**: a text file describing a change.

## Commands Learned

`git cherry-pick`, `git bisect start`, `git bisect good`, `git bisect bad`, `git bisect run`, `git bisect reset`, `git format-patch`, `git apply --check`, `git am`.

## Common Mistakes

1. **Forgetting `git bisect reset`.**
2. **Cherry-picking a commit that depends on an earlier one.**
3. **Expecting the copy to have the original's hash.**
4. **Changing files while bisecting.**
5. **Applying a patch without `--check`.**

## Practice

Do the exercises in [`exercises/ch28-exercises.md`](../../../exercises/ch28-exercises.md).

## Self-Test

1. Why does a cherry-picked commit have a different hash?
2. About how many tests does bisect need for 1000 commits?
3. What must a command do for `git bisect run` to use it?
4. What does `git bisect reset` do?
5. What does `git am` keep that a plain `git apply` and commit would lose?

## Before Moving On

You are ready for Chapter 29<!--ref:tags--> if you can:

- [ ] cherry-pick a commit
- [ ] find a bad commit with `git bisect run`
- [ ] make and apply a patch file

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `git cherry-pick` of one and of two commits; new hashes; author date kept | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R193 |
| `git bisect run` narrows to the first bad commit; `bisect reset` | Locally tested (as above); message wording may vary by version | R195 |
| `format-patch`, `apply --check`, `am` | Locally tested (as above); conflicts and email not run | R194 |

## Where this leads

Chapter 29<!--ref:tags--> names commits permanently. Chapter 34<!--ref:workflows--> discusses when teams cherry-pick, and Chapter 33<!--ref:gitsec--> covers the signing of commits and tags.
