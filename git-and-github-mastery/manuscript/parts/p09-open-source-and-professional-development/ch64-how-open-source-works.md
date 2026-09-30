---
key: oss
number: 64
tag: Core
first_read: part
status: draft
requires: [pr, collab]
ledger: [R314, R315, R316]
---
# Chapter 64 — How Open Source Works [Core]

**In this chapter**

- what "open source" means, and what it does not mean
- the roles people play in a project
- the contribution flow, from finding a project to a merged change
- `CONTRIBUTING.md`, the code of conduct and the community profile
- good first issues, sign-off, and contributing responsibly

> **How to read this chapter.** Statements about GitHub features come from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026); they were **not run on a live account**. The definition of open source and everything about licences is in Chapter 65<!--ref:licences-->, and **this book is not legal advice**. The roles and advice in this chapter are the author's description of common practice, not a standard; they are marked as such. One small command demonstration (sign-off) was recorded.

**Before you start.** Chapter 45<!--ref:pr--> and Chapter 49<!--ref:collab--> (forks, upstream, pull requests).

---

## 64.1 What "open source" means

You will meet three separate ideas that people mix up:

1. **Public.** Anyone can *see* the code (Chapter 39<!--ref:ghrepo-->: a public repository).
2. **Source-available.** The code can be read, but the licence may forbid some uses.
3. **Open source.** The code is public **and** the licence grants specific permissions to use, change and share it.

Being visible is not permission. This is the first of the seven distinctions this book keeps returning to: *reading* is not *copying*, and neither is *modifying* or *reusing*. The permission comes from the licence file, not from the repository being public. Chapter 65<!--ref:licences--> explains licences; **until you have read it, treat any code without a licence as not yours to reuse.**

---

## 64.2 Roles in a project

Projects use different words. This is one common description, the author's, not an official list:

| Role | What they usually do |
|---|---|
| User | Uses the software; may report problems |
| Contributor | Sends a change, a report, a translation or a documentation fix |
| Maintainer | Reviews and merges changes, triages issues, makes releases |
| Owner | Controls the repository or organization and its settings |

GitHub's permission levels (Chapter 49<!--ref:collab-->) are separate: they say what an account **can do**, while a role says what a person **does**. A maintainer with write access is common; a contributor with no access at all, working from a fork, is the normal case for a stranger.

---

## 64.3 The contribution flow

The steps below are Chapter 49<!--ref:collab--> and Chapter 45<!--ref:pr--> applied to someone else's project:

1. **Read first.** The README, `CONTRIBUTING.md`, the code of conduct, the licence.
2. **Look at the issues.** Is your idea, bug or fix already discussed? Say hello in an existing issue instead of duplicating it.
3. **Discuss before building anything large.** A quick issue asking "would you accept this?" can save days.
4. **Fork, clone, branch.** Work on a topic branch, never on `main` of your fork (Chapter 49<!--ref:collab-->).
5. **Make one small, focused change**, follow the project's style, add or update tests if the project has them.
6. **Open a pull request** that says what and why, links the issue, and follows the pull request template if there is one (Chapter 45<!--ref:pr-->).
7. **Respond to review** politely and promptly (Chapter 46<!--ref:review-->). A request for changes is normal, not a rejection.
8. **Accept the decision.** A maintainer may decline a good change because it does not fit the project. You can keep your fork.

---

## 64.4 The files that tell you the rules

GitHub's documentation describes these files:

- **`CONTRIBUTING.md`.** "To help your project contributors do good work, you can add a file with contribution guidelines to your project repository's root, `docs`, or `.github` folder. When someone opens a pull request or creates an issue, they will see a link to that file." If there are several, the one shown is chosen "in the following order: the `.github` directory, then the repository's root directory, and finally the `docs` directory". Filenames "are not case sensitive".
- **Code of conduct.** "A code of conduct defines standards for how to engage in a community." The documentation's advice to maintainers: "Consider carefully whether you are willing and able to enforce it", and, if you use one written by someone else, follow "any attribution guidelines from the source".
- **The community profile.** A checklist that "checks to see if a project includes recommended community health files, such as README, CODE_OF_CONDUCT, LICENSE, or CONTRIBUTING". As a contributor you can use it to see whether the project is set up to welcome you.
- **Templates** for issues and pull requests (Chapters 44<!--ref:issues--> and 45<!--ref:pr-->) and `SECURITY.md` (Chapter 62<!--ref:ghsec-->).
- **The licence** (Chapter 65<!--ref:licences-->).

Organizations and personal accounts can also supply **default** community health files for all their repositories, from a special `.github` repository.

> **Checked against GitHub's documentation (R314).** "Setting guidelines for repository contributors", "Adding a code of conduct to your project", "About community profiles for public repositories", "Creating a default community health file".

---

## 64.5 Good first issues

