---
key: bigrepos
number: 31
tag: Deep
first_read: later
status: draft
requires: [remotes, objects]
ledger: [R203, R204, R205, R206, R207]
---
# Chapter 31 — Big and Complex Repositories [Deep]

**In this chapter**

- `git worktree`: several folders, one repository
- shallow clones: download only recent history
- sparse checkout: show only part of a big project
- submodules: a repository inside a repository
- Git LFS: large files kept outside the history
- what this chapter does not cover, and why

> **Deep.** This chapter is marked **[Deep]**. You can skip it on a first read. Everything here solves a problem that appears when projects grow, and most small projects never meet them.

**Before you start.** Chapter 23<!--ref:remotes--> and Chapter 30<!--ref:objects-->. The recordings use `bakery-menu` and local folders as "remotes" (Chapter 23<!--ref:remotes-->). They ran in Bash and zsh on Git 2.43.0, and git-lfs 3.4.1, and were re-run in CI on Git 2.55.0.

---

## 31.1 Worktrees: another folder, same repository

You are in the middle of a task on one branch, and an urgent fix is needed on another. Chapter 24<!--ref:stash--> offered a stash; another way is a second **working folder** connected to the *same* repository.

> **New term: worktree.** An additional working folder that belongs to the same repository, with its own checked-out branch. All worktrees share one history.

```text
$ cd bakery-menu
$ git worktree add ../bakery-hotfix -b hotfix
Preparing worktree (new branch 'hotfix')
HEAD is now at 81f772e Add coconut cake
$ git worktree list
/home/learner/bakery-menu    81f772e [main]
/home/learner/bakery-hotfix  81f772e [hotfix]
```

*Recorded in Bash; `ch31-bigrepos/expected-worktree.bash.txt`.*

`git worktree add ../bakery-hotfix -b hotfix` created a new folder next to the current one, made a new branch `hotfix`, and checked it out there. `git worktree list` shows both. Work in the new folder like in any repository:

```text
$ cd ../bakery-hotfix
$ printf -- '- Bagels: 1.20\n' >> menu.md
$ git commit -am "Add bagels"
[hotfix 0a5f828] Add bagels
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch31-bigrepos/expected-worktree.bash.txt`.*

Back in the first folder, both branches are visible: the commit made in the other folder is in the shared history.

```text
$ cd ../bakery-menu
$ git log --oneline --all --graph
* 0a5f828 (hotfix) Add bagels
* 81f772e (HEAD -> main) Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch31-bigrepos/expected-worktree.bash.txt`.*

When the fix is finished, remove the extra folder. The branch stays:

```text
$ git worktree remove ../bakery-hotfix
$ git worktree list
/home/learner/bakery-menu  81f772e [main]
$ git branch
  hotfix
* main
```

*Recorded in Bash; `ch31-bigrepos/expected-worktree.bash.txt`.*

Two rules: a branch can be checked out in only *one* worktree at a time, and the extra folders are ordinary folders that you must not delete by hand (use `git worktree remove`).

---

## 31.2 Shallow clones: recent history only

A project with a long history takes time and disk space to download. A **shallow clone** takes only the most recent commits. To demonstrate, a bare repository `hub.git` plays the remote, and it is cloned by its `file://` address (a plain path would copy everything, and ignore the depth):

```text
$ git clone --bare -q bakery-menu hub.git
$ git clone --depth 1 file://$PWD/hub.git shallow
Cloning into 'shallow'...
```

*Recorded in Bash; `ch31-bigrepos/expected-shallow.bash.txt`.*

`--depth 1` asked for only the latest commit.

> **New term: shallow clone.** A clone that contains only the most recent commits, up to a chosen depth, instead of the whole history.

```text
$ cd shallow
$ git log --oneline
81f772e (grafted, HEAD -> main, origin/main, origin/HEAD) Add coconut cake
$ git rev-parse --is-shallow-repository
true
```

*Recorded in Bash; `ch31-bigrepos/expected-shallow.bash.txt`.*

The log has one commit, marked `grafted`: Git has cut the history off there. `--is-shallow-repository` confirms it. Missing history can be fetched later:

```text
$ git fetch --unshallow
$ git log --oneline
81f772e (HEAD -> main, origin/main, origin/HEAD) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
$ git rev-parse --is-shallow-repository
false
```

*Recorded in Bash; `ch31-bigrepos/expected-shallow.bash.txt`.*

After `git fetch --unshallow`, all three commits are there, and the repository is no longer shallow.

