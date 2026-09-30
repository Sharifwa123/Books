---
key: remotes
number: 23
tag: Core
first_read: full
status: draft
requires: [branching, internet, config]
ledger: [R178, R179, R180]
---
# Chapter 23 — Remotes [Core]

**In this chapter**

- what a remote is, using a shared folder on your own computer, with no account and no internet
- `clone`, `push`, `fetch` and `pull`, and the difference between them
- remote-tracking branches such as `origin/main`, and upstream tracking
- what happens when two people push at once
- managing remotes with `git remote`
- **Project 5**: share a repository between two "people"

**Before you start.** Chapter 20<!--ref:branching-->, Chapter 21<!--ref:merging-->, Chapter 22<!--ref:conflicts--> and the idea of a remote from Chapter 5<!--ref:internet-->. Everything here runs on one computer; a hosting platform such as GitHub appears only in Chapter 36<!--ref:whatgh-->.

Every recording was run in Bash and zsh on Git 2.43.0 and re-run in CI on Git 2.55.0.

---

## 23.1 A remote can be a folder

Until now your repository lived in one place. To share work, Git copies commits between repositories. The other repository is called a **remote**, and it does not have to be a website: it can be a folder on the same computer, or one reached over a network. The commands are identical, which is why we can learn them without an account.

We build the smallest sharing arrangement. One **bare repository** plays the shared place. Two people, Alice and Bob, each keep their own copy.

> **New term: bare repository.** A repository with no working files: only Git's database. It is what you share through, because nobody edits files inside it. Hosting platforms keep bare repositories.

```text
$ mkdir shared
$ git init --bare shared/bakery.git
Initialized empty Git repository in /home/learner/shared/bakery.git/
```

*Recorded in Bash; `ch23-remotes/expected-bare.bash.txt`.*

`git init --bare` creates the shared repository. By convention its folder name ends in `.git`. Now Alice **clones** it, meaning she makes her own copy:

```text
$ git clone shared/bakery.git alice
Cloning into 'alice'...
warning: You appear to have cloned an empty repository.
done.
```

*Recorded in Bash; `ch23-remotes/expected-bare.bash.txt`.*

The warning is expected: the shared repository is empty. Alice adds the first commit:

```text
$ cd alice
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.50\n- Rolls (six): 3.00\n' > menu.md
$ git add menu.md
$ git commit -m "Add the menu"
[main (root-commit) 807a5c6] Add the menu
 1 file changed, 4 insertions(+)
 create mode 100644 menu.md
```

*Recorded in Bash; `ch23-remotes/expected-bare.bash.txt`.*

---

## 23.2 The remote, and its name

Ask Git which remotes exist:

```text
$ git remote -v
origin	/home/learner/shared/bakery.git (fetch)
origin	/home/learner/shared/bakery.git (push)
```

*Recorded in Bash; `ch23-remotes/expected-bare.bash.txt`.*

`git clone` created a remote called `origin` and remembered its address. `origin` is only a **name**, a short label for the address, and it is the conventional name for "the place I cloned from". `(fetch)` and `(push)` are two directions and are normally the same address.

Now look at the branches with more detail:

```text
$ git branch -vv
* main 807a5c6 [origin/main: gone] Add the menu
```

*Recorded in Bash; `ch23-remotes/expected-bare.bash.txt`.*

`[origin/main: gone]` is Git's way of saying that Alice's `main` is set to follow `origin/main`, but that branch does not exist yet, because the shared repository is empty. Publishing it fixes that:

```text
$ git push -u origin main
To /home/learner/shared/bakery.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

*Recorded in Bash; `ch23-remotes/expected-bare.bash.txt`.*

Read the output. `* [new branch] main -> main` says a new branch was created in the remote. `-u` (short for `--set-upstream`) also told Git that Alice's `main` should follow `origin/main`:

```text
$ git branch -vv
* main 807a5c6 [origin/main] Add the menu
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

*Recorded in Bash; `ch23-remotes/expected-bare.bash.txt`.*

> **New term: remote-tracking branch.** Your local note of where a branch on a remote was the last time you looked, for example `origin/main`. You cannot commit on it; Git moves it only when you fetch, pull or push.

> **New term: upstream branch.** The branch on a remote that a local branch follows. It is what makes plain `git push` and `git pull` know where to go, and what lets `git status` say `Your branch is up to date with 'origin/main'`.

Now Bob clones the same shared repository:

```text
$ cd ..
$ git clone shared/bakery.git bob
Cloning into 'bob'...
done.
$ cd bob
$ git log --oneline
807a5c6 (HEAD -> main, origin/main, origin/HEAD) Add the menu
$ git remote -v
origin	/home/learner/shared/bakery.git (fetch)
origin	/home/learner/shared/bakery.git (push)
```

