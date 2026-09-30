---
key: deploy
number: 72
tag: Deep
first_read: later
status: draft
requires: [wfadvanced, internet]
ledger: [R337, R338]
---
# Chapter 72 — Deployment Pipelines [Deep]

**In this chapter**

- what deployment means, and the kinds of target
- a pipeline from commit to running software
- release directories and rollback, tried locally
- environments, approvals and deployment secrets
- how GitHub's documentation approaches third-party platforms

> **How to read this chapter.** This is a **Deep** chapter and can be read later. The local part, a release directory scheme with a switch and a rollback, was recorded in Bash and zsh. Statements about GitHub environments come from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026) and **were not run on a live account**. **No cloud platform, server or container service was used for this chapter**, and their commands are not reproduced: they belong to each provider's documentation and change often.

**Before you start.** Chapter 58<!--ref:wfadvanced--> (environments, Project 10) and Chapter 5<!--ref:internet--> (servers, HTTPS).

---

## 72.1 What deployment is

To **deploy** is to put a version of your software somewhere it runs for its users. A **pipeline** (Chapter 52<!--ref:cicd-->) automates the steps: build, test, package, publish, switch. **Continuous deployment** deploys every change that passes; **continuous delivery** makes it *ready* to deploy and leaves the final step to a person. Chapter 52<!--ref:cicd--> explains the words.

Different software needs different targets:

| Kind | Example | Typical deployment step |
|---|---|---|
| Static website | HTML, CSS, JavaScript | copy files to a host (Chapter 69<!--ref:pages-->) |
| Server application (Node.js, Python, others) | a web application | build, install dependencies, restart a process |
| Container | a packaged service | build an image, push it to a registry (Chapter 71<!--ref:packages-->), run it somewhere |
| Virtual private server (VPS) | a rented Linux server you administer | copy files or a container, restart services, keep the system updated |
| Managed cloud service | a platform that runs your code for you | hand the package to the platform's tool or API |

Which target is right depends on cost, skills and needs, and this book does not recommend a provider.

---

## 72.2 A pipeline from commit to running

Whatever the target, the shape is the same:

1. **Trigger**: a merge to the default branch, a tag, or a manual start (Chapter 58<!--ref:wfadvanced-->).
2. **Build and test**: the checks of Chapter 52<!--ref:cicd--> run again on the exact commit.
3. **Package** into one artifact with a version: an archive, an image, a static folder (Chapter 66<!--ref:releases-->).
4. **Approve** (for sensitive environments): a person or a rule allows the deployment.
5. **Deploy**: the artifact goes to the target with credentials that only this step holds.
6. **Check**: a health check confirms the new version works.
7. **Keep the previous version** so that you can go back.

GitHub's documentation on third-party platforms shows example workflows for several: Azure App Service for Node.js, Python, Java, .NET and Docker; Azure Static Web Apps; Amazon Elastic Container Service; Google Kubernetes Engine. Its Node.js example builds, tests and deploys "when there is a push to the `main` branch", takes the target's name from a variable in the workflow, and reads a **publish profile** from a repository secret (`secrets.AZURE_WEBAPP_PUBLISH_PROFILE`). Those examples need accounts and resources on those platforms and were not run for this book.

> **Checked against GitHub's documentation (R337).** "Deploying to third-party platforms" (the Node.js to Azure App Service page as a sample) and "Deployments and environments".

---

## 72.3 Release directories and rollback

The most useful idea in deployment is small: **never overwrite the running version; put each version in its own folder and switch a pointer.** On a Linux server the pointer can be a **symbolic link**, a file that names another folder. The recording plays this on your own computer, with two versions of the Sunrise Bakery page:

```text
$ mkdir -p server/releases
$ mkdir server/releases/v1 server/releases/v2
$ printf 'Sunrise Bakery, version 1\n' > server/releases/v1/index.txt
$ printf 'Sunrise Bakery, version 2\n' > server/releases/v2/index.txt
$ ln -sfn releases/v1 server/current
$ cat server/current/index.txt
Sunrise Bakery, version 1
$ readlink server/current
releases/v1
```

*Recorded in Bash; `ch72-deploy/expected-release-dirs.bash.txt`.*

`server/current` is the link. It points to `releases/v1`, so reading `current/index.txt` shows version 1, and `readlink` shows where the link points. Deploying version 2 changes only the link, and rolling back changes it back:

