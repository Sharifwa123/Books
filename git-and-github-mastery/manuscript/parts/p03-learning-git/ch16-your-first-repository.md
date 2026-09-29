---
key: firstrepo
number: 16
tag: Core
first_read: full
status: draft
requires: [model]
ledger: [R155, R156, R157]
---
# Chapter 16 — Your First Repository [Core]

**In this chapter**

- how to turn a folder into a Git repository (`git init`)
- how to read `git status`, the command you will run more than any other
- how to stage (`git add`) and record (`git commit`) your work
- **Project 1**: track a simple folder of study notes
- **Project 2 (start)**: put the Sunrise Bakery site under version control
- the everyday mistakes at this stage, with their real error messages

**Before you start.** Chapter 15<!--ref:model--> (working tree, index, repository, the four file states), Chapter 14<!--ref:config--> (your name, email and default branch are set) and Chapter 7<!--ref:terminal--> (typing commands). Open your terminal and go to `~/sharif-git-lab`.

Every recording in this chapter was run for real in Bash and zsh, using the fictional user Ada Learner. Hashes and dates in your own terminal will differ from the recordings.

---

## 16.1 Turning a folder into a repository

You do not "install" version control on a project. You tell Git: *start keeping the history of this folder*. That is `git init`.

> **New term: git init.** Creates a new, empty Git repository in the current folder, by making the hidden `.git` folder inside it.

Before you run it, look at where you are. **`git init` acts on the current folder**, so a wrong `pwd` gives you a repository in the wrong place.

```text
$ mkdir -p sharif-git-lab
$ cd sharif-git-lab
$ mkdir study-notes
$ cd study-notes
$ git status
fatal: not a git repository (or any of the parent directories): .git
$ git init
Initialized empty Git repository in /home/learner/sharif-git-lab/study-notes/.git/
$ ls -a
.  ..  .git
```

*Recorded in Bash; `ch16-firstrepo/expected-notes.bash.txt`.*

Read the recording step by step:

1. `mkdir study-notes` and `cd study-notes` made a new practice folder and entered it.
2. `git status` said `fatal: not a git repository`. That is not a disaster; it is the correct answer. It means: *this folder is not tracked by Git yet*. It is also the quickest way to find out whether a folder is a repository.
3. `git init` created the repository, and reported where: `.../study-notes/.git/`.
4. `ls -a` shows the new hidden folder `.git` (Chapter 2<!--ref:files-->).

The folder looks the same as before, but it now has a memory.

> **⚠️ CAUTION.** Run `git init` only in a folder that is meant to be one project. Never run it in your home folder, or in a folder that already sits inside another repository, because Git would then try to track everything below it. If you ever create one by mistake, delete only the hidden `.git` folder that you just made (and nothing else), after checking with `pwd` and `ls -a`. Deleting `.git` removes the *history*, not your files, so do it only when the repository is new and holds nothing you want.

---

## 16.2 `git status`: the command you will run constantly

> **New term: git status.** Shows which files are untracked, modified or staged, and which branch you are on.

Run `git status` before and after nearly everything you do. It never changes anything, so it is always safe. Chapter 15<!--ref:model--> introduced the four file states; here they are again in a real session:

```text
$ git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

*Recorded in Bash; `ch16-firstrepo/expected-notes.bash.txt`.*

A new, empty repository. `On branch main` names the branch (Chapter 20<!--ref:branching-->). `No commits yet` means the history is empty. Now the first file:

```text
$ printf '# Study notes\n\nToday I learned what version control is.\n' > notes.md
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	notes.md

nothing added to commit but untracked files present (use "git add" to track)
```

*Recorded in Bash; `ch16-firstrepo/expected-notes.bash.txt`.*

`notes.md` is **untracked**. Git lists it and suggests the next command: `git add`.

Git's suggestions in the parentheses, like `(use "git add <file>..." to include in what will be committed)`, are worth reading: they change with the state and tell you the command that makes sense next.

---

## 16.3 Staging: `git add`

> **New term: git add.** Puts the current contents of a file (or files) into the index, so that they will be part of the next commit.

```text
$ git add notes.md
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   notes.md

