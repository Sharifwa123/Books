---
key: whatgh
number: 36
tag: Core
first_read: full
status: draft
requires: [platforms, remotes]
ledger: [R224, R225, R226, R227]
---
# Chapter 36 — What GitHub Is (and Is Not) [Core]

**In this chapter**

- what GitHub is, in one honest paragraph
- what it is not
- how the Git you already know connects to it
- the pieces that a GitHub repository has, beyond Git
- how to read GitHub facts in this book

> **Independent publication.** This book is an independent educational publication by SHARIF TECHNOLOGIES. It is not affiliated with, endorsed by, sponsored by, or published by Git, GitHub, Microsoft, or any company mentioned. Names of products and companies are trademarks of their respective owners and are used here only to identify them.

> **⚠️ Read this first: how GitHub facts appear in this book.** Everything so far (Parts I to IV) was tested by running Git on a computer. Part V is different. GitHub is a *service on the internet* that changes over time, and its official documentation could not be reached while this part was written. So **every statement about how GitHub looks or behaves is marked *Verification pending*** and is recorded in the research ledger. Treat those statements as a map that must be checked against GitHub's current documentation and your own screen before you rely on them. The parts about **Git** (commands, the remote, URLs) were run and tested.

**Before you start.** Chapter 12<!--ref:platforms--> and Chapter 23<!--ref:remotes-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on Git 2.55.0.

---

## 36.1 One honest paragraph

**Git** is the version-control program that you have used in Parts III and IV. It runs on your computer, needs no account and no internet, and works the same with any remote (Chapter 23<!--ref:remotes-->).

**GitHub** (defined in Chapter 12<!--ref:platforms-->) is an online platform that hosts Git repositories and adds services around them, such as pull requests, issue tracking and automation.

In terms of what you learned, GitHub is **a remote with a website and services attached**. A remote is a place that holds a copy of your repository, that you `push` to and `fetch` from. The shared folder `hub.git` in Chapter 23<!--ref:remotes--> and Chapter 34<!--ref:workflows--> did the first part of that job. GitHub does the same, from anywhere on the internet, and adds features for working together: discussing changes, reviewing them, tracking tasks, and running automatic checks.

> **Verification pending [R224].** That summary of what GitHub offers is general knowledge. The precise list of features, and which of them are available on which plan, is time-sensitive and was not verified. The following chapters return to each feature in turn.

---

## 36.2 What GitHub is not

| Misunderstanding | The reality |
|---|---|
| "GitHub is Git." | Chapter 12<!--ref:platforms--> |
| "You need GitHub to use Git." | No. Everything in Parts III and IV worked with no account and no network. |
| "Everything on GitHub is Git." | A repository's *code and history* are Git. Features such as issues and pull requests belong to the platform, and are stored by it (not in your `.git` folder). |
| "A repository on GitHub is public." | Chapter 39<!--ref:ghrepo--> |
| "GitHub is a backup." | Chapter 23<!--ref:remotes--> |
| "GitHub is neutral and permanent." | Chapter 65<!--ref:licences--> |

> **Verification pending [R225].** The last two rows are general statements about services. The terms of service, the ownership of GitHub, and what happens to content when an account or a repository is removed were not checked against official documents.

---

## 36.3 How your Git connects to it

To Git, a GitHub repository is just another remote, with a web address. Add one to a repository. This example uses a made-up address (`example-owner/sunrise-bakery`) and **does not contact the internet**: `git remote add` only records the address.

```text
$ cd bakery-menu
$ git remote add origin https://github.com/example-owner/sunrise-bakery.git
```

*Recorded in Bash; `ch36-whatgh/expected-remote-url.bash.txt`.*

```text
$ git remote -v
origin	https://github.com/example-owner/sunrise-bakery.git (fetch)
origin	https://github.com/example-owner/sunrise-bakery.git (push)
```

*Recorded in Bash; `ch36-whatgh/expected-remote-url.bash.txt`.*

Two lines: one address to fetch from, one to push to. The address is stored in the configuration:

```text
$ git config --get remote.origin.url
https://github.com/example-owner/sunrise-bakery.git
```

*Recorded in Bash; `ch36-whatgh/expected-remote-url.bash.txt`.*

Notice that `git branch -vv` shows no connection to a remote branch yet:

```text
$ git branch -vv
* main 81f772e Add coconut cake
```

*Recorded in Bash; `ch36-whatgh/expected-remote-url.bash.txt`.*

That is right: nothing has been pushed, so `main` does not follow any `origin/main` (Chapter 23<!--ref:remotes-->). The rest of the connection works exactly as it did with the shared folder: `git push -u origin main`, `git fetch`, `git pull`. The differences are the *address*, and *who you are*: because the service belongs to somebody else, it needs to know who is asking (Chapter 6<!--ref:accounts-->, Chapter 38<!--ref:ghauth-->).

