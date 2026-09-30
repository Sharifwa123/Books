---
key: workflows_practice
number: 56
tag: Core
first_read: full
status: draft
requires: [actions]
ledger: [R288, R289, R290, R291]
---
# Chapter 56 — Practical Workflows [Core]

**In this chapter**

- variables and secrets, and passing values between steps
- artifacts and caches, and how they differ
- matrices: one job, many configurations
- manual and scheduled triggers, and how cron fields work
- recipes: tests on pull requests, a format check, a build, issue automation, scheduled maintenance

> **How to read this chapter.** The **cron field rules** and the **matrix expansion** were run and recorded, as tests of what GitHub's documentation says. Everything else is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026). **No workflow in this chapter was run on a live account by hand.** The recipes are built from documented syntax and the book's own suggestions, and each says which. Where a recipe is the book's design and not GitHub's, it is labelled.

**Before you start.** Chapter 54<!--ref:actions--> and Chapter 55<!--ref:exprs-->. The recordings ran in Bash and zsh with Python 3, and were re-run in CI.

---

## 56.1 Variables, secrets and passing values

**Environment variables.** A workflow can define variables with the `env` key, at three levels. GitHub's documentation lists them: for "the entire workflow, by using `env` at the top level", for "the contents of a job", and for "a specific step". "The scope of a custom variable set by this method is limited to the element in which it is defined." For values you want to share across many workflows, you can define a **configuration variable** at the organisation, repository or environment level. The documentation warns: "By default, variables render unmasked in your build outputs. If you need greater security for sensitive information, such as passwords, use secrets instead."

**Secrets.** A **secret** is a named value that you store on the platform (Chapter 38<!--ref:ghauth--> told you why a token never belongs in a file). A workflow reads it through the `secrets` context. GitHub's documentation gives these rules:

- "With the exception of `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository."
- "Secrets are not automatically passed to reusable workflows", and "are not available to workflows triggered by Dependabot events".
- "Secrets cannot be directly referenced in `if:` conditionals": put the secret in a job-level environment variable and test that.
- "If a secret has not been set, the return value of an expression referencing the secret ... will be an empty string."
- "Avoid passing secrets between processes from the command line, whenever possible", because "command-line processes may be visible to other users"; prefer environment variables or standard input.
- "Mask all sensitive information that is not a GitHub secret by using `::add-mask::VALUE`."

> **Checked against GitHub's documentation (R288).** "Store information in variables", "Using secrets in GitHub Actions" and the reusable text on forked repositories.

**Passing a value between steps.** Chapter 54<!--ref:actions--> showed that an environment variable does not survive from one step to the next. GitHub's own example writes to a special file: `echo 'NUM_OPEN_ISSUES='$numOpenIssues >> $GITHUB_ENV` in one step, and reads `$NUM_OPEN_ISSUES` in a later step. Files are shared, so this works.

---

## 56.2 Artifacts and caches

Two features store files on the platform and are easy to confuse.

| | Artifact | Cache |
|---|---|---|
| **What for** | Files **produced** by a job that you want to keep or pass on | Files that are **reused** between runs and expensive to make |
| **Examples** | Built programs, test results, logs, coverage reports | Downloaded dependencies |
| **Rule** | Survives after the run for you to download; can pass files between jobs | A job "should always be able to re-download or regenerate these files if a cache isn't available" |

GitHub's documentation: "An artifact is a file or collection of files produced during a workflow run. Artifacts allow you to persist data after a job has completed, and share that data with another job in the same workflow." The two actions are `upload-artifact` and `download-artifact`.

**Why caching exists.** "Jobs on GitHub-hosted runners start in a clean runner image and must download dependencies each time, causing increased network utilization, longer runtime, and increased cost."

> **⚠️ CAUTION.** Caches are a security question. The documentation says: "Caches are shared based on the branch or tag a workflow run uses, not on the identity of the workflow or job", that restored files should be treated "as untrusted input", and that you should "never store secrets or other sensitive data in a cache". "Poisoned caches can lead to code execution in trusted workflows"; GitHub gives workflows that run for low-trust triggers read-only access to caches in the default branch's scope. Chapter 60<!--ref:wfsec--> returns to this.

> **Checked against GitHub's documentation (R289).** "Store and share data with workflow artifacts", "Dependency caching" and "Manage caches".

---

## 56.3 Matrices

To run the same job in several configurations you use a **matrix**. From GitHub's documentation:

