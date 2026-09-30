---
key: packages
number: 71
tag: Deep
first_read: later
status: draft
requires: [workflows_practice]
ledger: [R334, R335, R336]
---
# Chapter 71 — GitHub Packages and Containers [Deep]

**In this chapter**

- what a package and a registry are
- what GitHub Packages offers
- publishing and installing: scopes, names and authentication
- package permissions and visibility
- containers: concept only

> **How to read this chapter.** This is a **Deep** chapter and can be read later. Everything about GitHub Packages comes from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026) and **was not run on a live account**: no package was published or installed, and `npm` was not run. The local recording writes package metadata and configuration files and shows where a credential must **not** be. **Limits, prices and the list of supported registries change and are not stated in full.** Containers and Docker are explained at concept level only.

**Before you start.** Chapter 56<!--ref:workflows_practice-->. Chapter 63<!--ref:secpractice--> on secrets and artifacts is useful.

---

## 71.1 Packages and registries

A **package** is software packaged so that others (or your own projects) can install it with a tool: a library for a language, a program, a container image. The tool is a **package manager** (Chapter 1<!--ref:computer-->). The place where packages are stored and downloaded from is a **registry**.

Chapter 67<!--ref:ossproject--> built a small library that others would copy by hand. A package lets them write one install command instead, and lets the tool pick the right version (Chapter 66<!--ref:releases--> on version numbers).

