---
key: secpractice
number: 63
tag: Core
first_read: part
status: draft
requires: [ghsec, collab]
ledger: [R311, R312, R313]
---
# Chapter 63 — Repository Security Practice [Core]

**In this chapter**

- least privilege in practice
- where secrets live: repository, environment and organization
- signed commits on GitHub
- artifacts: checksums and attestations
- the supply chain, and the difference between Git's security and GitHub's

> **How to read this chapter.** GitHub statements come from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026) and were **not run on a live account**. The checksum demonstration is a local recording; it needs `sha256sum`, which macOS does not provide under that name (it has `shasum -a 256`), so this book's recording was made on Linux only.

**Before you start.** Chapter 62<!--ref:ghsec--> and Chapter 49<!--ref:collab-->.

---

## 63.1 Least privilege in practice

Chapter 6<!--ref:accounts--> introduced least privilege; Chapter 60<!--ref:wfsec--> applied it to a workflow token. GitHub's documentation on credentials: "When generating credentials, we recommend that you grant the minimum permissions possible. For example, instead of using personal credentials, use deploy keys or a service account. Consider granting read-only permissions if that's all that is needed." When you generate a personal access token, "select the fewest scopes necessary". It also suggests a **GitHub App** instead of a personal token, because an app "uses fine-grained permissions and short lived tokens" and "is not tied to a user, so the workflow will continue to work even if the user who installed the app leaves your organization".

The pattern: **give each person, token and workflow the smallest access that does the job, and no permanent extra.** Chapter 49<!--ref:collab--> covered roles for people; this is the same idea for machines.

---

## 63.2 Where a secret lives

Actions secrets can be stored at three levels. From the documentation: "Secrets allow you to store sensitive information in your organization, repository, or repository environments."

| Level | Available to | Notes |
|---|---|---|
| Repository | Workflows in that repository | Simple; anyone who can write workflows there can use it in a run |
| Environment | Jobs that target that environment (Chapter 58<!--ref:wfadvanced-->) | You can require reviewers: "A workflow job cannot access environment secrets until approval is granted" |
| Organization | Repositories the organization allows | "you can use a policy to limit access by repository" |

Other rules from the documentation: a workflow "can only read a secret if you explicitly include the secret in a workflow"; secrets are encrypted before they reach GitHub; and log redaction "is not guaranteed" (Chapter 60<!--ref:wfsec-->). Choose the narrowest level that works: an environment secret for a production deployment is stronger than a repository secret, because approval gates it.

> **Checked against GitHub's documentation (R311).** "About secrets" (Actions concepts) and its links.

---

## 63.3 Signed commits on GitHub

Chapter 33<!--ref:gitsec--> signed a commit locally and asked Git to verify it. GitHub can show the result. Its documentation: "If a commit or tag has a GPG, SSH, or S/MIME signature that is cryptographically verifiable, GitHub marks the commit or tag 'Verified' or 'Partially verified.'" The default statuses:

| Status | Meaning |
|---|---|
| Verified | signed, and the signature verified |
| Unverified | signed, but the signature could not be verified |
| (none) | not signed |

Points the documentation makes:

- "For most individual users, GPG or SSH will be the best choice for signing commits." SSH signatures "are the simplest to generate"; you can upload an existing authentication key to use as a signing key. A GPG key "can expire or be revoked".
- Once verified on GitHub, the record persists: it "can't be edited and will persist ... even if signing keys are rotated, revoked, or if contributors leave the organization".
- **Signing a commit is not the same as signing off** (`git commit -s`, which only adds a line of text; Chapter 64<!--ref:oss--> returns to it).
- **Vigilant mode** (off by default) changes how unsigned commits from you are displayed.

A signature tells you *which key* made a commit, not that the change is good.

> **Checked against GitHub's documentation (R312).** "About commit signature verification". The SSH-signing behaviour of Git itself was not run (Chapter 33<!--ref:gitsec--> noted that `ssh-keygen` was unavailable).

---

## 63.4 Artifacts: checksums and attestations

An **artifact** is a file your build produces: a package, an archive, a program. People who download it want to know it is the file you published.

**A checksum** is a fingerprint computed from the file's bytes (Chapter 30<!--ref:objects--> used the same idea for Git objects). Publish it beside the file; the downloader computes it again and compares.

