---
key: runners
number: 59
tag: Deep
first_read: later
status: draft
requires: [actions]
ledger: [R298, R299, R300]
---
# Chapter 59 — Self-Hosted Runners, Concurrency and Limits [Deep]

**In this chapter**

- GitHub-hosted and self-hosted runners, and what each costs you
- why self-hosted runners are a security decision
- concurrency: stopping runs from colliding, or cancelling outdated ones
- the limits of GitHub Actions (verified facts only)

> **How to read this chapter.** This is a **Deep** chapter and can be read later. Everything is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026), and one limit was checked by arithmetic on your computer. **Limits, prices and plans change often**: the numbers below are those on the page at that commit, and the chapter states only what the page states. No runner was set up and no workflow was run on a live account by hand. This book's own workflow uses the `concurrency` feature, and section 59.3 says what that showed.

**Before you start.** Chapter 54<!--ref:actions--> and Chapter 56<!--ref:workflows_practice-->. The recording ran in Bash and zsh, and was re-run in CI.

---

## 59.1 Two kinds of runner

A **runner** is the machine that runs a job (Chapter 54<!--ref:actions-->). There are two kinds.

- **GitHub-hosted runners** are machines that GitHub provides. GitHub's documentation says they "start in a clean runner image", which is why a workflow must check out the repository and download its dependencies every time (Chapter 56<!--ref:workflows_practice-->).
- **Self-hosted runners** are "a system that you deploy and manage to execute jobs from GitHub Actions on GitHub". They "give you more control of hardware, operating system, and software tools", are "free to use with GitHub Actions, though you are responsible for the cost of maintaining your runner machines", can be "physical, virtual, in a container, on-premises, or in a cloud", and "don't need to have a clean instance for every job execution". They "receive automatic updates for the self-hosted runner application only", not for your operating system: "you are responsible for updating the operating system and all other software."

Repository-level runners "are dedicated to a single repository, while organization-level runners can process jobs for multiple repositories in an organization." In a workflow, a job chooses its runner with `runs-on`.

> **New term: self-hosted runner.** A machine that you set up and maintain yourself to run GitHub Actions jobs, instead of a machine that GitHub provides.

> **Checked against GitHub's documentation (R298).** "About self-hosted runners" (the quotations above) and "Understanding GitHub Actions".

**When would you want one?** When you need hardware or software that GitHub's machines do not offer, when a job must reach a private network, or when you already own the machines. Note that "free to use" is not the same as "free": the cost moves to you.

---

## 59.2 Why self-hosted runners are a security decision

A runner executes whatever the workflow tells it to. On a GitHub-hosted runner that happens on a clean, temporary machine. On a self-hosted runner it happens on **your** machine. GitHub's documentation on secure use says:

- "Self-hosted runners for GitHub do not have guarantees around running in ephemeral clean virtual machines, and can be persistently compromised by untrusted code in a workflow."
- "As a result, self-hosted runners should almost never be used for public repositories on GitHub, because any user can open pull requests against the repository and compromise the environment."
- When a runner is defined at the organization or enterprise level, "GitHub can schedule workflows from multiple repositories onto the same runner. Consequently, a security compromise of these environments can result in a wide impact." Organising runners into separate groups helps to limit the scope.
- Think about what sensitive information is on the machine, such as private SSH keys and API tokens.
- Destroying the runner after each job is only a partial defence: "there is no way to guarantee that a self-hosted runner only runs one job", and some jobs pass secrets as command-line arguments, which another job on the same machine could see. The documentation points to **just-in-time (JIT) runners**, which "perform at most one job before being automatically removed".

> **Checked against GitHub's documentation (R299).** "Secure use reference", section on hardening self-hosted runners. Chapter 60<!--ref:wfsec--> covers workflow security more widely.

**A rule for this book's readers:** do not attach a self-hosted runner to a public repository, and treat one attached to a private repository as a machine that trusts every person who can open a pull request there.

---

## 59.3 Concurrency

By default GitHub "allows multiple jobs within the same workflow, multiple workflow runs within the same repository, and multiple workflow runs across a repository owner's account to run concurrently". That is usually fine, but not always. The documentation gives two examples of when to limit it: "prevent multiple deployments from running at the same time, or cancel linters checking outdated commits".

> **New term: concurrency group.** A name that GitHub uses to allow only one workflow run or job with that name to be running or pending at a time.

You limit concurrency with the `concurrency` key. Two settings decide what happens to a run that arrives while another in the same group is going: it can wait, or the older one can be cancelled (`cancel-in-progress`). The documentation of its newest version adds that "when you limit concurrency, by default only one run can be pending in a concurrency group; any additional pending runs cancel the previous one", and that queuing must be opted into; that sentence is marked in the documentation source as depending on a feature flag, so check the page for your account.

**This book's own workflow.** Its file has exactly this at the top:

```yaml
concurrency:
  group: validate-${{ github.ref }}
  cancel-in-progress: true
```

