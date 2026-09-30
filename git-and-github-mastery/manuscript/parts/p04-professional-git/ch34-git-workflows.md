---
key: workflows
number: 34
tag: Core
first_read: part
status: draft
requires: [branching, merging, remotes, tags]
ledger: [R218, R219, R220]
---
# Chapter 34 — Git Workflows [Core]

**In this chapter**

- what a workflow is, and why teams need one
- working alone
- the **feature-branch workflow**, run end to end with two "people" on one computer
- the common named models, in general terms
- how to choose

**Before you start.** Chapter 20<!--ref:branching-->, Chapter 21<!--ref:merging-->, Chapter 23<!--ref:remotes--> and Chapter 29<!--ref:tags-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on Git 2.55.0.

Git does not tell you *how* to use branches. Two teams with the same Git commands can work in very different ways. This chapter is about the agreements that make a team's use of Git predictable.

---

## 34.1 A workflow is an agreement

> **New term: workflow.** The agreed way in which a person or a team uses branches, commits, merges and releases to get changes into a project.

A workflow answers questions such as:

- Where does new work start, and where does it end up?
- Who may change the main branch, and how?
- How does a change get reviewed?
- How are releases marked and fixed?

The commands are the same in every workflow (Chapters 20<!--ref:branching--> to 29<!--ref:tags-->). What differs is the **rules**: a shared understanding that everyone can state in one minute. A workflow that nobody can state is not a workflow; it is a habit.

---

## 34.2 Working alone

When you are the only person, the simplest workflow is fine:

- Commit on `main` in small steps (Chapter 19<!--ref:commits-->).
- Use a branch for anything risky or unfinished (Chapter 20<!--ref:branching-->).
- Tag the versions that matter (Chapter 29<!--ref:tags-->).
- Push to a remote as a backup (Chapter 23<!--ref:remotes-->).

Even alone, branches make experiments safe, and small commits make mistakes easy to undo (Chapter 25<!--ref:undo-->).

---

## 34.3 The feature-branch workflow, step by step

The most common team pattern is: **every change is made on its own short-lived branch, reviewed, and then merged into `main`**. `main` always holds work that has been accepted.

Here is the whole cycle, with two people on one computer. A shared bare repository, `hub.git`, plays the remote, and Alice and Bob each have a clone (Chapter 23<!--ref:remotes-->). Alice starts a branch and publishes it:

```text
$ cd alice
$ git switch -c add-tea
Switched to a new branch 'add-tea'
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[add-tea cece341] Add tea
 1 file changed, 1 insertion(+)
$ git push -u origin add-tea
To /home/learner/hub.git
 * [new branch]      add-tea -> add-tea
branch 'add-tea' set up to track 'origin/add-tea'.
```

*Recorded in Bash; `ch34-workflows/expected-feature-branch.bash.txt`.*

She pushes the branch to the shared place so that others can see it. (On a hosting platform, this is the point at which she would open a *pull request*: Chapter 45<!--ref:pr-->.) Bob looks at her work. First he fetches, which changes nothing of his own (Chapter 23<!--ref:remotes-->):

```text
$ cd ../bob
$ git fetch
From /home/learner/hub
 * [new branch]      add-tea    -> origin/add-tea
$ git branch -r
  origin/HEAD -> origin/main
  origin/add-tea
  origin/main
```

*Recorded in Bash; `ch34-workflows/expected-feature-branch.bash.txt`.*

Then he **reviews** the change by reading the difference between `main` and her branch:

```text
$ git diff main origin/add-tea
diff --git a/menu.md b/menu.md
index 97e3bea..ae8d71a 100644
--- a/menu.md
+++ b/menu.md
@@ -3,3 +3,4 @@
 - White loaf: 2.80
 - Rolls (six): 3.00
 - Coconut cake (slice): 4.00
+- Tea: 1.50
```

*Recorded in Bash; `ch34-workflows/expected-feature-branch.bash.txt`.*

