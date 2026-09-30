---
key: exprs
number: 55
tag: Deep
first_read: later
status: draft
requires: [actions]
ledger: [R286, R287]
---
# Chapter 55 — Expressions, Contexts and Conditionals [Deep]

**In this chapter**

- what `${{ }}` does
- contexts: the information a workflow can read
- `if` conditions, comparison rules and status functions
- the Git values behind `github.ref`, `github.ref_name` and `github.sha`

> **How to read this chapter.** This is a **Deep** chapter and can be read later. The Git values behind the `github` context were run and recorded. Everything about expressions is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026). No workflow was run on a live account, so no evaluation result of GitHub's engine is claimed beyond what the documentation says.

**Before you start.** Chapter 54<!--ref:actions-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI.

---

## 55.1 Expressions

A workflow file is mostly fixed text, but some parts must be worked out at run time: which branch triggered the run, whether a previous step succeeded, which operating system the runner has. An **expression** is a small formula that GitHub evaluates. You write it between `${{` and `}}`.

> **New term: expression.** A small formula, written between `${{` and `}}` in a workflow, that GitHub evaluates while it prepares or runs the workflow, using values, operators, functions and contexts.

Example, from GitHub's documentation: `myString: ${{ 'It''s open source!' }}` produces the text *It's open source!*. Inside an expression, a text value uses **single quotes**; the documentation says "wrapping with double quotes will throw an error", and a literal single quote is written as two single quotes.

> **Checked against GitHub's documentation (R286).** "Evaluate expressions in workflows and actions": the data types are boolean (`true`, `false`), null, number ("any number format supported by JSON") and string. In conditionals, "falsy values (`false`, `0`, `-0`, `""`, `''`, `null`) are coerced to `false` and truthy ... to `true`". The operators are grouping `( )`, index `[ ]`, property `.`, not `!`, the comparisons `<`, `<=`, `>`, `>=`, `==`, `!=`, and `&&` and `||`.

**Comparison surprises.** The documentation lists rules that beginners do not expect:

- "GitHub ignores case when comparing strings." So `'Main' == 'main'` is true.
- "GitHub performs loose equality comparisons": when the types differ, values are turned into numbers: null becomes 0, `true` 1 and `false` 0, and a string is parsed as a number, or becomes `NaN` (empty string is 0).
- "When `NaN` is one of the operands of any relational comparison, the result is always `false`."
- "Objects and arrays are only considered equal when they are the same instance."
- A step output such as `steps.<id>.outputs.<name>` "evaluates as a string": to compare it as a number, convert it with `fromJSON()`.

---

## 55.2 Contexts

> **New term: context.** A named collection of information that a workflow can read in an expression, such as the `github` context (about the run) or the `runner` context (about the machine).

The documentation's table of contexts:

| Context | It holds |
|---|---|
| `github` | Information about the workflow run |
| `env` | Variables set in a workflow, job or step |
| `vars` | Variables set at the repository, organisation or environment level |
| `job` | Information about the current job |
| `steps` | Information about the steps that have run in the current job |
| `runner` | Information about the machine running the job |
| `secrets` | The names and values of secrets available to the run (Chapter 56<!--ref:workflows_practice-->) |
| `strategy`, `matrix` | The matrix (many runs of one job) |
| `needs` | Outputs of the jobs this job depends on |
| `inputs` | Inputs of a reusable or manually started workflow |
| `jobs` | Outputs of jobs, for reusable workflows only |

You read a context with `github.sha` (property syntax) or `github['sha']` (index syntax). Property syntax needs the name to start with a letter or `_`. "If you attempt to dereference a nonexistent property, it will evaluate to an empty string": a misspelt name does not fail, it silently gives nothing.

**Contexts are not environment variables.** GitHub separates them: default environment variables "exist only on the runner that is executing your job", while most contexts can be used "at any point in your workflow", including *before* the job is sent to a runner. That is what lets an `if` decide whether a job runs at all.

> **Checked against GitHub's documentation (R287).** "Contexts": the table, the two syntaxes, the empty-string rule, and the contexts-versus-variables distinction. Which contexts are available at which place in a workflow is a further table ("Context availability") and is not reproduced here.

---

## 55.3 The Git values inside `github`

Three properties of the `github` context are plain Git ideas. The documentation says:

- `github.ref`: "the fully-formed ref of the branch or tag that triggered the workflow run", in the format `refs/heads/<branch_name>` for branches (and `refs/tags/<tag_name>` for tags); for a workflow triggered by `push` "this is the branch or tag ref that was pushed".
- `github.ref_name`: "the short ref name of the branch or tag", which "matches the branch or tag name shown on GitHub".
- `github.sha`: "the commit SHA that triggered the workflow", whose value depends on the event.

You can see the same three values in any repository with Git (Chapter 30<!--ref:objects--> explained refs):

