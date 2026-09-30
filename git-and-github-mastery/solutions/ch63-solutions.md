# Chapter 63 solutions

## Level 1
**1.1** Repository (a secret one project's workflows use), environment (a production credential gated by required reviewers) and organisation (a shared secret limited by a policy to chosen repositories).

**1.2** Verified, Unverified, and no status for an unsigned commit.

## Level 2
**2.1** For example `printf 'a\n' > f`, `sha256sum f > f.sha256`, `sha256sum -c f.sha256` prints `f: OK`; after `printf 'b\n' >> f` the check prints `f: FAILED`.

**2.2** It has fine-grained permissions and short-lived tokens, and it is not tied to a person who may leave.

## Level 3
**3.1** An attacker who can replace the file can replace the checksum on the same page. An attestation is a signed statement linking the artifact to its source and build, which a consumer can verify against a policy.

**3.2** A signature shows which key made the commit, not that the change is correct or safe; a compromised or careless key holder still produces Verified commits.

## Level 4
**4.1** An environment secret, with required reviewers for the production environment, a credential with the fewest permissions the deployment needs, and where possible a short-lived credential instead (Chapter 60<!--ref:wfsec-->).

## Level 5
**5.1** A corrupted download, a changed or replaced file, or a wrong checksum file. First download again, then compare from a second source before running the file.

**5.2** Whether the key used is registered with your account, and whether the commit author's email matches an identity for that key.