Satisfied, Bob merges the branch. He uses `--no-ff` (Chapter 21<!--ref:merging-->) so that the history records that a branch existed, and publishes the result:

```text
$ git merge --no-ff origin/add-tea -m "Merge add-tea"
Merge made by the 'ort' strategy.
 menu.md | 1 +
 1 file changed, 1 insertion(+)
$ git push origin main
To /home/learner/hub.git
   81f772e..9fff21e  main -> main
```

*Recorded in Bash; `ch34-workflows/expected-feature-branch.bash.txt`.*

Now the branch has done its job, so Bob deletes it on the remote:

```text
$ git push origin --delete add-tea
To /home/learner/hub.git
 - [deleted]         add-tea
$ git branch -r
  origin/HEAD -> origin/main
  origin/main
```

*Recorded in Bash; `ch34-workflows/expected-feature-branch.bash.txt`.*

Alice cleans up on her side. `git fetch --prune` updates her view of the remote, and *removes* her notes about branches that no longer exist there:

```text
$ cd ../alice
$ git fetch --prune
From /home/learner/hub
 - [deleted]         (none)     -> origin/add-tea
   81f772e..9fff21e  main       -> origin/main
$ git branch -vv
* add-tea cece341 [origin/add-tea: gone] Add tea
  main    81f772e [origin/main: behind 2] Add coconut cake
```

*Recorded in Bash; `ch34-workflows/expected-feature-branch.bash.txt`.*

Her own `add-tea` branch shows `[origin/add-tea: gone]`: the remote branch is gone. She returns to `main`, brings it up to date, and deletes her local branch (which Git allows now, because it is merged):

```text
$ git switch main
Switched to branch 'main'
Your branch is behind 'origin/main' by 2 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)
$ git pull
Updating 81f772e..9fff21e
Fast-forward
 menu.md | 1 +
 1 file changed, 1 insertion(+)
$ git branch -d add-tea
Deleted branch add-tea (was cece341).
```

*Recorded in Bash; `ch34-workflows/expected-feature-branch.bash.txt`.*

The history shows the shape of the workflow:

```text
$ git log --oneline --graph
*   9fff21e (HEAD -> main, origin/main, origin/HEAD) Merge add-tea
|\
| * cece341 Add tea
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch34-workflows/expected-feature-branch.bash.txt`.*

The cycle is: **branch, commit, push, review, merge, delete.** Everything else in this chapter is a variation on it.

**What made it work:**

- The branch was **short-lived** and about **one thing**.
- Somebody other than the author looked at it before it reached `main`.
- `main` only received changes through a merge.
- Nobody rewrote shared history.

**What a platform adds.** Hosting platforms wrap this cycle in a web page (a pull request), with comments, approvals and automatic checks (Chapter 45<!--ref:pr-->, Chapter 54<!--ref:actions-->). The Git commands underneath are the ones you just saw.

---

## 34.4 Named models

Teams have described their workflows with names. The descriptions below are **general**, and are not statements about any organisation's official practice.

| Model | Shape in one line |
|---|---|
| **Trunk-based** | Everyone commits to `main` (the "trunk") in very small steps, or on branches that last hours, and merges often. |
| **Feature branch** | As in section 34.3: one short branch per change, reviewed, merged to `main`. |
| **Release branch** | A branch is cut from `main` for a version being prepared, so that fixes go there while `main` moves on; fixes are then merged or copied back (Chapter 28<!--ref:tools--> introduced cherry-pick). |
| **A model with long-lived `develop` and release branches** | Work is collected on a `develop` branch; `main` holds only released versions; more branch types exist for releases and urgent fixes. It has many rules and suits projects with formal release cycles. |
| **Forking** | People without direct write access copy ("fork") the project, work in their copy, and propose changes back (Chapter 49<!--ref:collab-->). Common in open source. |

> **Verification pending [R219].** These descriptions come from general knowledge. The official descriptions of the models that carry names (in particular the ones hosting platforms publish), and who first proposed them, were not consulted; the official hosts could not be reached. This chapter does not attribute any model to any person or company.