**Trade-offs.** A shallow clone is fast and small, which is why it is used in automation (Chapter 54<!--ref:actions-->). But history commands (`log`, `blame`, `bisect`) see only what was downloaded, and some operations do not work in a shallow repository until you fetch more.

---

## 31.3 Sparse checkout: only some folders

Sometimes the whole history is fine, but you only want part of the *files* on disk. A repository with `docs` and `src` folders:

```text
$ cd bakery-menu
$ mkdir docs src
$ printf 'How to bake\n' > docs/guide.md
$ printf 'print\n' > src/main.py
$ git add .
$ git commit -m "Add docs and src"
[main ca85072] Add docs and src
 2 files changed, 2 insertions(+)
 create mode 100644 docs/guide.md
 create mode 100644 src/main.py
$ ls
docs  menu.md  src
```

*Recorded in Bash; `ch31-bigrepos/expected-sparse.bash.txt`.*

`git sparse-checkout set docs` limits the working folder to `docs` (and the files at the top level):

```text
$ git sparse-checkout set docs
$ ls
docs  menu.md
$ git sparse-checkout list
docs
```

*Recorded in Bash; `ch31-bigrepos/expected-sparse.bash.txt`.*

The `src` folder disappeared from the disk, but not from the repository: its files are still in every commit. Turn it off again to get everything back:

```text
$ git sparse-checkout disable
$ ls
docs  menu.md  src
```

*Recorded in Bash; `ch31-bigrepos/expected-sparse.bash.txt`.*

This is the *cone* style of sparse checkout, the simple one, which selects whole folders.

---

## 31.4 Submodules: a repository inside a repository

Sometimes a project uses another repository, such as a shared library, and wants to pin an exact version of it. A **submodule** does that.

> **New term: submodule.** A repository placed inside another repository at a fixed path. The outer repository records *which commit* of the inner one to use.

A small library repository is made first. Then the first attempt to add it as a submodule **fails**:

```text
$ mkdir lib-repo
$ cd lib-repo
$ git init -q
$ printf 'shared code\n' > lib.txt
$ git add lib.txt
$ git commit -q -m "Add lib"
$ cd ../bakery-menu
$ git submodule add ../lib-repo vendor/lib
Cloning into '/home/learner/bakery-menu/vendor/lib'...
fatal: transport 'file' not allowed
fatal: clone of '/home/learner/lib-repo' into submodule path '/home/learner/bakery-menu/vendor/lib' failed
```

*Recorded in Bash; `ch31-bigrepos/expected-submodule.bash.txt`.*

`fatal: transport 'file' not allowed`: Git refuses, by default, to use a local path as the source of a submodule. This is a deliberate safety rule in recent Git versions. For a normal submodule, the address is a network address, and this rule does not matter. To do the demonstration locally we have to allow it explicitly, for this one command only:

```text
$ git -c protocol.file.allow=always submodule add ../lib-repo vendor/lib
Cloning into '/home/learner/bakery-menu/vendor/lib'...
done.
```

*Recorded in Bash; `ch31-bigrepos/expected-submodule.bash.txt`.*

> **⚠️ CAUTION.** Do not switch this protection off permanently (`protocol.file.allow=always` in your global configuration) just to make a local demonstration convenient. The rule exists because cloning a malicious local repository can place unexpected files inside your repository's Git folder (see the documentation note below).

> **Checked against the documentation (Git 2.56.0, R205).** Git's `protocol.allow` documentation says that, by default, "known-safe protocols (http, https, git, ssh) have a default policy of `always`", while "all other protocols (including file) have a default policy of `user`". The `user` policy means that a protocol "is only able to be used when `GIT_PROTOCOL_FROM_USER` is either unset or has a value of 1", and that it is meant for protocols that you use directly but that you do not want used "by commands which execute clone/fetch/push commands without user input, e.g. recursive submodule initialization". The rule came with the security fix for **CVE-2022-39253** (Git 2.30.6 and later releases, including 2.38.1): the release notes say that "the value of `protocol.file.allow` is changed to be `user` by default", and that cloning from a malicious *local* repository could place "arbitrary files" in the new repository's `$GIT_DIR`. That is the reason for the refusal above.

Now the state:

```text
$ git status --short
A  .gitmodules
A  vendor/lib
$ cat .gitmodules
[submodule "vendor/lib"]
	path = vendor/lib
	url = ../lib-repo
$ git submodule status
 2e4ae7032781338fb40d5d24c3d4e709ac2eea22 vendor/lib (heads/main)
```

*Recorded in Bash; `ch31-bigrepos/expected-submodule.bash.txt`.*

