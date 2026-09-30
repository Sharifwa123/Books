---
key: codespaces
number: 70
tag: Deep
first_read: later
status: draft
requires: [ghrepo]
ledger: [R331, R332, R333]
---
# Chapter 70 — Codespaces and Dev Containers [Deep]

**In this chapter**

- what a codespace is, and why teams use them
- dev containers: `.devcontainer/devcontainer.json` and a Dockerfile (concept only)
- the lifecycle, saving work, and cost
- security of a cloud development environment
- local versus cloud development

> **How to read this chapter.** This is a **Deep** chapter and can be read later. Everything about Codespaces comes from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026) and **was not run on a live account**: no codespace was created. The one recording is local: it lays out dev container configuration files in a repository and shows that they are ordinary tracked files. **Prices, quotas and machine sizes change and are not stated.** Docker is explained at concept level only.

**Before you start.** Chapter 39<!--ref:ghrepo-->.

---

## 70.1 The problem: "it works on my computer"

Chapter 3<!--ref:editors--> and Chapter 13<!--ref:install--> had you install tools on your own computer. On a team, every person's computer differs: another operating system, another version of the language, a missing library. Setting up a new project can take a day.

A **codespace** is one answer. GitHub's documentation: "A codespace is a development environment that's hosted in the cloud. You can customize your project for GitHub Codespaces by committing configuration files to your repository (often known as Configuration-as-Code), which creates a repeatable codespace configuration for all users of your project."

Each codespace "is hosted by GitHub in a Docker container, running on a virtual machine". You choose from several machine types. By default it is created from an Ubuntu Linux image with popular languages and tools, "Regardless of your local operating system, your codespace will run in a Linux environment. Windows and macOS are not supported operating systems for the remote development container." You connect from a browser or in the other ways the documentation lists, and you are "placed within the Docker container".

A **container** is a packaged, isolated environment with its own tools and files that runs on a host machine. **Docker** is the best-known way to build and run containers. For this book, a container is "a ready-made computer-in-a-box that a configuration file describes"; how Docker builds one is out of scope.

> **Checked against GitHub's documentation (R331).** "What are GitHub Codespaces?".

---

## 70.2 Dev containers: the configuration in your repository

The configuration lives in the repository. The documentation:

- "Development containers, or dev containers, are Docker containers that are specifically configured to provide a fully featured development environment. Whenever you work in a codespace, you are using a dev container on a virtual machine."
- The files are in a `.devcontainer` directory. The primary file is `devcontainer.json`, "usually located in the `.devcontainer` directory". Alternatively it can be `.devcontainer.json` in the repository root.
- Several configurations are allowed: alternatives "must be located in their own subdirectory at the path `.devcontainer/SUBDIRECTORY/devcontainer.json`", and when someone creates a codespace they choose one. "Settings cannot be imported or inherited between `devcontainer.json` files."
- The file usually refers to a **Dockerfile**, "a text file that contains the instructions needed to create a Docker container image", or uses the `image` property "to refer directly to an existing image". "If neither a Dockerfile nor an image is found then the default container image is used."
- Use it for **customisation**, not **personalisation**: "You should only include things that everyone working on your codebase needs", such as linters; personal preferences like themes belong in your own settings, dotfiles or Settings Sync.

The documentation's Python example uses these keys: `name`, `image`, `features` (extra tools added to the container), `forwardPorts` (ports made available locally), `postCreateCommand` (a command run after the container is created), `customizations` (tool-specific settings such as editor extensions) and `remoteUser`.

A small local model. Two configuration files are written, one at the default place and one for a second choice, and a tiny script reads them as **strict JSON**:

```text
$ git init -q proj && cd proj
$ mkdir -p .devcontainer/docs-dev
$ printf '{\n  "name": "Python 3",\n  "image": "mcr.microsoft.com/devcontainers/python:0-3.11-bullseye",\n  "postCreateCommand": "pip3 install --user -r requirements.txt"\n}\n' > .devcontainer/devcontainer.json
$ printf '// a comment, as in the documentation examples\n{\n  "name": "Docs",\n  "image": "mcr.microsoft.com/devcontainers/python:0-3.11-bullseye"\n}\n' > .devcontainer/docs-dev/devcontainer.json
$ python3 ../dc.py .devcontainer/devcontainer.json .devcontainer/docs-dev/devcontainer.json
.devcontainer/devcontainer.json -> strict JSON ok; keys: ['image', 'name', 'postCreateCommand']
.devcontainer/docs-dev/devcontainer.json -> not strict JSON: JSONDecodeError
$ git add .devcontainer && git commit -q -m "Add dev container configurations"
```

*Recorded in Bash; `ch70-codespaces/expected-devcontainer.bash.txt`.*

Two lessons. First, the second file starts with a `//` comment and **strict JSON does not allow comments**: the script reports it. The documentation's own examples are written as `jsonc`, JSON *with comments*, which dev container tools accept. When you check such files with a strict JSON tool, remove the comments first, or use a tool that understands `jsonc`. Second, the configuration files are **ordinary files**:

```text
$ git ls-files
.devcontainer/devcontainer.json
.devcontainer/docs-dev/devcontainer.json
```

*Recorded in Bash; `ch70-codespaces/expected-devcontainer.bash.txt`.*

They are versioned, reviewed in pull requests and rolled back like any other file (Chapters 19<!--ref:commits--> and 45<!--ref:pr-->). Changing them changes the environment of everyone who creates a codespace afterwards.

