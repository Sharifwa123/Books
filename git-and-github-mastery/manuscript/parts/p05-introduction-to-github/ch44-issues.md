---
key: issues
number: 44
tag: Core
first_read: full
status: draft
requires: [ghrepo, markdown]
ledger: [R254, R255, R256, R257]
---
# Chapter 44 — Issues [Core]

**In this chapter**

- what an issue is, and what belongs in one
- labels, assignees and milestones
- how to reference issues, and how a pull request closes one
- issue templates and issue forms
- how Git commit messages and issues meet

> **How to read this chapter.** The Git and file parts (an issue form file, a closing keyword in a commit message) were run and recorded. Statements about GitHub are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used, and labels can change.

**Before you start.** Chapter 39<!--ref:ghrepo--> and Chapter 8<!--ref:markdown-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on newer Git versions.

---

## 44.1 What an issue is

> **New term: issue.** A numbered item in a repository's tracker: a bug report, a feature idea, a question, or any task that someone wants to write down and discuss. It has a title, a description, a conversation, and a state (open or closed).

GitHub's documentation says issues are for "plan, discuss, and track work", and that they "can track bug reports, new features and ideas, and anything else you need to write down or discuss with your team". An issue lives on the platform: it is **not** in your Git repository, and a normal clone does not bring it (Chapter 36<!--ref:whatgh-->).

An issue has a number that is unique inside its repository (`#12`) and is the way everything else refers to it.

**What makes a good issue.** Whoever reads it should be able to act without asking you anything:

1. A title that says the problem, not the feeling: "Rolls price shows 3.00 on menu but 3.20 in shop", not "Menu broken".
2. What you did, what you expected, what happened instead.
3. Where: which file, page or version.
4. Evidence: the exact text of an error, and a small example. Never a secret (Chapter 33<!--ref:gitsec-->).

---

## 44.2 Organising issues

> **Checked against GitHub's documentation (R254).** "About issues" lists the metadata you can add: issue types, **labels** and **milestones**, plus sub-issues and dependencies for breaking work down. New repositories come with default labels: `bug` (an unexpected problem or unintended behavior), `documentation`, `duplicate`, `enhancement` (new feature requests), `good first issue` (a good issue for first-time contributors), `help wanted`, `invalid`, `question`, `wontfix` and `accessibility`; you can edit or delete them later. Issues labelled `good first issue` "are used to populate the repository's contribute page". A **milestone** has a description, a due date, a completion percentage and lists of open and closed issues and pull requests. Issues and pull requests "support up to 10 assignees".

| Tool | What it answers |
|---|---|
| **Label** | What *kind* of thing is this? (bug, documentation, question) |
| **Assignee** | Who is *doing* it? |
| **Milestone** | *When* or in which group of work does it belong? |
| **Reference** | What else is *related*? |

**Use few labels, and use them the same way.** A team that invents forty labels ends with none that anyone trusts.

---

## 44.3 References and closing keywords

Writing `#12` in an issue, a pull request or a comment makes a link to issue 12 in the same repository; the documentation says "mentioning an issue in another issue or pull request will create references between them".

A pull request can also **close** an issue when it is merged.

> **Checked against GitHub's documentation (R255).** "Linking a pull request to an issue" says you can link them with a supported keyword in the pull request description or in a commit message. The keywords are `close`, `closes`, `closed`, `fix`, `fixes`, `fixed`, `resolve`, `resolves` and `resolved`. The syntax is `KEYWORD #ISSUE-NUMBER` for an issue in the same repository (for example `Closes #10`), and `KEYWORD OWNER/REPOSITORY#ISSUE-NUMBER` for another repository; for several issues, "use full syntax for each issue". The keywords "can be followed by colons or in uppercase". When the linked pull request is merged into the **default branch**, the issue is closed automatically. The keywords are "interpreted only when the pull request targets the repository's default branch": for any other branch "these keywords are ignored". Only manually linked pull requests can be manually unlinked; to unlink a keyword link, edit the description.

The keyword is just **text in a message**, so it is Git that stores it and the platform that reads it. Here a template file and a commit message with a keyword are made and looked at:

```text
$ cd bakery-menu
$ mkdir -p .github/ISSUE_TEMPLATE
$ printf 'name: Bug report\ndescription: Something on the menu is wrong\nbody:\n  - type: textarea\n    id: what\n    attributes:\n      label: What is wrong?\n    validations:\n      required: true\n' > .github/ISSUE_TEMPLATE/bug.yml
$ cat .github/ISSUE_TEMPLATE/bug.yml
name: Bug report
description: Something on the menu is wrong
body:
  - type: textarea
    id: what
    attributes:
      label: What is wrong?
    validations:
      required: true
$ git add .github
$ git commit -q -m "Add a bug report form"
$ git ls-files .github
.github/ISSUE_TEMPLATE/bug.yml
$ printf -- '- Rolls (six): 3.20\n' >> menu.md
$ git commit -q -am "Correct the price of the rolls" -m "Fixes #12"
$ git log -1 --format=%B
Correct the price of the rolls

Fixes #12

$ git log --oneline --grep='#12'
8bd8b2b (HEAD -> main) Correct the price of the rolls
```

