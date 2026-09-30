---
key: history_view
number: 17
tag: Core
first_read: full
status: draft
requires: [firstrepo]
ledger: [R158, R159, R160]
---
# Chapter 17 — Seeing Changes and History [Core]

**In this chapter**

- how to read the history of a project (`git log`) in several formats
- how to name a commit: hashes, `HEAD`, `HEAD~1` and ranges
- how to read a *diff*, the report of what changed, line by line
- the four comparisons Git can make (`git diff`, `git diff --staged`, `git diff HEAD` and commit-to-commit), and when to use each
- `git show`, for looking at one commit

**Before you start.** Chapter 16<!--ref:firstrepo--> (you can create a repository, stage and commit) and Chapter 15<!--ref:model--> (working tree, index, repository). This chapter uses a small new example, the bakery menu, that stays with us through Part III.

The recordings were made in Bash and zsh on Git 2.43.0 and re-run in CI on Git 2.55.0; they were identical, including every hash.

---

## 17.1 The example: a menu with three versions

A history is only interesting if it has something in it. Here is the history that this chapter reads: a repository called `bakery-menu` that holds one file, `menu.md`, with three commits. (The same repository will be used in Chapters 20<!--ref:branching--> to 24<!--ref:stash-->.) The commands are the ones you already know; the recording shows how it was made:

```text
$ mkdir bakery-menu
$ cd bakery-menu
$ git init
Initialized empty Git repository in /home/learner/bakery-menu/.git/
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.50\n- Rolls (six): 3.00\n' > menu.md
$ git add menu.md
$ git commit -m "Add the menu"
[main (root-commit) 8a52ffe] Add the menu
 1 file changed, 4 insertions(+)
 create mode 100644 menu.md
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.00\n' > menu.md
$ git commit -am "Raise the price of the white loaf"
[main 9f10b43] Raise the price of the white loaf
 1 file changed, 1 insertion(+), 1 deletion(-)
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git commit -am "Add coconut cake"
[main 81f772e] Add coconut cake
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch17-history/expected-build.bash.txt`.*

Each commit changed the menu: the first created it, the second raised the price of the white loaf, the third added a coconut cake.

---

## 17.2 Reading the history: `git log`

> **New term: git log.** Shows the history of the current branch: the commits, newest first.

```text
$ git log
commit 81f772ee32b93d8fcf80dbb34ab74053b69d97a2 (HEAD -> main)
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:08:00 2026 +0000

    Add coconut cake

commit 9f10b43614a19024637b4644c75e84a4aae6af83
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:07:00 2026 +0000

    Raise the price of the white loaf

commit 8a52ffecdf9a4a5f307aa1d31e3429b29ad0d6f9
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:06:00 2026 +0000

    Add the menu
```

*Recorded in Bash; `ch17-history/expected-build.bash.txt`.*

For each commit, `git log` shows:

- `commit 81f772e...`: the **full hash**, the commit's identifier. `(HEAD -> main)` marks that this is the commit HEAD and the branch `main` point to now (Chapter 15<!--ref:model-->).
- `Author`: who made the change.
- `Date`: when. (The recordings use invented, evenly spaced dates so that they are reproducible. Yours will be the real time.)
- The **message**, indented.

Commits are listed **newest first**, and each is the parent of the one above it.

> **Checked against the documentation (R158).** The `git` manual (Git 2.56.0) says that `-p`/`--paginate` pipes output "into `less` (or if set, `$PAGER`) if standard output is a terminal", and that `--no-pager` turns the pager off; `GIT_PAGER` overrides `$PAGER`. The `core.pager` documentation adds that when the `LESS` environment variable is unset, Git sets it to `FRX`. In a real terminal, Git shows long output through the pager (press `q` to quit and the space bar for the next page); the recordings switch it off, so it is not shown here.

### 17.2.1 Useful forms of `git log`

The full form is long. Git has options that show less, or more.

**One line per commit: `--oneline`.**

```text
$ git log --oneline
81f772e (HEAD -> main) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch17-history/expected-build.bash.txt`.*