```text
$ mkdir release && printf 'app v1\n' > release/app.txt
$ tar -cf app.tar release
$ sha256sum app.tar > app.tar.sha256
$ cat app.tar.sha256 | awk '{print length($1), $2}'
64 app.tar
$ sha256sum -c app.tar.sha256
app.tar: OK
$ printf 'tampered\n' >> app.tar
$ sha256sum -c app.tar.sha256 || echo "verification failed: the file changed"
app.tar: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
verification failed: the file changed
```

*Recorded in Bash; `ch63-secpractice/expected-checksum.bash.txt`.*

The fingerprint printed as 64 characters (SHA-256). After one line was appended, the check said `FAILED`. Two cautions: a checksum published on the *same* page as the file proves only that the download was not corrupted, not that the publisher is honest, because an attacker who replaces the file can replace the checksum; and Chapter 66<!--ref:releases--> returns to publishing.

**Artifact attestations** are GitHub's stronger answer. The documentation: they use **Sigstore**, an open-source signing project, to create a signed statement linking an artifact to "the source code and the build instructions that produced" it; reusable workflows can raise the **SLSA** level. It also warns: "artifact attestations are _not_ a guarantee that an artifact is secure", and "Generating attestations alone doesn't provide any security benefit, the attestations must be verified". It advises signing "binaries people will run, packages people will download", and **not** "frequent builds that are just for automated testing" nor "individual files like source code".

> **Checked against GitHub's documentation (R313).** "Artifact attestations" (concept). The checksum demonstration is locally tested; attestations were not run.

---

## 63.5 The supply chain

Your software is made of your code, your dependencies, your build tools, your workflows' actions, and the machines that run them. An attacker needs only one weak link. The features of Chapter 62<!--ref:ghsec--> and the habits of Chapter 60<!--ref:wfsec--> each cover a link:

| Link | Protection |
|---|---|
| Dependencies | dependency graph, Dependabot, review of updates |
| Actions used by workflows | pin to commit SHAs; keep updated |
| Secrets | least privilege, scoping, push protection |
| Source | protected branches, reviews, signed commits (Chapters 50<!--ref:protect--> and 46<!--ref:review-->) |
| Outputs | checksums, attestations |

---

## 63.6 Git security versus GitHub security

Keep the two apart. **Git** is a local tool: it stores content by hash, can sign commits, and has no notion of who may push; a rewritten history is only detected if someone compares hashes. **GitHub** adds accounts, permissions, branch protection, scanning and audit records around it. A protection that GitHub enforces (a required review) does not exist in a plain clone on someone's computer, and a protection Git offers (a signature) means little unless someone verifies it. When you read that "the repository is secure", ask *which layer* is meant.

---

## Checkpoint

## What You Learned

- Give people, tokens and workflows the minimum access.
- Secrets can be scoped to a repository, an environment (with approval) or an organization.
- GitHub marks signed commits Verified or Unverified; a signature says which key, not that the change is good.
- A checksum detects change; attestations link an artifact to its source and build, and must be verified.
- The supply chain has many links; Git and GitHub protect different layers.

## New Vocabulary

**Checksum**, **artifact**, **attestation**, **supply chain** (see the glossary).

## Commands Learned

`sha256sum` and `sha256sum -c`, on Linux.

## Common Mistakes

1. **Using a personal token where a narrower credential would do.**
2. **Storing a production secret at repository level when an environment gate is possible.**
3. **Treating "Verified" as "reviewed and safe".**
4. **Publishing a checksum only where an attacker could also replace it.**

## Practice

Do the exercises in [`exercises/ch63-exercises.md`](../../../exercises/ch63-exercises.md).

## Self-Test

1. Name the three levels at which Actions secrets can be stored.
2. What does an environment's required reviewer add?
3. What does "Verified" mean on a commit?
4. Why is a checksum next to the file weak evidence?
5. What is the difference between Git's security and GitHub's?

## Before Moving On

You are ready for Part IX if you can:

- [ ] choose the narrowest home for a secret
- [ ] make and verify a checksum
- [ ] explain what a signature does and does not show

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Checksum creation, matching and failure after a change | Locally tested: Bash 5.2 and zsh 5.9, Linux `sha256sum`; CI | R313 (local side) |
| Credential guidance, secret levels, signature statuses and persistence, attestations | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account** | R311-R313 |

## Where this leads

Part IX turns from protecting a project to sharing it: Chapter 64<!--ref:oss--> begins open source.