```

*Recorded in Bash; `ch16-firstrepo/expected-notes.bash.txt`.*

After `git add notes.md`, the same file appears under `Changes to be committed`. Nothing has been recorded yet: the file is **staged**. Notice the hint `(use "git rm --cached <file>..." to unstage)`; Chapter 25<!--ref:undo--> teaches how to take a file back out of the staging area.

### 16.3.1 The forms of `git add`

| Command | What it stages | When to use it |
|---|---|---|
| `git add notes.md` | That one file | The safest habit: you choose exactly what goes in |
| `git add notes.md menu.md` | Several named files | Same |
| `git add css/` | Everything inside a folder | A folder that belongs together |
| `git add .` | Every new and changed file in the current folder and below | Only after `git status` has shown you *what* is there |

> **⚠️ CAUTION.** `git add .` stages everything under the current folder, including things you never meant to record: passwords in a settings file, large downloads, temporary files. Chapter 18<!--ref:tracking--> teaches how to keep those out. Until then, run `git status` first and check every file in the list.

---

## 16.4 Recording: `git commit`

> **New term: git commit.** Records what is in the index as a new snapshot in the history, with a message.

```text
$ git commit -m "Add first study notes"
[main (root-commit) dffcc1c] Add first study notes
 1 file changed, 3 insertions(+)
 create mode 100644 notes.md
$ git status
On branch main
nothing to commit, working tree clean
```

*Recorded in Bash; `ch16-firstrepo/expected-notes.bash.txt`.*

Decode the output of `git commit -m "Add first study notes"`:

```text
[main (root-commit) dffcc1c] Add first study notes
 1 file changed, 3 insertions(+)
 create mode 100644 notes.md
```

- `main` is the branch that received the commit.
- `(root-commit)` appears only for the very first commit of a repository: it has no parent.
- `dffcc1c` is the short form of the new commit's hash.
- The rest of the first line is the message.
- The next line summarises the change: one file, three lines added.
- `create mode 100644 notes.md` says a new file was recorded (the number is its file mode, Chapter 15<!--ref:model-->).

Then `git status` says `nothing to commit, working tree clean`: the working tree matches the last snapshot.

### 16.4.1 The message

The `-m` option supplies the message on the command line, in quotes. Write what the change does, in a short sentence: `Add first study notes`, not `stuff` or `changes`. Chapter 19<!--ref:commits--> is about writing good messages, because you (and your team) will read them for years.

### 16.4.2 Reading the history

```text
$ git log
commit dffcc1c3a28fc135c5cc88c0fb8149fefc625a87 (HEAD -> main)
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:10:00 2026 +0000

    Add first study notes
```

*Recorded in Bash; `ch16-firstrepo/expected-notes.bash.txt`.*

`git log` shows the history, newest first: the full hash, the author, the date, and the message. Chapter 17<!--ref:history_view--> shows many more ways to read it.

---

## 16.5 Project 1: track a folder of study notes

> **Project 1.** *Goal:* put a folder of your own notes under version control and record three versions of it. *Time:* about 20 minutes. *You need:* a terminal in `sharif-git-lab` and a text editor.

1. Create a folder `study-notes` and enter it. Run `git status`; expect `fatal: not a git repository`.
2. Run `git init`. Check with `ls -a` and `git status`.
3. Create `notes.md` with a title and one sentence (use your editor, or the `printf` command in the recording above). Run `git status`. Which state is the file in?
4. Stage it (`git add notes.md`) and check `git status` again.
5. Commit it: `git commit -m "Add first study notes"`. Check `git status` and `git log`.
6. Add a second sentence to `notes.md`, save, and run `git status`. Which state is it in now? Stage and commit it with a suitable message.
7. Add a new file, `questions.md`, with two questions you have about Git. Stage and commit it.
8. Run `git log`. You should see three commits, with your own messages.

*Expected result:* `git status` reports `nothing to commit, working tree clean`, and `git log` lists three commits, newest first.

*Checkpoint questions:* At step 3, where was the change (working tree, index or repository)? What would have happened to `questions.md` at step 7 if you had run `git commit` without `git add`?

---

## 16.6 Project 2 (start): the Sunrise Bakery site

Now a real project. You copied the Sunrise Bakery starter files into `~/sharif-git-lab/sunrise-bakery` in Chapter 3<!--ref:editors-->. Put them under version control:

```text
$ cd sharif-git-lab/sunrise-bakery
$ ls
README.md  contact.html  css  images  index.html  menu.html
$ git init
Initialized empty Git repository in /home/learner/sharif-git-lab/sunrise-bakery/.git/
$ git status
On branch main

No commits yet

Untracked files:
```

*Recorded in Bash; `ch16-firstrepo/expected-bakery.bash.txt`.*

The listing shows the six items of the project, and `git status` shows them all as untracked (a folder such as `css/` is shown as one entry, and its files are staged individually later). Because this is the first commit and the folder holds only the files we mean to record, `git add .` is safe here.

```text
$ git add .
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   README.md
	new file:   contact.html
	new file:   css/style.css
	new file:   images/logo.svg
	new file:   index.html
	new file:   menu.html

$ git commit -m "Add the Sunrise Bakery starter site"
[main (root-commit) 0ed5bc9] Add the Sunrise Bakery starter site
 6 files changed, 127 insertions(+)
 create mode 100644 README.md
 create mode 100644 contact.html
 create mode 100644 css/style.css
 create mode 100644 images/logo.svg
 create mode 100644 index.html
 create mode 100644 menu.html