Each line is the short hash, the branch decoration if any, and the message's first line. This is the form you will use most.

**Only the last few: `-2`.**

```text
$ git log -2 --oneline
81f772e (HEAD -> main) Add coconut cake
9f10b43 Raise the price of the white loaf
```

*Recorded in Bash; `ch17-history/expected-build.bash.txt`.*

**With a summary of files changed: `--stat`.**

```text
$ git log --stat
commit 81f772ee32b93d8fcf80dbb34ab74053b69d97a2 (HEAD -> main)
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:08:00 2026 +0000

    Add coconut cake

 menu.md | 1 +
 1 file changed, 1 insertion(+)

commit 9f10b43614a19024637b4644c75e84a4aae6af83
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:07:00 2026 +0000

    Raise the price of the white loaf

 menu.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

commit 8a52ffecdf9a4a5f307aa1d31e3429b29ad0d6f9
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:06:00 2026 +0000

    Add the menu

 menu.md | 4 ++++
 1 file changed, 4 insertions(+)
```

*Recorded in Bash; `ch17-history/expected-build.bash.txt`.*

`--stat` adds a line per file changed and how many lines were added (`+`) and removed (`-`). It shows the *size* of each change at a glance.

**With the changes themselves: `-p`.**

```text
$ git log -p -1
commit 81f772ee32b93d8fcf80dbb34ab74053b69d97a2 (HEAD -> main)
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

*Recorded in Bash; `ch17-history/expected-build.bash.txt`.*

`-p` (for "patch") prints the actual changes after the message. Here `-1` limited it to one commit. The block after `diff --git` is a *diff*, explained in section 17.4.

**Your own format: `--format`.**

```text
$ git log --format='%h %an: %s'
81f772e Ada Learner: Add coconut cake
9f10b43 Ada Learner: Raise the price of the white loaf
8a52ffe Ada Learner: Add the menu
```

*Recorded in Bash; `ch17-history/expected-build.bash.txt`.*

`%h` is the short hash, `%an` the author's name and `%s` the subject (first line of the message). The Git manual lists many placeholders; you can build exactly the report you need.

**Only the commits that touched a file: `-- <path>`.**

```text
$ git log --oneline -- menu.md
81f772e (HEAD -> main) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch17-history/expected-build.bash.txt`.*

The `--` separates options from file names. Here all three commits changed `menu.md`, so all appear; in a larger project this narrows the history to one file.

### 17.2.2 Summary

| Command | Shows |
|---|---|
| `git log` | Full history, newest first |
| `git log --oneline` | One line per commit |
| `git log -n` or `git log -3` | Only the last *n* commits |
| `git log --stat` | Files changed and sizes |
| `git log -p` | The changes themselves |
| `git log --format=...` | A format you design |
| `git log -- <path>` | Only commits touching a path |

---

## 17.3 Naming a commit

Most Git commands take a commit as an argument. There are several ways to name one.

| Written | Means |
|---|---|
| `81f772ee32b93d8fcf80dbb34ab74053b69d97a2` | The **full hash** |
| `81f772e` | A **short hash**: enough of the beginning to be unambiguous (usually seven characters) |
| `HEAD` | The commit you are on now |
| `main` | The commit that the branch `main` points to |
| `HEAD~1` | The **parent** of `HEAD` (one step back) |
| `HEAD~2` | The parent's parent (two steps back) |
| `HEAD^` | The parent of `HEAD` (for a normal commit, the same as `HEAD~1`; merges, Chapter 21<!--ref:merging-->, have two parents and make the two forms differ) |
| `HEAD~2..HEAD` | A **range**: the commits reachable from `HEAD` but not from `HEAD~2` |

> **New term: revision.** Any way of naming a commit: a hash, a branch name, `HEAD`, `HEAD~2`. Git's manuals call these "revisions".

The command `git rev-parse` turns any revision into its full hash, which makes the relations visible:

```text
$ git rev-parse HEAD~1
81f772ee32b93d8fcf80dbb34ab74053b69d97a2
$ git rev-parse --short HEAD^
81f772e
$ git log --oneline HEAD~2..HEAD
0dff14c (HEAD -> main) Raise the price of rolls
81f772e Add coconut cake
```

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

`HEAD~1` was the third commit ("Add coconut cake"), and `HEAD^` gave the same commit in short form. The range `HEAD~2..HEAD` showed the two newest commits: the new one ("Raise the price of rolls", made in the same recording) and the one before it.

> **Checked against the documentation (R160).** The revision syntax is documented in `gitrevisions` (Git 2.56.0). Its worked example shows that `A^` is `A^1` and `A~1` (the parent), that `A^^` is `A~2`, and that `A^2` is the second parent of a merge; `<rev1>..<rev2>` means "commits that are reachable from `<rev2>` but exclude those that are reachable from `<rev1>`", and an omitted side "defaults to `HEAD`". The forms above are a small part of that page, which also lists forms such as `<rev>@{n}`, `<rev>^{/text}` and `:/text`.

**Why a hash, and not a number?** In a distributed system (Chapter 11<!--ref:distributed-->) two people make commits at the same time on different computers. Sequence numbers would collide. A hash is calculated from a commit's content, so every commit has its own name without any central authority. (Chapter 30<!--ref:objects--> explains how.)

---

## 17.4 Reading a diff

> **New term: diff.** A report of the differences between two versions of a file or project, line by line.

Chapter 9<!--ref:problem--> used the `diff` command to compare two files. Git produces a richer version. Read this real one, from the commit "Raise the price of the white loaf":

```text
$ git show HEAD~1
commit 9f10b43614a19024637b4644c75e84a4aae6af83
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:07:00 2026 +0000

    Raise the price of the white loaf