`.gitmodules` is a small text file, part of the project, that lists each submodule and where it comes from. `git submodule status` shows the exact commit that is checked out in it. Commit:

```text
$ git commit -m "Add the lib submodule"
[main b3a8826] Add the lib submodule
 2 files changed, 4 insertions(+)
 create mode 100644 .gitmodules
 create mode 160000 vendor/lib
$ git ls-tree -r HEAD
100644 blob 098fc94ae95f14ae76c1b1142e20206bb58df196	.gitmodules
100644 blob 97e3bea37ef238e599134c082bd1ebca865bdb2b	menu.md
160000 commit 2e4ae7032781338fb40d5d24c3d4e709ac2eea22	vendor/lib
```

*Recorded in Bash; `ch31-bigrepos/expected-submodule.bash.txt`.*

Look at the last line: the submodule is recorded as `160000 commit 2e4ae70...`. A submodule is not a folder of files in the outer repository; it is **a pointer to one commit** of the other repository. That is what "pinning a version" means, and it is why a submodule does not change on its own when the library changes.

**Warnings.** Submodules add work: after cloning, people must fetch their contents (the option `--recurse-submodules` does it), and updating a submodule is a separate commit in the outer project. They are a common source of confusion; use them when you truly need to pin another repository. The whole life cycle, recorded (the same `-c protocol.file.allow=always` is needed here only because the "remote" is a local folder). The library was added, committed, and then the project was cloned **with** `--recurse-submodules`:

```text
$ cd bakery-menu
$ git -c protocol.file.allow=always submodule add -q ../lib-repo vendor/lib
$ git commit -qm "Add the lib submodule"
$ cd ..
$ git -c protocol.file.allow=always clone -q --recurse-submodules bakery-menu bakery-copy
$ cd bakery-copy
$ git submodule status
 2e4ae7032781338fb40d5d24c3d4e709ac2eea22 vendor/lib (heads/main)
$ ls vendor/lib
lib.txt
```

*Recorded in Bash; `ch31-bigrepos/expected-submodule-flow.bash.txt`.*

The clone has the library's files (`lib.txt`) at the pinned commit. Now the library gets a new commit, and the project updates its submodule to the library's newest commit with `git submodule update --remote`:

```text
$ cd ../lib-repo
$ printf 'more shared code\n' >> lib.txt
$ git commit -qam "Update lib"
$ cd ../bakery-copy
$ git -c protocol.file.allow=always submodule update --remote vendor/lib
From /home/learner/lib-repo
   2e4ae70..41273bf  main       -> origin/main
Submodule path 'vendor/lib': checked out '41273bf3125415fc50ec5b8cbdb76d5821d39af7'
```

*Recorded in Bash; `ch31-bigrepos/expected-submodule-flow.bash.txt`.*

The outer project sees that the submodule pointer changed (` M vendor/lib`); the change has to be **committed**, so that the project pins the newer version:

```text
$ git status --short
 M vendor/lib
$ git commit -qam "Use the newer lib"
```

*Recorded in Bash; `ch31-bigrepos/expected-submodule-flow.bash.txt`.*

To **remove** a submodule, unregister it and delete it from the project, then commit:

```text
$ git submodule deinit -f vendor/lib
Cleared directory 'vendor/lib'
Submodule 'vendor/lib' (../lib-repo) unregistered for path 'vendor/lib'
$ git rm -q -f vendor/lib
$ git commit -qm "Remove the lib submodule"
$ git ls-files
.gitmodules
menu.md
```

*Recorded in Bash; `ch31-bigrepos/expected-submodule-flow.bash.txt`.*

`.gitmodules` remains in the list of files (now empty of submodule entries), and the library is gone from the project.

> **Checked by running it (R206).** The clone, update and removal above were run in Bash and zsh (Git 2.43.0; CI on 2.55.0). Git's `git submodule` documentation was checked for the commands `update --remote` and `deinit` (Git 2.56.0). Removing a submodule leaves some history behind (the module's Git data can remain in `.git/modules`); this was not investigated.

---

## 31.5 Git LFS: large files

Git stores every version of every file forever (Chapter 30<!--ref:objects-->). For large binary files (images, videos, datasets) that becomes heavy. **Git LFS** (Large File Storage) is an extension that keeps the *contents* of such files on a separate server and stores only a small *pointer* in the repository.

> **New term: Git LFS.** An extension to Git that stores large files outside the normal history, leaving small text pointers in the repository.

LFS is a separate program (`git-lfs`), which must be installed. To use it, first set it up once, then say which files to handle:

