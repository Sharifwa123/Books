---
key: wfsec
number: 60
tag: Core
first_read: part
status: draft
requires: [workflows_practice, gitsec]
ledger: [R301, R302, R303, R304]
---
# Chapter 60 — Securing Workflows [Core]

**In this chapter**

- why a workflow is privileged code, and what that means for secrets and the token
- least privilege for `GITHUB_TOKEN`
- third-party actions and pinning to a commit
- script injection: how a pull request title can run commands, reproduced safely
- untrusted pull requests, and the idea of OpenID Connect

> **How to read this chapter.** The script-injection example from GitHub's documentation was **reproduced with shell scripts** and recorded, without any workflow or GitHub account. Everything else is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026). No workflow was run on a live account by hand. This book's own workflow is used as a small real example of the settings discussed.

**Before you start.** Chapter 56<!--ref:workflows_practice--> and Chapter 33<!--ref:gitsec-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI.

---

## 60.1 A workflow is code that runs with your credentials

A workflow runs commands on a machine, often with access to secrets and to a token that can write to your repository. If someone can make it run **their** commands, they act with your authority. GitHub's documentation, on the risk of a compromised action: it "would have access to all secrets configured on your repository, and may be able to use the `GITHUB_TOKEN` to write to the repository". So the guiding principles are the ones of Chapter 33<!--ref:gitsec-->: **least privilege**, **do not trust input**, and **know what you run**.

---

## 60.2 Least privilege for the token

Every workflow run gets a temporary token, `GITHUB_TOKEN`. GitHub's documentation on secure use says:

- "Any user with write access to your repository has read access to all secrets configured in your repository. Therefore, you should ensure that the credentials being used within workflows have the least privileges required."
- "It's good security practice to set the default permission for the `GITHUB_TOKEN` to read access only for repository contents. The permissions can then be increased, as required, for individual jobs within the workflow file."

You set the token's permissions in the workflow with the `permissions` key. It can be at the top, for all jobs; the documentation's example is `permissions: read-all`, and a workflow can list individual scopes. The permissions "are initially set to the default setting for the enterprise, organization, or repository". For workflows from forks, "you can use the `permissions` key to add and remove read permissions ... but typically you can't grant write access".

**This book's workflow.** Its file starts with:

```yaml
permissions:
  contents: read
```

The book's checks only read the repository, so they ask for nothing more. If a step were compromised, it could not push to the repository with that token.

> **Checked against GitHub's documentation (R301).** "Secure use reference" and the `permissions` section of "Workflow syntax". The list of available permission scopes is in the documentation and is not reproduced here.

**Secrets, again.** Chapter 56<!--ref:workflows_practice--> listed the rules. Two more from the security page: "because there are multiple ways a secret value can be transformed, automatic redaction is not guaranteed", and if an unredacted secret reaches a log, "you should delete the log and rotate the secret". Do not put a secret inside structured data such as a JSON blob: redaction "largely relies on finding an exact match". Register any value derived from a secret (a Base64 copy, a signed token) as a secret too.

---

## 60.3 Third-party actions: pin them

Each `uses:` line runs someone else's code (Chapter 54<!--ref:actions-->). GitHub's documentation lists what to do:

- **Pin actions to a full-length commit SHA.** "Pinning an action to a full-length commit SHA is currently the only way to use an action as an immutable release." The reason: a tag can be moved to different code later, but a commit name cannot, because "they would need to generate a SHA-1 collision for a valid Git object payload" (Chapter 30<!--ref:objects--> explained why the hash identifies the content). "You should verify it is from the action's repository and not a repository fork."
- **Audit the source code** of the action: check "that secrets are not sent to unintended hosts, or are not inadvertently logged".
- **Pin to a tag only if you trust the creator.**

GitHub offers policies to require SHA pinning at the repository and organisation level, and Dependabot can keep actions up to date (Chapter 62<!--ref:ghsec-->).

**This book's workflow does it.** Its `uses:` lines look like this:

```yaml
- uses: actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803 # v6
```

The 40-character name is the commit that the `v6` tag pointed to when it was written, read from the action's own repository; the comment records which tag that was, so a human can find the next update.