GitHub's documentation: "GitHub Packages is a platform for hosting and managing packages, including containers and other dependencies. GitHub Packages combines your source code and packages in one place to provide integrated permissions management and billing." It offers registries for "commonly used package managers, such as npm, RubyGems, Apache Maven, Gradle, Docker, and NuGet", and a separate **container registry** "optimized for containers" that supports "Docker and OCI images". The documentation's table lists the package formats and clients: for example `package.json` and `npm` for JavaScript, `pom.xml` and `mvn` for Maven, and `nupkg` with the `dotnet` command-line tool for .NET. Other ecosystems (Python's public index, for example) are not in that list; check the current documentation for what is supported.

You can view a package's README and metadata such as licence, download statistics and version history on GitHub. For organisations there is also a "linked artifacts" view that records metadata about builds without hosting the files.

> **Checked against GitHub's documentation (R334).** "Introduction to GitHub Packages".

---

## 71.2 Publishing: names, scopes and credentials

The npm registry is the documentation's main worked example. It says:

- "GitHub Packages only supports scoped npm packages. Scoped packages have names with the format of `@NAMESPACE/PACKAGE-NAME`."
- "Package names and scopes must only use lowercase letters."
- You can route a scope to GitHub's registry with a project **`.npmrc`** file (a line of the form `@OWNER:registry=https://npm.pkg.github.com`), or with a `publishConfig` entry in `package.json`. The documentation notes that using an `.npmrc` file "prevents other developers from accidentally publishing the package to npmjs.org instead of GitHub Packages".
- A `repository` field in `package.json` can connect the package to a repository as soon as it is published.
- To **authenticate** you can put a token in your per-user `~/.npmrc` file, or log in with `npm login`. A workflow authenticates differently (section 71.4).

The recording writes those files in a sandbox, using made-up names, and checks the two naming rules with shell commands. The token is a **made-up** value and goes into the **user-level** file, outside the repository:

```text
$ git init -q lib && cd lib
$ printf '{\n  "name": "@ada/wordcount",\n  "version": "0.1.0",\n  "repository": "https://github.com/ada/wordcount"\n}\n' > package.json
$ printf '@ada:registry=https://npm.pkg.github.com\n' > .npmrc
$ printf '//npm.pkg.github.com/:_authToken=not-a-real-token\n' > ~/.npmrc
$ name=$(sed -n 's/.*"name": "\(.*\)",/\1/p' package.json); echo "$name"
@ada/wordcount
$ [ "$name" = "$(printf %s "$name" | tr A-Z a-z)" ] && echo "lowercase: ok"
lowercase: ok
$ case "$name" in @*/*) echo "scoped: ok";; *) echo "not scoped";; esac
scoped: ok
```

*Recorded in Bash; `ch71-packages/expected-scope.bash.txt`.*

Then it commits, lists what Git tracks, and searches the repository for the token line:

```text
$ git add -A && git commit -q -m "Add package metadata and scope mapping"
$ git ls-files
.npmrc
package.json
$ git grep -n '_authToken' || echo "no token in the repository"
no token in the repository
$ grep -c '_authToken' ~/.npmrc
1
```

*Recorded in Bash; `ch71-packages/expected-scope.bash.txt`.*

`git ls-files` shows `.npmrc` (the scope mapping, which contains **no** secret) and `package.json`. The search finds no `_authToken` in the repository, while the user-level file has one. That is the rule of Chapter 33<!--ref:gitsec--> applied to configuration: **the mapping may be committed; the token may not.** If a token ever lands in a committed file, treat it as leaked: revoke it first.

Which kind of token? The documentation says that to manage a package on some registries you must use a **personal access token (classic)** with the right scope, and that your account needs appropriate permissions; GitHub's advice on tokens is to use the fewest scopes necessary (Chapter 63<!--ref:secpractice-->). The exact scope names are in the documentation; they were not copied here.

> **Checked against GitHub's documentation (R335).** "Working with the npm registry". The recording checks naming rules, file placement and the absence of the token from the repository; it does not contact any registry.

---

## 71.3 Permissions and visibility

Two models exist, depending on the registry:

- **Granular permissions**: the package belongs to a personal account or organisation, and you set its access and visibility "separately from a repository that is connected (or linked) to a package".
- **Repository-scoped permissions**: the package "inherits the permissions and visibility of the repository in which the package is published". Some registries support only this model.

For linked packages the documentation says: "By default, if you publish a package that is linked to a repository, the package automatically inherits the access permissions (but not the visibility) of the linked repository. For example, a user who has read access to the linked repository will also have read access to the package." This only happens if you link the repository **before** publishing; linking later from the package settings leaves the existing permissions unchanged. When permissions are inherited, you change them in the repository's settings. For packages scoped to a personal account you can assign read, write or admin roles to other users.

**Visibility matters twice**: a *public* package can be installed by anyone; a private one only by those with access. Choose it on purpose, and never publish something that includes secrets (Chapter 33<!--ref:gitsec-->).

> **Checked against GitHub's documentation (R336).** "About permissions for GitHub Packages" and "Configuring a package's access control and visibility".

---

## 71.4 Publishing from a workflow

A workflow (Chapter 54<!--ref:actions-->) can publish a package when you push a tag or create a release (Chapter 66<!--ref:releases-->). The documentation says that when a package inherits access permissions from a linked repository, "GitHub Actions workflows in the linked repository also automatically get access to the package". That is why a workflow usually authenticates with its own short-lived token, `GITHUB_TOKEN` (Chapter 60<!--ref:wfsec-->), rather than with a personal token that someone pastes into a secret. Give the workflow only the permission that it needs; the name of the permission that lets a workflow write packages is in the documentation and was not copied here.

A publishing workflow makes an artifact public for many users. Guard it: publish only from a protected branch or a tag, require review for changes to the workflow file (Chapters 50<!--ref:protect--> and 60<!--ref:wfsec-->), and prefer pinned actions.

---

## 71.5 Containers, in one page

A **container image** packages a program with everything it needs to run: the system libraries, the language runtime and your code. It is stored in a registry and started as a **container** on any machine that can run containers (Chapter 70<!--ref:codespaces--> used them for development). **Docker** is the best-known tool.

GitHub's container registry accepts Docker and OCI images; the documentation shows how to link an image to a repository at publication, for example with the `org.opencontainers.image.source` label, so that it inherits the repository's access permissions. The commands to build, tag, log in and push are in the documentation and depend on Docker, which this book did not run.

Whether you need containers at all is a design decision, not a duty. A small library rarely does; a service that must run the same way in many places often does.

---

## 71.6 Installing safely

Installing a package runs someone else's code (Chapter 60<!--ref:wfsec--> and Chapter 63<!--ref:secpractice-->). Before you add a dependency: Who maintains it? Is the licence acceptable (Chapter 65<!--ref:licences-->)? How is it versioned? Does it have a security policy (Chapter 62<!--ref:ghsec-->)? Pin versions with a lock file, and let Dependabot propose updates.

---

## Checkpoint

## What You Learned

- A registry stores packages; GitHub Packages offers several, and a container registry.
- npm packages on GitHub must be scoped and lowercase; `.npmrc` maps a scope to the registry.
- Commit the mapping, never the token; keep tokens in a user-level file or in a workflow's `GITHUB_TOKEN`.
- Package permissions are either granular or inherited from a linked repository; link before publishing to inherit.
- A container image packages a program with its environment; Docker is only introduced.

## New Vocabulary

**Package**, **registry**, **package manager**, **scope**, **container image** (see the glossary).

## Commands Learned

No new Git commands. The recording used `tr`, `case` and `git grep -n`.

## Common Mistakes

1. **Committing a token in `.npmrc`.**
2. **Publishing an unscoped or upper-case package name to GitHub's npm registry.**
3. **Linking a repository after publishing and expecting inherited permissions.**
4. **Publishing from an unprotected workflow.**
5. **Installing a dependency without looking at it.**

## Practice

Do the exercises in [`exercises/ch71-exercises.md`](../../../exercises/ch71-exercises.md).

## Self-Test

1. What is a registry?
2. What must the name of an npm package on GitHub look like?
3. Where may a token live, and where not?
4. When does a package inherit a repository's permissions?
5. What does a container image contain?

## Before Moving On

You are ready for Chapter 72<!--ref:deploy--> if you can:

- [ ] explain package, registry and scope
- [ ] set up a scope mapping without leaking a token
- [ ] describe the two permission models

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Name rules, file placement, absence of the token from the repository | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R335 (local side) |
| What GitHub Packages offers, npm registry rules, permission models | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account**; `npm` and Docker not run | R334-R336 |
| Names of token scopes and workflow permissions for packages; container commands | **Not copied or checked** | none |

## Where this leads

Chapter 72<!--ref:deploy--> follows the last step of the chain: getting software running for users.