diff --git a/menu.md b/menu.md
index 0b15fe9..1f2a95a 100644
--- a/menu.md
+++ b/menu.md
@@ -1,4 +1,4 @@
 # Sunrise Bakery menu

-- White loaf: 2.50
+- White loaf: 2.80
 - Rolls (six): 3.00
```

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

The first block is `git show HEAD~1`; read the diff part line by line:

| Part | Example | Meaning |
|---|---|---|
| The header | `diff --git a/menu.md b/menu.md` | Comparing the file `menu.md` in version *a* (before) and version *b* (after) |
| Identifiers | `index 0b15fe9..1f2a95a 100644` | The stored contents before and after (Chapter 30<!--ref:objects-->), and the file mode |
| Old and new file | `--- a/menu.md` and `+++ b/menu.md` | The two versions being compared |
| The hunk header | `@@ -1,4 +1,4 @@` | This chunk covers lines 1 to 4 of the old file (`-1,4`) and lines 1 to 4 of the new one (`+1,4`) |
| Context lines | ` # Sunrise Bakery menu` | Unchanged lines around the change, shown with a leading space |
| A removed line | `-- White loaf: 2.50` | Present before, absent after. It begins with `-`, and the rest is the old line |
| An added line | `+- White loaf: 2.80` | Absent before, present after |

The line with the price appears twice: once with `-` (the old value) and once with `+` (the new one), so a *changed* line is shown as a removal and an addition next to each other. Everything else in the change is unchanged, and Git shows a few lines of it for context.

> **New term: hunk.** One contiguous chunk of changes in a diff, introduced by a header such as `@@ -1,4 +1,4 @@`.

Because the file was small, one hunk covers everything. In a large file, a diff has several hunks with unchanged stretches between them.

---

## 17.5 The four comparisons

Chapter 15<!--ref:model--> gave you three places: working tree, index and repository. `git diff` can compare any two of them. Learn the commands as a set; each answers a different question.

| Command | Compares | Answers the question |
|---|---|---|
| `git diff` | Working tree **and** index | *What have I changed that I have not yet staged?* |
| `git diff --staged` | Index **and** the last commit | *What will my next commit contain?* |
| `git diff HEAD` | Working tree **and** the last commit | *Everything I have changed since the last commit* |
| `git diff A B` | Commit **A** and commit **B** | *What changed between two versions?* |