```

*Recorded in Bash; `ch16-firstrepo/expected-bakery.bash.txt`.*

The `git status` after staging lists every file as `new file`, including `css/style.css` and `images/logo.svg` inside the folders. The commit output summarises the whole change: six files, 127 lines added.

```text
$ git log --stat
commit 0ed5bc9afc23af4d12117d41bb8a958c3cfccffd (HEAD -> main)
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:08:00 2026 +0000

    Add the Sunrise Bakery starter site

 README.md       | 12 ++++++++++++
 contact.html    | 27 +++++++++++++++++++++++++++
 css/style.css   | 24 ++++++++++++++++++++++++
 images/logo.svg |  5 +++++
 index.html      | 27 +++++++++++++++++++++++++++
 menu.html       | 32 ++++++++++++++++++++++++++++++++
 6 files changed, 127 insertions(+)
$ git ls-files
README.md
contact.html
css/style.css
images/logo.svg
index.html
menu.html
```

*Recorded in Bash; `ch16-firstrepo/expected-bakery.bash.txt`.*

`git log --stat` adds a summary of the files changed by each commit, and `git ls-files` lists all files Git tracks. Notice the paths, `css/style.css` and `images/logo.svg`: relative paths from the top of the project (Chapter 2<!--ref:files-->), exactly the form that Git uses in every message.

Project 2 continues in later chapters: you will change the site, review the changes, branch, merge, and publish it.

---

## 16.7 The mistakes everyone makes first

Every message below is real, recorded on Git 2.43.0 and re-run on a newer Git. Read them now, so that they are familiar when they appear.

### 16.7.1 Committing before staging

```text
$ git commit -m "Try to commit before staging"
On branch main

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	a.txt

nothing added to commit but untracked files present (use "git add" to track)
```

*Recorded in Bash; `ch16-firstrepo/expected-mistakes.bash.txt`.*

Git refused. It did not say "error"; it repeated the state (`Untracked files`) and ended with `nothing added to commit but untracked files present`. **A commit records only what is staged**, so with nothing staged there is nothing to commit. The fix is `git add`.

### 16.7.2 Leaving the message empty

If you run `git commit` without `-m`, Git opens your editor so that you can write a message, and expects you to save and close the editor. If you save an **empty** message, Git aborts:

```text
$ git add a.txt
$ git commit
hint: Waiting for your editor to close the file...
Aborting commit due to empty commit message.
$ git status --short
A  a.txt
```

*Recorded in Bash; `ch16-firstrepo/expected-mistakes.bash.txt`.*

`Aborting commit due to empty commit message.` The file stayed staged (`A  a.txt`), so no work was lost. (The hint line about the editor depends on your editor; the recording used a stand-in that closes at once and writes nothing.)

> **Deep.** If an unfamiliar editor opens and you cannot leave it, remember that it is a program like any other and that an editor's help or a search for its name plus "how to exit" will tell you. Better still, choose an editor you know for Git (Chapter 13<!--ref:install-->), or always use `-m`. (The exit keys of particular terminal editors are not covered here.)

### 16.7.3 Nothing new to commit

```text
$ git commit -m "Add a.txt"
[main (root-commit) 2cfec03] Add a.txt
 1 file changed, 1 insertion(+)
 create mode 100644 a.txt
$ git commit -m "Commit again with nothing new"
On branch main
nothing to commit, working tree clean
```

*Recorded in Bash; `ch16-firstrepo/expected-mistakes.bash.txt`.*

The second `git commit` said `nothing to commit, working tree clean`. That is not an error: it means there is no change to record.

### 16.7.4 A change that was never staged

```text
$ printf 'second\n' >> a.txt
$ git commit -m "Commit without staging"
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

*Recorded in Bash; `ch16-firstrepo/expected-mistakes.bash.txt`.*

The file was **modified** but not staged, so Git refused: `no changes added to commit`. Look at the last line: `(use "git add" and/or "git commit -a")`. The option `-a` means "automatically stage every change to files that Git already tracks":

```text
$ git commit -am "Stage and commit tracked changes in one step"
[main 1a3f294] Stage and commit tracked changes in one step
 1 file changed, 1 insertion(+)
$ git log --oneline
1a3f294 (HEAD -> main) Stage and commit tracked changes in one step
2cfec03 Add a.txt
```

*Recorded in Bash; `ch16-firstrepo/expected-mistakes.bash.txt`.*

`git commit -am "..."` staged the modification and committed it in one step. Use it only for files that Git already tracks; it never picks up *new* files, and it stages every tracked change, so check `git status` first. Chapter 19<!--ref:commits--> returns to this.

### 16.7.5 "Please tell me who you are"