```text
$ ln -sfn releases/v2 server/current
$ cat server/current/index.txt
Sunrise Bakery, version 2
$ ln -sfn releases/v1 server/current
$ cat server/current/index.txt
Sunrise Bakery, version 1
$ ls -1 server/releases
v1
v2
$ test -f server/current/index.txt && echo "health check: ok"
health check: ok
```

*Recorded in Bash; `ch72-deploy/expected-release-dirs.bash.txt`.*

Three properties follow:

- **Switching is fast**: one small change, not a copy of many files while visitors are reading them.
- **Rollback is the same operation in reverse**, with the previous version still in place. That is why step 7 of the pipeline keeps it.
- **The health check is a decision point**: a tiny `test -f` here; in real life a request to the running service. If the check fails, switch back automatically.

This is a local illustration; it does not model databases, running processes or caches, which make real rollbacks harder (a database change may not be reversible). The lesson is the shape, not the commands of a particular server.

---

## 72.4 Environments, approvals and secrets

GitHub's environments (Chapter 58<!--ref:wfadvanced-->) attach rules to a deployment target. The documentation: "Each job in a workflow can reference a single environment. Any protection rules configured for the environment must pass before a job referencing the environment is sent to a runner. The job can access the environment's secrets only after the job is sent to a runner." Protection rules can "require a manual approval, delay a job, or restrict the environment to certain branches". Required reviewers: "You can list up to six users or teams as reviewers", and one approval lets the job proceed; you can prevent self-review "so that deployments to protected environments are always reviewed by more than one person". A wait timer delays a job by a set number of minutes. **Availability of some rules depends on plan and repository visibility**; the documentation says, for example, that on some plans required reviewers are only available for public repositories.

**Deployment secrets** are credentials that let the workflow change your production system. Apply Chapter 63<!--ref:secpractice--> and Chapter 60<!--ref:wfsec-->:

- store them as **environment secrets**, so approval gates their use;
- give them the **fewest permissions** the deployment needs (for example, upload to one folder, not administer the account);
- prefer **short-lived credentials** issued to the job (the OpenID Connect idea of Chapter 60<!--ref:wfsec-->) over long-lived keys;
- **never print them**, and never put them in the repository or an image;
- **rotate** them, and revoke first if they leak.

---

## 72.5 Choosing and staging

**Staging** is a copy of production where you deploy first. A common design has two environments: `staging` (deploys automatically after the tests) and `production` (needs approval). The pipeline deploys the **same artifact** to both, so what you tested is what you release.

Some questions to answer before you build a pipeline:

1. What is the cheapest way to deploy that is safe enough?
2. How will you notice that it broke (logs, health check, alerts)?
3. How do you roll back, and have you tried it?
4. Who may deploy, and how is that recorded (Chapter 50<!--ref:protect-->)?
5. Where is the database, and what does a version change do to it?

---

## Checkpoint

## What You Learned

- A pipeline turns a commit into running software: trigger, test, package, approve, deploy, check, keep the previous version.
- Targets differ: static site, server application, container, VPS, managed service.
- Release directories plus a switching link give fast deployment and fast rollback.
- Environments add approvals, wait timers and branch limits, and gate environment secrets.
- Deployment secrets: least privilege, short-lived where possible, never printed, rotated.

## New Vocabulary

**Deployment**, **continuous deployment**, **rollback**, **staging**, **symbolic link** (see the glossary).

## Commands Learned

`ln -sfn`, `readlink`, `test -f`.

## Common Mistakes

1. **Overwriting the running version with no way back.**
2. **Deploying a different build from the one you tested.**
3. **Using one long-lived, all-powerful key for deployment.**
4. **Never practising a rollback.**
5. **Assuming a database change can be rolled back like files.**

## Practice

Do the exercises in [`exercises/ch72-exercises.md`](../../../exercises/ch72-exercises.md).

## Self-Test

1. What are the seven steps of the pipeline in section 72.2?
2. Why keep the previous release?
3. What does a symbolic link give a deployment?
4. What can an environment's protection rules do?
5. Why deploy the same artifact to staging and production?

## Before Moving On

You are ready for Chapter 73<!--ref:ghcli--> if you can:

- [ ] describe a deployment pipeline
- [ ] perform the switch and rollback locally
- [ ] name three rules for deployment secrets

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Release directories, the switching link, rollback | Locally tested: Bash 5.2 and zsh 5.9; CI | R338 |
| Environment protection rules, secrets access, sample third-party workflows | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account**; no provider used | R337 |
| Which target is best; provider commands | Not addressed; outside this book | none |

## Where this leads

Chapter 73<!--ref:ghcli--> shows GitHub from the command line.