```text
$ cd bakery-menu
$ git lfs install
Updated Git hooks.
Git LFS initialized.
$ git lfs track "*.png"
Tracking "*.png"
```

*Recorded in Bash; `ch31-bigrepos/expected-lfs.bash.txt`.*

`git lfs install` wired LFS into Git. `git lfs track "*.png"` says "treat all PNG files with LFS". The rule is stored in `.gitattributes`:

```text
$ cat .gitattributes
*.png filter=lfs diff=lfs merge=lfs -text
```

*Recorded in Bash; `ch31-bigrepos/expected-lfs.bash.txt`.*

Add a picture (here a fake one) and commit:

```text
$ printf 'not really a picture' > logo.png
$ git add .gitattributes logo.png
$ git commit -m "Add logo"
[main a21b8cd] Add logo
 2 files changed, 4 insertions(+)
 create mode 100644 .gitattributes
 create mode 100644 logo.png
```

*Recorded in Bash; `ch31-bigrepos/expected-lfs.bash.txt`.*

`git lfs ls-files` lists the files that LFS manages. And what does *Git* store? Ask for the content of that file inside the commit:

```text
$ git lfs ls-files
fe1a4ab1fb * logo.png
$ git cat-file -p HEAD:logo.png
version https://git-lfs.github.com/spec/v1
oid sha256:fe1a4ab1fb6347036bead73597d5d2958b26ac0b96f68ca2f6dcee53a50f297e
size 20
```

*Recorded in Bash; `ch31-bigrepos/expected-lfs.bash.txt`.*

The repository holds only a three-line **pointer**: a version, a hash (`oid`) and a size. The real 20 bytes are kept by LFS, outside the object database. In this recording nothing was sent to a server; a real project would have LFS storage on the remote.

> **⚠️ CAUTION.** A file committed *before* LFS tracking is already in the history and stays there. Setting up LFS afterwards does not shrink the repository. And the hosting platform may limit LFS storage or bandwidth, which is time-sensitive information that was not checked (Chapter 36<!--ref:whatgh--> returns to platform limits).

> **Checked against the Git LFS specification (R207).** The specification (`docs/spec.md` in the Git LFS project) says that pointer files "MUST contain only UTF-8 characters", that "the first key is _always_ `version`", that the required keys are `version` (a URL), `oid` (a hash "prefixed by its hashing method"; "currently, only `sha256` is supported") and `size` (in bytes), and that a pointer must be "less than 1024 bytes". The recorded pointer matches that format. To convert files that are **already in the history**, Git LFS has `git lfs migrate import`; its documentation says that such conversions "rewrite your Git history", so the cautions of Chapter 33<!--ref:gitsec--> and Chapter 27<!--ref:rebase--> apply. No push to an LFS server was run, and hosting-platform limits are covered in the chapters on the platform.

---

## 31.6 What is not covered

- **Partial clones** and **subtrees** are run below. **Monorepo** versus **multirepo** and **performance tuning** are design advice, not commands; they are described in general terms and not tested.
- **Monorepo** (one big repository for many projects) versus **multirepo** (many small ones). This is a design decision, not a command. Each choice has costs: a monorepo has one history and one place to look, but grows large; many repositories stay small, but sharing code between them is harder.
- **Performance tuning** of large repositories.

### Partial clone

A **partial clone** downloads the commits and trees but leaves out some file contents (blobs), fetching them only when needed. `git clone --filter=blob:none` asks the server for exactly that. The server must allow filters: Git's documentation for `uploadpack.allowFilter` says "if this option is set, `upload-pack` will support partial clone and partial fetch object filtering". Here the local "server" is set up to allow them, and the clone is made by its `file://` address:

```text
$ git clone -q --filter=blob:none file://$PWD/hub.git partial
$ cd partial
$ git config remote.origin.partialclonefilter
blob:none
$ git config extensions.partialclone
$ git log --oneline
81f772e (HEAD -> main, origin/main, origin/HEAD) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
$ git cat-file -p HEAD:menu.md
# Sunrise Bakery menu

- White loaf: 2.80
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch31-bigrepos/expected-partial-clone.bash.txt`.*

The clone records the filter in `remote.origin.partialclonefilter` (`blob:none`). The history is complete, and the first time a file's content is needed (here `git cat-file -p HEAD:menu.md`), Git fetches it on demand. Git's design notes call it "a performance optimization for Git that allows Git to function without having a complete copy of the repository", for "extremely large repositories". The documentation for `--filter` lists other forms, such as `blob:limit=<n>` and `object:type=`.