If you have not set `user.name` and `user.email` (Chapter 13<!--ref:install-->), Git cannot say who made the commit, and stops with a message beginning `Author identity unknown`, followed by instructions to set them. The exact wording depends on your computer's name, so it is not recorded here; the fix is the two `git config --global` commands from Chapter 13<!--ref:install-->.

### 16.7.6 A new repository's first branch

If `init.defaultBranch` is not set, older Git versions create a branch called `master` and print a long hint about it. Newer versions print the same kind of hint and announce a planned change of default:

```text
$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Initialized empty Git repository in /home/learner/demo/.git/
```

*Recorded in Bash; `ch16-firstrepo/expected-nodefault.bash.txt`.*

*This is Git 2.43.0. On the newer Git that ran in the book's automated checks (2.55.0), the same command prints a hint that says the default branch name **will change to "main" in Git 3.0**.*

```text
$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
```

*Recorded in Bash; `ch16-firstrepo/expected-nodefault.bash.alt.txt`.*

*The newer form, recorded from the automated check on Git 2.55.0.*

That is why Chapter 13<!--ref:install--> asked you to set `init.defaultBranch` yourself: with it set, no hint appears and the branch name is the one you chose.

> **Verification pending [R157].** The two hints were produced by two Git versions and the plan for a future default is stated by Git's own output; the official announcement and documentation have not been consulted.

---

## 16.8 What you can do now

You can turn any folder into a repository, see what state its files are in, choose what goes into a snapshot and record it with a message. That is a complete, working version-control workflow. Everything else in this book adds to it: seeing differences (Chapter 17<!--ref:history_view-->), keeping the wrong things out (Chapter 18<!--ref:tracking-->), writing good messages (Chapter 19<!--ref:commits-->), working in parallel (Chapters 20<!--ref:branching--> to 22<!--ref:conflicts-->), and sharing (Chapter 23<!--ref:remotes-->).

---

## Checkpoint

## What You Learned

- `git init` makes the current folder a repository by creating `.git`; run it in the right folder only.
- `git status` reports the state of every file, is always safe, and suggests the next command.
- `git add` stages; `git commit -m` records what is staged, with a message.
- The commit output tells you the branch, `(root-commit)` for the first commit, the short hash, the message and a summary.
- A commit records only what is staged; `git commit -am` stages tracked, modified files for you.
- Common errors: nothing staged, empty message, nothing to commit, an unstaged modification, unknown identity.

## New Vocabulary

- **git init**: creates a new repository in the current folder.
- **git status**: shows the state of files and the current branch.
- **git add**: stages files for the next commit.
- **git commit**: records the staged snapshot with a message.

## Commands Learned

`git init`, `git status`, `git status --short`, `git add <file>`, `git add .`, `git commit -m`, `git commit -am`, `git log`, `git log --oneline`, `git log --stat`, `git ls-files`.

## Common Mistakes

1. **Running `git init` in the wrong folder.**
2. **Running `git add .` without looking at `git status`.**
3. **Expecting a commit to include unstaged changes.**
4. **Saving an empty commit message.**
5. **Writing messages like "stuff".**
6. **Assuming "nothing to commit" is an error.**

## Practice

Do the exercises in [`exercises/ch16-exercises.md`](../../../exercises/ch16-exercises.md), including Project 1 (section 16.5).

## Self-Test

1. What does `git init` create, and where?
2. How can you find out whether a folder is already a repository?
3. What is the difference between `git add` and `git commit`?
4. What does `(root-commit)` in the commit output mean?
5. Why did `git commit -m "Commit without staging"` fail in the recording, and what fixes it?
6. What is the danger of `git add .`?

## Before Moving On

You are ready for Chapter 17<!--ref:history_view--> if you can:

- [ ] create a repository, stage a file and commit it from memory
- [ ] read a `git status` report and say which state each file is in
- [ ] explain "nothing to commit" and "no changes added to commit"
- [ ] show your project's history with `git log --oneline`

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `git init`, `git status`, `git add`, `git commit`, `git log`, `git ls-files` outputs for the study-notes and bakery projects | Locally tested: Bash 5.2 and zsh 5.9 on Git 2.43.0; re-run in CI on Git 2.55.0 with identical output | R155 |
| The error and refusal messages of section 16.7 | Locally tested; the initial-branch hint differs between 2.43.0 and 2.55.0 (both recorded) | R156, R157 |
| The `Author identity unknown` message | Described, not recorded: depends on the computer's name | R156 |

## Where this leads

Chapter 17<!--ref:history_view--> reads the history you have created and compares versions. Chapter 18<!--ref:tracking--> shows which files should never be staged and how to tell Git to ignore them. Chapter 19<!--ref:commits--> turns the habit of committing into the craft of good commits.
