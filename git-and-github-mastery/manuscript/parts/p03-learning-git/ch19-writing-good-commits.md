---
key: commits
number: 19
tag: Core
first_read: full
status: draft
requires: [history_view, tracking]
ledger: [R165, R166, R167, R168]
---
# Chapter 19 — Writing Good Commits [Core]

**In this chapter**

- why a commit is a message to a future reader, and what that reader needs
- the anatomy of a good commit message, and examples of bad ones
- how to fix the last commit (`git commit --amend`) and what that does to history
- *atomic* commits: one logical change per commit
- empty commits, authorship and timestamps
- habits that keep a history useful

**Before you start.** Chapter 16<!--ref:firstrepo--> (staging and committing), Chapter 17<!--ref:history_view--> (reading `git log`, `git show` and `git diff`) and Chapter 18<!--ref:tracking--> (keeping the wrong files out). The recordings use the `bakery-menu` repository of Chapter 17<!--ref:history_view-->, with its three commits.

Every recording was run in Bash and zsh on Git 2.43.0 and re-run in CI on Git 2.55.0.

---

## 19.1 Who reads a commit?

You will read your own commits far more often than you write them. Six months from now, something on the bakery's website is wrong, and you need to know *when it changed and why*. You will run `git log`, and the messages are all you have. A history that says `stuff`, `fixes` and `update` answers nothing. A history that says what changed, and *why*, answers the question in seconds.

So a commit has two audiences:

1. **Tools**, which store the snapshot correctly whatever you write.
2. **People**, including you later, who need to understand the change.

Only people need good commits, and they are the reason to write them.

---

## 19.2 The anatomy of a message

A commit message has up to three parts.

```text
Add the lemon tart to the menu                        <- subject: one short line

The tart sells well at the farmers' market and is now  <- body: why, in sentences
part of the regular range. Its price includes tax.

Refs: menu-42                                          <- footer: references (optional)
```

| Part | What to write | Habit |
|---|---|---|
| **Subject** | What the commit does, in one short line | Start with a capital letter, use the *imperative* ("Add", "Fix", "Raise", as if giving an order to the codebase), no full stop, keep it short (about 50 characters is a common guide) |
| **Blank line** | Separates subject from body | Needed: many tools treat the first line as the subject |
| **Body** | *Why* the change was made, and anything a reader could not guess from the diff | Write sentences; the diff already says *what* |
| **Footer** | References to related work items, and similar | Optional; team rules vary |

> **Checked against the documentation (R165).** Git itself asks for very little. `git commit` (Git 2.56.0, section DISCUSSION) says: "Though not required, it's a good idea to begin the commit message with a single short (no more than 50 characters) line summarizing the change, followed by a blank line and then a more thorough description. The text up to the first blank line in a commit message is treated as the commit title, and that title is used throughout Git." The Git project's own `SubmittingPatches` asks contributors to "describe your changes in imperative mood, e.g. 'make xyzzy do frotz'", calls 50 characters "the soft limit", to "skip the full stop", and to convey "the _why_ behind your change". Those are that project's conventions for its own contributors. The capital letter in the table above is another common habit (the Git project itself does not capitalise after its `area:` prefix), so treat every row as a convention and follow your team's.

### 19.2.1 Good and bad subjects

| Poor | Better | Why |
|---|---|---|
| `stuff` | `Add the lemon tart to the menu` | Says what changed |
| `fixes` | `Fix the broken link to the menu page` | Says which fix |
| `update` | `Raise the price of rolls to 3.20` | Says what and how much |
| `Changed some things and also added the hours and fixed the price` | Two commits: `Raise the price of rolls` and `Add the opening hours` | Two changes belong in two commits (section 19.4) |
| `WIP` | `Add a draft of the weekend menu` | "Work in progress" says nothing; describe the work |

### 19.2.2 Writing a body: two `-m` options

The `-m` option can be repeated. The first is the subject; each further `-m` becomes a paragraph, separated by a blank line:

```text
$ git commit --allow-empty -m "Summarise the change" -m "The body explains why, in complete sentences, after a blank line."
[main 573a346] Summarise the change
```

*Recorded in Bash; `ch19-commits/expected-messages.bash.txt`.*

Then `git log -1` shows the message as stored, subject and body separated by a blank line:

```text
$ git log -1
commit 573a3460805e3e95ac6f40a56908bc88249022b3 (HEAD -> main)
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:17:00 2026 +0000

    Summarise the change

    The body explains why, in complete sentences, after a blank line.
```

*Recorded in Bash; `ch19-commits/expected-messages.bash.txt`.*