The recording below walks through them in order. First a change is made to the menu (rolls go up to 3.20) and left unstaged:

```text
$ git status --short
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.20\n- Coconut cake (slice): 4.00\n' > menu.md
$ git status --short
 M menu.md
$ git diff
diff --git a/menu.md b/menu.md
index 97e3bea..9674cda 100644
--- a/menu.md
+++ b/menu.md
@@ -1,5 +1,5 @@
 # Sunrise Bakery menu

 - White loaf: 2.80
-- Rolls (six): 3.00
+- Rolls (six): 3.20
 - Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

`git status --short` shows ` M menu.md`: a modification in the working tree (the `M` is in the second column: not staged). `git diff` shows the change, `-3.00` becoming `+3.20`.

Now what does the **staged** comparison say at this moment?

```text
$ git diff --staged
```

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

Nothing: `git diff --staged` printed no output, because nothing is staged. Now stage the file, and ask again:

```text
$ git add menu.md
$ git status --short
M  menu.md
$ git diff
$ git diff --staged
diff --git a/menu.md b/menu.md
index 97e3bea..9674cda 100644
--- a/menu.md
+++ b/menu.md
@@ -1,5 +1,5 @@
 # Sunrise Bakery menu

 - White loaf: 2.80
-- Rolls (six): 3.00
+- Rolls (six): 3.20
 - Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

After `git add`, `git status --short` shows `M  menu.md` (the `M` is now in the *first* column: staged). Look at what changed:

- the second `git diff` now prints **nothing**: the working tree and the index are the same.
- `git diff --staged` now shows the change: the index differs from the last commit.

Whichever place holds the change, `git diff HEAD` shows it, since it compares the working tree with the last commit:

```text
$ git diff HEAD
diff --git a/menu.md b/menu.md
index 97e3bea..9674cda 100644
--- a/menu.md
+++ b/menu.md
@@ -1,5 +1,5 @@
 # Sunrise Bakery menu

 - White loaf: 2.80
-- Rolls (six): 3.00
+- Rolls (six): 3.20
 - Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

Finally, record it, and compare *two commits*:

```text
$ git commit -m "Raise the price of rolls"
[main 0dff14c] Raise the price of rolls
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git diff HEAD~2 HEAD
diff --git a/menu.md b/menu.md
index 1f2a95a..9674cda 100644
--- a/menu.md
+++ b/menu.md
@@ -1,4 +1,5 @@
 # Sunrise Bakery menu

 - White loaf: 2.80
-- Rolls (six): 3.00
+- Rolls (six): 3.20
+- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

