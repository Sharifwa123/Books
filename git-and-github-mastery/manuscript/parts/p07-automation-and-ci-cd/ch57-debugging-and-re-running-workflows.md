---
key: wfdebug
number: 57
tag: Core
first_read: full
status: draft
requires: [workflows_practice]
ledger: [R292, R293, R294]
---
# Chapter 57 — Debugging and Re-running Workflows [Core]

**In this chapter**

- a method for finding why a workflow failed, or never started
- reading logs, and turning on debug logging
- the usual causes: triggers, YAML, conditions, permissions
- re-running a workflow, and what a re-run uses
- skipping a run on purpose, and how Git stores that request

> **How to read this chapter.** The Git side (extra Git logging with `GIT_TRACE`, and how a skip request is stored in a commit message) was run and recorded. Statements about GitHub Actions are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026). No workflow was run on a live account by hand; the logs of this book's own workflow, read while writing it, taught the method in section 57.1.

**Before you start.** Chapter 56<!--ref:workflows_practice--> and Chapter 55<!--ref:exprs-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on newer Git versions.

---

## 57.1 A method

Most failures fall into one of four groups. Ask the questions in this order, because the earlier ones are cheaper.

1. **Did it start at all?** No run appears: the problem is the *trigger* (section 57.3).
2. **Did the file load?** A run appears, but with an error about the file: the problem is *YAML or syntax* (Chapter 53<!--ref:yaml-->).
3. **Which job or step failed, and what did it print?** Open the log, find the first red step, and read *upward* from the error: the line that failed is often not the line that caused it.
4. **Does it fail only there?** Try the same command on your own computer, in a clean copy of the repository (Chapter 52<!--ref:cicd--> made the script runnable anywhere).

**A real example.** When this book's workflow first ran the chapter transcripts, one job turned red because a recorded command needed a program (`git filter-repo`) that the runner did not have. The log showed the exact command and a Python `ModuleNotFoundError`. The fix was to install the program in an earlier step of the workflow, and then to make the recording tool, which runs with its own home folder, find it. The lesson: *the log usually names the cause*. Read the first error, not the last.

---

## 57.2 Logs

> **Checked against GitHub's documentation (R292).** "Troubleshooting workflows": "Each workflow run generates activity logs that you can view, search, and download." If the logs "do not provide enough detail to diagnose why a workflow, job, or step is not working as expected, you can enable additional debug logging." The same page also advises enabling the debug or verbose options of the tools you run, and gives Git as its example: "you can use ... `GIT_TRACE=1 GIT_CURL_VERBOSE=1 git ...` for git."

**Debug logging.** GitHub's documentation on enabling debug logging describes two switches, each set as a **secret or a variable** in the repository (with the same permissions as any secret or variable): `ACTIONS_RUNNER_DEBUG` set to `true` adds two files to the log archive, the runner process log and the worker process log (in a `runner-diagnostic-logs` folder); `ACTIONS_STEP_DEBUG` set to `true` "increases the verbosity of a job's logs during and after a job's execution". If both a secret and a variable are set, "the value of the secret takes precedence". Anyone who can run a workflow can also turn on both for a **re-run**. A step can test the `runner.debug` context to run only when debug logging is on.

**Git's own trace.** When a step fails in a `git` command, ask Git to explain itself. `GIT_TRACE=1` makes Git print the commands it runs. The recording strips the time stamps and source-line numbers, which vary, and keeps the message:

```text
$ cd bakery-menu
$ GIT_TRACE=1 git rev-parse --git-dir 2>&1 | sed -E 's/^[0-9:.]+ +[a-z.]+:[0-9]+ +//'
trace: built-in: git rev-parse --git-dir
.git
```

*Recorded in Bash; `ch57-debug/expected-skip-trace.bash.txt`.*

`trace: built-in: git rev-parse --git-dir` says which command ran. On a runner the same variable, set in the step's `env`, shows every Git command and the programs Git starts. The variable `GIT_CURL_VERBOSE=1` adds the details of web requests, which helps with a failing fetch or push. Remember that a log can print a token: read a trace before you share it (Chapter 33<!--ref:gitsec-->).

**Why did the job skip?** GitHub's documentation shows how to see how an `if` was evaluated: open the job, download the log archive, open `JOB-NAME/system.txt`, and look for the `Evaluating`, `Expanded` and `Result` lines. "The `Expanded` line shows the actual runtime values that were substituted into your `if` condition, making it clear why the expression evaluated to `true` or `false`."

---

## 57.3 The workflow never started

The documentation's checklist for triggers, in the words of this book:

- **Is the workflow disabled?** "A disabled workflow does not respond to its triggers."
- **Read the `on:` field.** Is the event you expect the one listed?
- **Some events run only from the default branch.** "Some triggering events only run from the default branch (i.e. `issues`, `schedule`). Workflow file versions that exist outside of the default branch will not trigger on these events."
- **A merge conflict stops pull-request runs.** "Workflows will not run on `pull_request` activity if the pull request has a merge conflict." Resolve the conflict (Chapter 22<!--ref:conflicts-->).
- **Filters.** Branch, tag and path filters can leave no run: "Workflow run creation will be skipped if the filter conditions apply to filter out the workflow." Path filtering "is limited to the first 3,000 files" of a diff in the current documentation; if more files changed, a workflow that depended on later files will not run.
- **A skip request in the commit message.** See section 57.5.
- **A scheduled workflow at an odd time.** Schedules "can be delayed during periods of high loads", especially at the start of an hour (Chapter 56<!--ref:workflows_practice-->).
- **A cancelled run that will not cancel.** A common cause is `always()`, which returns true even on cancellation; use `!cancelled()` instead.