*Recorded in Bash; `ch23-remotes/expected-bare.bash.txt`.*

Bob has Alice's commit and the same remote address. Notice `HEAD -> main, origin/main, origin/HEAD`: Bob's `main` and his note of `origin/main` currently point to the same commit.

---

## 23.3 Fetch, and why `pull` is two steps

Alice makes a new commit and pushes it:

```text
$ cd alice
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.00\n' > menu.md
$ git commit -am "Raise the price of the white loaf"
[main 23d585e] Raise the price of the white loaf
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push
To /home/learner/shared/bakery.git
   807a5c6..23d585e  main -> main
```

*Recorded in Bash; `ch23-remotes/expected-fetch.bash.txt`.*

`807a5c6..23d585e main -> main` shows the remote branch moving from the old commit to the new one. Bob has not heard about it yet:

```text
$ cd ../bob
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

*Recorded in Bash; `ch23-remotes/expected-fetch.bash.txt`.*

Bob's Git says he is up to date, but that only describes what he **last knew**. Git does not talk to the remote on its own. To learn what happened, Bob **fetches**:

```text
$ git fetch
From /home/learner/shared/bakery
   807a5c6..23d585e  main       -> origin/main
```

*Recorded in Bash; `ch23-remotes/expected-fetch.bash.txt`.*

> **New term: fetch.** Download new commits and update the remote-tracking branches, **without changing your own branches or files.**

Only `origin/main` moved. Bob's `main` and his files did not. Now his status can tell him something new:

```text
$ git status
On branch main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean
```

*Recorded in Bash; `ch23-remotes/expected-fetch.bash.txt`.*

He can look at the difference safely before deciding anything:

```text
$ git log --oneline main
807a5c6 (HEAD -> main) Add the menu
$ git log --oneline origin/main
23d585e (origin/main, origin/HEAD) Raise the price of the white loaf
807a5c6 (HEAD -> main) Add the menu
$ git diff main origin/main
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

*Recorded in Bash; `ch23-remotes/expected-fetch.bash.txt`.*

Then he brings the work into his branch with **pull**:

```text
$ git pull
Updating 807a5c6..23d585e
Fast-forward
 menu.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

*Recorded in Bash; `ch23-remotes/expected-fetch.bash.txt`.*

> **New term: pull.** Fetch, then integrate: `git pull` is `git fetch` followed by a merge (by default) of the upstream branch into your current branch.

Here the merge was a fast-forward (Chapter 21<!--ref:merging-->) because Bob had nothing of his own. Afterwards:

```text
$ git log --oneline
23d585e (HEAD -> main, origin/main, origin/HEAD) Raise the price of the white loaf
807a5c6 Add the menu
$ git branch -vv
* main 23d585e [origin/main] Raise the price of the white loaf
```

*Recorded in Bash; `ch23-remotes/expected-fetch.bash.txt`.*

**The rule to remember.** `fetch` is safe and only updates your notes. `pull` changes your branch. If you are unsure, fetch first, look, then merge.

---

## 23.4 When two people push at once

Now the case that makes remotes interesting. Alice pushes a commit. Bob, who did not fetch, commits something else and tries to push:

```text
$ cd alice
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.00\n' > menu.md
$ git commit -am "Raise the price of the white loaf"
[main 23d585e] Raise the price of the white loaf
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push
To /home/learner/shared/bakery.git
   807a5c6..23d585e  main -> main
```

*Recorded in Bash; `ch23-remotes/expected-diverge.bash.txt`.*

```text
$ cd ../bob
$ printf 'Open Monday to Saturday.\n' > hours.md
$ git add hours.md
$ git commit -m "Add opening hours"
[main 41cdbf3] Add opening hours
 1 file changed, 1 insertion(+)
 create mode 100644 hours.md
```

*Recorded in Bash; `ch23-remotes/expected-diverge.bash.txt`.*

Bob's push is **rejected**:

```text
$ git push
To /home/learner/shared/bakery.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '/home/learner/shared/bakery.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

*Recorded in Bash; `ch23-remotes/expected-diverge.bash.txt`.*

Read it. `! [rejected] main -> main (fetch first)` says the push was refused, and `(fetch first)` tells him why: the remote has work he does not have. Git protects the shared branch: it will not overwrite Alice's commit. The hint suggests `git pull`. Nothing is lost.

Bob fetches and asks for the state:

```text
$ git fetch
From /home/learner/shared/bakery
   807a5c6..23d585e  main       -> origin/main
$ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

nothing to commit, working tree clean
```

*Recorded in Bash; `ch23-remotes/expected-diverge.bash.txt`.*

