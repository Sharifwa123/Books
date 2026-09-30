---
key: protect
number: 50
tag: Deep
first_read: later
status: draft
requires: [pr, collab]
ledger: [R274, R275, R276]
---
# Chapter 50 — Branch Protection and Rulesets [Deep]

**In this chapter**

- how Git itself can refuse a dangerous push, on a server you control
- what GitHub's branch protection rules do
- what rulesets add, and how rules from several places layer
- what depends on plan, visibility and role

> **How to read this chapter.** This is a **Deep** chapter and can be read later. The Git server settings were run and recorded with a local bare repository. Statements about GitHub are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used. **Which plans and repository kinds get which protections is time-sensitive and is only partly checked**; look at the current page for your account before you rely on it.

**Before you start.** Chapter 45<!--ref:pr-->, Chapter 49<!--ref:collab--> and Chapter 27<!--ref:rebase--> (force pushes).

---

## 50.1 The problem

Some actions on shared branches are dangerous: a force push that rewrites history others have built on (Chapter 27<!--ref:rebase-->), deleting the branch everybody depends on, or merging without review. Good habits help, but habits fail. **Protection** turns the habit into a rule that the server enforces.

Git has a small version of this built in, on the receiving side. It is the ancestor of what a platform offers.

---

## 50.2 What Git itself can refuse

A repository that receives pushes (a *server* repository, such as a bare `hub.git`) can be told to refuse two dangerous kinds of push. Git's documentation of the `receive` settings says:

- `receive.denyNonFastForwards`: "If set to true, git-receive-pack will deny a ref update which is not a fast-forward. Use this to prevent such an update via a push, even if that push is forced."
- `receive.denyDeletes`: "If set to true, git-receive-pack will deny a ref update that deletes the ref."

The recording sets both on a server repository, then tries a forced push after amending a commit, and a deletion of `main`:

```text
$ git clone -q hub.git work
$ cd work
$ git -C ../hub.git config --get receive.denyNonFastForwards
true
$ git -C ../hub.git config --get receive.denyDeletes
true
$ git commit -q --amend -m "Add the menu (reworded)"
$ git push --force origin main
remote: error: denying non-fast-forward refs/heads/main (you should pull first)
To /home/learner/hub.git
 ! [remote rejected] main -> main (non-fast-forward)
error: failed to push some refs to '/home/learner/hub.git'
$ git push origin --delete main
remote: error: denying ref deletion for refs/heads/main
To /home/learner/hub.git
 ! [remote rejected] main (deletion prohibited)
error: failed to push some refs to '/home/learner/hub.git'
$ git ls-remote --heads origin
c4972f0d9a02edb567a40199915178833a1b91b9	refs/heads/main
```

*Recorded in Bash; `ch50-protect/expected-server-rules.bash.txt`.*

The forced push is refused by the *server* (`remote: error: denying non-fast-forward`), even though `--force` was given, and the deletion is refused too. Afterwards `git ls-remote` shows `main` unchanged. The word `remote:` marks messages that come from the other side.

> **Checked against the documentation (R274).** The two settings and their wording are from Git's `receive.*` configuration documentation (Git 2.56.0). The recorded run shows them working on a local server repository. A platform is not a bare repository with two settings: this section shows the *idea* that a server can enforce rules whatever the client does.

---

## 50.3 Branch protection rules on GitHub

> **New term: branch protection rule.** A setting on a hosted repository that names branches (by pattern) and the requirements or restrictions that apply to changing them.

GitHub's documentation: "You can enforce certain workflows or requirements before a collaborator can push changes to a branch in your repository, including merging a pull request into the branch, by creating a branch protection rule." A rule targets a branch name pattern. Its available settings include:

- **Require pull request reviews before merging**: changes reach the branch "only via a pull request that is approved by the required number of reviewers with write permissions"; if an admin chooses **Request changes**, that person must approve before merge.
- **Require status checks before merging**: required checks must be `successful`, `skipped` or `neutral`. A **strict** setting also requires the branch to be up to date with the base branch; a **loose** one does not.
- **Require conversation resolution**, **signed commits**, **linear history**, a **merge queue**, and **deployments to succeed**.
- **Lock branch**, **restrict who can push**, **allow force pushes**, **allow deletions**.

"By default, each branch protection rule disables force pushes to the matching branches and prevents the matching branches from being deleted." That is the same pair of protections as the recording above, on the platform.

Two limits matter. By default the restrictions "don't apply to people with admin permissions", unless you choose to apply them to administrators too. And "only a single branch protection rule can apply at a time".

When a push is refused the platform says so, for example: `remote: error: GH006: Protected branch update failed for refs/heads/main.` followed by the reason, such as `Changes have been requested.`

> **Checked against GitHub's documentation (R275).** "About protected branches" is the source of every quotation and setting in this section. Details of each setting, and its availability for private repositories on each plan, were **not** checked: one item in the documentation limits *branch restrictions* to public repositories of a free organisation and to all repositories of paid organisations, which shows that plan matters.

