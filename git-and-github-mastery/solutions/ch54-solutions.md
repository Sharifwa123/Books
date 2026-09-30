# Chapter 54 solutions

## Level 1
**1.1** Workflow: an automated process defined in a YAML file. Event: something that starts it. Job: steps that run on one runner. Step: a command or an action. Runner: the machine that runs a job. Action: a reusable piece of code used by a step.

**1.2** The file must be in `.github/workflows/`.

## Level 2
**2.1** For example: `d = yaml.safe_load(open(path)); on = d.get("on", d.get(True))` then loop over `d["jobs"].items()`.

**2.2** The second process prints `nothing`: environment variables do not carry over between processes, so they do not carry over between steps.

## Level 3
**3.1** In parallel: by default jobs have no dependencies and run in parallel.

**3.2** Adding `needs: check` to the `deploy` job makes it wait until `check` has finished (and, by default, succeeded) before starting.

## Level 4
**4.1** Answers vary. Look for actions with unpinned or floating versions and unfamiliar publishers.

## Level 5
**5.1** The checkout step: a runner starts clean, so the repository is not there until an action such as `actions/checkout` puts it there.

**5.2** Steps are separate processes. Carry a value in a file in the workspace, or with the mechanism for step outputs and environment files (Chapter 56<!--ref:workflows_practice-->).

**5.3** Workflow files must be in `.github/workflows` (with a leading dot) in the repository; `workflows/check.yml` at the root is not discovered.