`diverged` is the word from Chapter 21<!--ref:merging-->: each side has one commit the other lacks. Now he pulls:

```text
$ git pull
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```

*Recorded in Bash; `ch23-remotes/expected-diverge.bash.txt`.*

Recent versions of Git refuse a `git pull` on diverged branches until you say how to reconcile them: by merging, rebasing or accepting only fast-forwards. You choose once, either for one command or as a setting (Chapter 14<!--ref:config-->). This book chooses **merge** for now, with `--no-rebase`, and `--no-edit` only to skip the editor in the recording:

```text
$ git pull --no-rebase --no-edit
Merge made by the 'ort' strategy.
 menu.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

*Recorded in Bash; `ch23-remotes/expected-diverge.bash.txt`.*

```text
$ git log --oneline --graph
*   4d21943 (HEAD -> main) Merge branch 'main' of /home/learner/shared/bakery
|\
| * 23d585e (origin/main, origin/HEAD) Raise the price of the white loaf
* | 41cdbf3 Add opening hours
|/
* 807a5c6 Add the menu
```

*Recorded in Bash; `ch23-remotes/expected-diverge.bash.txt`.*

The graph is the merge from Chapter 21<!--ref:merging-->, and the merge commit's message names the remote address. Now Bob's push is accepted, since his branch contains everything the remote has:

```text
$ git push
To /home/learner/shared/bakery.git
   23d585e..4d21943  main -> main
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

*Recorded in Bash; `ch23-remotes/expected-diverge.bash.txt`.*

> **⚠️ CAUTION.** When a push is rejected, do **not** reach for `--force`. Forcing tells the remote to discard the commits you do not have, which would delete Alice's work. Fetch, integrate, then push normally. Chapter 33<!--ref:gitsec--> returns to why force-pushing shared branches is dangerous.

> **Checked against the documentation and the source (R180).** The `pull.rebase` and `pull.ff` settings are documented (Git 2.56.0): `pull.rebase` set to true rebases "instead of merging", and the manual calls this "a possibly dangerous operation"; `pull.ff` set to `only` allows only fast-forwards. The `git pull` manual of Git 2.50.0 said that on divergent branches "the user needs to specify how to reconcile the divergent branches with `--rebase` or `--no-rebase`". The manual of Git 2.55.0 and 2.56.0 instead lists `git pull --ff-only` as "the default". The source code settles which is right: in `builtin/pull.c` of Git v2.56.0, when no `--ff`, `--ff-only` or rebase choice is set (on the command line or in configuration) and the branches have diverged, Git shows the advice and stops with `Need to specify how to reconcile divergent branches.` So a plain `git pull` still fast-forwards when it can, still refuses when the branches have diverged, and the recordings on Git 2.43.0, 2.55.0 and 2.56.0 agree with the source. The 2.55+ manual sentence is looser than the behaviour; the book follows the behaviour.

---

## 23.5 Managing remotes

You can have more than one remote. The `git remote` commands manage them:

```text
$ cd alice
$ git remote
origin
$ git remote -v
origin	/home/learner/shared/bakery.git (fetch)
origin	/home/learner/shared/bakery.git (push)
```

*Recorded in Bash; `ch23-remotes/expected-remote-cmds.bash.txt`.*

Add a second remote, rename it, and push to it:

```text
$ git remote add backup ../shared/bakery.git
$ git remote -v
backup	../shared/bakery.git (fetch)
backup	../shared/bakery.git (push)
origin	/home/learner/shared/bakery.git (fetch)
origin	/home/learner/shared/bakery.git (push)
$ git remote rename backup mirror
$ git remote
mirror
origin
$ git push mirror main
Everything up-to-date
```

*Recorded in Bash; `ch23-remotes/expected-remote-cmds.bash.txt`.*

Here `mirror` points at the same shared repository, so Git found nothing new to send. List the remote-tracking branches, then remove the remote:

```text
$ git branch -r
  mirror/main
  origin/main
$ git remote remove mirror
$ git remote
origin
$ git branch -r
  origin/main
```

*Recorded in Bash; `ch23-remotes/expected-remote-cmds.bash.txt`.*

Removing a remote also removes its remote-tracking branches, as the second `git branch -r` shows. Finally, the tracking setup is stored as ordinary configuration (Chapter 14<!--ref:config-->):

```text
$ git config --get remote.origin.url
/home/learner/shared/bakery.git
$ git config --get branch.main.remote
origin
$ git config --get branch.main.merge
refs/heads/main
```

*Recorded in Bash; `ch23-remotes/expected-remote-cmds.bash.txt`.*

`branch.main.remote` says which remote, and `branch.main.merge` says which branch on it. Together they are the "upstream" from section 23.2.

---

## 23.6 Push, fetch and pull at a glance

