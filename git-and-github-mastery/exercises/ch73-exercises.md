# Chapter 73 exercises — GitHub CLI

Attempt each exercise before you open `solutions/ch73-solutions.md`. Exercises 2.1 to 2.2 need `gh` installed but no account. **No exercise asks you to paste a token anywhere.**

## Level 1 — Guided

**1.1 Two tools.** Complete: `git` works on ______; `gh` works on ______. Give two examples for each.

**1.2 Version.** Which command shows the `gh` version, and why does the version matter?

## Level 2 — Partially guided

**2.1 An alias.** Create an alias named `prd` for `pr create --draft`, then list your aliases and find it. Then delete it with `gh alias delete prd`.

**2.2 A setting.** Set your editor for `gh` to `code -w` (or another editor you have) and read it back. What does `-w` do?

## Level 3 — Independent

**3.1 A status check.** Write a shell snippet that runs `gh auth status` and prints "ready" or "please log in" according to its exit status.

**3.2 Telemetry.** Show, with `GH_TELEMETRY=log`, the event type of a command of your choice. Then show how you would disable telemetry with an environment variable and with a configuration setting.

## Level 4 — Professional scenario

**4.1 A workflow step.** Describe (words or YAML) a workflow step that runs `gh run list` or another `gh` command using `GITHUB_TOKEN`. Which permission would you restrict, and why?

## Level 5 — Troubleshooting

**5.1** `gh pr list` in a script prints "To get started with GitHub CLI, please run: gh auth login" and stops. Give two ways to give the script credentials, and say which one you prefer for a workflow.

**5.2** A colleague's `gh` says a command does not exist. Give two likely reasons.