```yaml
jobs:
  example_matrix:
    strategy:
      matrix:
        version: [10, 12, 14]
        os: [ubuntu-latest, windows-latest]
```

"A job will run for each possible combination of the variables. In this example, the workflow will run six jobs", created in the order shown in the documentation. A shell loop expands the same matrix, and reproduces the documented count and order:

```text
$ for version in 10 12 14; do for os in ubuntu-latest windows-latest; do echo "{version: $version, os: $os}"; done; done
{version: 10, os: ubuntu-latest}
{version: 10, os: windows-latest}
{version: 12, os: ubuntu-latest}
{version: 12, os: windows-latest}
{version: 14, os: ubuntu-latest}
{version: 14, os: windows-latest}
$ for version in 10 12 14; do for os in ubuntu-latest windows-latest; do echo x; done; done | wc -l
6
```

*Recorded in Bash; `ch56-practice/expected-matrix.bash.txt`.*

Six lines, in the documented order: the first variable is the outer loop. This is a **stand-in**, not GitHub's engine: it shows the arithmetic (3 versions times 2 systems is 6 jobs), which is why a matrix with many variables grows fast, and each combination uses a runner and time.

> **Checked against GitHub's documentation (R290).** "Running variations of jobs in a workflow" gives the example, the six combinations and their order. The recording reproduces them with nested shell loops.

---

## 56.4 Manual and scheduled triggers

**Manual.** `on: workflow_dispatch` lets a person start a workflow by hand. GitHub's documentation: "the 'Run workflow' button will be present if the workflow file exists on the default branch", and the workflow can define **inputs** that are read through the `inputs` context. Once a workflow has run at least once you can also start it against any branch or tag through the API or the GitHub CLI.

**Scheduled.** `on: schedule` runs a workflow at set times, written as **cron** expressions with five fields: minute, hour, day of month, month, day of week. The documentation says:

- "Use POSIX cron syntax", and scheduled workflows run "on the latest commit on the default branch" and (by default) in UTC. The shortest interval is once every 5 minutes.
- The schedule "can be delayed during periods of high loads", including "the start of every hour", so "schedule your workflow to run at a different time of the hour".
- "In a public repository, scheduled workflows are automatically disabled when no repository activity has occurred in 60 days."
- The operators are `*` (any), `,` (list), `-` (range) and `/` (step); "GitHub Actions does not support the non-standard syntax `@yearly`, `@monthly`, `@weekly`, `@daily`, `@hourly`, and `@reboot`."

The documentation gives examples of what its operators mean. A small script expands the minute and hour fields, and can test them:

```text
$ python3 cron.py '15 * * * *'
minutes: [15]
hours: 24 values from 0 to 23
$ python3 cron.py '2,10 4,5 * * *'
minutes: [2, 10]
hours: [4, 5]
$ python3 cron.py '30 4-6 * * *'
minutes: [30]
hours: [4, 5, 6]
$ python3 cron.py '20/15 * * * *'
minutes: [20, 35, 50]
hours: 24 values from 0 to 23
$ python3 cron.py '15 4,5 * * *'
minutes: [15]
hours: [4, 5]
```

*Recorded in Bash; `ch56-practice/expected-cron.bash.txt`.*

Each result matches the documentation: `15 * * * *` is minute 15 of every hour; `2,10 4,5 * * *` is minutes 2 and 10 of hours 4 and 5; `30 4-6 * * *` is minute 30 of hours 4, 5 and 6; and `20/15 * * * *` gives minutes 20, 35 and 50, the documentation's own words: "every 15 minutes starting from minute 20 through 59". The last line is the documentation's example schedule `15 4,5 * * *`.

The script covers only the minute and hour fields and only these operators; it is a check of the documentation, not a scheduler.

> **Checked against GitHub's documentation (R291).** "Events that trigger workflows": `schedule` and `workflow_dispatch`. Time zones: recent documentation describes an optional `timezone` key for schedules; this book uses UTC and does not depend on it.

---

## 56.5 Recipes

Every recipe below has the same shape: an event, a job, a runner, and steps (Chapter 54<!--ref:actions-->). They are **the book's designs**, built from documented keys; the two documented examples are marked.

**Recipe 1: run the checks on every pull request.** Use the check script of Chapter 52<!--ref:cicd-->:

```yaml
name: Check the menu
on: pull_request
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: sh ci.sh
```

**Recipe 2: a format check.** A separate job for style, so that a formatting mistake is reported in seconds and separately from the tests: the same shape with `run: sh lint.sh`.

