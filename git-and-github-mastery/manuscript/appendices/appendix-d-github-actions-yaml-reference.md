# Appendix D — GitHub Actions YAML Reference

A compact reference to the keys and expressions used in Chapters 54<!--ref:actions--> to 60<!--ref:wfsec-->. It is **not** the full syntax: for that, read GitHub's workflow syntax reference (the book checked the pages listed in the ledger against `github/docs` at commit `2eaab0b`). Only structure and file layout were tested locally; **no workflow was run on GitHub for this book**.

## D.1 File and top-level keys

| Key | Meaning | Chapter |
|---|---|---|
| file in `.github/workflows/NAME.yml` | one workflow per file | 54<!--ref:actions--> |
| `name` | display name | 54<!--ref:actions--> |
| `on` | the events that start the workflow | 54<!--ref:actions-->, 56<!--ref:workflows_practice--> |
| `permissions` | rights of `GITHUB_TOKEN` (set the least that works) | 60<!--ref:wfsec--> |
| `env` | environment variables for the workflow, a job or a step | 54<!--ref:actions--> |
| `concurrency` | one run per group; `cancel-in-progress` | 59<!--ref:runners--> |
| `jobs` | a map of job identifiers to jobs | 54<!--ref:actions--> |

**YAML reminders** (Chapter 53<!--ref:yaml-->): indentation with spaces, never tabs; quote strings that look like other types (`"3.10"`, `"no"`); the key `on` may be read as a boolean by some parsers, which is why some tools show `true`.

## D.2 Events (`on`)

| Event | When | Chapter |
|---|---|---|
| `push`, `pull_request` | a push, a pull request | 54<!--ref:actions--> |
| `workflow_dispatch` (with `inputs`) | started by hand | 58<!--ref:wfadvanced--> |
| `schedule` with `cron` | at set times (UTC, five fields) | 56<!--ref:workflows_practice--> |
| `workflow_call` | called by another workflow (reusable) | 58<!--ref:wfadvanced--> |
| `pull_request_target`, `workflow_run` | privileged triggers: do not check out untrusted code | 60<!--ref:wfsec--> |

## D.3 Jobs and steps

| Key | Meaning | Chapter |
|---|---|---|
| `runs-on` | the runner (for example `ubuntu-latest`) | 54<!--ref:actions-->, 59<!--ref:runners--> |
| `needs` | jobs that must finish first | 54<!--ref:actions--> |
| `if` | condition for a job or step | 55<!--ref:exprs--> |
| `strategy.matrix` | one job per combination | 56<!--ref:workflows_practice-->, 59<!--ref:runners--> |
| `timeout-minutes` | stop a job that runs too long | 59<!--ref:runners--> |
| `environment` | the deployment environment (approvals, secrets) | 58<!--ref:wfadvanced--> |
| `steps` | list of steps | 54<!--ref:actions--> |
| step `name` | label | 54<!--ref:actions--> |
| step `uses` | run an action (pin to a full commit name) | 54<!--ref:actions-->, 60<!--ref:wfsec--> |
| step `with` | inputs for the action | 54<!--ref:actions--> |
| step `run` | run a shell command | 54<!--ref:actions--> |
| step `env` | variables for that step (use for untrusted values) | 60<!--ref:wfsec--> |
| step `id` and `steps.ID.outputs.NAME` | pass values between steps | 55<!--ref:exprs--> |

## D.4 Expressions and contexts

Written `${{ ... }}`. Common contexts: `github` (for example `github.ref`, `github.ref_name`, `github.sha`, `github.event_name`), `env`, `vars`, `secrets`, `steps`, `job`, `runner`, `matrix`, `needs`, `inputs`. Functions: `contains`, `startsWith`, `format`, `join`, and status checks `success()`, `failure()`, `always()`, `cancelled()` (Chapter 55<!--ref:exprs-->).

**Danger:** `${{ }}` is pasted as text into `run:` scripts. Pass untrusted values (titles, branch names, bodies) through `env` and read them as `"$NAME"` (Chapter 60<!--ref:wfsec-->).

## D.5 Actions used in the book's examples

| Action | Use | Chapter |
|---|---|---|
| `actions/checkout` | get the code | 54<!--ref:actions--> |
| `actions/upload-artifact`, `actions/download-artifact` | keep and pass files | 54<!--ref:actions--> |
| `actions/configure-pages`, `actions/upload-pages-artifact`, `actions/deploy-pages` | publish a Pages site | 58<!--ref:wfadvanced-->, 69<!--ref:pages--> |

## D.6 A minimal, safe skeleton

```yaml
name: ci
on: [pull_request]
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<full 40-character commit name>
      - run: sh ci.sh
```

Replace the placeholder with a real commit name from the action's own repository (Chapter 60<!--ref:wfsec-->). This book's own workflow does exactly that.

## D.7 Limits and costs

Numbers such as maximum matrix size, run time and storage are in GitHub's limits page and change; Chapter 59<!--ref:runners--> gives the values as read on 29 September 2026 and says so.