> **Deep.** If you run `git commit` with no `-m`, Git opens your editor with an empty message and some comment lines. Write the subject on the first line, a blank line, then the body; save and close. Lines beginning with `#` are comments and are not part of the message (this is Git's normal behaviour, stated in its documentation; the editor session itself is not recorded here).

---

## 19.3 Fixing the last commit: `git commit --amend`

Everybody writes a bad message, or forgets a file. Git lets you fix the **last** commit.

> **New term: git commit --amend.** Replaces the last commit with a new one, so you can change its message or add forgotten changes to it.

### 19.3.1 A bad message

The recording adds an empty marker commit (section 19.5), makes a change and commits it with the message `stuff`, then fixes the message:

```text
$ cd bakery-menu
$ git commit --allow-empty -m "Mark the start of the spring menu"
[main aa2ff61] Mark the start of the spring menu
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n- Lemon tart: 3.50\n' > menu.md
$ git commit -am "stuff"
[main 72a36ee] stuff
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch19-commits/expected-messages.bash.txt`.*

```text
$ git commit --amend -m "Add the lemon tart to the menu"
[main 5c151e3] Add the lemon tart to the menu
 Date: Mon Jan 5 09:10:00 2026 +0000
 1 file changed, 1 insertion(+)
$ git log --oneline -3
5c151e3 (HEAD -> main) Add the lemon tart to the menu
aa2ff61 Mark the start of the spring menu
81f772e Add coconut cake
```

*Recorded in Bash; `ch19-commits/expected-messages.bash.txt`.*

Read what happened:

- The first block shows the commit `stuff` was recorded as `72a36ee`.
- After `git commit --amend -m "Add the lemon tart to the menu"`, the log shows `5c151e3 Add the lemon tart to the menu` in its place. The hash **changed** (`72a36ee` to `5c151e3`).
- The line ` Date: Mon Jan 5 09:10:00 2026 +0000` in the commit output is the *original* author date, kept by the amend.

### 19.3.2 A forgotten file

```text
$ printf 'Prices include tax.\n' > notes.txt
$ git add notes.txt
$ git commit --amend --no-edit
[main f71f66b] Add the lemon tart to the menu
 Date: Mon Jan 5 09:10:00 2026 +0000
 2 files changed, 2 insertions(+)
 create mode 100644 notes.txt
$ git show --stat --oneline HEAD
f71f66b (HEAD -> main) Add the lemon tart to the menu
 menu.md   | 1 +
 notes.txt | 1 +
 2 files changed, 2 insertions(+)
```

*Recorded in Bash; `ch19-commits/expected-messages.bash.txt`.*

`git add notes.txt` staged a forgotten file, and `git commit --amend --no-edit` added it to the last commit **without** changing the message (`--no-edit` means "keep the message"). The commit output shows `2 files changed`, and `git show --stat` confirms that the single commit now contains both files. The hash changed again (`5c151e3` to `f71f66b`).

### 19.3.3 What amend really does

A commit's hash is calculated from its content (Chapter 15<!--ref:model-->). Change the message or the snapshot, and you have a **different commit**. So `--amend` does not modify the old commit; it **creates a new commit and moves the branch to it**. The old commit is still in the repository, though nothing points to it. The reflog, Git's private record of where `HEAD` has been, proves it:

```text
$ git reflog -6
573a346 (HEAD -> main) HEAD@{0}: commit: Summarise the change
f71f66b HEAD@{1}: commit (amend): Add the lemon tart to the menu
5c151e3 HEAD@{2}: commit (amend): Add the lemon tart to the menu
72a36ee HEAD@{3}: commit: stuff
aa2ff61 HEAD@{4}: commit: Mark the start of the spring menu
81f772e HEAD@{5}: commit: Add coconut cake
$ git show --stat --oneline 72a36ee
72a36ee stuff
 menu.md | 1 +
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch19-commits/expected-messages.bash.txt`.*

The reflog lists each move of `HEAD`, newest first: two `commit (amend)` entries and the original commit `72a36ee stuff` further down. The last command shows that the old commit is still readable by its hash. (Chapter 26<!--ref:reflog--> uses this to recover work.)

> **⚠️ CAUTION.** Amend only commits that **you have not shared** with anyone. Once someone else has a copy of the old commit (Chapter 23<!--ref:remotes-->), replacing it creates two different histories with the same beginning, and sorting that out is painful. The rule for the whole book: **do not rewrite history that others already have.** Chapter 27<!--ref:rebase--> covers the safe exceptions.

---

## 19.4 Atomic commits

> **New term: atomic commit.** A commit that contains **one logical change**, complete in itself: not several unrelated changes together, and not half of a change.

The name comes from *atom*: indivisible. A useful test: **can you describe the commit in one sentence without using "and"?** If not, it is probably two commits.

**Why it matters.**

- **Review is easier.** A reader can check one idea at a time.
- **Undoing is precise.** If the price change was a mistake, you can undo it without also undoing the opening hours (Chapter 25<!--ref:undo-->).
- **Searching is easier.** `git log` becomes a readable list of changes.
- **Bugs are easier to find.** Chapter 28<!--ref:tools--> shows a tool that searches history for the commit that broke something; it works best when commits are small.

**How to make them.** You already have the tools: edit, then stage only *some* of the changes with `git add <file>`, and commit; repeat. In the recording, two unrelated changes were made at once: the price of rolls (a change to `menu.md`) and a new file `hours.md`:

```text
$ cd bakery-menu
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.20\n- Coconut cake (slice): 4.00\n' > menu.md
$ printf 'Open Monday to Saturday.\n' > hours.md
$ git status --short
 M menu.md
?? hours.md
$ git add menu.md
$ git commit -m "Raise the price of rolls"
[main bf46067] Raise the price of rolls
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git add hours.md
$ git commit -m "Add the opening hours"
[main b27846f] Add the opening hours
 1 file changed, 1 insertion(+)
 create mode 100644 hours.md
```

*Recorded in Bash; `ch19-commits/expected-atomic.bash.txt`.*

Because the changes were staged separately, they became **two** commits, each with its own message:

```text
$ git log --oneline --stat -2
b27846f (HEAD -> main) Add the opening hours
 hours.md | 1 +
 1 file changed, 1 insertion(+)
bf46067 Raise the price of rolls
 menu.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

*Recorded in Bash; `ch19-commits/expected-atomic.bash.txt`.*

Read the `--stat` summary: the newest commit added only `hours.md`; the one before only changed `menu.md`. Each can be understood, reviewed and undone on its own.

> **Deep.** What if two unrelated changes are inside *one file*? `git add -p` lets you choose, chunk by chunk (each chunk of a diff is a *hunk*, Chapter 17<!--ref:history_view-->), which parts to stage. Git shows each hunk and asks whether to stage it; you answer `y` for yes, `n` for no, `q` to quit and `?` for help. Its prompt is interactive, so it is not shown in a recording here. Practise it in a scratch repository before you rely on it.

**When not to be strict.** The "one logical change" test is a guide, not a law. A tiny fix to a typo you noticed while working, or a change that spans several files but is one idea, is fine. What matters is that a reader can tell what the commit is *for*.

---

## 19.5 Empty commits

> **New term: empty commit.** A commit with a message but no change to any file.

Normally, Git refuses to make a commit when there is nothing to record (Chapter 16<!--ref:firstrepo-->). The option `--allow-empty` overrides that:

```text
$ git commit --allow-empty -m "Mark the start of the spring menu"
[main aa2ff61] Mark the start of the spring menu
```

*Recorded in Bash; `ch19-commits/expected-messages.bash.txt`.*

Empty commits are unusual, but useful as a **marker** in the history ("start of the spring menu") or as a placeholder for a note. Use them sparingly; they add entries that carry no change.

---

## 19.6 Authorship and timestamps

Every commit records two identities and two times:

- **Author**: the person who *wrote* the change, and when.
- **Committer**: the person who *recorded* it in this repository, and when.

Usually they are the same person. They differ when someone applies another person's change (for example a maintainer accepting a contribution), or when a commit is rewritten later (Chapter 27<!--ref:rebase-->).

`git commit --author` records a different author. Here Ada commits a change written by "Grace Baker":

```text
$ cd bakery-menu
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n- Lemon tart: 3.50\n' > menu.md
$ git commit -am "Add the lemon tart to the menu" --author="Grace Baker <grace@example.net>"
[main 85d89ce] Add the lemon tart to the menu
 Author: Grace Baker <grace@example.net>
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch19-commits/expected-authorship.bash.txt`.*

The commit output notes `Author: Grace Baker <grace@example.net>`, because it differs from the committer. The format `fuller` shows both:

```text
$ git log -1 --format=fuller
commit 85d89ce09c6ec84fee0c1defc39afcc321167630 (HEAD -> main)
Author:     Grace Baker <grace@example.net>
AuthorDate: Mon Jan 5 09:09:00 2026 +0000
Commit:     Ada Learner <ada@example.org>
CommitDate: Mon Jan 5 09:09:00 2026 +0000

    Add the lemon tart to the menu
```

*Recorded in Bash; `ch19-commits/expected-authorship.bash.txt`.*

Notice `Author:` and `Commit:` are different people, each with a date (`AuthorDate` and `CommitDate`). A tailored format shows the same in one line per commit:

```text
$ git log --format='%h author=%an committer=%cn %s' -2
85d89ce author=Grace Baker committer=Ada Learner Add the lemon tart to the menu
81f772e author=Ada Learner committer=Ada Learner Add coconut cake
```

*Recorded in Bash; `ch19-commits/expected-authorship.bash.txt`.*

`%an` is the author's name and `%cn` the committer's.

**Honest authorship matters.** Use `--author` only to credit a real person whose change you are recording, with their permission. Git does not verify identities: anyone can *claim* any name and email. To *prove* who made a commit, commits can be **signed** (Chapter 33<!--ref:gitsec-->).

### 19.6.1 Times

The recordings show invented, evenly spaced dates so that they can be reproduced. In real use, Git writes your computer's clock time and time zone offset (for example `+0000`). If your clock or time zone is wrong, your history records the wrong time, and Git will not warn you.

---

## 19.7 Habits that keep history useful

1. **Look before you commit:** `git status`, then `git diff --staged` (Chapter 17<!--ref:history_view-->).
2. **One logical change per commit** (section 19.4).
3. **A subject that says what, a body that says why** (section 19.2).
4. **Commit early and often on your own computer** (small steps are easy to undo), and **tidy before sharing.** A private history may be messy; a shared one should be readable. Chapter 27<!--ref:rebase--> shows how to tidy safely.
5. **Do not commit secrets, large downloads or generated files** (Chapter 18<!--ref:tracking-->).
6. **Do not commit broken work to a shared branch** without a clear reason; an unfinished idea belongs on your own branch (Chapter 20<!--ref:branching-->).
7. **Use `git commit -a` sparingly.** It stages *every* change to tracked files, so you may commit changes you did not mean to (Chapter 16<!--ref:firstrepo-->).
8. **Do not amend a commit that someone else already has** (section 19.3.3).

---

## Checkpoint

## What You Learned

- A commit message is for future readers; write what changed (subject) and why (body).
- Conventions: a short imperative subject, a blank line, a body of sentences. These are conventions, not Git rules.
- `git commit --amend` replaces the last commit with a new one (new hash); the old one is still recoverable. Amend only unshared commits.
- Atomic commits contain one logical change; stage files selectively to make them.
- `--allow-empty` creates a marker commit with no change.
- A commit has an author and a committer, each with a time; `--author` credits another person; Git does not verify identities.

## New Vocabulary

- **git commit --amend**: replaces the last commit with a new one.
- **Atomic commit**: a commit containing one logical change.
- **Empty commit**: a commit with a message but no file change.

## Commands Learned

`git commit -m <subject> -m <body>`, `git commit --amend`, `git commit --amend --no-edit`, `git commit --allow-empty`, `git commit --author`, `git log -1 --format=fuller`, `git reflog`, `git show <hash>`.

## Common Mistakes

1. **Vague messages** such as `stuff` and `update`.
2. **Bundling unrelated changes** in one commit.
3. **Amending a commit that has already been shared.**
4. **Forgetting to look at `git diff --staged`** before committing.
5. **Using `git commit -a` without checking** what it will stage.
6. **Assuming the author field proves who wrote the change.**

## Practice

Do the exercises in [`exercises/ch19-exercises.md`](../../../exercises/ch19-exercises.md).

## Self-Test

1. What are the parts of a good commit message, and what belongs in each?
2. What does `git commit --amend --no-edit` do, and why does the hash change?
3. Give the test for an atomic commit.
4. Where does the commit you replaced with `--amend` go?
5. What is the difference between the author and the committer?
6. Why should you not amend a commit that a colleague already has?

## Before Moving On

You are ready for Chapter 20<!--ref:branching--> if you can:

- [ ] write a subject and body that a colleague would thank you for
- [ ] fix a bad last message and add a forgotten file with `--amend`
- [ ] split two unrelated changes into two commits
- [ ] explain why amending shared history is dangerous

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Message conventions (imperative subject, length, body, footer) | Blank line and 50-character title checked in `git commit`; imperative mood in the project's `SubmittingPatches`; the rest is convention | R165 |
| Amend behaviour: new hash, retained author date, forgotten file, old commit in the reflog and readable by hash | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; identical on the CI runner's Git 2.55.0. Concept and option statements also checked in the Git 2.56.0 manual (git-commit, git-reflog). | R166 |
| Author versus committer, `--author`, `fuller` format | Locally tested (as above). Concept and option statements also checked in the Git 2.56.0 manual (git-commit). | R167 |
| Atomic commits by staging files separately; empty commits | Locally tested (as above). Concept and option statements also checked in the Git 2.56.0 manual (git-commit). | R168 |
| `git add -p` prompt keys; editor comment lines | Described from general knowledge, not recorded | R165 |

## Where this leads

Chapter 20<!--ref:branching--> moves from a single line of commits to parallel lines of work. Chapter 25<!--ref:undo--> uses precise commits to undo changes safely, and Chapter 26<!--ref:reflog--> shows how to recover a commit that seems lost, such as the one replaced by `--amend`.
