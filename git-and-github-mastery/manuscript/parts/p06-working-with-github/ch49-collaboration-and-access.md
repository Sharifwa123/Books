---
key: collab
number: 49
tag: Core
first_read: part
status: draft
requires: [pr, review]
ledger: [R270, R271, R272, R273]
---
# Chapter 49 — Collaboration and Access [Core]

**In this chapter**

- who can do what in a repository: roles and permissions
- forks and clones: what each is, and how a fork stays in step with its upstream
- code owners (`CODEOWNERS`)
- community health files that a whole account can share

> **How to read this chapter.** The fork workflow was run and recorded with local bare repositories that stand in for the platform. Statements about GitHub are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used. Access control is a platform feature: **Git itself has no users, roles or permissions**, only whoever can reach a repository's address.

**Before you start.** Chapter 45<!--ref:pr--> and Chapter 46<!--ref:review-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on newer Git versions.

---

## 49.1 Roles

Two questions from Chapter 38<!--ref:ghauth--> come back: *who are you?* was authentication; *what may you do?* is **authorisation**, decided by **permissions**, and a **role** is a set of permissions given to a person or team.

For a repository owned by an **organization**, GitHub's documentation lists five roles, "from least access to most access":

| Role | The documentation recommends it for |
|---|---|
| **Read** | non-code contributors who want to view or discuss the project |
| **Triage** | contributors who need to manage issues and pull requests without write access |
| **Write** | contributors who actively push to the project |
| **Maintain** | project managers who need to manage the repository without access to sensitive or destructive actions |
| **Admin** | people who need full access, including sensitive and destructive actions like managing security or deleting a repository |

Organization owners have admin access to every repository of the organization. Enterprise plans can define **custom repository roles** (up to 20 in the documentation for the current version). The documentation's principle: "Choose the role that best fits each person or team's function in your project without giving people more access to the project than they need."

A repository owned by a **personal account** is simpler: it has "a single owner who has full control", and the owner can invite **collaborators**. For finer control the documentation suggests transferring the repository to an organization.

> **Checked against GitHub's documentation (R270).** "Repository roles for an organization" gives the five roles and the quoted principle; "About custom repository roles" says custom roles are limited (up to 20 in the current version); "Permission levels for a personal account repository" describes the single owner and the suggestion to move to an organization. Which exact actions each role may take is a long table in the documentation and is not reproduced here.

**Least privilege** (Chapter 33<!--ref:gitsec-->) applies: start with the smallest role that lets someone do their job, and remove access when they leave.

---

## 49.2 Fork, clone and branch

Three words that beginners mix up:

| | What it is | Where it lives |
|---|---|---|
| **Clone** | A copy of a repository on **your computer** | Your disk |
| **Branch** | A line of work **inside one** repository | The same repository |
| **Fork** | A copy of a repository **on the platform**, owned by you | A second hosted repository |

GitHub's documentation: "A fork is a copy of a repository that you own, connected to the original repository, called the upstream repository." A fork lets you "make changes in your own space without affecting the upstream project, and propose those changes back with a pull request". Use a **branch** "when you have write access and collaborate in a shared repository", and a **fork** "when you need independence from the upstream repository, or when you don't have write access".

> **New term: fork.** A copy of a hosted repository that you own, connected to the original (the *upstream*), so that you can work without write access to the original and propose your changes back with a pull request.

Two collaboration models follow: in the **shared repository model**, collaborators have push access to one repository and use topic branches (common in teams); in the **fork and pull model**, "anyone can fork" a repository they can read (if the owner allows it) and you "do not need permission from the upstream repository to push to a fork you created" (common in open source).

> **Checked against GitHub's documentation (R271).** "About forks" and the pull-request reference. The reference page adds that a fork and its upstream "share the same Git data": "all content uploaded to a fork is accessible from the upstream and all other forks of that upstream". Do not push anything to a fork that you would not publish to the upstream.

---

## 49.3 Keeping a fork in step