| Command | Talks to the remote? | Changes your branch? | Changes the remote? |
|---|---|---|---|
| `git fetch` | Yes | No (only `origin/...` notes) | No |
| `git pull` | Yes | Yes (fetch, then merge) | No |
| `git push` | Yes | No | Yes |
| `git clone` | Yes | Creates a new repository | No |
| `git status` | **No** | No | No |

The last row matters: `git status` compares with the **last fetched** state, not with what is on the remote right now.

---

## 23.7 Project 5: share a repository between two people

> **Project 5.** *Goal:* act as two collaborators on one computer. *Time:* about 40 minutes. *You need:* Git configured (Chapter 14<!--ref:config-->) and an empty folder to work in.

1. Create a bare repository `shared/bakery.git`. Clone it twice, as `alice` and `bob`.
2. As Alice, add `menu.md`, commit, and `git push -u origin main`.
3. As Bob, `git pull` and confirm that the menu arrived.
4. As Alice, change a price and push. As Bob, run `git fetch`, then `git status`, then `git diff main origin/main`, then `git pull`.
5. Make both people commit *different* files without fetching. Let Bob push first, then Alice; read Alice's rejection, fetch, pull, and push.
6. Draw the final graph with `git log --oneline --graph --all` and explain each line.

*Expected result:* step 5 produces one rejected push, and after the pull a merge commit and a successful push. Both clones end with the same history.

*Checkpoint questions:* Why did `git status` not tell Bob about Alice's change before he fetched? Which commands changed his branch, and which did not?

---

## Checkpoint

## What You Learned

- A remote is another repository; it can be a local folder. A bare repository is what you share through.
- `git clone` copies a repository and creates the remote `origin`.
- `git push -u origin main` publishes a branch and sets its upstream.
- `git fetch` updates `origin/...` without touching your branches; `git pull` is fetch plus merge.
- A push is rejected when the remote has commits you lack; fetch, integrate, push again. Never force it to get past this.
- `git remote` adds, renames, lists and removes remotes; tracking settings are ordinary configuration.

## New Vocabulary

- **Bare repository**: a repository without working files, used as a shared hub.
- **Remote-tracking branch**: your local note of a remote branch, such as `origin/main`.
- **Upstream branch**: the remote branch a local branch follows.
- **Fetch**: download new commits without changing your branches.
- **Pull**: fetch, then merge into the current branch.

## Commands Learned

`git init --bare`, `git clone`, `git remote`, `git remote -v`, `git remote add`, `git remote rename`, `git remote remove`, `git push -u origin main`, `git push`, `git fetch`, `git pull`, `git pull --no-rebase`, `git branch -vv`, `git branch -r`.

## Common Mistakes

1. **Believing `git status` shows the remote's current state.**
2. **Using `pull` blindly** instead of fetching and looking first.
3. **Forcing a rejected push.**
4. **Forgetting `-u`** on the first push, then wondering why `git pull` says there is no tracking information.
5. **Confusing the remote's name (`origin`) with its address.**

## Practice

Do the exercises in [`exercises/ch23-exercises.md`](../../../exercises/ch23-exercises.md), including Project 5 (section 23.7).

## Self-Test

1. What does `git clone` create besides a copy of the files?
2. What does `-u` do in `git push -u origin main`?
3. Which changes: `git fetch`, or `git pull`?
4. Why was Bob's push rejected in section 23.4, and what was the safe response?
5. What is `origin/main`, and when does it move?

## Before Moving On

You are ready for Chapter 24<!--ref:stash--> if you can:

- [ ] build a bare repository and clone it twice
- [ ] explain fetch versus pull, and prove it with `git status`
- [ ] resolve a rejected push without forcing
- [ ] list, add, rename and remove a remote

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Bare repository, clone, `remote -v`, `push -u`, tracking, `origin/main` | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; identical on CI's Git 2.55.0 | R178 |
| Fetch changes only `origin/...`; status wording after fetch; pull fast-forward | Locally tested (as above) | R179 |
| Rejected push, divergence, pull advice, `git remote` subcommands | Locally tested (as above), same result on Git 2.43.0, 2.55.0 and 2.56.0; `pull.rebase`/`pull.ff` and the `git pull` default checked in the manuals, source `builtin/pull.c` v2.56.0 confirms the refusal, the manual's "default" wording is looser; hosting-platform behaviour not covered | R180 |

## Where this leads

Chapter 24<!--ref:stash--> adds small everyday tools. Chapter 36<!--ref:whatgh--> and Chapter 39<!--ref:ghrepo--> replace the shared folder with a hosting platform: the commands stay the same, and only the address and the sign-in change. Chapter 45<!--ref:pr--> shows how platforms turn "pull before you push" into a review process.