**Recipe 3: build and keep the result.** After the checks, produce the deliverable and keep it as an artifact with the `upload-artifact` action (Section 56.2).

**Recipe 4 (documented): comment on a new issue.** GitHub's documentation gives this workflow. The GitHub CLI is "preinstalled on all GitHub-hosted runners", and "for each step that uses GitHub CLI, you must set an environment variable called `GH_TOKEN`":

```yaml
name: Comment when opened
on:
  issues:
    types:
      - opened
jobs:
  comment:
    runs-on: ubuntu-latest
    steps:
      - run: gh issue comment $ISSUE --body "Thank you for opening this issue!"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ISSUE: ${{ github.event.issue.html_url }}
```

Whether the default token may comment on issues depends on the permissions given to `GITHUB_TOKEN`, which is Chapter 60<!--ref:wfsec-->'s subject.

**Recipe 5 (documented): a scheduled report.** GitHub's documentation also shows a workflow that runs `on: schedule` with `cron: '20 8 * * *'` ("Daily at 8:20 UTC"), asks the platform how many issues are open with `gh api graphql`, saves the number with `echo 'NUM_OPEN_ISSUES='... >> $GITHUB_ENV`, and files an issue with `gh issue create`. That is scheduled maintenance: the same steps at the same time every day, with nobody remembering to do them.

> **⚠️ CAUTION.** Automation that writes to your repository or its issues can also do damage at scale, and a scheduled workflow keeps running when nobody is watching. Give each workflow the least permission it needs (Chapter 60<!--ref:wfsec-->), and read the log of the first few runs.

> **Checked against GitHub's documentation (R291).** The two documented recipes are from "Using GitHub CLI in workflows" (issue comment and report workflows); the syntax of `run`, `env`, `uses` and `on` is as in Chapter 54<!--ref:actions-->.

---

## Checkpoint

## What You Learned

- `env` sets variables at workflow, job or step level; secrets come through the `secrets` context and are not passed to workflows from forks (except `GITHUB_TOKEN`).
- A value moves between steps through a file such as `$GITHUB_ENV`.
- Artifacts keep and pass files produced by a job; caches reuse files that are costly to recreate, and are a security concern.
- A matrix runs one job once per combination: 3 versions and 2 systems make 6 jobs.
- Schedules use five cron fields in UTC, can be delayed, and pause after 60 days without activity in a public repository.

## New Vocabulary

**Artifact**, **matrix**, **cron** (introduced above). *Secret* was defined in Chapter 33<!--ref:gitsec-->; here it also means a value stored on the platform for workflows.

## Commands Learned

`echo 'NAME=value' >> $GITHUB_ENV` (inside a workflow), `gh issue comment`, `gh issue create`.

## Common Mistakes

1. **Putting a secret in `env` at the top of a public file** instead of using `secrets`.
2. **Expecting a secret in a workflow triggered from a fork.**
3. **Scheduling at the start of the hour.**
4. **A matrix that multiplies into dozens of jobs.**
5. **Storing sensitive files in a cache or an artifact.**

## Practice

Do the exercises in [`exercises/ch56-exercises.md`](../../../exercises/ch56-exercises.md).

## Self-Test

1. How do you pass a value from one step to the next?
2. What is the difference between an artifact and a cache?
3. How many jobs does a matrix with 4 versions and 3 systems create?
4. Which cron expression gives minutes 0, 15, 30 and 45?
5. Why might a scheduled workflow stop running in a public repository?

## Before Moving On

You are ready for Chapter 57<!--ref:wfdebug--> if you can:

- [ ] read a workflow with `env`, `secrets`, a matrix and a schedule
- [ ] say what artifacts and caches are for
- [ ] explain why a workflow should ask for as little as possible

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Documented cron examples expand to the documented minutes and hours; a 3 by 2 matrix gives six jobs in the documented order | Locally tested (stand-ins in Python and shell): Bash 5.2 and zsh 5.9; CI | R290, R291 (local side) |
| Variables, secrets, artifacts, caches, matrices, manual and scheduled triggers, the two documented recipes | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account** | R288-R291 |
| Recipes 1-3 | **The book's own designs**, built from documented keys, not run | R291 |

## Where this leads

Chapter 57<!--ref:wfdebug--> reads logs and fixes failures. Chapter 58<!--ref:wfadvanced--> reuses workflows and adds environments, and Chapter 60<!--ref:wfsec--> covers permissions and untrusted input.
