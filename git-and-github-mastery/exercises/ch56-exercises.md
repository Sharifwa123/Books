# Chapter 56 exercises — Practical Workflows

Attempt each exercise before you open `solutions/ch56-solutions.md`. Exercises 1 to 3 need only your computer. Exercise 5 needs a repository where you may add workflows.

## Level 1 — Guided

**1.1 Expand a matrix.** With shell loops, expand a matrix with `version: [10, 12, 14]` and `os: [ubuntu-latest, windows-latest]`. How many combinations are there?

**1.2 Read a cron.** For `2,10 4,5 * * *`, say in words when it runs.

## Level 2 — Partially guided

**2.1 Step values.** For `*/20 * * * *` and `20/15 * * * *`, list the minutes. Check your answer with a small script.

**2.2 Another matrix.** How many jobs does a matrix with `python: [3.10, 3.11, 3.12]`, `os: [ubuntu-latest, macos-latest]` and `arch: [x64, arm64]` create? Why should you be careful with matrices?

## Level 3 — Independent

**3.1 A pull request workflow.** Write a workflow that runs `sh ci.sh` on every pull request. Then add a second job `lint` that runs in parallel.

**3.2 Pass a value.** Write two steps: the first stores `PRICE=2.80` in `$GITHUB_ENV`, the second prints it. Explain why the value survives although steps are separate processes.

## Level 4 — Professional scenario

**4.1 A weekly report.** Design a scheduled workflow that files an issue every Monday morning with the number of open pull requests. Choose a cron expression that avoids the start of the hour, and list the permissions it needs.

## Level 5 — Troubleshooting

**5.1** A workflow works on branches of the repository but the secret is empty when a contributor opens a pull request from a fork. Explain.

**5.2** A scheduled workflow in a public repository stopped running after a quiet summer. Why, and how is it reactivated?

**5.3** A cache step restores a file that turns out to contain a malicious script. Which documented risk is this, and what does GitHub do to limit it?