**What was not run.** Whether these two files would start a working codespace was not tested. The image name and Python version are copied from the documentation's example; image tags change.

> **Checked against GitHub's documentation (R332).** "Introduction to dev containers" and "Setting up your Python project for GitHub Codespaces". The recording checks file layout and JSON syntax only.

---

## 70.3 Lifecycle, saving and cost

The documentation's lifecycle:

- A codespace's life "begins when you create a codespace and ends when you delete it". You can disconnect and reconnect, and you "may stop and restart a codespace without losing changes".
- **Save your work to Git.** "If your codespace is deleted, then your work will be deleted too. To persist your work, you will need to commit your changes and push them to your remote repository." If you create a new codespace each time, push regularly; if you keep one for weeks, pull from the default branch each time you start.
- **Timeouts.** "By default, a codespace will timeout after 30 minutes of inactivity" and stops; the default can be customised. Data is preserved from the last save.
- **Rebuilding** applies changes to the dev container configuration; creating a new codespace is often the alternative.
- **Limits on the number of codespaces** exist; the numbers are in the documentation.

**Cost.** "All personal GitHub accounts have a monthly quota of free use of GitHub Codespaces included in the Free or Pro plan." If you create a codespace from an organization-owned repository, "use of the codespace will either be charged to the organization (if the organization is configured for this), or to your personal account". Owners of organizations on some plans can pay for members' use and set a spending limit (Chapter 68<!--ref:orgs-->). **The size of the quota and the prices are not stated here.** Check the billing page before you rely on codespaces for regular work, and stop or delete codespaces you no longer use.

> **Checked against GitHub's documentation (R333).** "Understanding the codespace lifecycle" and "What are GitHub Codespaces?" (billing overview).

---

## 70.4 Security

A codespace runs code and holds a token. The documentation's "Security in GitHub Codespaces" says:

- Each codespace has its **own virtual machine** ("Two codespaces are never co-located on the same VM") and **own virtual network**; incoming connections from the internet are blocked and outbound connections are allowed.
- Every time a codespace is created or restarted it is assigned a **new token with an automatic expiry**, scoped to your access: with write access, read/write on the repository; with only read access, clone-only, and a commit or push leads to a fork with read/write access to that fork.
- **Only the creator** can connect to a codespace.
- **Forwarded ports** are private by default (only the creator, after authenticating). They can be made public **to anyone on the internet without authentication**, and organization owners can restrict this. A public port reverts to private when you remove and re-add it or restart the codespace.
- "You should only open and work within repositories you know and trust." Code in a codespace can use its token: the risks of Chapter 60<!--ref:wfsec--> (untrusted code, secrets) apply.

Treat secrets as in Chapter 63<!--ref:secpractice-->: do not put them in the dev container configuration, which is committed to the repository. GitHub documents a way to declare which secrets a repository recommends; the mechanism was not examined for this book.

---

## 70.5 Local or cloud?

| | Local | Codespace |
|---|---|---|
| Set-up | you install and maintain | the configuration file builds it |
| Works offline | yes | no |
| Same for everyone | no | yes, within the configuration |
| Cost | your computer | quota or paid use |
| Speed | your hardware | the chosen machine type |
| Your files | on your disk | in the cloud until pushed |

Neither is "better". A common pattern: local for daily work, a codespace for quick fixes, reviewing a pull request in a running environment, teaching a class, or onboarding a new contributor in minutes.

---

## Checkpoint

## What You Learned

- A codespace is a cloud development environment in a container on a virtual machine, always Linux.
- The environment is configuration as code in `.devcontainer/devcontainer.json`; alternatives sit in subfolders.
- Configuration files are ordinary tracked files; comments in `jsonc` are not strict JSON.
- Unpushed work in a deleted codespace is lost; codespaces time out after inactivity and cost quota.
- Security: isolated VM and network, expiring token, private ports by default, trust only repositories you know.

## New Vocabulary

**Codespace**, **dev container**, **container**, **Docker**, **Dockerfile** (see the glossary).

## Commands Learned

No new Git commands; `python3 dc.py` was a helper for the recording.

## Common Mistakes

1. **Keeping the only copy of work in a codespace.**
2. **Putting personal preferences or secrets in `devcontainer.json`.**
3. **Making a forwarded port public and forgetting it.**
4. **Leaving codespaces running or undeleted.**
5. **Assuming a container works on Windows or macOS natively.**

## Practice

Do the exercises in [`exercises/ch70-exercises.md`](../../../exercises/ch70-exercises.md).

## Self-Test

1. What is a codespace made of?
2. Where does `devcontainer.json` live, and how do you offer two configurations?
3. What happens to unpushed work if a codespace is deleted?
4. Who can connect to a codespace?
5. What does it mean that a forwarded port is public?

## Before Moving On

You are ready for Chapter 71<!--ref:packages--> if you can:

- [ ] explain a dev container in one paragraph
- [ ] place configuration files correctly
- [ ] list three security points

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Layout of dev container files; strict JSON rejects comments; the files are tracked | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0, Python 3; CI on newer Git | R332 (local side) |
| What codespaces are, lifecycle, cost model, security | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account** | R331-R333 |
| That the example configuration starts a working codespace | **Not tested** | none |

## Where this leads

Chapter 71<!--ref:packages--> publishes and installs packages from GitHub.
