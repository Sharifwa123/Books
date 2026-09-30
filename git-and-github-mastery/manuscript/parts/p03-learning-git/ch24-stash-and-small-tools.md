---
key: stash
number: 24
tag: Core
first_read: part
status: draft
requires: [merging]
ledger: [R181, R182, R183]
---
# Chapter 24 — Stash and Small Tools [Core]

**In this chapter**

- `git stash`: put unfinished work aside and bring it back
- a first look at tags, which are names for particular commits
- `git clean`: remove untracked files, carefully
- `git grep`, `git blame` and `git log -S`: find things in a repository
- a **practice session** that tidies up the Sunrise Bakery site

**Before you start.** Chapter 21<!--ref:merging--> and Chapter 17<!--ref:history_view-->. The recordings use the `bakery-menu` repository and were run in Bash and zsh on Git 2.43.0, then re-run in CI on Git 2.55.0.

This chapter is a toolbox. Each tool is small, and each solves a problem you will meet within your first weeks.

---

## 24.1 Stash: put work aside

You are in the middle of an edit when someone asks you to fix something else on `main`. Your work is not ready to commit, and Git will not let you switch branches if it would overwrite it (Chapter 20<!--ref:branching-->). You need somewhere to put the half-finished work.

> **New term: stash.** A shelf inside your repository where Git stores uncommitted changes, so that the working tree becomes clean again. You can bring the changes back later.

Here is a half-finished edit to `menu.md`, and a new file, `ideas.txt`:

```text
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n- Tea: 1.50\n' > menu.md
$ printf 'draft\n' > ideas.txt
$ git status --short
 M menu.md
?? ideas.txt
```

*Recorded in Bash; `ch24-stash/expected-stash.bash.txt`.*

`M` means a tracked file was modified; `??` means Git does not track `ideas.txt` yet. Now stash:

```text
$ git stash
Saved working directory and index state WIP on main: 81f772e Add coconut cake
$ git status --short
?? ideas.txt
```

*Recorded in Bash; `ch24-stash/expected-stash.bash.txt`.*

Read it carefully. The **modified** file was saved on the shelf and reverted, so `menu.md` is clean again. But `ideas.txt` is **still there**: by default `git stash` only takes changes to tracked files. Check the shelf:

```text
$ git stash list
stash@{0}: WIP on main: 81f772e Add coconut cake
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.80
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch24-stash/expected-stash.bash.txt`.*

The entry `stash@{0}` is the newest one (they form a stack: the last in is the first out). The file `menu.md` has its committed content again, without the tea line. Now bring the work back:

```text
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   menu.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	ideas.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (9958d02c6f90ac44192aff2010753d5a93af29c9)
$ git status --short
 M menu.md
?? ideas.txt
```

*Recorded in Bash; `ch24-stash/expected-stash.bash.txt`.*

`git stash pop` **applied** the saved changes and **dropped** the entry from the shelf (`Dropped refs/stash@{0} (...)`). The status shows the modified file back.

To include untracked files, add `-u`:

```text
$ git stash -u
Saved working directory and index state WIP on main: 81f772e Add coconut cake
$ git status --short
$ git stash list
stash@{0}: WIP on main: 81f772e Add coconut cake
```

*Recorded in Bash; `ch24-stash/expected-stash.bash.txt`.*

Both files went onto the shelf, and the working tree is completely clean. Bring them back the same way:

```text
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   menu.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	ideas.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (130e22629620c583dc9031508b0eda23eecf5126)
$ git status --short
 M menu.md
?? ideas.txt
```

*Recorded in Bash; `ch24-stash/expected-stash.bash.txt`.*

And when the shelf is empty:

```text
$ git stash drop
No stash entries found.
```

*Recorded in Bash; `ch24-stash/expected-stash.bash.txt`.*

**Two stash habits.**

- `git stash pop` applies and removes. `git stash apply` applies and **keeps** the entry, which is useful when you are not sure the apply will work.
- Stashes are not a safe archive. They are easy to forget, and dropping one removes your only reference to it (Chapter 26<!--ref:reflog--> shows how recovery works). If the work matters for more than an hour, commit it on a branch instead.

> **⚠️ CAUTION.** If applying a stash conflicts with newer changes, you get the same kind of conflict as in Chapter 22<!--ref:conflicts-->. Resolve it the same way. Check `git status` before you stash and after you pop.

---

## 24.2 Tags: names for commits

A branch name moves when you commit. Sometimes you want a name that **stays** on one commit: "this is version 1.0". That is a **tag**.

> **New term: tag.** A fixed name for one commit, used to mark a point in history such as a release. Unlike a branch, a tag does not move when you commit.

Two kinds exist:

> **New term: lightweight tag.** A tag that is only a name pointing at a commit.