The group name includes the branch (`github.ref`, Chapter 55<!--ref:exprs-->), so each branch or pull request has its own group, and a new push cancels the run for the older commit. While this book was written, that is what happened when two commits were pushed a minute apart: the first run of the pair ended as *cancelled* and only the newest commit was tested. That saves time and runner minutes. The price is that you may never see the result of the older commit, which is fine for a check on a branch and would be wrong for a deployment that must finish.

> **Checked against GitHub's documentation (R300).** "Concurrency" and "Control the concurrency of workflows and jobs"; the observation about this book's workflow is from its own run history.

---

## 59.4 Limits

GitHub's page on Actions limits says: "You may be rate limited by GitHub Actions when you scale your usage. Some limits can be increased by contacting GitHub Support. Unless otherwise stated, the expected behavior when a limit is reached is that the workflow/job will get cancelled. These limits are subject to change." Some of the limits on the page at the checked commit:

| Limit | Value on that page |
|---|---|
| Workflow run time | 35 days per workflow run, including time spent waiting and on approval |
| Job execution time on GitHub-hosted runners | 6 hours |
| Job execution time on self-hosted runners | 5 days |
| Job queue time on self-hosted runners | 24 hours |
| Job matrix | 256 jobs per workflow run |
| Re-runs | 50 per workflow run |
| Workflow file size | 500 KB per file (a larger file "will not start runs") |
| Concurrent jobs, standard GitHub-hosted runners | 20 on the Free plan and 40 on the Pro plan (of which at most 5 macOS jobs) |
| Dependency cache uploads | 200 per minute per repository |

**Testing the matrix limit.** A matrix multiplies (Chapter 56<!--ref:workflows_practice-->), and the limit is easy to pass by accident. Shell arithmetic shows how:

```text
$ echo "versions 3 x systems 2 = $((3*2)) jobs"
versions 3 x systems 2 = 6 jobs
$ echo "versions 4 x systems 4 x arch 4 x options 5 = $((4*4*4*5)) jobs"
versions 4 x systems 4 x arch 4 x options 5 = 320 jobs
$ if [ $((4*4*4*5)) -gt 256 ]; then echo "over the documented limit of 256 jobs per workflow run"; fi
over the documented limit of 256 jobs per workflow run
```

*Recorded in Bash; `ch59-runners/expected-matrix-limit.bash.txt`.*

Three versions on two systems is 6 jobs. A matrix of 4 by 4 by 4 by 5 is 320 jobs, over the documented limit of 256, so a workflow like that would be cancelled or refused. The arithmetic checks the documentation's number; it does not run a matrix.

> **Checked against GitHub's documentation (R300).** "Actions limits", the source of every number in the table. The table is a selection; the page has more (for example runner registration rates and storage limits). Prices and included minutes are **not** in this chapter: they are time-sensitive and depend on your plan, so read the billing page for your account.

---

## Checkpoint

## What You Learned

- GitHub-hosted runners are clean machines that GitHub maintains; self-hosted runners are yours to secure, update and pay for.
- Self-hosted runners "should almost never be used for public repositories".
- `concurrency` with a group name limits simultaneous runs, and `cancel-in-progress` drops outdated ones.
- Actions has documented limits, including 256 jobs per matrix, 6 hours per hosted job and 35 days per run.
- Numbers on limits and plans change: check the current page.

## New Vocabulary

**Self-hosted runner**, **concurrency group** (introduced above).

## Commands Learned

Shell arithmetic `$((a*b))` (to check a matrix size).

## Common Mistakes

1. **A self-hosted runner on a public repository.**
2. **Assuming a self-hosted runner is clean for every job.**
3. **`cancel-in-progress` on a deployment.**
4. **A matrix that multiplies past the limit.**
5. **Copying a limit from an old article.**

## Practice

Do the exercises in [`exercises/ch59-exercises.md`](../../../exercises/ch59-exercises.md).

## Self-Test

1. Who updates the operating system of a self-hosted runner?
2. Why are self-hosted runners risky for public repositories?
3. What does `cancel-in-progress: true` do, and where is it a bad idea?
4. How many jobs may a matrix produce in one run?

## Before Moving On

You are ready for Chapter 60<!--ref:wfsec--> if you can:

- [ ] explain the security difference between the two kinds of runner
- [ ] write a `concurrency` block that cancels outdated runs
- [ ] say where to look up a current limit

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The matrix-size arithmetic against the documented 256-job limit | Locally tested (shell arithmetic): Bash 5.2 and zsh 5.9; CI | R300 (local side) |
| Runner types, self-hosted security guidance, concurrency, limits | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account**; limits change | R298-R300 |
| This book's own concurrency block and its effect | Observed in this repository's workflow runs | R300 |

## Where this leads

Chapter 60<!--ref:wfsec--> covers permissions, third-party actions and untrusted input, and Chapter 61<!--ref:externalci--> compares Actions with other CI systems.
