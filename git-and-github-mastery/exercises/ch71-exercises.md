# Chapter 71 exercises — GitHub Packages and Containers

Attempt each exercise before you open `solutions/ch71-solutions.md`. Exercises 2.1 and 2.2 use your terminal; nothing needs a GitHub account, a registry or Docker.

## Level 1 — Guided

**1.1 Vocabulary.** Explain package, registry and package manager in one sentence each.

**1.2 Names.** Which of these npm package names could be published to GitHub's npm registry according to the chapter: `wordcount`, `@Ada/wordcount`, `@ada/wordcount`?

## Level 2 — Partially guided

**2.1 The mapping.** In a sandbox repository, create `package.json` with the name `@ada/wordcount` and an `.npmrc` that maps the scope `@ada` to `https://npm.pkg.github.com`. Commit both.

**2.2 The token.** Create a user-level file (in your home folder, not in the repository) containing a made-up token line, and prove with `git grep` that the token is not in the repository.

## Level 3 — Independent

**3.1 A check script.** Write a shell script that fails if `_authToken` appears in any tracked file.

**3.2 Two models.** Describe granular and repository-scoped package permissions and give one advantage of each.

## Level 4 — Professional scenario

**4.1 A publishing workflow.** Write a design (in words, no YAML needed) for publishing a package when a release tag is pushed: the trigger, the credential, who may change the workflow, and what could go wrong.

## Level 5 — Troubleshooting

**5.1** You linked a repository to a package after publishing it, and the repository's readers still cannot read the package. Why, according to the chapter?

**5.2** A token appears in a committed `.npmrc`. List the steps in order.