> **Checked against GitHub's documentation (R302).** "Secure use reference", section "Using third-party actions".

---

## 60.4 Script injection

A workflow's `run:` step is a shell script. Before the shell sees it, GitHub replaces every `${{ ... }}` expression with its value, as **text**. If the value comes from a stranger, the stranger's text becomes part of your script.

GitHub's documentation gives the classic example, a step that checks a pull request title:

```yaml
- name: Check PR title
  run: |
    title="${{ github.event.pull_request.title }}"
    if [[ $title =~ ^octocat ]]; then
      echo "PR title starts with 'octocat'"
```

"To inject commands into this workflow, the attacker could create a pull request with a title of `a"; ls $GITHUB_WORKSPACE"`." The title closes the quotation, ends the command with a semicolon and adds a command of its own.

Here is the same mechanism with no workflow at all. A shell variable holds a hostile title. Two scripts are written: the first builds itself by pasting the title into its text (what the substitution does), the second receives the title as an **environment variable** and does not paste it:

```text
$ title='a"; echo INJECTED-COMMAND-RAN; #'
$ echo "$title"
a"; echo INJECTED-COMMAND-RAN; #
$ printf 'title="%s"\necho "checking: $title"\n' "$title" > vulnerable.sh
$ cat vulnerable.sh
title="a"; echo INJECTED-COMMAND-RAN; #"
echo "checking: $title"
$ sh vulnerable.sh
INJECTED-COMMAND-RAN
checking: a
$ printf 'echo "checking: $TITLE"\n' > safe.sh
$ cat safe.sh
echo "checking: $TITLE"
$ TITLE="$title" sh safe.sh
checking: a"; echo INJECTED-COMMAND-RAN; #
```

*Recorded in Bash; `ch60-wfsec/expected-injection.bash.txt`.*

Read it closely. The hostile title is `a"; echo INJECTED-COMMAND-RAN; #`. Pasted into the script text, it became `title="a"; echo INJECTED-COMMAND-RAN; #"`, which is **two commands**, and running the script printed `INJECTED-COMMAND-RAN`: the stranger's command ran. Passed through an environment variable, the same title is only *data*: the script printed it, whole, and nothing ran. That is the documentation's recommendation: "set the value of the expression to an intermediate environment variable", and use it in the script as `"$TITLE"`:

```yaml
- name: Check PR title
  env:
    TITLE: ${{ github.event.pull_request.title }}
  run: |
    if [[ "$TITLE" =~ ^octocat ]]; then
```

The documentation explains why this works: "the value ... is stored in memory and used as a variable, and doesn't interact with the script generation process". It also names a stronger option: "create a JavaScript action that processes the context value as an argument", since then the value is never used to make a shell script.

**Which values are untrusted?** The documentation: contexts that "typically end with `body`, `default_branch`, `email`, `head_ref`, `label`, `message`, `name`, `page_name`, `ref`, and `title`", such as `github.event.issue.title` and `github.event.pull_request.body`. And less obvious ones: "branch names and email addresses, which can be quite flexible in terms of their permitted content. For example, `zzz";echo${IFS}"hello";#` would be a valid branch name". The last line of the recording asks Git whether it agrees, and it does:

```text
$ git check-ref-format --branch 'zzz";echo${IFS}"hello";#' && echo "Git accepts that as a branch name"
zzz";echo${IFS}"hello";#
Git accepts that as a branch name
```

*Recorded in Bash; `ch60-wfsec/expected-injection.bash.txt`.*

`git check-ref-format --branch` accepts that name (Chapter 20<!--ref:branching--> listed the characters Git forbids, and quotes, semicolons, `$`, braces and `#` are not among them). So a branch name, a commit message and an author name are all *text chosen by someone else*.

> **Checked against GitHub's documentation (R303).** "Script injections" and "Secure use reference": the example, the recommendation, the list of untrusted contexts and the branch-name example are quoted from them. The recording reproduces the shell mechanism with two small scripts; it is not a GitHub run.

---

## 60.5 Untrusted pull requests

