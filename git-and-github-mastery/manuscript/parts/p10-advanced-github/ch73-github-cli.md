---
key: ghcli
number: 73
tag: Deep
first_read: later
status: draft
requires: [ghauth, terminal, pr]
ledger: [R339, R340]
---
# Chapter 73 — GitHub CLI [Deep]

**In this chapter**

- what `gh` is, and how it differs from `git`
- installing it and checking what you installed
- the commands that need no account, run and recorded
- the commands that need one, from GitHub's documentation
- authentication in scripts and workflows, and the CLI's telemetry

> **How to read this chapter.** This is a **Deep** chapter and can be read later. The commands in section 73.3 were run with **GitHub CLI 2.102.0** (released 30 September 2026), downloaded from the official release page and checked against its published checksum, in Bash and zsh, and re-run in CI with the same pinned version. **Commands that talk to GitHub (`gh pr list` with a login, `gh repo create`, `gh issue create` and others) were not run**, because that needs an authenticated account (a step the book's author has not yet done on a live account); they are described from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026). Output wording of a tool changes between versions: expect differences from what you see.

**Before you start.** Chapter 38<!--ref:ghauth--> (signing in), Chapter 7<!--ref:terminal--> and Chapter 45<!--ref:pr-->.

---

## 73.1 Two tools with similar names

GitHub's documentation gives the difference directly:

- "The Git command line interface (`git`) allows you to work with a local or remote Git repository. The remote repository may be hosted on GitHub or it may be hosted by another service."
- "GitHub CLI (`gh`) is specifically for working with GitHub." It lets you use the command line "to interact with GitHub in all sorts of ways", and "makes it easier for you to create scripts to automate GitHub operations".

The rule of thumb: **`git` works on your repository and its history; `gh` works on the things that GitHub adds** (Chapter 36<!--ref:whatgh-->): pull requests, issues, releases, workflow runs, codespaces, repository settings. `gh` is not a replacement for Git: it uses Git underneath for some tasks, and you still commit and push with `git`.

| To do this | Use |
|---|---|
| commit, branch, merge, rebase, push | `git` |
| open, list, review or merge a pull request | `gh pr` (or the web interface) |
| create or view an issue | `gh issue` |
| create a release from a tag (Chapter 66<!--ref:releases-->) | `gh release` |
| list, watch or re-run a workflow run (Chapter 57<!--ref:wfdebug-->) | `gh run`, `gh workflow` |
| manage codespaces (Chapter 70<!--ref:codespaces-->) | `gh codespace` |

---

## 73.2 Installing and checking

`gh` is a separate program. The documentation says how to install it for each system on its pages; this book does not repeat the steps, because they change and depend on your system. Two habits from earlier chapters apply:

- **Get it from an official source** (Chapter 13<!--ref:install-->) and, if you download a file, **check its checksum** (Chapter 63<!--ref:secpractice-->). The version used for this chapter was downloaded from the project's release page on GitHub; the file's SHA-256 matched the value in the release's published checksum list, and the CI job checks it again against a value written in the workflow file.
- **Check what you have**: `gh --version` prints the version and the release page. A very old `gh` may lack commands described here.

Ask `gh` for help with `gh` alone (a list of top-level commands) and add `--help` to any command: `gh issue --help`, `gh issue create --help`. The documentation names the top-level areas `issue`, `pr`, `repo` and others.

---

## 73.3 Commands that need no account

Several `gh` commands only read or write local settings, and the ones that need GitHub tell you so. The first recording makes a shortcut, a setting, and asks about the login state:

```text
$ gh alias set prd "pr create --draft"
- Creating alias for prd: pr create --draft
✓ Added alias prd
$ gh alias list | grep prd
prd: pr create --draft
$ gh config set editor "code -w"
$ gh config get editor
code -w
$ gh auth status || echo "not logged in (exit status $?)"
You are not logged into any GitHub hosts. To log in, run: gh auth login
not logged in (exit status 1)
```

*Recorded in Bash; `ch73-ghcli/expected-offline.bash.txt`.*

- `gh alias set` created an **alias**, a short name for a longer command. The documentation's example is the same: `gh alias set prd "pr create --draft"` and then `gh prd` opens a draft pull request. `gh alias list` shows aliases; here `grep` picks the one we made because the list also contains defaults.
- `gh config set editor ...` stored the editor that `gh` opens when it needs you to write text (the documentation's example is `gh config set editor "code -w"`, where `-w` makes the command wait until you close the file), and `gh config get editor` read it back. These settings are files in your home folder; Chapter 14<!--ref:config--> did the same for Git.
- `gh auth status` reported "You are not logged into any GitHub hosts" and **exited with status 1**. In a script, that exit status is how you detect it.

Next, the same tool in a Git repository with no remote asks for something that needs GitHub:

```text
$ git init -q project && cd project
$ gh pr list || echo "gh needs authentication (exit status $?)"
To get started with GitHub CLI, please run:  gh auth login
Alternatively, populate the GH_TOKEN environment variable with a GitHub API authentication token.
gh needs authentication (exit status 4)
```

*Recorded in Bash; `ch73-ghcli/expected-offline.bash.txt`.*

It did not guess: it said `gh auth login` and offered the other route, an environment variable named `GH_TOKEN`, and exited with status 4. **What `gh pr list` prints when you are logged in was not run.**

---

## 73.4 Commands that need an account

These are from GitHub's quickstart for the CLI and were **not run** for this book. When you first use some of them you may be asked to add scopes to your token; the documentation says to follow the on-screen instructions.

| Command | What the documentation says it does |
|---|---|
| `gh auth login` | signs in (interactive) |
| `gh status` | shows your current work on GitHub across the repositories you are subscribed to |
| `gh repo view OWNER/REPO` | shows the description and README; `--web` opens the browser; inside a clone you can omit the name |
| `gh repo clone OWNER/REPO` | clones a repository |
| `gh repo create` | creates a repository, and can push an existing local one |
| `gh issue list --repo OWNER/REPO` | lists recent open issues |
| `gh pr list --repo OWNER/REPO`, `gh pr list --label NAME` | lists open pull requests |
| `gh search prs --review-requested=@me --state=open` | lists pull requests you were asked to review |
| `gh pr create` | creates a pull request, following the prompts |
| `gh release create TAG` | creates a release (Chapter 66<!--ref:releases-->) |
| `gh run rerun RUN_ID`, `--failed`, `--debug`, `gh run watch` | re-run or follow workflow runs (Chapter 57<!--ref:wfdebug-->) |
| `gh codespace create`, `gh codespace list` | manage codespaces (`cs` is accepted for `codespace`) |
| `gh auth switch` | switch between accounts on the same host |

The documentation adds that `gh` can be extended with **extensions**, installed from other people. An extension is code written by someone else that runs with your credentials: apply Chapter 60<!--ref:wfsec-->'s thinking (who wrote it, do you trust it) before installing one.

> **Checked against GitHub's documentation (R339).** "About GitHub CLI" and "GitHub CLI quickstart". The commands in the table were not executed.

---

## 73.5 Authentication in scripts and workflows

Interactive login suits a person. For automation, the documentation describes passing a token in an **environment variable**: "Instead of using the `gh auth login` command, pass an access token as an environment variable called `GH_TOKEN`. GitHub recommends that you use the built-in `GITHUB_TOKEN` instead of creating a token." In a workflow you write `GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}` in the step's `env` (Chapter 54<!--ref:actions-->), and give the workflow's token only the permissions the command needs (Chapter 60<!--ref:wfsec-->). If you must create a token, "store your token as a secret".

The recording above showed the same door from the other side: without a login and without `GH_TOKEN`, `gh` refuses.

---

## 73.6 Telemetry: what the tool reports

GitHub's documentation has a page on **telemetry**: the CLI collects usage data. It says telemetry "is not collected when the target is GitHub Enterprise Server", that the tool is open source, and that you can see what would be sent. Setting the environment variable `GH_TELEMETRY=log`, or `gh config set telemetry log`, prints "the JSON payload that would normally be sent ... to stderr instead". To opt out, set `GH_TELEMETRY=false` (any falsy value), or `DO_NOT_TRACK=true`, or `gh config set telemetry disabled`; "the environment variables take precedence over the configuration value". Extensions "may collect their own usage data and are not controlled by opting out".

The last recording lines run both modes, with the output cut to two fields so that random identifiers and times do not appear:

```text
$ GH_TELEMETRY=log gh config get editor 2>&1 | grep -E '"(type|command)"'
      "type": "command_invocation",
        "command": "gh config get",
$ GH_TELEMETRY=false gh config get editor 2>&1 | grep -c "Telemetry payload" || true
0
```

*Recorded in Bash; `ch73-ghcli/expected-offline.bash.txt`.*

In log mode the payload named the event type (`command_invocation`) and the command (`gh config get`); with `GH_TELEMETRY=false` no payload was printed (the count is 0). A full payload contains more fields, such as the version and operating system and identifiers; **read your own with `GH_TELEMETRY=log`**. This book does not judge the policy. It tells you that the setting exists, and it is your decision.

> **Checked against GitHub's documentation (R340) and locally tested.** "GitHub CLI telemetry" (behaviour), and the recording (log and disabled modes on version 2.102.0).

---

## 73.7 `gh` in your habits

1. **Use it for what GitHub adds**: pull requests, issues, releases, runs.
2. **Keep the browser** for reading long discussions and reviews.
3. **Script carefully**: check the exit status; never print a token; prefer `GITHUB_TOKEN` in workflows.
4. **Put common commands under aliases**, and keep them in your own configuration.
5. **Check `--help`** rather than trusting a book's flags: they change.

---

## Checkpoint

## What You Learned

- `git` works on repositories; `gh` works on GitHub's additions and uses your login.
- `gh alias`, `gh config` and `gh auth status` work without an account; other commands ask you to log in or set `GH_TOKEN`.
- Exit status tells scripts what happened: 1 for not logged in, 4 for authentication needed (in this version).
- In workflows pass `GITHUB_TOKEN` as `GH_TOKEN`, with least privilege.
- `gh` has telemetry that can be inspected (`GH_TELEMETRY=log`) and disabled.

## New Vocabulary

**GitHub CLI**, **alias**, **telemetry** (see the glossary).

## Commands Learned

`gh alias set`, `gh alias list`, `gh config set`, `gh config get`, `gh auth status`, `gh pr list`, `gh --help`.

## Common Mistakes

1. **Thinking `gh` replaces `git`.**
2. **Pasting a token into a command line or a script.**
3. **Installing extensions without looking at them.**
4. **Assuming output and flags are the same in every version.**
5. **Ignoring exit statuses in scripts.**

## Practice

Do the exercises in [`exercises/ch73-exercises.md`](../../../exercises/ch73-exercises.md).

## Self-Test

1. What is the difference between `git` and `gh`?
2. Which exit status did `gh auth status` return when not logged in?
3. How does a workflow authenticate `gh`?
4. How can you see what `gh` telemetry would send?
5. Why be careful with extensions?

## Before Moving On

You are ready for Chapter 74<!--ref:api--> if you can:

- [ ] say when to use `gh` rather than `git`
- [ ] create an alias and read a setting
- [ ] describe token authentication for scripts

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Alias, config, unauthenticated behaviour and exit statuses; telemetry log and disabled modes | Locally tested with `gh` 2.102.0 (checksum-verified download), Bash 5.2, zsh 5.9; CI with the same pinned version | R339, R340 (local side) |
| What `gh` is; commands that need a login; `GH_TOKEN`; extensions; telemetry statements | Checked against `github/docs` (commit `2eaab0b`); commands that need an account **not run** | R339, R340 |

## Where this leads

Chapter 74<!--ref:api--> goes one level down: the REST API, webhooks and apps, which `gh api` and your scripts use.
