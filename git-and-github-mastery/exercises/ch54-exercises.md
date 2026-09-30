# Chapter 54 exercises — GitHub Actions Fundamentals

Attempt each exercise before you open `solutions/ch54-solutions.md`. Exercises 1 to 3 need only your computer (Python 3 with PyYAML); 5 needs a repository where you may add files.

## Level 1 — Guided

**1.1 Six words.** Write one sentence for each of workflow, event, job, step, runner and action.

**1.2 A file.** In `bakery-menu`, create `.github/workflows/check.yml` with the workflow of section 54.2 (it may name the checkout action `actions/checkout@v6`). Commit it.

## Level 2 — Partially guided

**2.1 Read it.** Write a small Python script that parses the file with PyYAML and prints the workflow name, its events, and each job with its steps. Remember that PyYAML may read the key `on` as `True`.

**2.2 Two processes.** Run `sh -c 'export A=1; echo $A'` and then `sh -c 'echo ${A:-nothing}'`. Explain what this shows about steps.

## Level 3 — Independent

**3.1 A second job.** Add a job `lint` to the workflow that runs a lint script, with no dependency on `check`. Will the two jobs run in sequence or in parallel, by default?

**3.2 A dependency.** Read the documentation of `needs` (or ask your teacher) and make `deploy` wait for `check`. Explain what "wait" means.

## Level 4 — Professional scenario

**4.1 Read a real one.** Find a workflow in a public repository you like. Following the method of section 54.5, write down: the events, the jobs, the runner of each job, and every action used with its version. Say which action you trust least and why.

## Level 5 — Troubleshooting

**5.1** A workflow starts, but its first `run` step fails with "No such file: ci.sh". The file is in the repository. What is missing?

**5.2** A step sets `export VERSION=2` and the next step prints an empty value. Explain, and name two ways to carry a value between steps.

**5.3** A learner saved the workflow as `workflows/check.yml` in the repository root and nothing happens. Explain.