**The anatomy of that address.** `https://github.com/example-owner/sunrise-bakery.git` has the parts that Chapter 5<!--ref:internet--> described: a scheme (`https`), a host (`github.com`), and a path: an **owner** (`example-owner`, a person or an organisation) and a **repository name** (`sunrise-bakery`). The `.git` at the end is common but often optional.

> **Verification pending [R226].** That the same commands work against GitHub, that `.git` is optional in the address, and the other address styles (SSH addresses, for example) were not tested; there was no internet access to GitHub for this chapter. Chapter 39<!--ref:ghrepo--> runs them, with a real account and the current documentation, when its facts can be checked.

---

## 36.4 What a repository has beyond Git

A GitHub repository contains your Git repository, and around it a set of services. As a **map for the next chapters** (all of it to be checked):

| Piece | What it is for | Chapter |
|---|---|---|
| Code and history | Your Git repository (files, commits, branches, tags) | Chapter 39<!--ref:ghrepo--> |
| README and licence | The description shown for the project; the terms of reuse | Chapter 39<!--ref:ghrepo--> and Chapter 65<!--ref:licences--> |
| Issues | Tracking tasks, bugs and ideas | Chapter 44<!--ref:issues--> |
| Pull requests | Proposing, discussing and reviewing changes | Chapter 45<!--ref:pr--> |
| Actions | Automatic checks and tasks that run on the platform's computers | Chapter 54<!--ref:actions--> |
| Releases | Named, downloadable versions built on tags | Chapter 66<!--ref:releases--> |
| Settings and security | Access, protection, scanning and secrets | Chapter 49<!--ref:collab--> and Chapter 62<!--ref:ghsec--> |

> **Verification pending [R227].** This table is general knowledge of what GitHub offers at the time of writing. Names, availability and the exact scope of each piece must be checked in the official documentation and on a real account. The chapter numbers refer to where this book covers each one.

**Where does it live?** The first row is in your Git repository, and you can clone it. The other pieces, such as issues and pull requests, are stored by the platform; a normal `git clone` does **not** bring them with you. If you want to keep them, you need another way (Chapter 74<!--ref:api-->).

---

## 36.5 Why learn Git first

This book taught computers first, then Git, then GitHub, on purpose. Because you know what a remote is, a repository is, a branch is, and how to undo and to recover, the platform's features make sense as *layers* over things you already understand. And if the platform changes its buttons, its plans or its name, the Git knowledge remains.

---

## Checkpoint

## What You Learned

- GitHub is an online platform that hosts Git repositories and adds services; it is not Git.
- You do not need GitHub to use Git.
- To Git, a GitHub repository is a remote with a web address; `git remote add` only records it.
- A repository's code is Git; issues, pull requests and similar features are stored by the platform.
- Every GitHub statement in this book is marked *Verification pending* until checked.

## New Vocabulary

No new terms. This chapter uses **GitHub** and **hosting platform** from Chapter 12<!--ref:platforms-->.

## Commands Learned

`git remote add origin <url>`, `git remote -v`, `git config --get remote.origin.url`.

## Common Mistakes

1. **Believing that GitHub is Git.**
2. **Thinking a clone brings issues and pull requests with it.**
3. **Publishing a repository without deciding that it should be public.**
4. **Treating a hosted copy as a backup plan.**
5. **Trusting a GitHub fact, in any source, without checking its date.**

## Practice

Do the exercises in [`exercises/ch36-exercises.md`](../../../exercises/ch36-exercises.md). None needs a GitHub account.

## Self-Test

1. In one sentence, what is GitHub, in terms of what you know about remotes?
2. Name two things in this book that worked without GitHub.
3. Which pieces of a GitHub repository come with `git clone`, and which do not?
4. What does `git remote add origin <url>` do, and what does it not do?
5. Why are the GitHub facts in this part marked as pending?

## Before Moving On

You are ready for Chapter 37<!--ref:ghaccount--> if you can:

- [ ] explain the difference between Git and GitHub
- [ ] add a remote by address and read `git remote -v`
- [ ] name the parts of a GitHub repository address
- [ ] say which features belong to the platform and not to Git

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `git remote add`, `remote -v`, `config --get`, no upstream before a push | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0; **no network access to GitHub** | R226 |
| What GitHub offers, and the map of features | **Not verified** (official documentation not reachable) | R224, R227 |
| Terms, ownership, permanence, plans | **Not verified** | R225 |

## Where this leads

Chapter 37<!--ref:ghaccount--> covers accounts and profiles, Chapter 38<!--ref:ghauth--> covers signing in from Git, and Chapter 39<!--ref:ghrepo--> creates a first repository. Each will be verified against the official documentation before it is finished.
