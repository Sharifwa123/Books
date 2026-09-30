---
key: pr
number: 45
tag: Core
first_read: full
status: draft
requires: [branching, merging, remotes, issues]
ledger: [R258, R259, R260, R261, R262]
---
# Chapter 45 — Pull Requests [Core]

**In this chapter**

- what a pull request is, and what it is not
- base and compare, and why a pull request shows a three-dot diff
- draft pull requests and the parts of a pull request page
- the three ways to merge one, shown as Git commands
- fetching a pull request to your computer
- keeping a pull request up to date, closing it, and reverting it

> **How to read this chapter.** The Git behind pull requests was run and recorded on local repositories that stand in for the platform. Statements about GitHub are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used, and labels can change. A pull request is a platform feature: **Git has no pull request**, only branches, commits and merges.

**Before you start.** Chapter 20<!--ref:branching-->, Chapter 21<!--ref:merging-->, Chapter 23<!--ref:remotes--> and Chapter 44<!--ref:issues-->. The recordings ran in Bash and zsh on Git 2.43.0 and were re-run in CI on newer Git versions.

---

## 45.1 What a pull request is

> **New term: pull request.** A proposal to merge the changes on one branch into another branch, with a place to discuss and review them first. The name comes from asking the owner of a repository to *pull* your changes.

GitHub's documentation puts it this way: "A pull request proposes merging code changes from one branch into another", and "pull requests turn a set of code changes into a conversation. Instead of merging work directly, you propose it so that collaborators can weigh in." It lists the benefits: catch bugs and problems early, discuss changes with feedback tied to specific lines, and keep a reviewable history of what changed and why.

The important sentence for a Git learner: a pull request is **not a Git object**. Your repository holds branches and commits. The platform holds the conversation, the reviews and the checks, and links them to two branches. Chapter 36<!--ref:whatgh--> said the same of issues.

The workflow you already know, from Chapter 23<!--ref:remotes--> and Chapter 34<!--ref:workflows-->, becomes:

1. create a branch and commit on it;
2. push the branch;
3. open a pull request from it into the branch you want to change (usually `main`);
4. discuss and revise: more commits on the same branch update the same pull request;
5. merge, and delete the branch.

> **Checked against GitHub's documentation (R258).** "Creating a pull request" says a pull request is opened by choosing a **base** branch, "the branch where you want to merge your changes", and a **compare** branch, "the topic branch where you made your changes", and that "pull requests can only be opened between two different branches". If you do not have write access, you fork the repository first. "About pull requests" lists what a pull request page gathers: **Conversation** (description, comments, reviews, timeline), **Commits**, **Checks** (results of automated tests and builds), **Files changed** (the diff reviewers comment on), and a **merge box** that "summarizes whether you can merge your changes or not". The reference page adds a **Findings** tab with automated code-review results.

---

## 45.2 Base, compare and the three-dot diff

The **base** is where the change is going; the **compare** (or *head*) branch is where it comes from. The page shows what the compare branch *adds* to the base. Git has two ways to compare branches, and they answer different questions. Take a repository in which `main` got a new commit after `add-tea` was branched off:

```text
$ cd bakery-menu
$ git log --oneline --graph --all
* cd79e50 (HEAD -> main) Raise the price of the white loaf
| * a13923d (add-tea) Add tea
|/
* 8a52ffe Add the menu
$ git diff --stat main...add-tea
 menu.md | 1 +
 1 file changed, 1 insertion(+)
$ git diff --stat main..add-tea
 menu.md | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
$ git merge-base main add-tea
8a52ffecdf9a4a5f307aa1d31e3429b29ad0d6f9
```

*Recorded in Bash; `ch45-pr/expected-compare.bash.txt`.*

`git diff main...add-tea` (three dots) compares the compare branch with the **merge base**, the common ancestor: it shows only the one line that the tea branch added. `git diff main..add-tea` (two dots) compares the two branch *tips* directly: it also shows the price change that `main` made and `add-tea` never saw, as if `add-tea` had undone it.

> **Checked against GitHub's documentation (R259).** "Pull requests on GitHub show a three-dot diff": `git diff A...B` compares "the most recent common commit of both branches (merge base) and the most recent version of the topic branch", while the two-dot `git diff A..B` compares "the most recent state of the base branch ... and the most recent version of the topic branch". The three-dot comparison "focuses on 'what a pull request introduces'" and "keeps showing the changes introduced by the topic branch since the branches diverged". The documentation also warns that "compare pages and pull request pages can calculate changed files from different merge bases", so the same two branches can sometimes show different diffs in the two places, and advises merging the base branch into the topic branch often and merging pull requests soon, so that they stay small.

---

## 45.3 Draft pull requests

A **draft** pull request says "not ready yet". GitHub's documentation: "Draft pull requests cannot be merged, and code owners are not automatically requested to review them. Drafts are useful when you want to share work-in-progress without formally requesting reviews." You can convert a pull request to a draft at any time, and mark it **Ready for review** from the merge box when it is ready.

> **Checked against GitHub's documentation (R260).** The quotations in this section are from the pull-request reference and "Changing the stage of a pull request". The names of the buttons are the documentation's and can change.