```text
$ cd bakery-menu
$ git symbolic-ref HEAD
refs/heads/feature-tea
$ git rev-parse --abbrev-ref HEAD
feature-tea
$ git rev-parse HEAD
52240815e6798c7aa39dc658ac7faf9ea4b9b3c2
$ git rev-parse --symbolic-full-name v1.0
refs/tags/v1.0
$ git rev-parse --abbrev-ref v1.0
v1.0
$ git for-each-ref --format='%(refname)'
refs/heads/feature-tea
refs/heads/main
refs/tags/v1.0
```

*Recorded in Bash; `ch55-exprs/expected-github-refs.bash.txt`.*

`git symbolic-ref HEAD` gives the **full ref** of the current branch, `refs/heads/feature-tea`, the shape of `github.ref`. The abbreviated form, `feature-tea`, is the shape of `github.ref_name`. `git rev-parse HEAD` is the commit SHA. For the tag, the full name is `refs/tags/v1.0` and the short one `v1.0`. `git for-each-ref` lists every ref in the full form.

So a condition like `github.ref == 'refs/heads/main'` (the documentation's own example) asks: "did this run come from the branch `main`?" The full form matters: comparing `github.ref` with `'main'` would never be true.

---

## 55.4 Conditions with `if`

An `if` key decides whether a job or a step runs. GitHub's example, in the documentation's contexts page:

```yaml
jobs:
  prod-check:
    if: ${{ github.ref == 'refs/heads/main' }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying to production server on branch $GITHUB_REF"
```

The documentation explains that the `if` "is processed by GitHub Actions, and the job is only sent to the runner if the result is `true`". Once the job runs, the shell sees the **default environment variable** `$GITHUB_REF`, not the context.

**Status functions.** In an `if`, four functions look at how the job is going:

| Function | Returns true when |
|---|---|
| `success()` | all previous steps have succeeded (this is the default check, applied unless you use another status function) |
| `failure()` | any previous step of the job failed (for chained jobs, if any ancestor job failed) |
| `cancelled()` | the workflow was cancelled |
| `always()` | always, "even when canceled" |

The documentation warns: "Avoid using `always` for any task that could suffer from a critical failure, for example: getting sources, otherwise the workflow may hang until it times out", and recommends `if: ${{ !cancelled() }}` to run a step whatever its success or failure.

> **Checked against GitHub's documentation (R287).** The status functions, the default `success()` check, and the warning about `always()`, are from "Evaluate expressions in workflows and actions".

---

## 55.5 Functions

The documentation lists built-in functions: `contains`, `startsWith`, `endsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles` and `case`. Two are worth knowing early: `contains('Hello world', 'llo')` tests for a substring (case is ignored), and `fromJSON` turns text into a number or object, which is how you compare a step's output as a number. Chapter 56<!--ref:workflows_practice--> uses them.

---

## Checkpoint

## What You Learned

- `${{ }}` marks an expression that GitHub evaluates; text inside uses single quotes.
- Comparisons ignore string case and coerce types loosely; a misspelt context property gives an empty string.
- Contexts (`github`, `env`, `steps`, `secrets`, `needs`, `matrix`, and others) are information; default environment variables exist only on the runner.
- `github.ref` is the full ref (`refs/heads/main`), `github.ref_name` the short name, `github.sha` the commit.
- `if` decides whether a job or step runs; `success()`, `failure()`, `cancelled()` and `always()` look at status.

## New Vocabulary

**Expression**, **context** (introduced above).

## Commands Learned

`git symbolic-ref HEAD`, `git rev-parse --abbrev-ref`, `git rev-parse --symbolic-full-name`, `git for-each-ref`.

## Common Mistakes

1. **Double quotes inside an expression.**
2. **Comparing `github.ref` with a short name.**
3. **A misspelt context property**, which silently gives an empty string.
4. **Using `always()` on a step that fetches the code.**
5. **Comparing a step output as a number without `fromJSON`.**

## Practice

Do the exercises in [`exercises/ch55-exercises.md`](../../../exercises/ch55-exercises.md).

## Self-Test

1. What is the difference between `github.ref` and `github.ref_name`?
2. Why does `'Main' == 'main'` evaluate to true?
3. What is the default status check of an `if`?
4. Why is a context available before a job reaches a runner, while `$GITHUB_REF` is not?

## Before Moving On

You are ready for Chapter 56<!--ref:workflows_practice--> if you can:

- [ ] read an `if` condition aloud
- [ ] name the Git command that gives each `github` value
- [ ] say what the four status functions mean

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The Git commands that give the ref forms and the commit SHA | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R287 (Git side) |
| Expression syntax, literals, operators, comparison rules, functions, status functions | Checked against `github/docs` (commit `2eaab0b`); **not evaluated** by GitHub's engine here | R286 |
| Contexts, syntaxes, contexts vs variables, `github.ref`, `github.sha` | Checked against `github/docs` | R287 |

## Where this leads

Chapter 56<!--ref:workflows_practice--> uses expressions in practical workflows, and Chapter 57<!--ref:wfdebug--> shows how to find out why an `if` did not do what you expected.