A fork is a snapshot from the moment you made it. The upstream keeps moving. To catch up on your computer, you add the upstream repository as a second **remote**, conventionally named `upstream`, then fetch it and merge. The steps below are GitHub's documented commands. The recording uses local bare repositories instead of GitHub: `upstream.git` is the original, `fork.git` is your fork, and `my-clone` is your clone of the fork.

```text
$ git clone -q fork.git my-clone
$ cd my-clone
$ git remote -v
origin	/home/learner/fork.git (fetch)
origin	/home/learner/fork.git (push)
$ git remote add upstream ../upstream.git
$ git remote -v
origin	/home/learner/fork.git (fetch)
origin	/home/learner/fork.git (push)
upstream	../upstream.git (fetch)
upstream	../upstream.git (push)
$ git switch -q -c add-tea
$ printf -- "- Tea: 1.50\n" >> menu.md
$ git commit -q -am "Add tea"
$ git push -q -u origin add-tea
$ git -C ../upstream.git branch
* main
$ git clone -q ../upstream.git ../maintainer
$ git -C ../maintainer -c user.name=Maintainer -c user.email=maintainer@example.org commit -q --allow-empty -m "Update the contributing guide"
$ git -C ../maintainer push -q origin main
$ git switch -q main
$ git fetch -q upstream
$ git log --oneline --all --graph
* ce2b049 (upstream/main) Update the contributing guide
| * 9c3dcee (origin/add-tea, add-tea) Add tea
|/
* c4972f0 (HEAD -> main, origin/main, origin/HEAD) Add the menu
$ git merge --ff-only upstream/main
Updating c4972f0..ce2b049
Fast-forward
$ git push -q origin main
$ git log --oneline --graph --all
* ce2b049 (HEAD -> main, upstream/main, origin/main, origin/HEAD) Update the contributing guide
| * 9c3dcee (origin/add-tea, add-tea) Add tea
|/
* c4972f0 Add the menu
```

*Recorded in Bash; `ch49-collab/expected-fork.bash.txt`.*

> **Your Git may show one more label.** Git 2.55.0 (re-run in CI) also lists `upstream/HEAD` beside `upstream/main` in the graph, because it records which branch is the upstream's default. The commits are the same.

Follow the story. `git remote -v` first shows only `origin`, your fork. `git remote add upstream` adds the original. A pushed branch `add-tea` shows in the fork. A maintainer then adds a commit to the upstream. In your clone, `git fetch upstream` brings it as `upstream/main`, and the graph shows the two lines: your `add-tea` branch, and the upstream change. `git merge --ff-only upstream/main` moves your `main` forward, and `git push origin main` updates your fork. Afterwards `main` and `upstream/main` are the same commit.

`--ff-only` is a safety choice: it refuses to create a merge commit, so if your `main` had drifted from the upstream you would notice at once (Chapter 21<!--ref:merging-->).

> **Checked against GitHub's documentation (R272).** "Configuring a remote repository for a fork" gives `git remote add upstream <URL>`; "Syncing a fork" gives `git fetch upstream`, switching to your local default branch, and `git merge upstream/main`, and also describes an **Update branch** button on the platform (with conflicts, the platform prompts you to create a pull request to resolve them) and a command of the GitHub CLI. The recorded commands show the Git side, with local stand-ins for the platform.

**Rule of thumb.** Never do your work on the fork's `main`. Keep `main` as a mirror of the upstream, and do each change on its own branch (Chapter 20<!--ref:branching-->), so that syncing is always a clean fast-forward.

---

## 49.4 Code owners

A repository can say *who should review which files*, in a file named `CODEOWNERS`. Each line is a pattern followed by owners (`@username` or `@organization/team`). It is a plain file, committed like any other, so it is versioned and reviewed like code.

> **New term: code owner.** A person or team named in a `CODEOWNERS` file as responsible for certain files, who is automatically requested to review pull requests that change them.

