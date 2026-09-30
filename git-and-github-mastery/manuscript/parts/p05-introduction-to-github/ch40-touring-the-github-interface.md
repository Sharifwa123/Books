---
key: ghtour
number: 40
tag: Core
first_read: full
status: draft
requires: [ghrepo]
ledger: [R241, R242, R243]
---
# Chapter 40 — Touring the GitHub Interface [Core]

**In this chapter**

- how to read a repository's page as a view of Git
- which part of the page shows which part of Git
- the tabs, and which of them belong to the platform and not to Git
- how to find your way when the interface changes

> **How to read this chapter.** A web interface changes often: names, positions and icons move between visits. The chapter was checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026), which describes each feature but not a fixed screen, and no live account was used; so the description of the interface **avoids exact button names and positions**. What is stable is the *idea* behind each part, which is a piece of Git that you already know. The Git equivalents below were run and recorded.

**Before you start.** Chapter 39<!--ref:ghrepo--> (a repository on a platform), Chapter 17<!--ref:history_view-->, Chapter 20<!--ref:branching-->, Chapter 29<!--ref:tags-->. The recordings ran in Bash and zsh on Git 2.43.0 and were re-run in CI on Git 2.55.0.

---

## 40.1 The main idea

A repository's page is a **window onto a Git repository**, with extra services beside it. Almost everything in the window can be reproduced with a command that you already know, and knowing the command tells you what the page is *really* showing.

> **Checked in part against GitHub's documentation (R241).** The documentation has a section for each feature in the table below: issues, pull requests, GitHub Actions, GitHub Discussions, projects, wikis, code security and repository settings. It also mentions, for example, the **Pulse** view under the **Insights** tab of a repository, and that the contents of the README are "automatically shown on the front page of your repository". The documentation does not fix the order or the labels of the page, so the table is a list of things to *look for*, not a description of exact wording.

---

## 40.2 Git on the page, and its command

| You see, on a repository's page | It is showing | The Git command that gives the same information |
|---|---|---|
| A list of **files and folders** with the latest commit message beside each | the tree of one commit (Chapter 30<!--ref:objects-->) | `git ls-tree HEAD` |
| A **branch selector** | the branches (Chapter 20<!--ref:branching-->) | `git branch --all` |
| A **tag** list, or a **release** list | tags (Chapter 29<!--ref:tags-->) | `git tag` |
| A count of **commits**, and a **history** of the repository or of one file | the log (Chapter 17<!--ref:history_view-->) | `git log`, `git log -- <file>` |
| A **comparison** of two branches or commits | a diff (Chapter 17<!--ref:history_view-->) | `git diff`, `git diff <a> <b>` |
| A view of a file with the **author of each line** | blame (Chapter 24<!--ref:stash-->) | `git blame` |
| A **download** of the code as an archive | a snapshot without history | `git archive` |
| A **clone** address | the remote address (Chapter 36<!--ref:whatgh-->) | `git clone <address>` |

Try some of these on the sample project. The history of one file, and who made the latest commit:

```text
$ cd bakery-menu
$ git log --oneline -- menu.md
81f772e (HEAD -> main) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
$ git log -1 --format='%an, %ad' --date=short
Ada Learner, 2026-01-05
```

*Recorded in Bash; `ch40-tour/expected-equivalents.bash.txt`.*

`git log -- menu.md` is the command behind a "history" view of a single file: only the commits that changed it. The comparison view corresponds to `git diff`. Comparing the current commit with two commits back, as a summary:

```text
$ git diff --stat HEAD~2 HEAD
 menu.md | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
```

*Recorded in Bash; `ch40-tour/expected-equivalents.bash.txt`.*

The list of branches, and a tag (a "release" on a platform is built on a tag, Chapter 29<!--ref:tags-->):

```text
$ git branch --all
* main
$ git tag -a v1.0 -m "First public menu"
$ git tag
v1.0
```

*Recorded in Bash; `ch40-tour/expected-equivalents.bash.txt`.*

And the "download the code" button gives you the files of one commit **without** the history. `git archive` does the same. The recording lists the archive's content, using `tar -t`:

```text
$ git archive --format=tar --prefix=bakery-menu-v1.0/ v1.0 | tar -t
bakery-menu-v1.0/
bakery-menu-v1.0/menu.md
```

*Recorded in Bash; `ch40-tour/expected-equivalents.bash.txt`.*

The archive holds the files under a folder name, and no `.git` folder: it is a **snapshot**, not a repository. If you download the archive, you cannot run `git log` in it. To get the history, clone (Chapter 39<!--ref:ghrepo-->).