Use a draft when you want early feedback on a direction, or when checks are still failing and you do not want to ask anybody to review yet.

---

## 45.4 Three ways to merge

When a pull request is approved and its checks pass, the platform merges it. GitHub's documentation lists three strategies, and what each does to history:

| Strategy | The documentation's result | Git commands that do the same |
|---|---|---|
| **Merge commit** | "Preserves every commit from the pull request branch and adds an explicit merge point." | `git merge --no-ff topic` |
| **Squash and merge** | "Combines all commits in the pull request into a single commit on the base branch." | `git merge --squash topic`, then `git commit` |
| **Rebase and merge** | "Adds each commit onto the base branch without a merge commit, for a linear history." | `git rebase <base>` on the topic, then `git merge --ff-only topic` on the base |

The commands are the ones from Chapter 21<!--ref:merging--> and Chapter 27<!--ref:rebase-->. Starting from the same base, each strategy is applied to the same two-commit topic (tea, then coffee):

```text
$ cd bakery-menu
$ git switch -q strategy-merge
$ git merge --no-ff -m "Merge topic" topic
Merge made by the 'ort' strategy.
 menu.md | 2 ++
 1 file changed, 2 insertions(+)
$ git log --oneline --graph
*   66ffa82 (HEAD -> strategy-merge) Merge topic
|\
| * 85667ec (topic) Add coffee
| * d0ffe5a Add tea
|/
* 7877d40 (strategy-squash, main) Add the menu
$ git switch -q strategy-squash
$ git merge --squash topic
Updating 7877d40..85667ec
Fast-forward
Squash commit -- not updating HEAD
 menu.md | 2 ++
 1 file changed, 2 insertions(+)
$ git commit -q -m "Add tea and coffee"
$ git log --oneline --graph
* 9655a53 (HEAD -> strategy-squash) Add tea and coffee
* 7877d40 (main) Add the menu
$ git switch -q topic
$ git rebase strategy-rebase
Successfully rebased and updated refs/heads/topic.
$ git switch -q strategy-rebase
$ git merge --ff-only topic
Updating ed8302b..14100dc
Fast-forward
 menu.md | 2 ++
 1 file changed, 2 insertions(+)
$ git log --oneline --graph
* 14100dc (HEAD -> strategy-rebase, topic) Add coffee
* 1b66442 Add tea
* ed8302b Raise the price of the white loaf
* 7877d40 (main) Add the menu
```

*Recorded in Bash; `ch45-pr/expected-strategies.bash.txt`.*

Read the three graphs. The merge commit keeps both commits and adds a merge point where the two lines join. The squash leaves **one** new commit, `Add tea and coffee`, and the two original commits are not in that branch's history. The rebase puts the two commits, with **new hashes**, after the other change on the base, in a straight line (the hashes differ from before, as Chapter 27<!--ref:rebase--> explained).

> **Checked against GitHub's documentation (R261).** "Pull request merges" gives the table quoted above and says when to choose each: a merge commit "when your team values complete history or when the individual commits ... are meaningful on their own"; squash "when a pull request represents one logical change, especially if the branch includes many small fixup commits"; rebase "when your team wants a linear history and the pull request commits are already organized clearly". It warns that squash merging "works best for short-lived branches": if you keep working on the same head branch after a squash merge, "later pull requests can include commits that were already squashed into the base branch", which can make conflicts more likely. If the platform cannot safely rebase automatically, you can rebase locally, resolve conflicts and push. A pull request can also be marked merged indirectly, when its commits become reachable from the base by another route. What the platform runs internally is not shown: the table's commands reproduce the *results* described, not GitHub's implementation.

> **Which one?** There is no best strategy. Use the one your team has chosen; if you choose, prefer a merge commit when the individual commits matter, squash when the branch is one change with noisy commits, and rebase for a straight history. Repository administrators can restrict which strategies are allowed (Chapter 50<!--ref:protect-->).

---

## 45.5 Keeping it up to date, closing, reverting

- **In sync.** Before merging, update the pull request branch with changes from the base, to catch conflicts and failing tests early. The documentation says you can do it from the page "by merging the base branch into your head branch or by rebasing your changes onto the latest base branch", but only when there are no conflicts; with conflicts you resolve them yourself (Chapter 22<!--ref:conflicts-->).
- **Wrong base.** "If you opened a pull request with the wrong base branch, instead of closing it and opening a new one, you can change the base branch."
- **Closing.** A pull request can be closed without merging. Its branch and its conversation remain.
- **Reverting.** "Reverting a merged pull request creates a new pull request that reverts the original merge commit." If reverting causes conflicts, or the pull request was not merged on the platform, revert individual commits with `git revert` (Chapter 25<!--ref:undo-->); reverting a merge commit needs `-m` (Chapter 25<!--ref:undo--> section on reverting a merge).

> **Checked against GitHub's documentation (R262 part).** Quotations in this section are from "Keeping your pull request in sync with the base branch", "Changing the base branch of a pull request" and "Reverting a pull request".

---

## 45.6 A pull request on your computer

