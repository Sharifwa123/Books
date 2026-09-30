---
key: ghsec
number: 62
tag: Core
first_read: part
status: draft
requires: [gitsec, wfsec]
ledger: [R307, R308, R309, R310]
---
# Chapter 62 — GitHub Security Features [Core]

**In this chapter**

- the dependency graph, Dependabot alerts, security updates and version updates
- secret scanning and push protection
- code scanning and CodeQL (the concept)
- security advisories, `SECURITY.md` and private vulnerability reporting
- security overview

> **How to read this chapter.** Everything about GitHub here comes from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026). **Nothing was run on a live account**: availability depends on plan, repository visibility and licence, and changes over time, so it is only summarised here, and the settings screens are not described. The one locally tested part is small: a `dependabot.yml` example from the documentation and a `SECURITY.md` file, checked as ordinary files in Git.

**Before you start.** Chapter 33<!--ref:gitsec--> (secrets and history) and Chapter 60<!--ref:wfsec--> (least privilege and pinning).

---

## 62.1 Why these features exist

Chapter 33<!--ref:gitsec--> said that Git itself does not protect you: it stores whatever you commit. GitHub adds services around the repository that look for the two most common problems: **a dependency with a known weakness** and **a secret in the code**. This chapter names each feature and says what it does, in the words of the documentation. **Which repositories can use which feature, and at what price, changes**: for anything you plan to rely on, read the current documentation for your account type.

---

## 62.2 The dependency graph

Your project uses other people's packages (its **dependencies**). GitHub's documentation: the dependency graph "automatically parses dependencies by analyzing manifests and lock files in your repository". A **manifest** lists what the project needs; a **lock file** records the exact versions chosen. You can also submit dependency data yourself. When a pull request changes dependencies, the graph is used for a **dependency review**, which "indicate[s] whether the dependencies contain vulnerabilities and, if so, the version of the dependency in which the vulnerability was fixed".

For public repositories the graph also lists **dependents**: other public repositories that depend on yours. The supported ecosystems are listed in the documentation.

---

## 62.3 Dependabot

**Dependabot** is the name for three related things.

1. **Dependabot alerts.** GitHub "scans your repository's default branch and sends alerts" when a new vulnerability is added to the GitHub Advisory Database, or when your dependency graph changes. An alert shows the affected file, the vulnerability's details and severity, and a fixed version "when available". Repository administrators and organisation owners can enable alerts.
2. **Dependabot security updates.** If enabled, when an alert is raised, Dependabot "automatically tries to fix it": it "raises a pull request to update the dependency to the minimum version that includes the patch and links the pull request to the ... alert". You review and merge it like any pull request (Chapter 45<!--ref:pr-->). Alerts close when the related pull request is merged.
3. **Dependabot version updates.** Not about vulnerabilities: it keeps dependencies **up to date**. "You enable ... by checking a `dependabot.yml` configuration file into your repository." When a dependency is outdated it raises a pull request to update the manifest. It also can keep the versions of **actions** in your workflow files up to date, which suits Chapter 60<!--ref:wfsec-->'s advice to pin.

The configuration file is ordinary YAML (Chapter 53<!--ref:yaml-->). The documentation lists the required keys: `version`, `updates`, and for each entry `package-ecosystem`, `directory` (or `directories`) and `schedule.interval` (`daily`, `weekly` or `monthly`). Its minimal example, written and checked locally:

```text
$ mkdir -p .github
$ printf 'version: 2\nupdates:\n  - package-ecosystem: "npm"\n    directory: "/"\n    schedule:\n      interval: "daily"\n' > .github/dependabot.yml
$ cat .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
$ python3 check.py .github/dependabot.yml
version: 2
ecosystem: npm | directory: / | interval: daily
```

*Recorded in Bash; `ch62-ghsec/expected-config.bash.txt`.*

The script only reads the file with PyYAML and prints what it found, so you see that the structure is what the documentation describes. It does **not** contact GitHub, and it does not prove that Dependabot accepts the file: only pushing to GitHub does that. The file lives in the `.github` folder, which is where GitHub looks for such files.

> **Checked against GitHub's documentation (R307).** "About Dependabot alerts", "About Dependabot security updates", "About Dependabot version updates", "About the dependabot.yml file", "About the dependency graph". The recording reproduces the documentation's example file as a plain file; no Dependabot ran.

---

## 62.4 Secret scanning and push protection

**Secret scanning** "scans your entire Git history on all branches of your repository for hardcoded credentials, including API keys, passwords, tokens, and other known secret types", and periodically rescans when new secret types are added. It raises an alert on the repository's Security tab. GitHub's advice on an alert: "rotate the affected credential immediately to prevent unauthorized access. While you can also remove secrets from your Git history, this is time-intensive and often unnecessary if you've already revoked the credential." That is exactly the order of Chapter 33<!--ref:gitsec-->: **revoke first**. For many providers GitHub also notifies the provider, "so they can take action, such as revoking the credential". You can add **custom patterns** (regular expressions) for secrets of your own.

**Push protection** works earlier: it "blocks pushes that contain secrets *before* they reach your repository". It applies to pushes from the command line, to commits and uploads in the web interface, and to REST API requests. A blocked push comes with a message; you remove the secret and push again. For repositories it "is disabled by default" and can be enabled by a repository administrator, an organisation owner or a security manager.