Workflows for `pull_request` events from forks run with reduced privileges (no secrets except `GITHUB_TOKEN`, Chapter 56<!--ref:workflows_practice-->). Two other triggers, `pull_request_target` and `workflow_run`, are different. GitHub's documentation: they are "privileged, which means they share the same cache of the main branch with other privileged workflow triggers, and may have repository write access and access to referenced secrets", and used "with the checkout of an untrusted pull request, expose the repository to security compromises". Its advice: "Avoid using the `pull_request_target` workflow trigger if it's not necessary", and never let such a workflow "explicitly check out untrusted code, including from pull request forks".

The rule for beginners: **never check out and run code from a stranger's pull request in a workflow that has secrets or write access.**

---

## 60.6 OpenID Connect, in one paragraph

Deploying to a cloud service needs credentials, which are usually stored as long-lived secrets. GitHub's documentation describes an alternative, **OpenID Connect (OIDC)**: after a trust connection is set up with a cloud provider, "you can configure your workflow to request a short-lived access token directly from the cloud provider". Benefits it lists: "no cloud secrets" to duplicate in GitHub, finer control through the provider's own rules, and credentials that are "only valid for a single job, and then automatically expire". Setting it up depends on the provider and is outside this book; the idea to keep is *short-lived credentials beat long-lived secrets*.

> **Checked against GitHub's documentation (R304).** "Secure use reference" (untrusted pull requests) and "OpenID Connect" (concept).

---

## 60.7 A checklist

1. Set `permissions` to the least that works, at the top of every workflow.
2. Pin third-party actions to a full commit SHA, from the action's own repository.
3. Never paste an untrusted `${{ }}` value into a `run:` script; use an environment variable.
4. Treat titles, bodies, branch names, commit messages and author names as hostile.
5. Do not use `pull_request_target` or `workflow_run` with code from a fork.
6. Keep secrets out of logs, files and caches; rotate any that leak.
7. Use short-lived credentials where you can.
8. Do not put a self-hosted runner on a public repository (Chapter 59<!--ref:runners-->).

---

## Checkpoint

## What You Learned

- A workflow runs with credentials; least privilege limits the damage of a mistake.
- `permissions` sets the token's rights; read-only contents is a good default.
- Pin actions to a full commit SHA from the action's repository.
- `${{ }}` is pasted as text into a script; pass untrusted values through an environment variable.
- Branch names, titles and author names can contain shell syntax.
- Do not check out untrusted code in a privileged workflow; prefer short-lived credentials (OIDC).

## New Vocabulary

**Script injection**, **least privilege** (the second from Chapter 33<!--ref:gitsec-->), **OIDC** (introduced above).

## Commands Learned

`git check-ref-format --branch`, and passing values as `TITLE="$title" sh safe.sh`.

## Common Mistakes

1. **Pasting `${{ github.event... }}` into a `run:` script.**
2. **Pinning to a tag or branch of an unknown action.**
3. **Leaving the token with write access it does not need.**
4. **Using `pull_request_target` with a checkout of the pull request.**
5. **Logging a secret or a value derived from one.**

## Practice

Do the exercises in [`exercises/ch60-exercises.md`](../../../exercises/ch60-exercises.md).

## Self-Test

1. Why is a commit SHA a safer reference than a tag?
2. What does the substitution of `${{ }}` in a `run:` script do to a hostile title?
3. What is the safe way to use an untrusted value in a script?
4. Why is a branch name potentially hostile?
5. Which trigger runs with secrets even for pull requests from forks?

## Before Moving On

You are ready for Chapter 62<!--ref:ghsec--> if you can:

- [ ] write a `permissions` block with least privilege
- [ ] rewrite an injectable step safely
- [ ] explain why third-party actions are pinned

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The injection mechanism and the environment-variable defence; Git accepts the documented hostile branch name | Locally tested with shell scripts and Git: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R303 (local side) |
| Token permissions, secrets guidance, pinning, untrusted-input contexts, `pull_request_target`, OIDC | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account** | R301-R304 |
| The commit SHA in this book's workflow | Read from the action's repository with `git ls-remote` | R302 |

## Where this leads

Chapter 62<!--ref:ghsec--> covers GitHub's security features for the whole repository, and Chapter 61<!--ref:externalci--> compares Actions with other CI systems.
