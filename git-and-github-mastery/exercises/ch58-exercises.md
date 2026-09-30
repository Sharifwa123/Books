# Chapter 58 exercises — Reusable Workflows, Environments and Deployments

Attempt each exercise before you open `solutions/ch58-solutions.md`. Exercises 1 and 2 need only your computer. Project 10 (section 58.4) needs an account.

## Level 1 — Guided

**1.1 Package a site.** Make a folder `dist` with `index.html` and `style.css`. Check that it has no symbolic links, pack it with `tar -cf artifact.tar -C dist .`, list it, and check a gzip copy with `gzip -t`.

**1.2 Header of a reusable workflow.** Write the `on:` block of a workflow that can be called, with one required string input `config-path`.

## Level 2 — Partially guided

**2.1 The link rule.** Add a symbolic link to `dist` and run `find dist -type l`. Why must you fix this before a Pages deployment?

**2.2 Call it.** Write a caller job that calls `./.github/workflows/build.yml` from the same repository, and a second caller job that calls a workflow `example-org/shared/.github/workflows/deploy.yml` pinned to a commit SHA.

## Level 3 — Independent

**3.1 Environment plan.** Design two environments, `staging` and `production`, for the bakery site. Say which protection rules each gets and which branches may deploy to each.

**3.2 Reusable or composite?** For each need, choose reusable workflow or composite action: (a) three jobs on different operating systems; (b) three steps that set up a tool in any job; (c) a shared deployment pipeline for ten repositories.

## Level 4 — Professional scenario

**4.1 Project 10.** Do Project 10 in section 58.4. Write down each step where your screen differed from the description.

## Level 5 — Troubleshooting

**5.1** A deploy job starts before the site is built and cannot find an artifact. What is missing from the job?

**5.2** A called workflow's checkout step shows the wrong files. Explain from the documentation which repository it checked out.

**5.3** A team passes an environment secret from a caller workflow and the called workflow gets nothing. Why?