Reviewers often want to run the change. The platform keeps a reference for every pull request on its server, and GitHub's documentation shows how to fetch it: `git fetch origin pull/ID/head:BRANCH_NAME`, then switch to it. The `refs/pull/` namespace is **read-only**: pushing there produces `deny updating a hidden ref`.

The recording uses a local bare repository as the stand-in server. It has a branch `add-tea` and a reference `refs/pull/1/head` pointing at the same commit, and it is configured (with `receive.hideRefs`) to refuse pushes to `refs/pull`, as the documentation says the platform does:

```text
$ git clone -q hub.git reviewer
$ cd reviewer
$ git ls-remote origin
c4972f0d9a02edb567a40199915178833a1b91b9	HEAD
3b6b90d431743ed80865ba77ac3d3296eb498332	refs/heads/add-tea
c4972f0d9a02edb567a40199915178833a1b91b9	refs/heads/main
3b6b90d431743ed80865ba77ac3d3296eb498332	refs/pull/1/head
$ git fetch -q origin pull/1/head:pr-1
$ git switch -q pr-1
$ git log --oneline
3b6b90d (HEAD -> pr-1, origin/add-tea) Add tea
c4972f0 (origin/main, origin/HEAD, main) Add the menu
$ git push origin HEAD:refs/pull/1/head
To /home/learner/hub.git
 ! [remote rejected] HEAD -> refs/pull/1/head (deny updating a hidden ref)
error: failed to push some refs to '/home/learner/hub.git'
```

*Recorded in Bash; `ch45-pr/expected-pr-ref.bash.txt`.*

`git ls-remote` lists the extra reference. The fetch created a local branch `pr-1` with the pull request's commit, the log shows it, and the push to the hidden reference is refused with the message quoted in the documentation. This is only a **stand-in**: the real platform creates and updates `refs/pull/...` itself, and this book did not fetch from GitHub.

> **Checked against GitHub's documentation (R262).** "Checking out pull requests locally" gives the fetch command above, says the `refs/pull/` namespace is read-only and shows the rejection `! [remote rejected] HEAD -> refs/pull/1/head (deny updating a hidden ref)`. The reference page says that when you open a pull request GitHub "creates temporary Git references that point to the pull request's head branch and, when possible, to a simulated merge result".

---

## 45.7 A good pull request

1. **Small.** One change that a reviewer can understand in ten minutes.
2. **A title and description that explain why.** Link the issue with a closing keyword (Chapter 44<!--ref:issues-->).
3. **Passing checks** before you ask anyone (Chapter 54<!--ref:actions-->).
4. **Reviewed by someone else**, and merged by the author or the maintainer according to the team's rules (Chapter 46<!--ref:review-->).
5. **Branch deleted after merging**, so that old branches do not pile up.

---

## Checkpoint

## What You Learned

- A pull request proposes merging a compare branch into a base branch; it lives on the platform, not in Git.
- The page shows a three-dot diff: what the branch introduced since it diverged.
- A draft cannot be merged and does not request code owners.
- Merge commit, squash and rebase leave different histories: joined, one commit, or a straight line with new hashes.
- `git fetch origin pull/ID/head:NAME` brings a pull request to your computer; `refs/pull/` cannot be pushed to.

## New Vocabulary

**Pull request**, **base branch**, **compare branch** (introduced above).

## Commands Learned

`git diff A...B`, `git diff A..B`, `git merge-base`, `git merge --squash`, `git merge --ff-only`, `git ls-remote`, `git fetch origin pull/ID/head:NAME`.

## Common Mistakes

1. **Treating a pull request as part of the repository** and expecting a clone to have it.
2. **Very large pull requests** that nobody can review.
3. **Choosing squash for a long-running branch**, then meeting the same conflicts again.
4. **Reading a two-dot diff** as "what this branch changes".
5. **Trying to push to `refs/pull/...`**.

## Practice

Do the exercises in [`exercises/ch45-exercises.md`](../../../exercises/ch45-exercises.md).

## Self-Test

1. Is a pull request stored in your Git repository?
2. What does `git diff main...topic` show that `git diff main..topic` may not?
3. What can a draft pull request not do?
4. How many commits does a squash merge add to the base branch?
5. Which command brings pull request 7 to your computer?

## Before Moving On

You are ready for Chapter 46<!--ref:review--> if you can:

- [ ] open a pull request from a pushed branch (or explain each step)
- [ ] say what each merge strategy does to history
- [ ] explain what the three-dot diff shows

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Three-dot and two-dot diffs; merge base | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R259 (Git side) |
| Merge commit, squash and rebase leave the histories shown | Locally tested (same) with Git commands that reproduce the described results; not GitHub's implementation | R261 (Git side) |
| Fetching a pull request ref and the hidden-ref rejection | Locally tested against a **stand-in** bare repository; the platform itself was not contacted | R262 (Git side) |
| Pull request page, base/compare, drafts, merge strategies, sync, revert, `refs/pull` | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R258-R262 |

## Where this leads

Chapter 46<!--ref:review--> covers how changes are read and discussed. Chapter 49<!--ref:collab--> covers forks and access, and Chapter 50<!--ref:protect--> how a repository can require reviews and checks before a merge.