> **⚠️ CAUTION.** A partial clone depends on the server being reachable later: commands that need a missing file will fetch it, and fail offline.

### Subtree

`git subtree` is an alternative to submodules: the other project's files are copied **into** yours, and its history is either merged or squashed. It is a separate command, from Git's `contrib` collection, and is included in many installations (check with `git subtree`). Adding the library as a squashed subtree:

```text
$ cd bakery-menu
$ git subtree add -q --prefix=vendor/lib ../lib-repo main --squash
git fetch ../lib-repo main
From ../lib-repo
 * branch            main       -> FETCH_HEAD
$ ls vendor/lib
lib.txt
```

*Recorded in Bash; `ch31-bigrepos/expected-subtree.bash.txt`.*

The files are now ordinary files of the outer project, not a pointer:

```text
$ git log --oneline
75db5cc (HEAD -> main) Merge commit '3747446675b9f9036312d68ab8f0bd7e40fc9c87' as 'vendor/lib'
3747446 Squashed 'vendor/lib/' content from commit 2e4ae70
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch31-bigrepos/expected-subtree.bash.txt`.*

The log shows a squashed commit (the library's content at one commit) and a merge commit that puts it under `vendor/lib`. Git's `git-subtree` documentation describes `add`, `merge`, `pull`, `push` and `split`; only `add` was run here. Compared with a submodule, a subtree needs no extra clone step for other people, but the library's history is mixed into your own or squashed.

---

## Checkpoint

## What You Learned

- `git worktree add` gives a second working folder on the same repository; `git worktree remove` cleans up.
- A shallow clone (`--depth`) fetches only recent history; `git fetch --unshallow` completes it.
- Sparse checkout limits which folders appear on disk.
- A submodule records a pointer to one commit of another repository, described in `.gitmodules`; Git refuses local-path submodules by default.
- Git LFS keeps large files outside the history and stores small pointer files.

## New Vocabulary

- **Worktree**: an extra working folder sharing one repository.
- **Shallow clone**: a clone with only recent history.
- **Submodule**: a repository placed inside another, pinned to one commit.
- **Git LFS**: an extension that stores large files outside the normal history.

## Commands Learned

`git worktree add`, `git worktree list`, `git worktree remove`, `git clone --depth`, `git fetch --unshallow`, `git sparse-checkout set`, `git sparse-checkout disable`, `git submodule add`, `git submodule status`, `git lfs install`, `git lfs track`, `git lfs ls-files`.

## Common Mistakes

1. **Deleting a worktree folder by hand.**
2. **Expecting `git log` in a shallow clone to show everything.**
3. **Thinking a sparse checkout removes files from the repository.**
4. **Expecting a submodule to update itself.**
5. **Adding LFS after a large file is already in the history.**

## Practice

Do the exercises in [`exercises/ch31-exercises.md`](../../../exercises/ch31-exercises.md).

## Self-Test

1. What do two worktrees share, and what does each have of its own?
2. Why does `git log` show `grafted` in a shallow clone?
3. What does sparse checkout change: the repository or the folder on disk?
4. What does a submodule record in the outer repository?
5. What does Git store for a file tracked by LFS?

## Before Moving On

You are ready for Chapter 32<!--ref:custom--> if you can:

- [ ] create and remove a worktree
- [ ] make a shallow clone and complete it
- [ ] limit a working folder with sparse checkout
- [ ] explain what a submodule and an LFS pointer are

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Worktree add, list, remove | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R203 |
| Shallow clone, unshallow; sparse checkout | Locally tested (as above), with local bare repositories | R203 |
| Submodule add, the `file` transport refusal, `.gitmodules`, mode 160000 | Locally tested (as above); the reason and the release that introduced the rule checked against the Git documentation and the 2.30.6 release notes | R205 |
| Git LFS install, track, pointer file | Locally tested with git-lfs 3.4.1 (CI: runner's git-lfs), and the pointer format checked against the Git LFS specification; no LFS server | R207 |
| Partial clone (`--filter=blob:none`) and `git subtree add` | Locally tested (as above); checked against the Git 2.56.0 documentation | R204 |
| Monorepo versus multirepo; performance tuning | General advice, **not tested** | R204 |
| Submodule clone (`--recurse-submodules`), `update --remote`, `deinit` and removal | Locally tested (as above) | R206 |

## Where this leads

Chapter 32<!--ref:custom--> customises Git's behaviour. Chapter 54<!--ref:actions--> shows shallow clones in automation, and Chapter 36<!--ref:whatgh--> returns to hosting-platform limits.