---

## 40.3 What is not Git

Some tabs and sections belong to the **platform**. They are stored by the service, not in the repository (Chapter 36<!--ref:whatgh-->), and a `git clone` does not bring them:

| Typical section | Chapter |
|---|---|
| Issues | Chapter 44<!--ref:issues--> |
| Pull requests | Chapter 45<!--ref:pr--> |
| Actions | Chapter 54<!--ref:actions--> |
| Projects and Discussions | Chapter 47<!--ref:projects-->, Chapter 48<!--ref:discussions--> |
| Wiki | Chapter 43<!--ref:settings--> |
| Security | Chapter 62<!--ref:ghsec--> |
| Insights | Chapter 51<!--ref:insights--> |
| Settings | Chapter 43<!--ref:settings--> |

> **Checked in part against GitHub's documentation (R242).** That availability varies is confirmed for the parts the documentation covers: repository visibility (public, private, and internal for enterprise organizations), permissions, and the plan (for example, private repositories on the free plan have a limited feature set). Do not assume that a missing tab is a mistake.

---

## 40.4 Where things are, when the interface changes

- **Look for the idea, not the label.** If you need "history", look for a clock, a list of commits, or the word *commits*.
- **Use the search and the keyboard shortcuts** that the platform offers, and its help pages (Chapter 35<!--ref:readdocs-->).
- **Check the date** of any screenshot or tutorial (Chapter 35<!--ref:readdocs-->).
- **Prefer addresses to clicks.** A repository's pages have addresses that you can read and share; the parts of an address name the owner, the repository, and what you are viewing.
- **When in doubt, go back to Git.** A clone and the commands in Parts III and IV always work, whatever the web page looks like.

---

## 40.5 A tour to do yourself

With a repository of your own (Chapter 39<!--ref:ghrepo-->), or any **public** repository, visit and write one line about each:

1. The **file list**: which is the newest commit, and how do you know?
2. The **branch selector**: how many branches are there?
3. The **history**: who made the first commit?
4. The **history of one file**.
5. A **comparison** between two commits or branches.
6. The **tags or releases**, if any.
7. The **clone address**: can you find both the HTTPS and the SSH address (Chapter 38<!--ref:ghauth-->)?
8. **Which tabs** belong to the platform and not to Git?

For each, name the Git command that gives the same information. If you cannot, look at Chapter 17<!--ref:history_view--> again.

> **Note (R243).** These steps were not run on a live interface. If a step does not match what you see, use the "idea, not label" rule, and tell the author.

---

## Checkpoint

## What You Learned

- A repository's page is a view of a Git repository, plus platform services.
- Files, branches, tags, history, comparisons, blame and downloads each correspond to a Git command.
- `git archive` produces the files of one commit without history; a download from the page is such a snapshot.
- Issues, pull requests, actions, projects, wiki, security and settings belong to the platform and are not in a clone.
- When the interface changes, look for the idea, not the label, and fall back on Git.

## New Vocabulary

No new terms.

## Commands Learned

`git ls-tree HEAD`, `git log -- <file>`, `git branch --all`, `git archive --format=tar`.

## Common Mistakes

1. **Assuming that a downloaded archive contains the history.**
2. **Assuming that a missing tab means an error.**
3. **Following an old screenshot literally.**
4. **Expecting a clone to include issues and pull requests.**
5. **Not checking what is visible to strangers.**

## Practice

Do the exercises in [`exercises/ch40-exercises.md`](../../../exercises/ch40-exercises.md).

## Self-Test

1. Which Git command gives the same information as the file history on a repository page?
2. What does the "download the code" button give you that a clone does not, and the other way round?
3. Name three sections of a repository page that are not Git.
4. What should you do when a tutorial's screenshot does not match your screen?

## Before Moving On

You are ready for Chapter 41<!--ref:notify--> if you can:

- [ ] map each part of the page to the Git idea behind it
- [ ] separate Git parts from platform parts
- [ ] find your way when labels change

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Git equivalents: file history, latest commit, diff summary, branches, tag, archive | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R243 (Git side) |
| The layout and names of the repository page, and which sections exist | Feature sections checked against `github/docs`; exact layout **not** fixed by the documentation and not seen on a live account | R241, R242 |
| The tour steps | **Not run** on a live interface | R243 |

## Where this leads

Chapter 41<!--ref:notify--> covers how the platform tells you about activity. Chapter 42<!--ref:readme--> shows how to make a repository's front page useful, and Chapter 43<!--ref:settings--> covers the Settings, Security and Wiki sections.