`git diff HEAD~2 HEAD` compares the commit two steps back with the newest: the net effect of two commits in one report (rolls' price and the coconut cake). And the size of a longer stretch:

```text
$ git diff --stat HEAD~3 HEAD
 menu.md | 5 +++--
 1 file changed, 3 insertions(+), 2 deletions(-)
```

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

`--stat` gives the summary instead of the lines.

### 17.5.1 A habit worth forming

**Before every commit, run `git status` and `git diff --staged`.** `git status` says which files are staged; `git diff --staged` shows *exactly what* will be recorded. That is the last chance to notice a stray change, or a password, before it enters history. (You will use this habit for the rest of the book.)

---

## 17.6 One commit at a time: `git show`

> **New term: git show.** Displays one commit: its message and the changes it made.

Chapters ago you saw the last commit's raw data. `git show` is the readable version:

```text
$ git show
commit 81f772ee32b93d8fcf80dbb34ab74053b69d97a2 (HEAD -> main)
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

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

With no argument, `git show` shows the commit `HEAD`. With an argument (`git show HEAD~1`, as in section 17.4) it shows that commit. With `--stat` it shows only the summary:

```text
$ git show --stat HEAD~2
commit 8a52ffecdf9a4a5f307aa1d31e3429b29ad0d6f9
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:06:00 2026 +0000

    Add the menu

 menu.md | 4 ++++
 1 file changed, 4 insertions(+)
```

*Recorded in Bash; `ch17-history/expected-diff.bash.txt`.*

This is the quickest way to answer, "What did that commit actually do?"

---

## 17.7 Putting the tools together

| You want to know… | Use |
|---|---|
| What is the history of the project? | `git log --oneline` |
| What did commit X change? | `git show X` |
| What have I changed since the last commit? | `git diff HEAD` (or `git status` first) |
| What is about to be committed? | `git diff --staged` |
| What changed between two versions? | `git diff A B` |
| Who touched this file, and when? | `git log -- <file>` |
| How big was each change? | `git log --stat` or `git diff --stat` |

Chapter 24<!--ref:stash--> adds `git blame`, which shows for every line who last changed it, and searches through history.

---

## Checkpoint

## What You Learned

- `git log` shows history, newest first; `--oneline`, `-n`, `--stat`, `-p`, `--format` and `-- <path>` change what it shows.
- A commit can be named by hash, short hash, branch, `HEAD`, `HEAD~n`, `HEAD^` and ranges.
- A diff shows removed lines with `-`, added lines with `+`, context lines with a space, in hunks with `@@` headers.
- `git diff` (working tree vs index), `git diff --staged` (index vs last commit), `git diff HEAD` (working tree vs last commit) and `git diff A B` (two commits).
- `git show` displays one commit.
- Before every commit, check `git status` and `git diff --staged`.

## New Vocabulary

- **git log**: shows the history of commits.
- **Revision**: any way of naming a commit (hash, branch, `HEAD~2`).
- **Diff**: a report of line-by-line differences between two versions.
- **Hunk**: one contiguous chunk of changes in a diff.
- **git show**: displays one commit's message and changes.

## Commands Learned

`git log`, `git log --oneline`, `git log -n`, `git log --stat`, `git log -p`, `git log --format`, `git log -- <path>`, `git show`, `git show --stat`, `git diff`, `git diff --staged`, `git diff HEAD`, `git diff <a> <b>`, `git diff --stat`, `git rev-parse`.

## Common Mistakes

1. **Running `git diff` and seeing nothing** after `git add`, and concluding that nothing changed. Use `git diff --staged`.
2. **Confusing `-` and `+` lines.** `-` is the old version, `+` is the new one.
3. **Reading the log oldest-first.** It is newest first.
4. **Assuming `HEAD~1` and `HEAD^` are always the same.** They differ for merge commits.
5. **Skipping `git diff --staged` before committing.**

## Practice

Do the exercises in [`exercises/ch17-exercises.md`](../../../exercises/ch17-exercises.md).

## Self-Test

1. In a diff, what do a line starting with `-`, a line starting with `+` and a line starting with a space mean?
2. You edited and staged a file. Which command shows the staged change, and why does `git diff` show nothing?
3. What does `HEAD~2` mean? What does `HEAD~2..HEAD` mean?
4. Which command shows exactly what your next commit will contain?
5. How would you list only the commits that changed `menu.html`?
6. Why does Git name commits with hashes rather than numbers?

## Before Moving On

You are ready for Chapter 18<!--ref:tracking--> if you can:

- [ ] read a diff and say what changed
- [ ] use the four `git diff` forms and say which two places each compares
- [ ] show a project's history in three different formats
- [ ] name a commit three different ways

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| All `git log` forms and their output | Locally tested: Bash 5.2, zsh 5.9, Git 2.43.0; identical on the CI runner's Git 2.55.0 (including hashes) | R158 |
| The four `git diff` comparisons and their output at each stage | Locally tested (as above) | R159 |
| `HEAD~n`, `HEAD^`, ranges, `git rev-parse` | Locally tested (as above); forms checked against `gitrevisions` (Git 2.56.0) | R160 |
| The behaviour of the pager | Checked against the `git` and `core.pager` documentation (not shown in the recordings) | R158 |

## Where this leads

Chapter 18<!--ref:tracking--> shows how to keep files out of the snapshots, and how to rename and delete files in a way Git understands. Chapter 19<!--ref:commits--> shows how to write commits worth reading. Chapter 25<!--ref:undo--> uses `git diff` and the revisions of this chapter to undo changes.
