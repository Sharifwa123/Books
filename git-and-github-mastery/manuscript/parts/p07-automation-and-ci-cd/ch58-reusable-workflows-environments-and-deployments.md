---
key: wfadvanced
number: 58
tag: Deep
first_read: later
status: draft
requires: [workflows_practice, protect]
ledger: [R295, R296, R297]
---
# Chapter 58 — Reusable Workflows, Environments and Deployments [Deep]

**In this chapter**

- reusable workflows, and how they differ from composite actions
- environments: approvals, wait timers, branch rules and secrets
- deploying a static website with GitHub Pages and a workflow
- **Project 10**: deploy the Sunrise Bakery website

> **How to read this chapter.** This is a **Deep** chapter and can be read later. The packaging of a site as a Pages artifact (the constraints the documentation sets) was run and recorded locally. Everything else is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026). **No workflow or deployment in this chapter was run on a live account.** Project 10 is written for you to run; its expected result is what the documentation says, not something this book has observed.

**Before you start.** Chapter 56<!--ref:workflows_practice--> and Chapter 50<!--ref:protect-->. The recording ran in Bash and zsh, and was re-run in CI.

---

## 58.1 Reusable workflows

When several repositories need the same pipeline, copying the file everywhere means fixing every copy. GitHub's documentation: "Rather than copying and pasting from one workflow to another, you can make workflows reusable."

> **New term: reusable workflow.** A workflow written so that other workflows can call it as a whole, with inputs and secrets passed in. The calling one is the *caller*; the called one is the *called* workflow.

A workflow becomes reusable when its `on` includes `workflow_call`:

```yaml
on:
  workflow_call:
    inputs:
      config-path:
        required: true
        type: string
    secrets:
      personal_access_token:
        required: true
```

The documentation says reusable workflows live in `.github/workflows` and that "subdirectories of the `workflows` directory are not supported". A caller uses the `uses` keyword **directly in a job**, "and not from within job steps". The reference forms are:

- `./.github/workflows/{filename}` for a workflow in the same repository (it comes from the same commit as the caller);
- `{owner}/{repo}/.github/workflows/{filename}@{ref}` for another repository, where the `{ref}` can be "a SHA, a release tag, or a branch name". The documentation adds: "Using the commit SHA is the safest option for stability and security."

Three facts to remember. "Secrets are not automatically passed to reusable workflows" (they are passed in `secrets:` or inherited with `secrets: inherit`). If a called workflow uses `actions/checkout`, "the action checks out the contents of the repository that hosts the *caller* workflow, not the called workflow". And environment secrets cannot be passed from the caller, because `workflow_call` does not support the `environment` keyword.

**Reusable workflow or composite action?** The documentation compares them: a reusable workflow "allows you to reuse an entire workflow, with multiple jobs and steps"; a composite action "combines multiple steps that you can then run within a job step" and "cannot contain jobs". In the log, a reusable workflow shows every job and step separately; a composite action shows just the one step. If the steps must run on a different type of machine, use a reusable workflow.

> **Checked against GitHub's documentation (R295).** "Reuse workflows" and "Reusing workflow configurations".

---

## 58.2 Environments

> **New term: environment.** A named deployment target such as `staging` or `production`, with its own protection rules and secrets, that a workflow job can name.

GitHub's documentation: "Environments are used to describe a general deployment target like production, staging, or development." A job can reference **one** environment, and "any protection rules configured for the environment must pass before a job referencing the environment is sent to a runner. The job can access the environment's secrets only after the job is sent to a runner."

The protection rules the documentation lists for an environment:

| Rule | What it does |
|---|---|
| **Required reviewers** | Up to 6 people or teams; "only one of the required reviewers needs to approve the job for it to proceed"; an option prevents people from approving runs they triggered (*prevent self-review*) |
| **Wait timer** | A number of minutes to wait before the job may proceed |
| **Deployment branches and tags** | Which branches and tags may deploy to this environment |
| **Custom deployment protection rules** | Rules created with GitHub Apps |
| **Bypass** | Administrators can bypass the rules unless you turn that off |

Environments also hold **environment secrets** and **environment variables**, available "only to workflow jobs that use the environment", and only after the rules pass. A workflow that deploys to an environment appears in the repository's **Deployments** page (Chapter 43<!--ref:settings-->).

> **Checked against GitHub's documentation (R296).** "Managing environments for deployment" and "Deployment environments". The documentation notes that on the Free plan environments can only be configured for public repositories; check the page for your plan.

---

## 58.3 Deploying a website with GitHub Pages

**GitHub Pages** publishes static files (HTML, CSS, images) as a website. GitHub's documentation describes building the site with **custom workflows** made of three actions:

1. **`actions/configure-pages`** gathers information about the site.
2. **`actions/upload-pages-artifact`** packages the built site. "The Pages artifact should be a compressed gzip archive containing a single tar file. The tar file must be under 10GB in size and should not contain any symbolic or hard links."
3. **`actions/deploy-pages`** publishes the artifact. The job that uses it must have the permissions `pages: write` and `id-token: write`, must set `needs` to the build job ("not setting this parameter may result in an independent deployment that continuously searches for an artifact that hasn't been created"), and must name an environment; "the default environment is `github-pages`". The URL of the site comes out of the step as `steps.deployment.outputs.page_url`.

The documentation's deploy job:

```yaml
jobs:
  deploy:
    permissions:
      contents: read
      pages: write
      id-token: write
    runs-on: ubuntu-latest
    needs: jekyll-build
    environment:
      name: github-pages
      url: ${{steps.deployment.outputs.page_url}}
    steps:
      - name: Deploy artifact
        id: deployment
        uses: actions/deploy-pages@v4
```