*Recorded in Bash; `ch44-issues/expected-forms-keywords.bash.txt`.*

Git stores `Fixes #12` in the commit message like any other words, and `git log --grep` finds it. What the platform does with it is described above; Git does nothing.

> **⚠️ CAUTION.** A closing keyword acts when the change reaches the default branch. A commit message is part of history and is hard to change once it is shared (Chapter 27<!--ref:rebase-->), while a pull request description can be edited at any time, and GitHub's documentation says that to unlink a keyword link you edit the description. So put keywords in the pull request description more often than in commit messages.

---

## 44.4 Templates and forms

Projects that receive issues from strangers get better issues when they ask for the right information. GitHub offers two ways.

> **New term: issue form.** A template for issues written as a YAML file that defines input fields (text areas, dropdown menus, checkboxes) so that contributors fill in a form instead of free text.

> **Checked against GitHub's documentation (R256).** Issue templates are stored on the repository's **default branch**, in the hidden `.github/ISSUE_TEMPLATE` directory; "if you create a template in another branch, it will not be available". Markdown templates need a `.md` extension; **issue forms** need `.yml`. A form's top-level keys `name`, `description` and `body` are all required, and `body` is an array of elements with a `type` such as `textarea`, `dropdown`, `checkboxes`, `input` or `markdown`. When a contributor submits a form, "the form inputs are converted to a standard markdown issue comment". A file `.github/ISSUE_TEMPLATE/config.yml` can set `blank_issues_enabled: false` to remove the blank-issue option, and `contact_links` to send some reports elsewhere. Pull request templates can live in the root, `docs` or `.github`.

The smallest form, from the recording above:

```yaml
name: Bug report
description: Something on the menu is wrong
body:
  - type: textarea
    id: what
    attributes:
      label: What is wrong?
    validations:
      required: true
```

Because the template is a file in `.github/ISSUE_TEMPLATE`, it is **part of your Git repository**: it is committed, reviewed and versioned like code, and it must be on the default branch to take effect. (YAML, the format, is taught in Chapter 53<!--ref:yaml-->.)

---

## 44.5 A workable habit

1. Search for an existing issue before opening one.
2. One problem per issue.
3. Open the issue before the work, so the pull request can close it.
4. When you start, assign yourself; when it is done, close it with the pull request, not by hand.
5. If an issue cannot be acted on, say what is missing and label it, instead of leaving it open forever.

---

## Checkpoint

## What You Learned

- An issue is a numbered item on the platform, not in the Git repository.
- Labels say what kind, assignees say who, milestones say when, references say what is related.
- Keywords such as `Fixes #12` in a pull request description or commit message close the issue when the change reaches the default branch.
- Issue templates and forms live in `.github/ISSUE_TEMPLATE` on the default branch, and are files in the repository.

## New Vocabulary

**Issue**, **issue form** (introduced above).

## Commands Learned

`git commit -m ... -m ...` (subject and body), `git log --grep`.

## Common Mistakes

1. **Vague titles.**
2. **Closing keywords in commits on the wrong branch**, so nothing closes.
3. **Too many labels.**
4. **Putting secrets in an issue.**
5. **Adding an issue template on a branch other than the default.**

## Practice

Do the exercises in [`exercises/ch44-exercises.md`](../../../exercises/ch44-exercises.md).

## Self-Test

1. Is an issue part of the Git repository? How do you know?
2. Which keyword syntax closes an issue in another repository?
3. Why might `Fixes #12` in a pull request into a feature branch not close the issue?
4. Where do issue forms live, and on which branch?
5. Name the four things an issue should say.

## Before Moving On

You are ready for Chapter 45<!--ref:pr--> if you can:

- [ ] write an issue that someone else can act on
- [ ] use a closing keyword correctly
- [ ] say where an issue form is stored

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| A form file is committed like any file; a keyword is text in the commit message found by `--grep` | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R257 (Git side) |
| Labels, milestones, assignees, references | Checked against `github/docs` (commit `2eaab0b`) | R254 |
| Closing keywords and their rules | Checked against `github/docs` | R255 |
| Templates, forms, `config.yml` | Checked against `github/docs`; the form file was not run on a live account | R256 |

## Where this leads

Chapter 45<!--ref:pr--> shows how a pull request uses these references, and Chapter 46<!--ref:review--> how it is reviewed. Chapter 47<!--ref:projects--> plans work across many issues.
