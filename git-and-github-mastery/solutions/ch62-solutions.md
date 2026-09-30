# Chapter 62 solutions

## Level 1
**1.1** Dependency graph: lists what you depend on. Alerts: warn of known vulnerabilities in them. Security updates: open a pull request with the fix. Version updates: keep dependencies current. Secret scanning: finds committed secrets. Push protection: blocks a push that contains a secret. Code scanning: finds weaknesses in your own code.

**1.2** Read the alert; rotate the credential; then, only if needed, remove it from history.

## Level 2
**2.1** `mkdir -p .github`, then write the five-line example from the chapter and `cat .github/dependabot.yml`.

**2.2** For example: "Report vulnerabilities privately to security@example.org. Do not open a public issue. Include the version and steps to reproduce. We will reply within a reasonable time." The address is an example.

## Level 3
**3.1** Security updates react to a vulnerability alert and open a pull request that moves to the minimum fixed version. Version updates work on a schedule and keep dependencies up to date whether or not there is a vulnerability. Both open pull requests that you review.

**3.2** Version updates, which can update action references in workflow files. Pinning fixes a version; updating moves it forward in a reviewed pull request.

## Level 4
**4.1** A sensible answer: `SECURITY.md`, Dependabot alerts, secret scanning, push protection, version updates for dependencies and actions; postpone code scanning if it is not available for your repository type or if you have no time to triage alerts. Justify each in a sentence. Check current availability first.

## Level 5
**5.1** Remove the secret from the commit and push again, and rotate the credential if it was ever exposed. Never bypass the protection or push the secret anyway.

**5.2** Read the failure, the changelog in the pull request and the release notes. Fix the code, or postpone the update with a note; do not merge a failing pull request.
