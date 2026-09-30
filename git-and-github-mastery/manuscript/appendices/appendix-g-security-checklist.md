# Appendix G — Security Checklist

A checklist that gathers the security advice of the book. Tick what you have done; a box you cannot tick is a task. **GitHub features vary by plan and repository visibility**: use the Security tab of your repository to see what is available to you (Chapter 62<!--ref:ghsec-->). Items marked *Git* work anywhere; items marked *GitHub* were taken from GitHub's documentation and were not run on a live account.

## G.1 You and your account

- [ ] Two-factor authentication is on, and recovery codes are stored safely (*GitHub*; Chapter 38<!--ref:ghauth-->).
- [ ] You sign in with a password manager and a password used nowhere else (Chapter 6<!--ref:accounts-->).
- [ ] Your SSH key has a passphrase and you know where the private key is (Chapter 38<!--ref:ghauth-->).
- [ ] Personal access tokens have the fewest scopes, an expiry, and a note saying what they are for; old ones are revoked (Chapter 63<!--ref:secpractice-->).
- [ ] You would recognise a phishing message: unexpected urgency, a link to a look-alike address (Chapter 6<!--ref:accounts-->).

## G.2 Secrets

- [ ] No password, key or token is in the repository, in its history, in an issue or in a log (Chapter 33<!--ref:gitsec-->).
- [ ] `.env` and other local settings files are in `.gitignore` **before** the first `git add` (Chapter 18<!--ref:tracking-->).
- [ ] A forced add (`git add -f`) of an ignored file is treated as a warning sign (Chapter 77<!--ref:capstone-->).
- [ ] Secret scanning and push protection are on where available (*GitHub*; Chapter 62<!--ref:ghsec-->).
- [ ] If a secret leaks: **revoke first**, then clean up (Chapter 79<!--ref:playbooks-->).

## G.3 Repository and access

- [ ] `SECURITY.md` says how to report a vulnerability privately (Chapter 62<!--ref:ghsec-->).
- [ ] Roles are the least that work; the base permission is low; at least two owners in an organization (Chapter 68<!--ref:orgs-->).
- [ ] The default branch is protected: pull requests, required checks, no force pushes (*GitHub*; Chapter 50<!--ref:protect-->).
- [ ] Deploy keys and outside collaborators are reviewed regularly (Chapter 68<!--ref:orgs-->).
- [ ] Commits are signed where your team requires it, and you know a signature shows a key, not a good change (Chapter 63<!--ref:secpractice-->).

## G.4 Dependencies and supply chain

- [ ] Dependabot alerts and updates are on (*GitHub*; Chapter 62<!--ref:ghsec-->).
- [ ] Every dependency was chosen on purpose: maintainer, licence, activity (Chapter 71<!--ref:packages-->).
- [ ] Lock files are committed (Chapter 62<!--ref:ghsec-->).
- [ ] Artifacts people run come with a checksum, and where possible an attestation (Chapter 63<!--ref:secpractice-->).

## G.5 Workflows

- [ ] `permissions` is set to the least that works, at the top of each workflow (Chapter 60<!--ref:wfsec-->).
- [ ] Third-party actions are pinned to a full commit name from the action's own repository (Chapter 60<!--ref:wfsec-->).
- [ ] No untrusted value (title, branch name, body) is pasted into a `run:` script; use `env` (Chapter 60<!--ref:wfsec-->).
- [ ] `pull_request_target` and `workflow_run` never check out code from a fork (Chapter 60<!--ref:wfsec-->).
- [ ] Self-hosted runners are not used for public repositories (Chapter 59<!--ref:runners-->).
- [ ] Deployment credentials are environment secrets, least-privilege and, where possible, short-lived (Chapter 72<!--ref:deploy-->).

## G.6 Your computer

- [ ] You read a script before you run it, especially one that deletes things (Chapter 81<!--ref:assessment-->).
- [ ] Downloads are from official sources and checked against a published checksum (Chapter 13<!--ref:install-->).
- [ ] Extensions and integrations (editor, `gh`, apps) are treated as third-party code (Chapters 73<!--ref:ghcli--> and 74<!--ref:api-->).