**The packaging rules, tested.** The artifact rules are concrete enough to check on your own computer before you push. The recording builds a tiny site in `dist`, checks that there are no symbolic links, packs the folder as one tar file, lists the tar file, and compresses it with gzip. Then it adds a symbolic link, to show what the check would catch:

```text
$ cd bakery-site
$ find dist -type l | wc -l
0
$ tar -cf artifact.tar -C dist .
$ tar -tf artifact.tar | sort
./
./index.html
./style.css
$ gzip -c artifact.tar > artifact.tar.gz
$ gzip -t artifact.tar.gz && echo "the gzip archive is valid"
the gzip archive is valid
$ ln -s index.html dist/home.html
$ find dist -type l
dist/home.html
```

*Recorded in Bash; `ch58-deploy/expected-pages-artifact.bash.txt`.*

There are no links in `dist`; the tar file holds `index.html` and `style.css`; the gzip archive is valid. After `ln -s`, `find dist -type l` finds `dist/home.html`, which would break the rule. This is the packaging step only: it does not contact GitHub, and it is not the `upload-pages-artifact` action.

> **Checked against GitHub's documentation (R297).** "Using custom workflows with GitHub Pages" (the three actions, the packaging rules, the permissions, `needs`, the environment and the URL output; the action versions shown are those in that page: `configure-pages@v5`, `upload-pages-artifact@v4`, `deploy-pages@v4`). The local recording tests the packaging rules only.

---

## 58.4 Project 10: deploy the Sunrise Bakery website

> **Project 10.** *Goal:* publish the Sunrise Bakery site so that a merge to `main` updates the live page, with an approval on the way. *Time:* about 60 minutes. *You need:* a GitHub account, a repository with the site in a folder `site/` (Chapter 39<!--ref:ghrepo-->), and the ability to change the repository's Pages and environment settings.

1. **Build locally first.** Put `index.html` and `style.css` in `site/`. Run the packaging checks of section 58.3 on `site/` (no symbolic links; one tar file).
2. **Enable Pages with workflows.** In the repository settings, choose GitHub Actions as the source for Pages (the documentation, "Configuring a publishing source", explains the choice). The label may differ; look for the idea.
3. **Write the workflow** `.github/workflows/deploy.yml`: `on` push to `main` and `workflow_dispatch`; a `build` job that checks out the code, runs `configure-pages` and `upload-pages-artifact` with `path: site`; a `deploy` job with the permissions, `needs: build`, the `github-pages` environment and the `deploy-pages` step.
4. **Add a protection rule.** In the `github-pages` environment, add yourself (or a teammate) as a required reviewer, and limit deployment to the `main` branch.
5. **Push, approve, and look.** Merge the workflow. The deploy job waits for approval; approve it; open the URL from the job.
6. **Break it and read the log.** Introduce a mistake (for example a missing `needs`) and use Chapter 57<!--ref:wfdebug--> to find it.

*Expected result (from the documentation, not observed by this book):* the workflow builds the artifact, waits for the required reviewer, deploys, and the site is available at the URL given by `steps.deployment.outputs.page_url`. If a step differs on your account, use the "idea, not label" rule of Chapter 40<!--ref:ghtour-->.

*Checkpoint questions:* Why must the deploy job list the build job in `needs`? What does the required reviewer protect against? What would you change to allow a `staging` environment that deploys without approval?

---

## Checkpoint

## What You Learned

- A workflow with `on: workflow_call` can be called by another workflow from a job with `uses`; pin third-party references to a commit SHA.
- Reusable workflows reuse whole jobs; composite actions reuse steps.
- An environment adds approvals, wait timers, branch rules, secrets and a deployment history to a job that names it.
- A Pages deployment uses three actions, the permissions `pages: write` and `id-token: write`, `needs` on the build job and an environment; the artifact must be one tar file with no links.

## New Vocabulary

**Reusable workflow**, **environment** (introduced above).

## Commands Learned

`tar -cf`, `tar -tf`, `gzip -t`, `find -type l`.

## Common Mistakes

1. **Calling a third-party workflow by a branch name** that can change under you.
2. **Passing environment secrets from a caller.**
3. **A deploy job without `needs`.**
4. **Symbolic links in a Pages artifact.**
5. **Giving a production environment no reviewer.**

## Practice

Do the exercises in [`exercises/ch58-exercises.md`](../../../exercises/ch58-exercises.md). Project 10 is in section 58.4.

## Self-Test

1. Which key makes a workflow reusable, and where is it called from?
2. Why is a commit SHA the safest reference for a reusable workflow in another repository?
3. What does a required reviewer on an environment do?
4. Which three actions deploy a Pages site with a custom workflow?

## Before Moving On

You are ready for Chapter 59<!--ref:runners--> or Chapter 60<!--ref:wfsec--> if you can:

- [ ] write the header of a reusable workflow
- [ ] say what an environment adds
- [ ] describe the three Pages actions

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Packaging rules for a Pages artifact (no links, one tar, gzip) checked on a local folder | Locally tested: Bash 5.2 and zsh 5.9; CI | R297 (local side) |
| Reusable workflows, environments, Pages actions and permissions | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account** | R295-R297 |
| Project 10 expected result | **Documentation's description; not observed** | R297 |

## Where this leads

Chapter 59<!--ref:runners--> covers where jobs run, Chapter 60<!--ref:wfsec--> how to secure workflows, and Chapter 69<!--ref:pages--> GitHub Pages in more detail.
