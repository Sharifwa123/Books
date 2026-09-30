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

> **Independent publication.** This book is an independent educational work by Sharif Tingane Issah, issued under the SHARIF TECHNOLOGIES name. It is not affiliated with, endorsed by, sponsored by, or published by Git, GitHub, Microsoft, or any company mentioned. Names of products and companies are trademarks of their respective owners and are used here only to identify them.

> **How GitHub facts are checked in this book.** Parts I to IV were tested by running Git on a computer. GitHub is a *service on the internet* that changes over time, so its statements are checked differently: against GitHub's own documentation, whose source is published as the open `github/docs` repository (checked at commit `2eaab0b`, 29 September 2026), and, for legal terms, against GitHub's `site-policy` repository (commit `b9578b5`, 29 May 2026). Both are recorded in `research/sources-manifest.csv`. What the *website looks like* was not seen on a live account, so descriptions of screens are labelled, and anything the sources do not cover stays marked *Verification pending*. The parts about **Git** (commands, the remote, URLs) were run and tested.

**Before you start.** Chapter 12<!--ref:platforms--> and Chapter 23<!--ref:remotes-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on Git 2.55.0.

---

## 36.1 One honest paragraph

**Git** is the version-control program that you have used in Parts III and IV. It runs on your computer, needs no account and no internet, and works the same with any remote (Chapter 23<!--ref:remotes-->).

**GitHub** (defined in Chapter 12<!--ref:platforms-->) is an online platform that hosts Git repositories and adds services around them, such as pull requests, issue tracking and automation.

In terms of what you learned, GitHub is **a remote with a website and services attached**. A remote is a place that holds a copy of your repository, that you `push` to and `fetch` from. The shared folder `hub.git` in Chapter 23<!--ref:remotes--> and Chapter 34<!--ref:workflows--> did the first part of that job. GitHub does the same, from anywhere on the internet, and adds features for working together: discussing changes, reviewing them, tracking tasks, and running automatic checks.

> **Checked against GitHub's documentation (R224).** GitHub's page "What is GitHub?" says GitHub "is a platform for building software" that supports the stages Plan, Create, Review, Test, Deploy and Operate, and that it "is based on the open-source software, Git" and builds on it "by hosting your Git projects, called repositories, in the cloud, as well as adding planning and collaboration tools". Which features are available on which plan is time-sensitive; look at the current plans page before relying on one.

---

## 36.2 What GitHub is not

| Misunderstanding | The reality |
|---|---|
| "GitHub is Git." | Chapter 12<!--ref:platforms--> |
| "You need GitHub to use Git." | No. Everything in Parts III and IV worked with no account and no network. |
| "Everything on GitHub is Git." | A repository's *code and history* are Git. Features such as issues and pull requests belong to the platform, and are stored by it (not in your `.git` folder). |
| "A repository on GitHub is public." | Chapter 39<!--ref:ghrepo--> |
| "GitHub is a backup." | Chapter 23<!--ref:remotes--> |
| "GitHub is neutral and permanent." | GitHub's Terms of Service (site-policy repository) say "You own Your Content", that GitHub "may refuse or remove User-Generated Content that violates applicable law or our terms and policies", and that after an account is cancelled GitHub will, barring legal requirements, "delete your full profile and the Content of your repositories within 90 days" and that this "cannot be recovered". The same terms name Microsoft as an Affiliate of GitHub. Chapter 65<!--ref:licences--> returns to ownership and licences. |

> **Checked against the Terms of Service (R225).** The row above quotes GitHub's Terms of Service as published in its `site-policy` repository on the date given at the start of this chapter. The book quotes it to show that a hosting service is not a permanent archive; it is not legal advice, and terms change. Read the current terms before you rely on any of it.

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

**The anatomy of that address.** `https://github.com/example-owner/sunrise-bakery.git` has the parts that Chapter 5<!--ref:internet--> described: a scheme (`https`), a host (`github.com`), and a path: an **owner** (`example-owner`, a person or an organization) and a **repository name** (`sunrise-bakery`). The `.git` at the end is common but often optional.

> **Checked in part against GitHub's documentation (R226).** "About remote repositories" says that you can push to two kinds of address, an HTTPS URL like `https://github.com/user/repo.git` and an SSH URL like `git@github.com:user/repo.git`, that HTTPS clone URLs "are available on all repositories, regardless of visibility" and "work even if you are behind a firewall or proxy", and that SSH needs a key pair with the public key added to your account. That `.git` at the end of the address is optional was **not** found in these pages and is not relied on. The `git remote add` commands here were run locally without contacting GitHub.

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

> **Checked against GitHub's documentation (R227).** Each row names a feature that has its own section in the current documentation: repositories, issues, pull requests, GitHub Actions and releases. For releases, "About releases" says that they "are based on Git tags", that a tag date "may be different" from a release date, and that GitHub "will automatically include links to download a zip file and a tarball containing the contents of the repository at the point of the tag's creation". Names and availability can change; the chapter numbers refer to where this book covers each one.

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
- GitHub statements in this book are checked against GitHub's own documentation and are labelled where they could not be.

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
| What GitHub offers, and the map of features | Checked against `github/docs` (commit `2eaab0b`); plan availability not checked | R224, R227 |
| Terms, ownership, removal of content | Quoted from `site-policy` (commit `b9578b5`); plans not checked | R225 |

## Where this leads

Chapter 37<!--ref:ghaccount--> covers accounts and profiles, Chapter 38<!--ref:ghauth--> covers signing in from Git, and Chapter 39<!--ref:ghrepo--> creates a first repository. Each will be verified against the official documentation before it is finished.
