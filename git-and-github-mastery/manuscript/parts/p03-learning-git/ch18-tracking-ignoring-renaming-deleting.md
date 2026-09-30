---
key: tracking
number: 18
tag: Core
first_read: full
status: draft
requires: [firstrepo, text]
ledger: [R161, R162, R163, R164]
---
# Chapter 18 — Tracking, Ignoring, Renaming, Deleting [Core]

**In this chapter**

- which files belong in a repository, and which never should
- the `.gitignore` file: how to write it, test it and fix it
- personal ignore rules that apply to every repository (the global ignore file)
- why ignoring a file does *not* stop Git tracking it, and what to do about that
- renaming and deleting files in a way that Git understands
- why secrets never belong in a repository

**Before you start.** Chapter 16<!--ref:firstrepo--> (staging, committing), Chapter 17<!--ref:history_view--> (reading `git status` and diffs) and Chapter 4<!--ref:text--> (why files can differ in invisible ways). The Sunrise Bakery project is used again; recordings begin from its first commit.

Every recording was run in Bash and zsh on Git 2.43.0 and re-run in CI on Git 2.55.0, with identical output.

---

## 18.1 Not everything belongs in a repository

Chapter 16<!--ref:firstrepo--> warned that `git add .` stages *everything*. A repository is a project's history, and history should hold the project's **source**: the things people write and need. It should not hold things that are:

| Kind of file | Why it should not be committed | Examples |
|---|---|---|
| **Secrets** | Anything committed stays in history, even after deletion (section 18.8). | Passwords, API keys, private keys, `.env` files |
| **Generated files** | They can be rebuilt from the source, and they change on every build, filling history with noise. | Compiled output, minified files, `build/` or `dist/` folders |
| **Dependencies** | They belong to other people, are large, and can be downloaded again from a list. | `node_modules/`, downloaded libraries |
| **Logs and temporary files** | They are private to one run or one computer. | `*.log`, `*.tmp`, editor swap files |
| **Personal or machine-specific files** | They mean nothing on another computer. | `.DS_Store`, `Thumbs.db`, editor settings |
| **Very large binary files** | They bloat every copy of the history forever. | Raw video, big archives (see Chapter 31<!--ref:bigrepos-->) |

The tool for keeping them out is a plain text file called `.gitignore`.

---

## 18.2 The four kinds of file, and a fifth

You met four states in Chapter 15<!--ref:model-->: untracked, modified, staged, committed. Ignoring adds a fifth.

> **New term: ignored file.** A file that Git has been told to leave alone: it is not shown as untracked and is not staged by `git add .`.

An ignored file still exists in your working tree. Git just pretends not to see it.

---

## 18.3 `.gitignore`

> **New term: .gitignore.** A text file, kept in the repository, that lists patterns of files Git should ignore.

The recording starts with a clean bakery project. A learner adds three files that should not be committed: a build log, a temporary note and a settings file that holds a secret. (The "secret" is a made-up value. Nothing in this book ever asks you to use a real one.)

```text
$ cd sharif-git-lab/sunrise-bakery
$ git status
On branch main
nothing to commit, working tree clean
$ printf 'error log\n' > build.log
$ printf 'draft notes\n' > notes.tmp
$ printf 'PAYMENT_API_KEY=FAKE_TOKEN_DO_NOT_USE_0000\n' > .env
$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.env
	build.log
	notes.tmp

nothing added to commit but untracked files present (use "git add" to track)
$ git status --short
?? .env
?? build.log
?? notes.tmp
```

*Recorded in Bash; `ch18-tracking/expected-tracking.bash.txt`.*

Git lists all three as untracked. `git add .` would have staged every one of them. Now the ignore file:

```text
$ printf '*.log\n*.tmp\n.env\n' > .gitignore
$ git status --short
?? .gitignore
```

*Recorded in Bash; `ch18-tracking/expected-tracking.bash.txt`.*

