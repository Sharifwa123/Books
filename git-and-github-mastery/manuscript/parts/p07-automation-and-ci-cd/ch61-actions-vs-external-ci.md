---
key: externalci
number: 61
tag: Deep
first_read: later
status: draft
requires: [actions]
ledger: [R305, R306]
---
# Chapter 61 — Actions vs External CI [Deep]

**In this chapter**

- how any CI system, not only Actions, reports back to a pull request
- checks and commit statuses
- criteria for choosing between GitHub Actions and an external CI system

> **How to read this chapter.** This is a [Deep] chapter about trade-offs; you can skip it on a first read. The statements about GitHub come from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026). **This chapter makes no claims about the features, prices or limits of any other CI product**: they change, and none was checked. The comparison is a list of questions you can ask about any product.

**Before you start.** Chapter 54<!--ref:actions-->.

---

## 61.1 CI is an idea, not a product

Chapter 52<!--ref:cicd--> defined continuous integration: every change is built and tested automatically. GitHub Actions is one way to do it. Others are a CI server that you run yourself, or a hosted service from another company. All of them do the same three things: notice a change, run your commands on a machine, and report the result.

The third step is where GitHub matters, because the result must appear on the pull request.

---

## 61.2 How a result reaches the pull request

GitHub's documentation on status checks: "Status checks show whether commits meet the conditions set for a repository. They are usually created by external systems, such as continuous integration builds, tests, code scanning, or deployment checks." There are two kinds:

| Kind | Detail | Created by |
|---|---|---|
| Checks | Detailed output, annotations and messages | GitHub Apps, including GitHub Actions |
| Commit statuses | A simpler status for a commit | External services and integrations |

The documentation adds that "GitHub Actions generates checks, not commit statuses, when workflows are run", that both are created through GitHub's API, and that "Anyone with write permissions to a repository can set the state for any status check in the repository". If a status check is **required** for a protected branch (Chapter 50<!--ref:protect-->), it must pass before merging; "required status checks can be checks or commit statuses".

The point to remember: **a required check is a name and a result attached to a commit.** GitHub does not care which system produced it, as long as it is reported through the API. That is what makes external CI possible.

The other direction also exists: an external service can start a workflow. The documentation lists the `repository_dispatch` webhook as a way for "an external event" to trigger a workflow, and the `deployment_status` event for "a third party" that provides a deployment status.

> **Checked against GitHub's documentation (R305).** "Status checks" and "Events that trigger workflows".

---

## 61.3 Questions to ask when choosing

Use this list on any candidate, GitHub Actions included. The answers change over time, so **look them up at decision time** rather than trusting a book.

| Question | Why it matters |
|---|---|
| Where does the code run: on the vendor's machines or on yours? | Chapter 59<!--ref:runners--> and Chapter 60<!--ref:wfsec-->: self-run machines are yours to secure |
| What does it cost for your amount of use, and for private repositories? | Limits and billing differ by plan and change |
| Which operating systems and processor types can it run? | Your users may need Windows, macOS or Linux tests |
| Where are the secrets kept, and how are they scoped? | A leak reaches everything the pipeline can touch |
| How does the pipeline definition live? | A file in the repository is reviewed like code; a web form is not |
| Can it be reproduced locally? | Chapter 52<!--ref:cicd-->: the pipeline should be a script you can run yourself |
| How does it report to pull requests, and can the result be required? | See section 61.2 |
| What happens if you leave? | Lock-in: how much of the pipeline is portable |
| Who maintains the reusable pieces, and can you pin them? | Chapter 60<!--ref:wfsec--> on pinning |

---

## 61.4 A portable habit

The most useful habit is independent of the product: **keep the real work in scripts inside the repository and let the CI configuration only call them.** The workflow of this book does that: its checks are the scripts in `tools/` and `verification/`, which a reader can run on their own computer, and the workflow only installs Git and calls them. Moving to another system then means rewriting a short file, not the checks.

Chapter 52<!--ref:cicd--> built a local pipeline for the same reason.

---

## 61.5 When to keep Actions, when to look elsewhere

There is no universal answer. Actions is convenient when the code is already on GitHub: no second account, no second place for secrets, and results appear as checks on the pull request. Reasons to look elsewhere are usually specific: a required machine type, a policy about where code may run, or an existing pipeline you do not want to rewrite. Decide with the questions in section 61.3 and current documentation. Mixing is common: one system for tests, another for deployment.

---

## Checkpoint

## What You Learned

- CI is a practice; any system can do it.
- Results reach a pull request as checks (rich, from apps such as Actions) or commit statuses (simple, from integrations).
- A required status check is a name and result on a commit; it can come from any system.
- Choose by asking questions and reading current documentation.
- Keep real work in scripts so the CI system is replaceable.

## New Vocabulary

**Commit status** and **check** (as GitHub uses them; see the glossary).

## Commands Learned

No new commands.

## Common Mistakes

1. **Assuming a comparison in a book is current.** Prices and limits change.
2. **Putting the whole pipeline in CI-specific syntax.**
3. **Making a status check required before it reports reliably.**

## Practice

Do the exercises in [`exercises/ch61-exercises.md`](../../../exercises/ch61-exercises.md).

## Self-Test

1. What are the two kinds of status check on GitHub?
2. Which kind does GitHub Actions create?
3. Can an external system's result be required for merging?
4. Give two questions you would ask about any CI product.
5. Why keep the real work in scripts?

## Before Moving On

You are ready for Chapter 62<!--ref:ghsec--> if you can:

- [ ] distinguish a check from a commit status
- [ ] list three criteria for choosing a CI system

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Checks, commit statuses, required status checks, external triggers | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R305 |
| The choosing questions and the portable habit | Reasoning and this book's own workflow; no other CI product was examined | R306 |

## Where this leads

Part VIII turns to the security features GitHub offers for a whole repository, beginning with Chapter 62<!--ref:ghsec-->.
