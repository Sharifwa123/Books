# Chapter 62 exercises — GitHub Security Features

Attempt each exercise before you open `solutions/ch62-solutions.md`. Exercises 2.1 and 2.2 use your terminal; none needs a GitHub account.

## Level 1 — Guided

**1.1 Match.** Match each feature to its job: dependency graph, Dependabot alerts, security updates, version updates, secret scanning, push protection, code scanning.

**1.2 Order.** A secret is found in a commit. Put these in order: rotate the credential, remove it from history, read the alert.

## Level 2 — Partially guided

**2.1 Write it.** In a sandbox folder, create `.github/dependabot.yml` from the documentation's minimal example (npm, directory `/`, interval `daily`). Read it back with `cat`.

**2.2 A policy.** Write a `SECURITY.md` of four lines: how to report, where, what not to do, and what the reporter can expect. Use an example address that does not exist.

## Level 3 — Independent

**3.1 Explain.** In three sentences, explain the difference between Dependabot security updates and Dependabot version updates.

**3.2 Actions.** Which Dependabot feature helps to keep pinned actions current (Chapter 60<!--ref:wfsec-->)? Say why pinning and updating go together.

## Level 4 — Professional scenario

**4.1 A small project.** You maintain a small open-source project. List, in order, the five things you would switch on this week, and the one you would postpone, with a reason each.

## Level 5 — Troubleshooting

**5.1** A push is refused with a message that it contains a secret. What are the two safe next steps, and what must you never do?

**5.2** Dependabot opened a pull request that fails your tests. What do you do?