The command wrote a `.gitignore` containing three lines: `*.log`, `*.tmp` and `.env`. Afterwards `git status --short` shows *only* `.gitignore` itself as new: the three files have disappeared from Git's view. Git can even tell you *why* each was ignored:

```text
$ git check-ignore -v build.log notes.tmp .env
.gitignore:1:*.log	build.log
.gitignore:2:*.tmp	notes.tmp
.gitignore:3:.env	.env
```

*Recorded in Bash; `ch18-tracking/expected-tracking.bash.txt`.*

`git check-ignore -v` prints, for each file, the rule that ignores it: the file `.gitignore`, the line number and the pattern. This command is your first tool when an ignore rule does not behave as you expect.

To see the ignored files themselves, add `--ignored`:

```text
$ git status --short --ignored
?? .gitignore
!! .env
!! build.log
!! notes.tmp
```

*Recorded in Bash; `ch18-tracking/expected-tracking.bash.txt`.*

The `!!` marks mean *ignored*. Finally, commit the ignore file itself, so that everyone who clones the project gets the same rules:

```text
$ git add .gitignore
$ git commit -m "Ignore logs, temporary files and the local environment file"
[main 8de9399] Ignore logs, temporary files and the local environment file
 1 file changed, 3 insertions(+)
 create mode 100644 .gitignore
$ git ls-files
.gitignore
README.md
contact.html
css/style.css
images/logo.svg
index.html
menu.html
```

*Recorded in Bash; `ch18-tracking/expected-tracking.bash.txt`.*

Notice that the listing of tracked files contains `.gitignore` but none of the three ignored files.

> **A rule worth remembering.** `.gitignore` is a normal, tracked file. Commit it, so the whole team shares the rules.

> **Checked against the documentation (R161).** The pattern rules recorded here agree with `gitignore` (Git 2.56.0): a blank line matches nothing; a line starting with `#` is a comment; `!` at the start negates a pattern, but "it is not possible to re-include a file if a parent directory of that file is excluded"; a slash at the end matches only directories; `*` matches anything except a slash and `?` any one character except a slash; a pattern with a slash at the beginning or middle is relative to the `.gitignore` file's directory, and otherwise may match at any level below. Also documented there: `**/` matches in all directories, `/**` matches everything inside, and `a/**/b` matches zero or more directories. The order of precedence (command line, then `.gitignore` files, then `.git/info/exclude`, then `core.excludesFile`) and the default for `core.excludesFile`, `$XDG_CONFIG_HOME/git/ignore` (or `$HOME/.config/git/ignore`), are in the same page.

---

## 18.4 Writing patterns

Each line of `.gitignore` is a **pattern**. Blank lines are skipped, and a line starting with `#` is a comment. The patterns used in this chapter are these:

| Pattern | Matches | Notes |
|---|---|---|
| `*.log` | Any file whose name ends in `.log`, in any folder | `*` stands for any characters |
| `build/` | A folder called `build`, and everything in it | A trailing `/` means *directory* |
| `/todo.txt` | `todo.txt` in the **top folder only** | A leading `/` anchors the pattern to the top of the repository |
| `docs/*.tmp` | `.tmp` files directly inside `docs` | A pattern with a `/` in the middle is relative to the top |
| `!important.log` | An **exception**: do not ignore this file, even though an earlier rule did | `!` negates; it must come after the rule it overrides |

A recording tests all of them at once. Eight files are created and the five patterns are written:

```text
$ mkdir patterns-demo
$ cd patterns-demo
$ git init
Initialized empty Git repository in /home/learner/patterns-demo/.git/
$ mkdir build docs logs
$ printf 'x\n' > app.log
$ printf 'x\n' > important.log
$ printf 'x\n' > todo.txt
$ printf 'x\n' > docs/todo.txt
$ printf 'x\n' > build/output.js
$ printf 'x\n' > docs/draft.tmp
$ printf 'x\n' > docs/notes.md
$ printf 'x\n' > logs/today.log
$ printf '*.log\n!important.log\nbuild/\n/todo.txt\ndocs/*.tmp\n' > .gitignore
```