> **New term: annotated tag.** A tag that is a full Git object with a tagger, a date and a message. This is the kind normally used for releases.

```text
$ git tag
$ git tag v0.1
$ git tag -a v1.0 -m "First public menu"
$ git tag
v0.1
v1.0
```

*Recorded in Bash; `ch24-stash/expected-tags.bash.txt`.*

The first command listed no tags. `git tag v0.1` made a lightweight tag; `git tag -a v1.0 -m "First public menu"` made an annotated one. Tags show up in the log when you ask for decorations:

```text
$ git log --oneline --decorate
81f772e (HEAD -> main, tag: v1.0, tag: v0.1) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch24-stash/expected-tags.bash.txt`.*

Both tags point to the same commit here. An annotated tag stores extra information, which `git show` reveals before showing the commit:

```text
$ git show v1.0
tag v1.0
Tagger: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:11:00 2026 +0000

First public menu

commit 81f772ee32b93d8fcf80dbb34ab74053b69d97a2 (HEAD -> main, tag: v1.0, tag: v0.1)
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:08:00 2026 +0000

    Add coconut cake

diff --git a/menu.md b/menu.md
index 1f2a95a..97e3bea 100644
--- a/menu.md
+++ b/menu.md
@@ -2,3 +2,4 @@

 - White loaf: 2.80
 - Rolls (six): 3.00
+- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch24-stash/expected-tags.bash.txt`.*

Delete and filter tags:

```text
$ git tag -d v0.1
Deleted tag 'v0.1' (was 81f772e)
$ git tag
v1.0
$ git tag -l "v1.*"
v1.0
```

*Recorded in Bash; `ch24-stash/expected-tags.bash.txt`.*

`git tag -d` deleted only the *name*; the commit is untouched. The pattern `"v1.*"` in `git tag -l` is a wildcard. Chapter 29<!--ref:tags--> covers version numbering, sharing tags with a remote, and the difference between a tag and a GitHub Release.

---

## 24.3 Clean: remove untracked files

Sometimes a project fills with files Git does not track: build leftovers, scratch notes. `git clean` removes them. It is also one of the few Git commands that deletes files **for good**, because untracked files were never saved in a commit. Git therefore makes you say so.

```text
$ printf 'scratch\n' > scratch.txt
$ mkdir tmp
$ printf 'x\n' > tmp/a.txt
$ git status --short
?? scratch.txt
?? tmp/
```

*Recorded in Bash; `ch24-stash/expected-clean.bash.txt`.*

Here are a scratch file and a folder with a file in it. Always start with a **dry run**, `-n`:

```text
$ git clean -n
Would remove scratch.txt
$ git clean -n -d
Would remove scratch.txt
Would remove tmp/
```

*Recorded in Bash; `ch24-stash/expected-clean.bash.txt`.*

Without `-d`, untracked *folders* are left alone. The dry run names exactly what would go. When you are sure, `-f` (force) makes it real:

```text
$ git clean -f
Removing scratch.txt
$ git status --short
?? tmp/
$ git clean -f -d
Removing tmp/
```

*Recorded in Bash; `ch24-stash/expected-clean.bash.txt`.*

```text
$ git status --short
$ ls
menu.md
```

*Recorded in Bash; `ch24-stash/expected-clean.bash.txt`.*

> **⚠️ CAUTION.** `git clean -f` cannot be undone: the files are not in any commit, so nothing can bring them back. Run `git clean -n` first, read the list, and check that nothing important is on it. Files that `.gitignore` covers (Chapter 18<!--ref:tracking-->) are skipped unless you add `-x`, which is a further reason to be careful.

---

## 24.4 Finding things

Three tools answer three different questions.

**"Where does this text appear?"** `git grep` searches the tracked files:

```text
$ git grep "loaf"
menu.md:- White loaf: 2.80
$ git grep -n "Rolls"
menu.md:4:- Rolls (six): 3.00
$ git grep -c "e"
menu.md:3
```

*Recorded in Bash; `ch24-stash/expected-search.bash.txt`.*

`-n` adds line numbers and `-c` counts matching lines per file. You can also search an **old version**. Here, two commits back, the loaf cost 2.50:

```text
$ git grep "loaf" HEAD~2
HEAD~2:menu.md:- White loaf: 2.50
```

*Recorded in Bash; `ch24-stash/expected-search.bash.txt`.*

**"Who last changed each line?"** `git blame` prints each line with the commit that last touched it:

```text
$ git blame -s menu.md
^8a52ffe 1) # Sunrise Bakery menu
^8a52ffe 2)
9f10b436 3) - White loaf: 2.80
^8a52ffe 4) - Rolls (six): 3.00
81f772ee 5) - Coconut cake (slice): 4.00
$ git blame -s -L 3,3 menu.md
9f10b436 3) - White loaf: 2.80
```