**Comparing them.**

| | Change size | Branch lifetime | Review | Release handling | Suits |
|---|---|---|---|---|---|
| Trunk-based | very small | hours | often after the fact, or pairing | tags on `main` | small teams; strong automated tests |
| Feature branch | small | days | before merge | tags on `main` | most teams |
| Release branch | any | weeks (release branch) | before merge | one branch per version | products with several supported versions |
| `develop` and release branches | any | long | before merge | dedicated branches | formal, scheduled releases |
| Forking | any | varies | maintainers review | maintainers | open source; outside contributors |

---

## 34.5 Choosing

There is no best workflow. Ask four questions:

1. **How many people** change the code at once? (More people, more need for rules.)
2. **How much do you trust your automated tests?** (Good tests allow smaller, faster merges.)
3. **How many versions do you support at once?** (Several supported versions need release branches.)
4. **Who may write to the repository?** (Outsiders need forks.)

Then apply the smallest workflow that answers them, write it down in a short file in the repository (for example `CONTRIBUTING.md`, Chapter 64<!--ref:oss-->), and change it when it stops fitting.

> **⚠️ CAUTION.** The most damaging habits are the same in every workflow: long-lived branches that drift away from `main` and then produce enormous conflicts (Chapter 22<!--ref:conflicts-->); rewriting shared history (Chapter 27<!--ref:rebase-->, Chapter 33<!--ref:gitsec-->); and committing directly to a branch that everyone depends on without anyone looking.

> **Verification pending [R220].** The advice in this section, and the size of the teams for which each model suits, is general experience and not a tested or cited fact.

---

## Checkpoint

## What You Learned

- A workflow is an agreement about how a team uses branches, reviews and merges; it is not a Git feature.
- The feature-branch cycle: branch, commit, push, review, merge, delete.
- `git fetch --prune` removes remote-tracking branches whose remote branch was deleted.
- Common models: trunk-based, feature branch, release branches, a model with a `develop` branch, and forking.
- Choose the smallest workflow that fits the team, and write it down.

## New Vocabulary

- **Workflow**: the agreed way a team uses branches, reviews, merges and releases.

## Commands Learned

`git push -u origin <branch>`, `git diff main origin/<branch>`, `git merge --no-ff`, `git push origin --delete <branch>`, `git fetch --prune`, `git branch -vv`.

## Common Mistakes

1. **Long-lived branches that drift from `main`.**
2. **Merging without anyone else looking.**
3. **Leaving merged branches lying around.**
4. **Adopting a complicated model for a small team.**
5. **Not writing the workflow down.**

## Practice

Do the exercises in [`exercises/ch34-exercises.md`](../../../exercises/ch34-exercises.md).

## Self-Test

1. What do all workflows share, and what differs between them?
2. Name the six steps of the feature-branch cycle.
3. What does `git fetch --prune` remove?
4. Why did Bob merge with `--no-ff`?
5. Which questions help you choose a workflow?

## Before Moving On

You are ready for Chapter 35<!--ref:readdocs--> if you can:

- [ ] run the feature-branch cycle with a shared bare repository
- [ ] explain fetch, diff and merge as a review step
- [ ] describe at least three named models in one sentence each
- [ ] say what you would choose for a small team, and why

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Feature-branch cycle with a shared bare repository (push, fetch, diff, `--no-ff` merge, remote branch deletion, `fetch --prune`, `branch -d`) | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R218 |
| Descriptions of named models | **Not verified** (general knowledge; no attribution) | R219 |
| Advice on choosing | General experience, **not tested** | R220 |

## Where this leads

Chapter 35<!--ref:readdocs--> teaches how to read the official documentation for everything in Part IV. Chapter 45<!--ref:pr--> turns the review step into a pull request on a hosting platform, and Chapter 49<!--ref:collab--> covers the forking model.