*Recorded in Bash; `ch18-tracking/expected-patterns.bash.txt`.*

Which files does Git now treat as new, and which are ignored?

```text
$ git status --short
?? .gitignore
?? docs/
?? important.log
$ git status --short --ignored
?? .gitignore
?? docs/
?? important.log
!! app.log
!! build/
!! docs/draft.tmp
!! logs/
!! todo.txt
```

*Recorded in Bash; `ch18-tracking/expected-patterns.bash.txt`.*

Read the two reports together.

- **New (not ignored):** `.gitignore`; `docs/` (it still holds `docs/todo.txt` and `docs/notes.md`, which no pattern matches); and `important.log`, saved by the `!important.log` exception.
- **Ignored (`!!`):** `app.log` (rule `*.log`); `build/` (the whole folder, rule `build/`); `docs/draft.tmp` (rule `docs/*.tmp`); `logs/` (its only file, `today.log`, matches `*.log`); and `todo.txt` in the top folder (rule `/todo.txt`).
- **Not ignored although named `todo.txt`:** `docs/todo.txt`: the leading `/` anchored the rule to the top folder only.

Now the explanation by rule:

```text
$ git check-ignore -v app.log important.log todo.txt docs/todo.txt build/output.js docs/draft.tmp logs/today.log
.gitignore:1:*.log	app.log
.gitignore:2:!important.log	important.log
.gitignore:4:/todo.txt	todo.txt
.gitignore:3:build/	build/output.js
.gitignore:5:docs/*.tmp	docs/draft.tmp
.gitignore:1:*.log	logs/today.log
```

*Recorded in Bash; `ch18-tracking/expected-patterns.bash.txt`.*

Read each line as *file, line number and pattern, then the path it applied to*. Notice that `important.log` was reported with the exception rule `!important.log`, that is, it matched an exception and is therefore **not** ignored; and `docs/todo.txt` does not appear because no rule matched it. (Git also stops looking inside an ignored folder: `build/output.js` was ignored because the folder `build/` was.)

### 18.4.1 Comments and organisation

A `.gitignore` can carry comments to say *why*, which is kind to the next person:

```text
# Secrets and local settings: never commit these
.env

# Build output: rebuilt from the source
build/
dist/

# Editor and operating-system files
.DS_Store
*.swp
```

### 18.4.2 Starting points for real projects

Projects of the same kind ignore similar things. These are *starting points*, not complete lists; adapt them to your own project.

**A static website like the bakery's**

```text
.env
*.log
*.tmp
.DS_Store
Thumbs.db
```

**A project that downloads its libraries with a package tool (for example a JavaScript project)**

```text
node_modules/
dist/
build/
.env
*.log
```

**A Python project**

```text
__pycache__/
*.pyc
.venv/
.env
```