The documentation: "You can apply the `good first issue` label to issues in your public repository so that people can find them when searching by labels." GitHub "uses an algorithm to determine the most approachable issues in each repository and surface them in various places", and the label "can increase the likelihood that your issues are surfaced". As a newcomer, search for that label, read the issue **and** the surrounding discussion, and say you would like to take it before you start, so that two people do not do the same work.

> **Checked against GitHub's documentation (R315).** "Encouraging helpful contributions to your project with labels". How GitHub's algorithm chooses issues was not examined.

---

## 64.6 Sign-off

Some projects ask contributors to **sign off** their commits, meaning to add a line that says the author has the right to submit the change under the project's rules. **It is text, not a cryptographic signature** (Chapter 33<!--ref:gitsec--> and Chapter 63<!--ref:secpractice--> covered real signatures). Git can add the line for you:

```text
$ git init -q proj && cd proj
$ printf 'hello\n' > a.txt && git add a.txt
$ git commit -q -s -m "Add greeting"
$ git log -1 --format=%B
Add greeting

Signed-off-by: Ada Learner <ada@example.org>

$ git log -1 --format='%(trailers:key=Signed-off-by,valueonly)'
Ada Learner <ada@example.org>
```

*Recorded in Bash; `ch64-oss/expected-signoff.bash.txt`.*

`git commit -s` added `Signed-off-by:` with the name and email from your configuration (Chapter 14<!--ref:config-->). The `%(trailers:...)` format picks that line out of the message, and it can be used to see which commits have one:

```text

$ git commit -q --allow-empty -m "No sign-off here"
$ git log --format='%s | %(trailers:key=Signed-off-by,valueonly,separator=)'
No sign-off here |
Add greeting | Ada Learner <ada@example.org>
```

*Recorded in Bash; `ch64-oss/expected-signoff.bash.txt`.*

GitHub's documentation on the web interface: "Commit signoffs enable users to affirm that a commit complies with the rules and licensing governing a repository." A repository or organization can require sign-off for commits made **through the web interface**; the documentation describes that setting only for web-based commits. What a given project means by sign-off is stated in that project's own contribution guide: read it, and do not sign off if you do not have the right to submit the work.

> **Checked against GitHub's documentation (R316) and locally tested.** "Managing the commit signoff policy for your repository". The recording ran on Git 2.43.0 in Bash and zsh and is re-run in CI on newer Git.

---

## 64.7 Contributing responsibly

This advice is the author's, and common in open-source projects, not a rule:

- **Respect maintainers' time.** Most are volunteers. Read before asking; make your change easy to review.
- **Keep the change small and single-purpose.**
- **Do not submit what you do not understand or cannot explain**, whoever or whatever wrote it, and do not submit work you have no right to submit (Chapter 65<!--ref:licences-->).
- **Never include secrets or personal data** in a pull request (Chapter 33<!--ref:gitsec-->).
- **Be patient and kind.** Follow the code of conduct, in the tone of every comment.
- **Report security problems privately**, using the project's `SECURITY.md` (Chapter 62<!--ref:ghsec-->), not in a public issue.
- **Say thank you.** It costs nothing.

---

## Checkpoint

## What You Learned

- Public does not mean open source; the licence grants the permissions.
- A role (what you do) differs from a permission (what you can do).
- The flow: read, look, discuss, fork and branch, change, open a pull request, respond, accept.
- `CONTRIBUTING.md`, the code of conduct and the community profile state a project's rules.
- Sign-off is a line of text added with `git commit -s`; read the project's meaning.

## New Vocabulary

**Open source**, **maintainer**, **contributor**, **code of conduct**, **sign-off** (see the glossary).

## Commands Learned

`git commit -s`; `git log --format='%(trailers:key=...)'`.

## Common Mistakes

1. **Assuming public code may be reused.**
2. **Starting a large change without asking.**
3. **Working on `main` of a fork.**
4. **Submitting several unrelated changes in one pull request.**
5. **Taking offence at a request for changes.**

## Practice

Do the exercises in [`exercises/ch64-exercises.md`](../../../exercises/ch64-exercises.md).

## Self-Test

1. What is the difference between public and open source?
2. Name the steps of the contribution flow in order.
3. Where can `CONTRIBUTING.md` live, and which one wins?
4. What does `git commit -s` add?
5. Is sign-off the same as a signed commit?

## Before Moving On

You are ready for Chapter 65<!--ref:licences--> if you can:

- [ ] explain why visible code is not automatically reusable
- [ ] describe the contribution flow to a friend
- [ ] find a project's contribution rules

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `git commit -s` adds a `Signed-off-by` trailer; the trailers format reads it | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R316 (local side) |
| Contribution guidelines, code of conduct, community profile, `good first issue`, commit signoff setting | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account** | R314-R316 |
| Roles, flow and responsible-contribution advice | The author's description of common practice; not a standard | none |

## Where this leads

Chapter 65<!--ref:licences--> explains copyright and licences, the thing that turns public code into code you may use.
