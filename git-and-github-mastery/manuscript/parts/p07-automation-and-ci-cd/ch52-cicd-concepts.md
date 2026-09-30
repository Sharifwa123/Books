---
key: cicd
number: 52
tag: Core
first_read: full
status: draft
requires: [pr, terminal]
ledger: [R279, R280]
---
# Chapter 52 — CI/CD Concepts [Core]

**In this chapter**

- what continuous integration and continuous deployment mean
- the stages of a pipeline: build, test, lint, deploy
- how a check script's exit code says pass or fail
- why the same checks should run on a server, not only on your computer

> **How to read this chapter.** The local pipeline was run and recorded. Statements about GitHub Actions are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used. This chapter is about **ideas**, and Chapter 54<!--ref:actions--> shows the platform's way of doing them.

**Before you start.** Chapter 45<!--ref:pr--> and Chapter 7<!--ref:terminal-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on newer Git versions.

---

## 52.1 The problem that CI solves

Chapter 45<!--ref:pr--> said a pull request is a place for review. Reviewers are people, and people are slow at one job: checking that a change does not break something. A computer is good at exactly that. The idea of **continuous integration** is to let a machine run the same checks on every change, automatically and immediately.

> **New term: continuous integration (CI).** The practice of committing code often to a shared repository and having every change built and tested automatically, so that errors are found early.

GitHub's documentation defines it as "a software practice that requires frequently committing code to a shared repository", and says: "Committing code more often detects errors sooner and reduces the amount of code a developer needs to debug when finding the source of an error. Frequent code updates also make it easier to merge changes from different members of a software development team."

> **New term: continuous deployment (CD).** The practice of using automation to publish and deploy software updates, usually after the code is built and tested automatically.

The documentation: "Continuous deployment (CD) is the practice of using automation to publish and deploy software updates. As part of the typical CD process, the code is automatically built and tested before deployment." CD is "often coupled with" CI.

> **Checked against GitHub's documentation (R279).** "About continuous integration" and "About continuous deployment" are the sources of the quotations above. The documentation notes that tests can include "code linters (which check style formatting), security checks, code coverage, functional tests, and other custom checks", and that you can build and test updates locally before pushing "or you can use a CI server that checks for new code commits in a repository".

---

## 52.2 The stages

The stages differ between projects, but four words cover most of them. A sequence of stages is a **pipeline**.

| Stage | Question it answers | Example for the bakery menu |
|---|---|---|
| **Lint** | Is the file written in the agreed style? | No tab characters in `menu.md` |
| **Test** | Does it behave correctly? | Every menu item has a price with two decimals |
| **Build** | Can the deliverable be produced? | Write `dist/menu.txt` |
| **Deploy** | Is it published where people use it? | Copy `dist/menu.txt` to a web server |

> **New term: pipeline.** The ordered stages a change passes through automatically, for example lint, test, build and deploy. A failure in one stage normally stops the later ones.

The order matters: cheap and fast checks first, so that a mistake is reported in seconds and the slow stages do not run for nothing.

---

## 52.3 A pipeline in ten lines

A CI service is not magic. At heart it runs a script and looks at whether the script succeeded. Here the bakery project has such a script, `ci.sh`, with three stages. First read it, then run it:

```text
$ cd bakery-menu
$ cat ci.sh
#!/bin/sh
echo "lint: no tab characters"
if grep -q "$(printf '\t')" menu.md; then echo "FAIL lint: a tab was found"; exit 1; fi
echo "test: every item has a price"
if grep '^- ' menu.md | grep -v -E ': [0-9]+\.[0-9]{2}$'; then echo "FAIL test: a line has no price"; exit 1; fi
echo "build: write dist/menu.txt"
mkdir -p dist && cp menu.md dist/menu.txt
echo "PASS"
$ sh ci.sh
lint: no tab characters
test: every item has a price
build: write dist/menu.txt
PASS
$ echo "exit code: $?"
exit code: 0
$ ls dist
menu.txt
```

*Recorded in Bash; `ch52-cicd/expected-local-pipeline.bash.txt`.*

Every stage prints what it is doing. The script ends with `PASS`, and `echo "exit code: $?"` shows **exit code 0**. In the shell, **exit code 0 means success and anything else means failure**, and that is the signal that CI tools such as GitHub Actions read from each step (Chapter 54<!--ref:actions-->) (Chapter 7<!--ref:terminal-->). A `dist/menu.txt` file was produced by the build stage.

Now a mistake is introduced: a menu line with a price written in words.

