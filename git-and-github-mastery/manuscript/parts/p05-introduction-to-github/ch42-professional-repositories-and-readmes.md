---
key: readme
number: 42
tag: Core
first_read: full
status: draft
requires: [ghrepo, markdown]
ledger: [R247, R248, R249]
---
# Chapter 42 — Professional Repositories and READMEs [Core]

**In this chapter**

- what a README is for, and where GitHub looks for it
- a README skeleton for each common kind of project
- links inside a repository that keep working in a clone
- the description, website and topics that sit beside a README
- a checklist for a repository that a stranger can understand

> **How to read this chapter.** The Git and file parts were run and recorded. The statements about GitHub are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used. The README skeletons are **this book's suggestions**, not GitHub rules, and each says so.

**Before you start.** Chapter 39<!--ref:ghrepo--> (a repository on the platform) and Chapter 8<!--ref:markdown--> (the writing format). The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on newer Git versions.

---

## 42.1 What a README is for

> **New term: README.** A file in a repository, usually named `README.md`, that introduces the project to the people who arrive: what it is, why it is useful, how to start, where to get help and who looks after it.

A stranger decides in seconds whether a project is worth their time, and the README is the first thing they read. GitHub's documentation lists what READMEs typically contain:

- what the project does
- why the project is useful
- how users can get started
- where users can get help
- who maintains and contributes to the project

> **Checked against GitHub's documentation (R247).** "About READMEs" says a README "is often the first item a visitor will see". If you put it in the hidden `.github` folder, the root, or a `docs` folder, GitHub "will recognize and automatically surface" it; when there is more than one, the one shown is chosen from `.github`, then the root, then `docs`. In the rendered view "any content beyond 500 KiB will be truncated". GitHub also builds a table of contents from the headings of any rendered Markdown file, and offers links to headings. The same page says a README "should only contain information necessary for developers to get started using and contributing to your project" and that longer documentation is "best suited for wikis".

**Keep it short at the top.** The first screen should answer *what is this?* in two sentences, and *how do I try it?* in a few lines. Details go lower, or in other files.

---

## 42.2 A first README

The smallest useful README for the Sunrise Bakery project:

````markdown
# Sunrise Bakery menu

The weekly menu of Sunrise Bakery, kept as a plain Markdown file so that
anyone on the team can update it.

## Use it

Open `menu.md`. Prices are in the local currency.

## Change it

Edit `menu.md`, describe the change in one line, and open a pull request.

## Who looks after it

Ada Learner (`@example-owner`).
````

Nothing here needs a tool: it is Markdown (Chapter 8<!--ref:markdown-->). What makes it *good* is that each heading answers one of the questions above.

---

## 42.3 Skeletons for different kinds of project

These are **suggestions from this book**, not rules of the platform. Take the headings that fit, and delete the rest. The bracketed words are placeholders you replace.

| Kind of project | Headings that usually help |
|---|---|
| **Beginner / learning project** | What I built · What I learned · How to run it · What I want to improve |
| **Web application** | What it does · Screenshot · Run it locally · Configuration (never real secrets) · Tests · Deploy · Licence |
| **Mobile application** | What it does · Screenshots · Supported systems · Build and run · Permissions it asks for · Privacy · Licence |
| **Open-source project** | What it is · Install · Quick example · Documentation · Contributing (link to `CONTRIBUTING`) · Code of conduct · Security reports · Licence |
| **Library** | What it does · Install · Minimal example · Supported versions · API reference link · Changelog · Licence |
| **API service** | What it does · Base address · Authentication (how to get access, no keys in the file) · Example request and response · Errors · Rate limits · Support |
| **Command-line tool** | What it does · Install · Usage with two or three examples · Options · Exit codes · Licence |
| **Business or internal project** | Purpose · Owner and team · How to get access · How to run and deploy · Who to ask · Links to runbooks |

A README for a **library** shows the *smallest working example* near the top, because a reader wants proof that it does what they need:

````markdown
# menu-tools

Small functions for reading a bakery menu file.

## Install

Copy `menu_tools.py` into your project.

## Example

```python
from menu_tools import read_menu

menu = read_menu("menu.md")
print(menu["White loaf"])
```

## Licence

See `LICENSE`.
````

> **⚠️ CAUTION.** Never put a real password, key or token in a README, even as an "example". Use a clearly fake value, and say so (Chapter 33<!--ref:gitsec-->).

---

## 42.4 Links that keep working

A README often points to other files in the repository. GitHub's documentation recommends **relative links**: a link to a file *relative to the current file*. GitHub "will automatically transform your relative link or image path based on whatever branch you're currently on, so that the link or path always works", links starting with `/` are relative to the repository root, and `./` and `../` work. The link text "should be on a single line". The documentation adds: "Relative links are easier for users who clone your repository. Absolute links may not work in clones of your repository."

The link is only text. Git does not know it is a link, so **renaming the file breaks it silently**. Here is the whole cycle:

```text
$ cd bakery-menu
$ mkdir docs
$ printf '# Sunrise Bakery menu\n\nSee [how to help](docs/CONTRIBUTING.md).\n' > README.md
$ printf 'Be kind.\n' > docs/CONTRIBUTING.md
$ grep -o '](.*)' README.md
](docs/CONTRIBUTING.md)
$ test -f docs/CONTRIBUTING.md && echo "target found"
target found
$ git add README.md docs
$ git commit -q -m "Add a README and a contributing guide"
$ git mv docs/CONTRIBUTING.md docs/HELP.md
$ test -f docs/CONTRIBUTING.md || echo "target missing: the link is now broken"
target missing: the link is now broken
$ git status --short
R  docs/CONTRIBUTING.md -> docs/HELP.md
```

*Recorded in Bash; `ch42-readme/expected-relative-links.bash.txt`.*

The link `docs/CONTRIBUTING.md` was found while the file existed. After `git mv` renamed it to `HELP.md`, the same test reports the target missing, and `git status` shows only a rename: nothing warned that the README now points nowhere. That is why a repository worth its name is checked for broken links before a release (the same idea as this book's own link check).

> **Checked against GitHub's documentation (R248).** The relative-link behaviour above is quoted from "About READMEs" and the shared text it includes. The recorded commands show only the Git side: a link is plain text and a rename does not update it.

---

## 42.5 The description, website and topics

Beside the README, the repository page has a short **About** area with a description, an optional website address and **topics**.

> **New term: topic.** A short label that classifies a repository by purpose, subject area, community or language, so that people can find related projects.

> **Checked against GitHub's documentation (R249).** "Classifying your repository with topics" says topics "appear on the main page of a repository", that clicking a topic shows other repositories with it, and that repository admins can add any topics they like. When creating a topic: "use lowercase letters, numbers, and hyphens", "use 50 characters or less", and "add no more than 20 topics". Topic names "are always public, even if you create the topic from within a private repository". On the public site GitHub may suggest topics for public repositories, which admins can accept or reject; private repositories get no suggestions. You edit them from the gear icon beside "About".

**Practical advice.**

- Write the description as one plain sentence: what it is and who it is for.
- Add three to six topics that a stranger would search for.
- Do not put anything private in a topic or description: both are public for a public repository.

---

## 42.6 Files that sit beside a README

A README is one of several files that communicate expectations. GitHub's documentation groups them: "A README, along with a repository license, citation file, contribution guidelines, and a code of conduct, communicates expectations for your project and helps you manage contributions." Later chapters cover each: the licence (Chapter 65<!--ref:licences-->), contribution guidelines and code of conduct (Chapter 64<!--ref:oss-->) and the security policy (Chapter 62<!--ref:ghsec-->).

---

## 42.7 A checklist

1. The first two sentences say what the project is.
2. A reader can run or use it in five minutes by following the README.
3. Every link works, and links to files in the repository are relative.
4. No secret appears anywhere, including the history (Chapter 33<!--ref:gitsec-->).
5. The About description and topics are filled in and contain nothing private.
6. It says who looks after it and where to ask.
7. It names the licence, or says plainly that none has been chosen (Chapter 65<!--ref:licences-->).

---

## Checkpoint

## What You Learned

- A README introduces a project: what it is, why it helps, how to start, where to get help, who maintains it.
- GitHub shows a README from `.github`, the root or `docs` (in that order of preference) and truncates beyond 500 KiB.
- Different kinds of project need different headings; the skeletons are suggestions.
- Relative links keep working in clones; a rename silently breaks them, and Git does not warn you.
- Topics are lowercase, at most 50 characters, at most 20 per repository, and always public.

## New Vocabulary

**README**, **topic** (introduced above).

## Commands Learned

`grep -o`, `test -f`, `git mv` (used for the link demonstration).

## Common Mistakes

1. **A README that only says the project name.**
2. **Absolute links to files in the same repository.**
3. **Renaming a file without fixing the links that point to it.**
4. **Real secrets in "example" configuration.**
5. **Topics or descriptions that reveal something private.**

## Practice

Do the exercises in [`exercises/ch42-exercises.md`](../../../exercises/ch42-exercises.md).

## Self-Test

1. Which folders does GitHub search for a README, and which wins?
2. Why is a relative link better than an absolute one for files in the same repository?
3. What happens to a link when its target file is renamed?
4. Give the limits for topics.
5. Which two sentences should open every README?

## Before Moving On

You are ready for Chapter 43<!--ref:settings--> if you can:

- [ ] write a README that answers the five questions
- [ ] choose the right skeleton for a kind of project
- [ ] find a broken relative link

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| A link is plain text; a rename leaves it broken; `git mv` shows as a rename | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R248 (Git side) |
| README location, order, size limit, contents, relative links | Checked against `github/docs` (commit `2eaab0b`) | R247, R248 |
| Topic rules, About area | Checked against `github/docs` | R249 |
| README skeletons per kind of project | **Book's own suggestions**, not sourced rules | R247 |

## Where this leads

Chapter 43<!--ref:settings--> tours the Settings, Security and Wiki sections. Chapter 44<!--ref:issues--> and Chapter 45<!--ref:pr--> cover how people contribute once they have read the README.