*Recorded in Bash; `ch24-stash/expected-search.bash.txt`.*

> **Your Git may show a longer hash.** With `git blame -s -L 3,3`, Git 2.43.0 and 2.55.0 print the hash as 8 characters (`9f10b436`) and Git 2.56.0 prints 7 (`9f10b43`). Hashes shortened to different lengths still name the same commit.

`-s` hides names and dates so the output is short. The hash on each line is the commit that last changed it. A leading `^` (as in `^8a52ffe`) marks a line from the very first commit. `-L 3,3` limits the output to line 3. Despite the name, blame is not about fault: it is how you find the commit that explains a line, and then `git show <hash>` tells you why.

**"When did this text first appear (or disappear)?"** `git log -S` finds commits that added or removed a given string:

```text
$ git log -S"Coconut" --oneline
81f772e (HEAD -> main) Add coconut cake
```

*Recorded in Bash; `ch24-stash/expected-search.bash.txt`.*

---

## 24.5 Practice session: a tidy-up

> **Practice session.** *Goal:* use the small tools on the Sunrise Bakery site. *Time:* about 30 minutes. *You need:* the `sunrise-bakery` repository with a few commits.

1. Edit a tracked file without committing, and create a new untracked file. Use `git stash -u`, check that the tree is clean, then `git stash pop`.
2. Tag the current commit `v0.1` (lightweight) and `v1.0` (annotated, with a message). List them and run `git show v1.0`.
3. Create a scratch file and a scratch folder. Run `git clean -n -d` first, read the list, then `git clean -f -d`.
4. Use `git grep` to find every place a price appears. Use `git blame -s` on `menu.html` (or your menu file) and pick one line; then `git show` its commit.
5. Use `git log -S"cake" --oneline` to find when the cake first appeared.

*Expected result:* each command behaves as in this chapter, and the final `git status` is clean.

*Checkpoint questions:* Which of these steps could lose work if you were careless? What did you do to make it safe?

---

## Checkpoint

## What You Learned

- `git stash` shelves changes to tracked files; `-u` includes untracked files; `pop` applies and removes.
- A tag is a fixed name for a commit; annotated tags carry a message and tagger.
- `git clean` deletes untracked files for good: run `-n` first.
- `git grep` searches content, `git blame` shows the commit for each line, `git log -S` finds when text changed.

## New Vocabulary

- **Stash**: a shelf for uncommitted changes.
- **Tag**: a fixed name for one commit.
- **Lightweight tag**: a tag that is only a name.
- **Annotated tag**: a tag with a tagger, date and message.

## Commands Learned

`git stash`, `git stash -u`, `git stash list`, `git stash pop`, `git stash drop`, `git tag`, `git tag -a`, `git tag -d`, `git tag -l`, `git clean -n`, `git clean -f`, `git clean -f -d`, `git grep`, `git blame -s`, `git log -S`.

## Common Mistakes

1. **Assuming `git stash` also takes untracked files.**
2. **Treating the stash as permanent storage.**
3. **Running `git clean -f` without a dry run.**
4. **Thinking `git tag -d` deletes the commit.**
5. **Reading `git blame` as a way to assign fault.**

## Practice

Do the exercises in [`exercises/ch24-exercises.md`](../../../exercises/ch24-exercises.md), including the practice session (section 24.5).

## Self-Test

1. Why did `ideas.txt` stay behind after the first `git stash`?
2. What is the difference between `git stash pop` and `git stash apply`?
3. Why does the book insist on `git clean -n` first?
4. What is the difference between a lightweight and an annotated tag?
5. Which command tells you when a string was first added?

## Before Moving On

You are ready for Chapter 25<!--ref:undo--> if you can:

- [ ] stash and restore work, with and without untracked files
- [ ] create, list, show and delete tags
- [ ] preview and perform a clean
- [ ] search, blame and pickaxe a repository

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `stash`, `stash -u`, `list`, `pop`, empty-shelf message | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; identical on CI's Git 2.55.0. Concept and option statements also checked in the Git 2.56.0 manual (git-stash). | R181 |
| Lightweight and annotated tags, `show`, `-d`, `-l`; `clean -n/-f/-d` | Locally tested (as above). Concept and option statements also checked in the Git 2.56.0 manual (git-clean, git-tag). | R182 |
| `git grep`, `git blame -s`, `git log -S` | Locally tested (as above). Concept and option statements also checked in the Git 2.56.0 manual (git-blame, git-grep, git-log). | R183 |

## Where this leads

Chapter 25<!--ref:undo--> is about undoing things safely, where stash and clean appear again. Chapter 29<!--ref:tags--> returns to tags for versioning, and Chapter 33<!--ref:gitsec--> returns to why history that contains a secret is hard to clean.