```text
$ printf -- '- Coffee: two pounds\n' >> menu.md
$ sh ci.sh
lint: no tab characters
test: every item has a price
- Coffee: two pounds
FAIL test: a line has no price
$ echo "exit code: $?"
exit code: 1
```

*Recorded in Bash; `ch52-cicd/expected-local-pipeline.bash.txt`.*

The lint stage still passes, the test stage prints the offending line and stops with `FAIL test: a line has no price`, and the exit code is **1**. The build stage never runs, so no broken deliverable is produced. This is what a red cross on a pull request means: some stage of such a script returned a non-zero exit code.

The script is a stand-in for a real project's tools (a compiler, a test runner, a linter), but the *shape* is the same.

---

## 52.4 Why run it on a server too

You can run `ci.sh` on your own computer, and you should (Chapter 32<!--ref:custom--> shows a hook that could run it before each push). A CI *server* adds three things.

1. **A clean, known environment.** "It works on my computer" often means "it depends on something only my computer has". A fresh machine finds that.
2. **Everyone, every time.** Nobody can forget to run it, and it runs on pull requests from people who have never heard of your script.
3. **A visible result.** GitHub's documentation says it "runs your CI tests and provides the results of each test in the pull request, so you can see whether the change in your branch introduces an error", and that when all pass the changes "are ready to be reviewed by a team member or merged".

Two habits keep CI useful. **Keep it fast**, because a check that takes an hour is skipped. **Keep it trustworthy**: a check that fails at random ("flaky") teaches people to ignore red, and then real failures are missed.

> **⚠️ CAUTION.** Passing checks show that the checks passed, not that the code is right. A test that does not exist cannot fail. And never let a pipeline print or store secrets in its output (Chapter 33<!--ref:gitsec-->, Chapter 60<!--ref:wfsec-->).

---

## 52.5 Where GitHub Actions fits

GitHub's documentation says CI with GitHub Actions "offers workflows that can build the code in your repository and run your tests". Workflows "can run on GitHub-hosted virtual machines, or on machines that you host yourself", and can be configured to run when an event occurs (for example, "when new code is pushed to your repository"), "on a set schedule, or when an external event occurs". When you set up CI, GitHub "analyzes the code in your repository and recommends CI workflows based on the language and framework", offering workflow templates. The same tool can run continuous deployment: it "can build the code in your repository and run your tests before deploying", with **environments** that can "require approval for a job to proceed, restrict which branches can trigger a workflow, or limit access to secrets".

> **Checked against GitHub's documentation (R280).** "About continuous integration", "About continuous deployment" and "Understanding GitHub Actions". Chapter 54<!--ref:actions--> defines the terms *workflow*, *event*, *job*, *step*, *runner* and *action*, and Chapter 58<!--ref:wfadvanced--> covers environments.

---

## Checkpoint

## What You Learned

- CI runs the same checks on every change automatically; CD publishes software automatically after the checks.
- A pipeline is an ordered set of stages; cheap checks come first.
- A check script succeeds with exit code 0 and fails with anything else.
- A server gives a clean environment, coverage of everyone, and a visible result.
- Passing checks are evidence, not proof.

## New Vocabulary

**Continuous integration (CI)**, **continuous deployment (CD)**, **pipeline** (introduced above).

## Commands Learned

`sh script.sh`, `echo "exit code: $?"`, `grep -E`, `mkdir -p`.

## Common Mistakes

1. **Believing that green means correct.**
2. **Slow checks** that people bypass.
3. **Flaky checks** that people learn to ignore.
4. **Deploying without a test stage.**
5. **Printing secrets in pipeline output.**

## Practice

Do the exercises in [`exercises/ch52-exercises.md`](../../../exercises/ch52-exercises.md).

## Self-Test

1. What does exit code 0 mean, and what does any other code mean?
2. Why should cheap checks come first?
3. Give two things a CI server provides that your own computer does not.
4. What is the difference between CI and CD?

## Before Moving On

You are ready for Chapter 53<!--ref:yaml--> if you can:

- [ ] name the four stages of a pipeline
- [ ] read a check script and say which stage failed
- [ ] explain what a red cross on a pull request means

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| A script's exit code decides pass or fail; a failing stage stops the later ones | Locally tested: Bash 5.2 and zsh 5.9 (POSIX `sh`), Git 2.43.0 environment; CI on newer Git | R280 (local side) |
| Definitions of CI and CD, what CI runs and reports, where Actions fits | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R279, R280 |
| The stage table and habits | The book's own explanation, not a sourced rule | R279 |

## Where this leads

Chapter 53<!--ref:yaml--> teaches the file format that workflows use, and Chapter 54<!--ref:actions--> writes a real workflow.