Neither feature is a reason to be careless: they find *known patterns*. Chapter 33<!--ref:gitsec-->'s habits still apply.

> **Checked against GitHub's documentation (R308).** "About secret scanning" and "About push protection".

---

## 62.5 Code scanning and CodeQL

**Code scanning** finds "potential vulnerability or error in your code" and shows alerts in the repository; when you fix the code, the alert closes. You can run scans on a schedule or on events such as a push. It uses **CodeQL**, an analysis product maintained by GitHub, or a third-party tool that outputs **SARIF** (a standard result format). The documentation states that code scanning "uses GitHub Actions, with each workflow run consuming GitHub Actions minutes", and that for private repositories you need a licence. Beginners' takeaway: it is another automated check on your pull requests (Chapter 52<!--ref:cicd-->).

> **Checked against GitHub's documentation (R309).** "About code scanning".

---

## 62.6 Advisories, SECURITY.md and private reporting

You found a hole in your own project, or someone reports one to you. What happens next?

- **`SECURITY.md`.** A file in the repository that "gives instructions on how to report a security vulnerability in your project". It belongs beside `README.md` (Chapter 42<!--ref:readme-->). The recording made a small one: it says to report privately and not in a public issue. **The address in it is an example and does not exist.**
- **Private vulnerability reporting.** Lets a reporter "disclose vulnerability details directly and privately to the repository maintainers by proposing a draft repository advisory".
- **Repository security advisories.** Maintainers can "create a draft security advisory, and use the draft to privately discuss the impact", "privately collaborate to fix the vulnerability in a temporary private fork", and "publish the security advisory to alert your community" when a patch is released.
- **CVE numbers.** A **CVE** is a public identifier for a vulnerability. GitHub "is a CVE Numbering Authority" and can assign one when you publish an advisory.

The steps of the recording, continued:

```text
$ printf '# Security policy\n\nReport a vulnerability privately to security@example.org.\nPlease do not open a public issue.\n' > SECURITY.md
$ cat SECURITY.md
# Security policy

Report a vulnerability privately to security@example.org.
Please do not open a public issue.
$ git init -q .
$ git add .github SECURITY.md
$ git ls-files
.github/dependabot.yml
```

*Recorded in Bash; `ch62-ghsec/expected-config.bash.txt`.*

The practice behind all of this is called **coordinated disclosure**: fix first, then announce.

> **Checked against GitHub's documentation (R310).** "About repository security advisories", "Creating a default community health file" (for SECURITY.md) and the vulnerability-reporting concept pages.

---

## 62.7 Security overview

For organisations, **security overview** gives "insights into the overall security landscape of your organization" and helps "identify repositories that require intervention". It is an organisation feature and is outside a single-repository beginner's needs; Chapter 68<!--ref:orgs--> returns to organisations.

---

## 62.8 What to switch on, in order

For a repository you own, and subject to what your plan offers: (1) `SECURITY.md`; (2) Dependabot alerts; (3) secret scanning and push protection; (4) Dependabot version updates for dependencies and for actions; (5) code scanning if it is available to you. Look at the Security tab first: it shows what is available for **your** repository.

---

## Checkpoint

## What You Learned

- The dependency graph lists what you depend on; Dependabot alerts warn about known weaknesses.
- Security updates fix vulnerable dependencies; version updates keep everything current.
- Secret scanning finds committed secrets; push protection blocks them before they arrive. Rotate first.
- Code scanning, with CodeQL or other tools, is an automated check for weaknesses.
- `SECURITY.md`, private reporting and advisories make reporting and fixing orderly.
- Availability by plan changes: read the current documentation.

## New Vocabulary

**Dependency graph**, **Dependabot**, **push protection**, **code scanning**, **CodeQL**, **security advisory**, **CVE** (see the glossary).

## Commands Learned

No new Git commands; `git ls-files` lists tracked files, as in the recording.

## Common Mistakes

1. **Believing scanning makes secrets safe.** It finds known patterns.
2. **Cleaning history before rotating the credential.**
3. **Merging every Dependabot pull request without tests.**
4. **Publishing a vulnerability in a public issue.**

## Practice

Do the exercises in [`exercises/ch62-exercises.md`](../../../exercises/ch62-exercises.md).

## Self-Test

1. What is the difference between Dependabot security updates and version updates?
2. What does push protection do that secret scanning does not?
3. What should you do first when a secret is found?
4. Where does a `dependabot.yml` file live?
5. What is `SECURITY.md` for?

## Before Moving On

You are ready for Chapter 63<!--ref:secpractice--> if you can:

- [ ] describe each feature in one sentence
- [ ] write a minimal `dependabot.yml`
- [ ] write a `SECURITY.md`

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The `dependabot.yml` example is well-formed YAML with the documented keys; a `SECURITY.md` is an ordinary tracked file | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0, PyYAML 6.0.1; CI on newer Git | R307 (local side) |
| What each feature does; who can enable it; alert, advisory and CVE behaviour | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account**; availability by plan not established | R307-R310 |

## Where this leads

Chapter 63<!--ref:secpractice--> turns these features into a practice: scopes, signed commits, artifacts and the supply chain.
