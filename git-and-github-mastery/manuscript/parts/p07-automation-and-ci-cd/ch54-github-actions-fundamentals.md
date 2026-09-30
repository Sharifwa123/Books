---
key: actions
number: 54
tag: Core
first_read: full
status: draft
requires: [yaml, pr]
ledger: [R283, R284, R285]
---
# Chapter 54 — GitHub Actions Fundamentals [Core]

**In this chapter**

- the six words of GitHub Actions: workflow, event, job, step, runner, action
- where a workflow file lives and how to read one
- `on`, `jobs`, `runs-on`, `steps`, `uses` and `run`
- why each step is its own process
- what a real project's workflow looks like, including this book's own

> **How to read this chapter.** The workflow file and the step behaviour were run and recorded locally. Statements about GitHub Actions are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026). No workflow was run on a live account **by hand**; but this book's repository has its own workflow, which ran on GitHub while the book was written, and section 54.6 reports what it showed.

**Before you start.** Chapter 53<!--ref:yaml--> and Chapter 45<!--ref:pr-->. The recording ran in Bash and zsh on Git 2.43.0 and Python 3 with PyYAML, and was re-run in CI.

---

## 54.1 The six words

GitHub's documentation defines the pieces of GitHub Actions in one paragraph. Read it slowly, then see the picture.

> **New term: workflow (GitHub Actions).** A configurable automated process, defined in a YAML file in the repository, that runs one or more jobs when triggered by an event.

- A **workflow** is triggered by an **event** in your repository, "such as a pull request being opened or an issue being created".
- The workflow contains one or more **jobs**, which "can run in sequential order or in parallel".
- Each job runs on its own **runner** (a virtual machine, or a container) and has one or more **steps**.
- A step either runs a script that you define, or runs an **action**: "a reusable extension" that does a common task.

> **New term: event.** Something that happens in a repository, such as a push, a pull request or an issue, that can start a workflow. Events can also be a schedule, a call to the platform's programming interface, or a manual start.

> **New term: job.** A set of steps in a workflow that run on the same runner. By default jobs "have no dependencies and run in parallel".

> **New term: step.** One task in a job: either a shell command (`run`) or an action (`uses`). Steps run in order.

> **New term: runner.** The machine that runs a job. GitHub provides Linux, Windows and macOS virtual machines, or you can host your own.

> **New term: action.** A pre-defined, reusable set of code that does a specific task inside a workflow, such as pulling your Git repository onto the runner or setting up a language toolchain.

> **Checked against GitHub's documentation (R283).** "Understanding GitHub Actions" is the source of the definitions and quotations. It adds that an event "can also originate from ... a schedule, by posting to a REST API, or manually", that steps "are executed in order and are dependent on each other" and, since they run on the same runner, "you can share data from one step to another", that a **matrix** runs the same job many times with different variables such as operating systems or language versions, and that you can find actions in the Marketplace or write your own.

---

## 54.2 A workflow is a file

A workflow is a YAML file (Chapter 53<!--ref:yaml-->) in the repository. GitHub's documentation is exact about where:

- "Workflow files use YAML syntax, and must have either a `.yml` or `.yaml` file extension."
- "You must store workflow files in the `.github/workflows` directory of your repository."
- The `name` key gives the workflow's name in the Actions tab; "if you omit `name`, GitHub displays the workflow file path relative to the root of the repository".

Because it is a file in the repository, a workflow is **versioned, reviewed and merged like code**: you change it on a branch and open a pull request (Chapter 45<!--ref:pr-->).

Here is a small workflow for the bakery project. It runs the check script from Chapter 52<!--ref:cicd--> on every push and every pull request. After it, a few lines of Python read the file and print its structure:

```text
$ cd bakery-menu
$ mkdir -p .github/workflows
$ printf 'name: Check the menu\non: [push, pull_request]\njobs:\n  check:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Get the code\n        uses: actions/checkout@v6\n      - name: Run the checks\n        run: sh ci.sh\n' > .github/workflows/check.yml
$ cat .github/workflows/check.yml
name: Check the menu
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Get the code
        uses: actions/checkout@v6
      - name: Run the checks
        run: sh ci.sh
$ python3 outline.py .github/workflows/check.yml
name: Check the menu
events: ['push', 'pull_request']
job check runs-on ubuntu-latest
  step 1 uses actions/checkout@v6
  step 2 run  sh ci.sh
$ git add .github menu.md
$ git commit -q -m "Add a workflow that runs the checks"
$ git ls-files .github
.github/workflows/check.yml
```