> **Checked against GitHub's template collection (R162).** These lists are short illustrations. Compared with the `Node.gitignore` and `Python.gitignore` templates in GitHub's `github/gitignore` repository (the collection used by GitHub's template chooser): `node_modules/`, `dist`, `.env` and `*.log` appear in the Node template (which has `build/Release` rather than a plain `build/`); `__pycache__/`, `.venv`, `.env`, `build/` and `dist/` appear in the Python template, and it ignores `*.py[codz]`, a wider pattern than `*.pyc`. The templates are much longer than the lists here. Before relying on a list for a real project, start from a current, maintained template and adjust it to your own project.

### 18.4.3 Exceptions and ignored folders

An exception only works if Git still *looks inside* the folder. Suppose a project has a folder of large originals, `assets/raw/`, which should be ignored, except for one file, `logo-final.psd`, that must be kept. The obvious rules do not work; the recording shows both the failure and the fix:

```text
$ mkdir -p assets/raw
$ printf 'x\n' > assets/raw/logo-final.psd
$ printf 'x\n' > assets/raw/big.psd
$ printf 'assets/raw/\n!assets/raw/logo-final.psd\n' > .gitignore
$ git status --short --ignored
?? .gitignore
!! assets/
$ printf 'assets/raw/*\n!assets/raw/logo-final.psd\n' > .gitignore
$ git status --short --ignored
?? .gitignore
?? assets/
!! assets/raw/big.psd
```

*Recorded in Bash; `ch18-tracking/expected-exception.bash.txt`.*

With the rule `assets/raw/` (the folder), Git ignored the **whole folder** (`!! assets/`) and never looked at the exception, so `logo-final.psd` was ignored too. After the rules were changed to ignore the folder's *contents* (`assets/raw/*`) and then to re-include the one file, the file appears as new (`?? assets/`) and only `big.psd` stays ignored (`!! assets/raw/big.psd`).

**The rule:** you cannot re-include a file if a parent folder is ignored. Ignore the folder's contents instead of the folder.

---

## 18.5 Personal rules: the global ignore file

Some files you want ignored in *every* repository on your computer, because they come from *your* tools, not from the project: an operating-system file, an editor's swap files. Putting those in each project's `.gitignore` would clutter it with other people's habits. Git lets you keep a personal list.

```text
$ mkdir demo
$ cd demo
$ git init
Initialized empty Git repository in /home/learner/demo/.git/
$ git config --global core.excludesFile ~/.gitignore_global
$ printf '.DS_Store\n*.swp\n' > ~/.gitignore_global
$ git config --global --get core.excludesFile
/home/learner/.gitignore_global
$ printf 'x\n' > .DS_Store
$ printf 'y\n' > notes.txt
$ git status --short
?? notes.txt
$ git check-ignore -v .DS_Store
/home/learner/.gitignore_global:1:.DS_Store	.DS_Store
```

*Recorded in Bash; `ch18-tracking/expected-global-ignore.bash.txt`.*

The setting `core.excludesFile` (Chapter 14<!--ref:config-->) points at a file of your choice; the recording writes two patterns into it, `.DS_Store` and `*.swp`, and then creates two files in a fresh repository. `git status --short` shows only `notes.txt`. `git check-ignore -v` shows the rule came from the **global** file: `/home/learner/.gitignore_global`, line 1.

**Where each kind of rule belongs.**

| Rule | Put it in | Why |
|---|---|---|
| Something every contributor must ignore (`node_modules/`, `.env`) | The project's `.gitignore` | Shared with the team |
| Something only *your* tools produce | Your global ignore file | Private to you |

---

## 18.6 Ignoring does not untrack

This is the most common surprise. `.gitignore` only affects files that Git is **not yet tracking**. If a file is already in the history, adding it to `.gitignore` changes nothing:

```text
$ printf 'temporary\n' > scratch.txt
$ git add scratch.txt
$ git commit -m "Add scratch file"
[main 0c6c05c] Add scratch file
 1 file changed, 1 insertion(+)
 create mode 100644 scratch.txt
$ printf 'scratch.txt\n' > .gitignore
$ git status --short
?? .gitignore
```

*Recorded in Bash; `ch18-tracking/expected-states.bash.txt`.*

`scratch.txt` was committed. The learner then wrote `scratch.txt` into `.gitignore`. `git status --short` reports only the new `.gitignore`; it says **nothing** about `scratch.txt`, which Git is still tracking and will keep tracking. Ignoring alone did not help.

To stop tracking a file **without deleting it** from your working tree, use `git rm --cached`:

```text
$ git rm --cached scratch.txt
rm 'scratch.txt'
$ git status --short
D  scratch.txt
?? .gitignore
$ git commit -am "Stop tracking the scratch file"
[main 936eed8] Stop tracking the scratch file
 1 file changed, 1 deletion(-)
 delete mode 100644 scratch.txt
$ git status --short
?? .gitignore
```

*Recorded in Bash; `ch18-tracking/expected-states.bash.txt`.*

- `git rm --cached scratch.txt` removed the file from the index only. `git status --short` shows `D  scratch.txt`: *staged for deletion from the repository*, while the file itself stays in the folder.
- The commit recorded that the repository no longer contains it. From now on the `.gitignore` rule applies, and the file is left alone.

> **⚠️ CAUTION.** Stopping tracking removes the file from *future* versions. It remains in the older commits, so anyone can still read it in history. If a file contains a secret, ignoring or untracking it is **not enough**; see section 18.8 and Chapter 33<!--ref:gitsec-->.

---

## 18.7 Renaming and deleting

### 18.7.1 Renaming: `git mv`

> **New term: git mv.** Renames or moves a file and stages that change in one step.

```text
$ git mv menu.html carte.html
$ git status --short
R  menu.html -> carte.html
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    menu.html -> carte.html

```

*Recorded in Bash; `ch18-tracking/expected-states.bash.txt`.*

`git mv menu.html carte.html` renamed the file and staged the rename. `git status` reports `renamed: menu.html -> carte.html`. Git does not actually store "renames": it stores snapshots. It works out that a rename happened because a file disappeared and another with (nearly) the same contents appeared. The commit output says so in words: `rename menu.html => carte.html (100%)`, where 100% means the contents are identical.

You can also rename the file in your file manager or with `mv`, and then tell Git with `git add` for both the old and the new name; Git will still recognise the rename. `git mv` is simply the tidier way.

> **Renaming has a side effect for a website.** Other pages that link to `menu.html` now point at a file that no longer exists. Git tracked the rename but cannot fix your links: check them.

### 18.7.2 Deleting: `git rm`

> **New term: git rm.** Deletes a file from the working tree and stages the deletion.

```text
$ git rm contact.html
rm 'contact.html'
$ git status --short
R  menu.html -> carte.html
D  contact.html
```

*Recorded in Bash; `ch18-tracking/expected-states.bash.txt`.*

`git rm contact.html` deleted the file and staged the deletion (`D` in the first column). Now the commit:

```text
$ git commit -m "Rename the menu page and remove the contact page"
[main a496e78] Rename the menu page and remove the contact page
 2 files changed, 27 deletions(-)
 rename menu.html => carte.html (100%)
 delete mode 100644 contact.html
$ git ls-files
README.md
carte.html
css/style.css
images/logo.svg
index.html
$ git log --oneline --stat -1
a496e78 (HEAD -> main) Rename the menu page and remove the contact page
 menu.html => carte.html |  0
 contact.html            | 27 ---------------------------
 2 files changed, 27 deletions(-)
```

*Recorded in Bash; `ch18-tracking/expected-states.bash.txt`.*

The commit recorded two things at once: a rename and a deletion. `git log --oneline --stat -1` shows them: the renamed file with `0` lines changed, and `contact.html` with 27 lines removed. Because Git keeps history, **the deleted file is not lost**: it still exists in the earlier commit, and Chapter 25<!--ref:undo--> shows how to bring it back.

### 18.7.3 Deleting without `git rm`

If you delete a file in your file manager, or with `rm`, Git notices and tells you, but does not stage the deletion for you:

```text
$ rm contact.html
$ git status --short
 D contact.html
$ git status
On branch main
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    contact.html

no changes added to commit (use "git add" and/or "git commit -a")
```

*Recorded in Bash; `ch18-tracking/expected-manual-delete.bash.txt`.*

The state is `deleted` in the *working tree*, not staged (` D`, the letter in the second column). You can stage the deletion with `git add` (it works for deleted files too), or undo the deletion:

```text
$ git add contact.html
$ git status --short
D  contact.html
$ git restore --staged contact.html
$ git restore contact.html
$ git status --short
$ ls
README.md  contact.html  css  images  index.html  menu.html
```

*Recorded in Bash; `ch18-tracking/expected-manual-delete.bash.txt`.*

- `git add contact.html` staged the deletion (`D  contact.html`).
- `git restore --staged contact.html` took it out of the index again, and `git restore contact.html` brought the file back from the last commit. The final `ls` shows `contact.html` is back.

This is the first look at **restoring**; Chapter 25<!--ref:undo--> teaches it properly. Note that it worked because the file had been committed: **Git can only restore what it has recorded.**

---

## 18.8 Secrets never belong in a repository

Section 18.1 listed secrets first for a reason. Suppose the settings file `.env` held a real password, and a learner ran `git add .` and committed. The password is now part of the history. Deleting the file later removes it from the *newest* version only. It remains in the commit where it was added, and in every copy of the repository that has that commit: every clone, and every backup. Anyone with the repository can read it.

Here is the proof, recorded with a made-up token. A settings file is committed, then deleted in the next commit:

```text
$ mkdir secret-demo
$ cd secret-demo
$ git init
Initialized empty Git repository in /home/learner/secret-demo/.git/
$ printf 'PAYMENT_API_KEY=FAKE_TOKEN_DO_NOT_USE_0000\n' > .env
$ git add .env
$ git commit -m "Add settings"
[main (root-commit) c512a2f] Add settings
 1 file changed, 1 insertion(+)
 create mode 100644 .env
$ git rm .env
rm '.env'
$ git commit -m "Remove the settings file"
[main 9ee72a4] Remove the settings file
 1 file changed, 1 deletion(-)
 delete mode 100644 .env
$ git ls-files
$ git log --oneline
9ee72a4 (HEAD -> main) Remove the settings file
c512a2f Add settings
$ git show HEAD~1:.env
PAYMENT_API_KEY=FAKE_TOKEN_DO_NOT_USE_0000
```

*Recorded in Bash; `ch18-tracking/expected-secret-history.bash.txt`.*

The file is gone from the newest version (`git ls-files` printed nothing), yet `git show HEAD~1:.env` printed it exactly as it was in the earlier commit. The syntax `<commit>:<path>` means *the file at that path, as of that commit*. The "deleted" secret is one command away for anyone with the repository. (`git log -p -- .env` would show it too, in the diff of the commit that added the file.)

The habit that prevents the problem is the one shown in section 18.3:

1. **Create `.gitignore` before the first commit**, listing `.env` and similar files.
2. Run `git status` before you stage anything, and **read the whole list**.
3. Keep a template such as `.env.example`, with fake values, in the repository, so that others know what settings to create.
4. If a secret *is* committed, treat the secret as **stolen**: replace it at once (change the password, revoke the key), and only then think about cleaning history (Chapter 33<!--ref:gitsec--> and Chapter 79<!--ref:playbooks-->).

> **Security note.** In this book, every example secret contains the word `FAKE`, and the repository's automated checks refuse to accept anything that looks like a real credential and does not carry that marker.

---

## 18.9 When `.gitignore` seems not to work

Work through these questions, in order. The first tool is `git check-ignore -v <file>`.

| Symptom | Likely cause | Fix |
|---|---|---|
| The file is still shown as modified or staged | The file is already **tracked** (section 18.6) | `git rm --cached <file>` and commit |
| `git check-ignore -v` prints nothing for the file | No pattern matches | Check the pattern and where the rule lives (leading `/`, trailing `/`) |
| A file inside an ignored folder is not ignored *as expected* | A later `!` exception un-ignored it | Read the rules in order; the last matching rule wins |
| The rule is in the wrong folder | A `.gitignore` applies to its own folder and below | Move the rule to the right file |
| The rule is in a *local-only* place | You put it in your global file, so teammates do not have it | Put shared rules in the project's `.gitignore` |

---

## Checkpoint

## What You Learned

- A repository should hold source, not secrets, generated files, dependencies, logs, machine-specific or very large files.
- `.gitignore` lists patterns of files to ignore; commit it so that everyone shares it.
- Patterns: `*`, a trailing `/` for directories, a leading `/` for the top folder, `!` for exceptions.
- `git check-ignore -v` explains why a file is ignored; `git status --ignored` lists ignored files.
- Personal rules go in a global ignore file (`core.excludesFile`).
- Ignoring does not untrack a file that is already tracked: use `git rm --cached`.
- `git mv` renames and `git rm` deletes, both staged; Git recognises renames by content.
- Files deleted outside Git show as `deleted`; `git restore` can bring back committed files.
- A secret in history is exposed even after the file is deleted.

## New Vocabulary

- **Ignored file**: a file Git has been told to leave alone.
- **.gitignore**: a text file listing patterns of files Git should ignore.
- **git mv**: renames or moves a file and stages the change.
- **git rm**: deletes a file and stages the deletion.

## Commands Learned

`git check-ignore -v`, `git status --ignored`, `git rm`, `git rm --cached`, `git mv`, `git restore`, `git restore --staged`, `git config --global core.excludesFile`.

## Common Mistakes

1. **Adding a secret to the repository** "just to get it working".
2. **Writing a `.gitignore` rule after the file is already tracked**, and expecting it to untrack the file.
3. **Forgetting the trailing `/`** for a directory pattern, or the leading `/` for a top-level file.
4. **Putting personal rules in the shared `.gitignore`.**
5. **Using `rm`/`mv` outside Git and forgetting to stage the change.**
6. **Not committing the `.gitignore`.**

## Practice

Do the exercises in [`exercises/ch18-exercises.md`](../../../exercises/ch18-exercises.md).

## Self-Test

1. Name four kinds of file that should not be committed, and say why.
2. Write the `.gitignore` lines that ignore all `.log` files, a folder called `build`, and a file `secret.txt` only in the top folder.
3. What does the exception pattern `!important.log` do, and why must it come after the rule it overrides?
4. You added `notes.tmp` to `.gitignore`, but Git still shows it as modified. Why, and what do you do?
5. What is the difference between `git rm file` and `git rm --cached file`?
6. A real password was committed yesterday and deleted from the newest version today. Is it safe? What should you do first?

## Before Moving On

You are ready for Chapter 19<!--ref:commits--> if you can:

- [ ] write a `.gitignore` for the bakery project and test it with `git check-ignore -v`
- [ ] explain why `.gitignore` alone does not untrack a file
- [ ] rename and delete a tracked file with Git
- [ ] explain why a committed secret is exposed even after deletion

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The behaviour and output of ignoring, check-ignore, status --ignored, the global ignore file, and of the five patterns | Locally tested: Bash 5.2, zsh 5.9, Git 2.43.0; identical on the CI runner's Git 2.55.0; pattern rules checked in `gitignore` (Git 2.56.0) | R161 |
| The `.gitignore` starting points for a website, JavaScript and Python projects | Compared with GitHub's `Node.gitignore` and `Python.gitignore` templates; not run | R162 |
| Ignoring does not untrack; `git rm --cached`; `git mv`; `git rm`; deleted-outside-Git and `git restore` | Locally tested (as above) | R163 |
| A secret stays in history after the file is deleted | Locally tested with a made-up token (`session-secret-history`); Chapter 33<!--ref:gitsec--> shows the full incident response | R164 |

## Where this leads

Chapter 19<!--ref:commits--> turns the habit of committing into good commits. Chapter 25<!--ref:undo--> returns to `git restore` and shows how to undo changes safely. Chapter 33<!--ref:gitsec--> deals in depth with secrets that have already been committed, and Chapter 32<!--ref:custom--> shows the related file `.gitattributes`.