> **Checked against GitHub's documentation (R293).** All quotations in this section are from "Troubleshooting workflows".

---

## 57.4 Re-running

You can re-run all the jobs of a workflow run, or only the failed ones, from the run's page or with the GitHub CLI. Two rules from the documentation matter:

- "Re-runs use the privileges of the actor who initially triggered the workflow, not the privileges of the actor who initiated the re-run. The workflow will also use the same `GITHUB_SHA` (commit SHA) and `GITHUB_REF` (git ref) of the original event that triggered the workflow run."
- "A workflow run can be re-run a maximum of 50 times."

The first rule has a Git meaning: a re-run tests **the same commit**, not the latest one. If you pushed a fix, do not re-run the old run: look for the new run that your push started, or the fix is not being tested. A re-run is right when the failure was in the environment (a network hiccup) and the commit is the one you want to test.

**A failure that goes away on a re-run is still a bug.** A check that passes on the second try is *flaky* (Chapter 52<!--ref:cicd-->). Note it, find the cause, and do not simply re-run until green.

> **Checked against GitHub's documentation (R294).** "Re-running workflows and jobs" (quotations above) and "Enabling debug logging" for the debug options on a re-run.

---

## 57.5 Skipping on purpose

Sometimes a change should not start the checks, for example a change to a comment. GitHub's documentation says workflows that would be triggered by `push` or `pull_request` "won't be triggered" if the commit message (of the push, or the head commit of a pull request) contains any of `[skip ci]`, `[ci skip]`, `[no ci]`, `[skip actions]` or `[actions skip]`. You can instead add a `skip-checks: true` trailer at the end of the message.

To Git this is just text. Here two commits ask for a skip, one in the subject and one as a trailer, and Git's own trailer tool reads the second:

```text
$ printf -- '- Rolls (six): 3.00\n' >> menu.md
$ git commit -q -am "Add rolls [skip ci]"
$ git log -1 --format=%s
Add rolls [skip ci]
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -q -am "Add tea" -m "skip-checks: true"
$ git log -1 --format=%B | git interpret-trailers --parse
skip-checks: true
$ git log --oneline
0de6891 (HEAD -> main) Add tea
785584e Add rolls [skip ci]
5224081 Add the menu
```

*Recorded in Bash; `ch57-debug/expected-skip-trace.bash.txt`.*

`git interpret-trailers --parse` lists `skip-checks: true` as a recognised trailer. Git did nothing else; it is the platform that reads the message and decides not to start a run.

> **⚠️ CAUTION.** A skipped check is a check that did not run. The documentation notes that when a workflow is skipped this way, or by path or branch filtering, the checks "will remain in a 'Pending' state", and a pull request that requires those checks can be blocked from merging. Use a skip request only when you are sure, and never on a change that reaches production.

---

## Checkpoint

## What You Learned

- Ask in order: did it start, did the file load, which step failed, does it fail elsewhere?
- Logs can be searched and downloaded; `ACTIONS_STEP_DEBUG` and `ACTIONS_RUNNER_DEBUG` add detail; `GIT_TRACE=1` explains a failing Git command.
- A workflow may not start because it is disabled, on the wrong branch or event, blocked by a merge conflict, filtered out, or skipped by the commit message.
- A re-run uses the same commit and the same privileges as the original run, and is limited to 50.
- `[skip ci]` and a `skip-checks: true` trailer are plain text in a commit message that the platform reads.

## New Vocabulary

None: this chapter uses the terms *workflow*, *job*, *step* and *log* from earlier chapters.

## Commands Learned

`GIT_TRACE=1 git ...`, `git interpret-trailers --parse`.

## Common Mistakes

1. **Reading the last error instead of the first.**
2. **Re-running an old run after pushing a fix.**
3. **Re-running until green** instead of finding a flaky cause.
4. **Sharing a trace or log that contains a token.**
5. **Skipping the checks on a change that matters.**

## Practice

Do the exercises in [`exercises/ch57-exercises.md`](../../../exercises/ch57-exercises.md).

## Self-Test

1. Which question in the method comes first, and why?
2. Name two switches that add debug detail and what each adds.
3. Give three reasons a workflow may not start.
4. Which commit does a re-run test?
5. How does a `skip-checks` trailer look to Git?

## Before Moving On

You are ready for Chapter 58<!--ref:wfadvanced--> if you can:

- [ ] follow the four-question method
- [ ] name where to find the reason an `if` was true or false
- [ ] say what a re-run uses

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `GIT_TRACE` output and `git interpret-trailers --parse` on a `skip-checks` trailer | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R294 (Git side) |
| Logs, debug secrets and variables, trigger checklist, re-run rules, skip strings | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R292-R294 |
| The "real example" of the missing program | Observed in this book's own workflow run while writing it | R292 |

## Where this leads

Chapter 58<!--ref:wfadvanced--> covers reusable workflows and environments; Chapter 60<!--ref:wfsec--> covers what workflows should never be allowed to do.