*Recorded in Bash; `ch54-actions/expected-workflow-file.bash.txt`.*

Read the file from the top.

- `name: Check the menu` is the name shown on the Actions tab.
- `on: [push, pull_request]` lists two **events**. The outline tool prints `events: ['push', 'pull_request']`. (Chapter 53<!--ref:yaml--> warned that some YAML tools read a key called `on` as a Boolean; the outline script handles that, and GitHub's own tools read `on` as the trigger key.)
- `jobs:` holds the jobs, each under an identifier of your choice. Here there is one, `check`.
- `runs-on: ubuntu-latest` picks the **runner**, a GitHub-hosted Linux machine.
- `steps:` is a list. Step 1 uses an action, `actions/checkout@v6`, which puts a copy of your repository on the runner. Step 2 runs a command, `sh ci.sh`.

The `@v6` after the action name selects a **version** of the action. Section 54.5 and Chapter 60<!--ref:wfsec--> return to why that choice matters.

> **Checked against GitHub's documentation (R284).** The `on`, `jobs`, `runs-on`, `steps`, `uses` and `run` keys are as in the quickstart and the workflow-syntax reference: the quickstart workflow uses `on: [push]`, a job with `runs-on: ubuntu-latest`, and steps that either `run` a command or `uses` the checkout action, whose current documented form is `actions/checkout@v6`. The syntax reference says a job "contains a sequence of tasks called `steps`" that "can run commands, run setup tasks, or run an action". What GitHub does with this exact file was **not** run by hand; the outline script only shows that it parses and what it contains.

---

## 54.3 Why the first step is almost always `checkout`

A runner starts as a clean machine. Your repository is **not** on it. The step that uses the checkout action clones it, and only then can later steps run your scripts, tests or build. Forgetting it is the classic first mistake: the job starts, and `sh ci.sh` fails with "No such file".

The quickstart workflow shows the same order: it prints some information, uses the checkout action, then lists the files with `ls`.

---

## 54.4 Each step is its own process

GitHub's documentation says: "Each step runs in its own process in the runner environment and has access to the workspace and filesystem. Because steps run in their own process, changes to environment variables are not preserved between steps."

This is ordinary operating-system behaviour, and it can be reproduced with two separate shell processes. The last two lines of the recording do it:

```text
$ sh -c 'export MENU_PRICE=2.80; echo "step 1 sets MENU_PRICE=$MENU_PRICE"'
step 1 sets MENU_PRICE=2.80
$ sh -c 'echo "step 2 sees MENU_PRICE=${MENU_PRICE:-nothing}"'
step 2 sees MENU_PRICE=nothing
```

*Recorded in Bash; `ch54-actions/expected-workflow-file.bash.txt`.*

The first process sets `MENU_PRICE` and prints it. The second, a new process, does not see it: it prints `nothing`. Files, unlike environment variables, **are** shared, because all steps see the same workspace. So to pass a value between steps you write it to a file, or use the mechanism that Chapter 56<!--ref:workflows_practice--> introduces for outputs and environment variables.

> **Checked against GitHub's documentation (R285).** The quotation is from "Workflow syntax: jobs.<job_id>.steps". The recording reproduces the operating-system behaviour with `sh -c`; it does not run a GitHub step.

---

## 54.5 Reading a workflow you did not write

A method for any workflow file:

1. **Find `on`.** When does it run?
2. **Find `jobs`.** How many jobs, and do any depend on others (`needs`)?
3. **For each job, find `runs-on`.** Where does it run?
4. **Read the steps in order.** What does each `uses`, and what does each `run`?
5. **For every `uses`, look at what it is and which version it names.** An action is code that runs with access to your repository and possibly your secrets. Treat it like a dependency (Chapter 60<!--ref:wfsec-->).

---

## 54.6 A real example: this book's own workflow

The repository of this book has a workflow file, `.github/workflows/validate.yml`, that runs on every push to `main`, every pull request and on manual start. Its jobs, as they appear as checks on a pull request, are:

| Job (check name) | What it does |
|---|---|
| Structure, references, ledger, secrets | Runs the static checks (`tools/check_all.sh`) |
| Git command tests (runner's Git version) | Runs the older Git verification scripts on the runner's Git |
| Chapter command transcripts (bash and zsh) | Re-runs every recorded chapter session and compares the output |
| Chapter command transcripts on Git v2.56.0 (built from source) | Builds Git v2.56.0, then re-runs the same sessions |
| PDF edition (build and machine checks) | Builds the PDF and EPUB editions from the manuscript and checks them with machine validators |

Each job uses `ubuntu-latest`, starts with the checkout action, installs what it needs with `run` steps, and ends with the command that does the work. When a recording differs on a newer Git, that job turns red and the difference is printed in the job's log, which is exactly how the differences noted in Chapters 20<!--ref:branching-->, 27<!--ref:rebase-->, 28<!--ref:tools--> and 49<!--ref:collab--> were found. This is the CI idea of Chapter 52<!--ref:cicd--> applied to a book: the pipeline is the test of the text.

**What this shows.** A workflow is ordinary configuration in the repository; several jobs run in parallel; a job's failure appears on the pull request. **What it does not show:** how to design a workflow for your project. That is Chapter 56<!--ref:workflows_practice-->.

---

## Checkpoint

## What You Learned

- A workflow is triggered by events, contains jobs, and each job runs steps on a runner; a step runs a command or an action.
- Workflow files are YAML in `.github/workflows` with the extension `.yml` or `.yaml`.
- The checkout action puts your repository on the runner; without it, your files are not there.
- Each step is its own process: environment variables do not carry over, but files do.
- Read a workflow by finding `on`, `jobs`, `runs-on` and each step.

## New Vocabulary

**Workflow (GitHub Actions)**, **event**, **job**, **step**, **runner**, **action** (introduced above). Chapter 34<!--ref:workflows--> used *workflow* for a way of working with Git; here it means the automated process.

## Commands Learned

`python3 outline.py <workflow>` (the book's small reader for workflow structure), `sh -c '...'` (to show separate processes).

## Common Mistakes

1. **Forgetting the checkout step.**
2. **Expecting an environment variable to carry over to the next step.**
3. **A workflow file outside `.github/workflows`**, so it is never found.
4. **Indenting with a tab** (Chapter 53<!--ref:yaml-->).
5. **Using an action without knowing what it is or which version.**

## Practice

Do the exercises in [`exercises/ch54-exercises.md`](../../../exercises/ch54-exercises.md).

## Self-Test

1. Where must a workflow file be, and what extensions may it have?
2. What is the difference between a job and a step?
3. What does the checkout action do, and what happens without it?
4. Why is a variable set in one step not visible in the next?
5. Read `on: [push, pull_request]`: when does the workflow run?

## Before Moving On

You are ready for Chapter 55<!--ref:exprs--> or Chapter 56<!--ref:workflows_practice--> if you can:

- [ ] name the six parts of Actions
- [ ] read a small workflow file aloud
- [ ] explain why steps do not share variables

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The outline of the workflow file parses; two processes do not share an environment variable | Locally tested: Bash 5.2 and zsh 5.9, Python 3 with PyYAML; CI | R284, R285 (local side) |
| Concepts, file location, `name`, steps run in their own process, matrix, events | Checked against `github/docs` (commit `2eaab0b`); not run by hand on a live account | R283-R285 |
| This book's own workflow and its job names | Observed as pull-request checks while writing this book (GitHub Actions results) | R284 |
| Current form of the checkout action | The `github/docs` reusable text says `actions/checkout@v6`; the tag `v6` exists in the action's repository | R284 |

## Where this leads

Chapter 55<!--ref:exprs--> adds expressions and conditions, Chapter 56<!--ref:workflows_practice--> builds practical workflows, and Chapter 57<!--ref:wfdebug--> reads their logs.
