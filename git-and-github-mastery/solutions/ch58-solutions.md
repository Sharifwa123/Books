# Chapter 58 solutions

## Level 1
**1.1** As in the recording: `find dist -type l | wc -l` prints 0; `tar -tf artifact.tar` lists `./`, `./index.html` and `./style.css`; `gzip -t` succeeds silently.

**1.2** `on:` then `workflow_call:` then `inputs:` then `config-path:` with `required: true` and `type: string`.

## Level 2
**2.1** The documentation says the tar file "should not contain any symbolic or hard links", so the artifact would break the rule.

**2.2** `uses: ./.github/workflows/build.yml` in one job; `uses: example-org/shared/.github/workflows/deploy.yml@<full commit SHA>` in another.

## Level 3
**3.1** For example: staging with no reviewers, deploying from any branch; production with one required reviewer, prevent self-review, and only `main` allowed.

**3.2** (a) Reusable workflow (different machines); (b) composite action (steps); (c) reusable workflow (central maintenance of a whole pipeline).

## Level 4
**4.1** Answers vary.

## Level 5
**5.1** `needs: <build job>`.

**5.2** The repository that hosts the caller workflow: "the action checks out the contents of the repository that hosts the caller workflow, not the called workflow".

**5.3** Environment secrets cannot be passed from the caller, because `workflow_call` does not support the `environment` keyword; use the environment inside the called job or pass an ordinary secret.