> **Checked against GitHub's documentation (R273).** "About code owners": code owners "are automatically requested for review when someone opens a pull request that modifies code that they own", but "are not automatically requested to review draft pull requests"; they are notified when a draft is marked ready. The file is called `CODEOWNERS` and lives in `.github/`, the root or `docs/`; if several exist, GitHub uses the first found in that order. Each file applies to **one branch**, and "to trigger review requests, pull requests use the version of `CODEOWNERS` from the base branch". Owners "must have write permissions for the repository", and a team must be visible and have write permission. The pattern follows most `gitignore` rules, but three do **not** work: escaping a leading `#`, negating with `!`, and character ranges with `[ ]`. Files must be under 3 MB. Administrators can also require approval from a code owner before merging (Chapter 50<!--ref:protect-->).

An example, as text (the syntax is the documentation's):

```text
# Everything in the repository is reviewed by the maintainers
*            @example-owner

# The menu file is reviewed by the person who knows the prices
menu.md      @ada
```

---

## 49.5 Files that a whole account can share

Files such as `CONTRIBUTING.md`, a code of conduct or issue templates can be shared by all of an account's repositories.

> **Checked against GitHub's documentation (R273).** "Creating a default community health file": put them in a repository named `.github` (it "must be public"), and GitHub will use them for any repository of the account that does not have its own file of that type. For files that can live in several places the order is the `.github` folder, the root, then `docs`. If a repository has its own valid issue templates, none of the default `.github/ISSUE_TEMPLATE` contents are used. Such files "won't appear in the file browser or Git history of the individual repositories, and are not included in their clones, packages, or downloads".

That last sentence has a consequence for a Git user: the shared defaults are **not in your clone**. Someone reading your clone offline does not see them.

---

## Checkpoint

## What You Learned

- Organization repositories use five roles: Read, Triage, Write, Maintain, Admin; give the least that works.
- A clone is on your computer, a branch is inside a repository, a fork is a hosted copy you own.
- A fork stays in step through a second remote, `upstream`: fetch it and fast-forward your `main`.
- `CODEOWNERS` requests reviews automatically, from the base branch's copy of the file.
- A `.github` repository can hold defaults for a whole account; they are not in clones.

## New Vocabulary

**Fork**, **code owner** (introduced above).

## Commands Learned

`git remote add upstream <address>`, `git fetch upstream`, `git merge --ff-only upstream/main`.

## Common Mistakes

1. **Working on the fork's `main`**, so it can no longer be fast-forwarded.
2. **Giving admin to everyone** for convenience.
3. **Believing that what you push to a fork is separate from the upstream**: the documentation says a fork and its upstream share Git data.
4. **A `CODEOWNERS` file on the wrong branch**, so nobody is requested.
5. **Expecting shared default files to appear in a clone.**

## Practice

Do the exercises in [`exercises/ch49-exercises.md`](../../../exercises/ch49-exercises.md).

## Self-Test

1. Which role fits a contributor who manages issues but must not push code?
2. What is the difference between a clone and a fork?
3. Which commands add the upstream and bring in its changes?
4. Which copy of `CODEOWNERS` does a pull request use?
5. Where do shared community health files live?

## Before Moving On

You are ready for Chapter 50<!--ref:protect--> if you can:

- [ ] choose a role for a person by function
- [ ] set up and use an `upstream` remote
- [ ] write a `CODEOWNERS` line

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Adding `upstream`, fetching it, fast-forwarding `main`, pushing to the fork | Locally tested with local bare repositories as stand-ins: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R272 (Git side) |
| Roles, custom roles, personal-account ownership | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R270 |
| Forks, shared data, collaboration models | Checked against `github/docs` | R271 |
| Sync commands and the platform's update button | Checked against `github/docs` | R272 |
| `CODEOWNERS` rules and default community health files | Checked against `github/docs` | R273 |

## Where this leads

Chapter 50<!--ref:protect--> covers rules that make reviews and checks mandatory. Chapter 64<!--ref:oss--> shows how open-source projects use forks, and Chapter 68<!--ref:orgs--> covers organizations in depth.