---

## 50.4 Rulesets

> **New term: ruleset.** A named list of rules that a hosting platform enforces on chosen branches or tags, and that can be layered with other rulesets.

Rulesets are the newer, more flexible mechanism. GitHub's documentation: "A ruleset is a named list of rules that applies to a repository or to multiple repositories in an organization" (multi-repository rulesets are for customers on the Team and Enterprise plans). You can have up to 75 rulesets per repository. Differences from branch protection rules, in the documentation's words:

- "Multiple rulesets can apply to the same branch at the same time, while only one branch protection rule applies."
- "You can change a ruleset's enforcement status without deleting the ruleset."
- "Anyone with read access to a repository can view its active rulesets."
- Rulesets can control **commit metadata**, such as messages and author email addresses.
- They can target **branches or tags**, or block pushes to a whole fork network, with `fnmatch` patterns such as `releases/**/*`.

**Enforcement statuses.** *Active* enforces at once; *Disabled* enforces nothing; *Evaluate* (where offered) "will not be enforced, but you will be able to monitor which actions would or would not violate rules", so you can test a ruleset safely.

**Layering.** "A ruleset does not have a priority." If several rulesets target the same branch, their rules are **aggregated**, and where the same rule differs, "the most restrictive version of the rule applies"; rulesets also layer with branch protection rules. The documentation's example: one source requires signed commits and three reviews, another requires linear history and two reviews; the result requires signed commits, linear history and **three** reviews.

The available rules include: restrict creations, updates and deletions; require linear history; require a merge queue; require signed commits; require a pull request before merging (with review settings); require status checks; block force pushes; require code-scanning and secret-scanning results; require workflows to pass; restrict commit metadata, file paths, path length, extensions and file size.

> **Checked against GitHub's documentation (R276).** "About rulesets" and "Available rules for rulesets". Bypass lists (roles, teams or apps allowed to bypass a ruleset) exist; who may be added depends on the account type. The documentation also describes converting existing branch protection rules to rulesets.

---

## 50.5 Choosing

1. **Protect the default branch first.** Require a pull request, at least one review, and passing checks (Chapter 54<!--ref:actions-->).
2. **Block force pushes and deletions** on shared branches; this is the cheapest and most valuable rule.
3. **Use rulesets for anything new** if your plan offers them, because you can test in *Evaluate* mode and stack rules; keep old branch protection rules working until you convert them.
4. **Keep the bypass list short.** Anyone who can bypass a rule can also make the mistake it prevents.
5. **Write the rules down** in `CONTRIBUTING.md` (Chapter 64<!--ref:oss-->) so contributors are not surprised by a refusal.

> **⚠️ CAUTION.** A rule that blocks everyone, including you, on the day you need an emergency fix is a real cost. Decide in advance who may bypass, and how that is recorded.

---

## Checkpoint

## What You Learned

- A server can refuse dangerous pushes whatever the client does; Git has `receive.denyNonFastForwards` and `receive.denyDeletes`.
- GitHub's branch protection rules default to blocking force pushes and deletions, and add reviews, checks and more; only one rule applies at a time.
- Rulesets stack: several can apply, the most restrictive version of each rule wins, and they can be tested in Evaluate mode.
- What you get depends on plan, visibility and role.

## New Vocabulary

**Branch protection rule**, **ruleset** (introduced above).

## Commands Learned

`git config receive.denyNonFastForwards true`, `git config receive.denyDeletes true` (on a server repository).

## Common Mistakes

1. **Assuming `--force` overrides the server.**
2. **Giving many people bypass rights.**
3. **Forgetting that admins are exempt by default.**
4. **Requiring checks that nobody maintains.**
5. **Assuming a protection is available on your plan.**

## Practice

Do the exercises in [`exercises/ch50-exercises.md`](../../../exercises/ch50-exercises.md).

## Self-Test

1. What stops a forced push to a protected branch, whatever the client does?
2. Which two protections does a GitHub branch protection rule enable by default?
3. How do rulesets differ from branch protection rules on overlap?
4. What does Evaluate mode do?

## Before Moving On

You are ready for Chapter 51<!--ref:insights--> if you can:

- [ ] explain what a server-side refusal is
- [ ] list three settings of a protection rule
- [ ] say how layered rulesets combine

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `receive.denyNonFastForwards` and `receive.denyDeletes` refuse a forced push and a deletion | Both officially verified (Git 2.56.0 documentation) and locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R274 |
| Branch protection rules, defaults, settings | Checked against `github/docs` (commit `2eaab0b`); plan availability **not** fully checked | R275 |
| Rulesets, layering, enforcement, available rules | Checked against `github/docs`; plan availability **not** fully checked | R276 |

## Where this leads

Chapter 58<!--ref:wfadvanced--> uses protection with environments and deployments, and Chapter 62<!--ref:ghsec--> with security features.
