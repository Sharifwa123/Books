# 01 — Learning Outcomes

Levels: **B**eginner, **I**ntermediate, **A**dvanced, **E**xpert/Mastery. Each outcome is assessed in the final mastery assessment (see 05).

## Computer foundation (B)
1. Explain hardware vs software, operating system, file, folder, path, extension, hidden file, permission.
2. Navigate, create, copy, move, delete files/folders in a graphical file manager and in a terminal.
3. Explain internet vs web, client vs server, local vs remote, account/authentication.

## Git core (B→I)
4. Explain version control and why Git exists in plain language.
5. Install, verify and configure Git (identity, default branch, editor, line endings).
6. Describe the working tree / index / repository / commit / HEAD / branch / tag / remote model and draw it.
7. Initialise a repo; track, stage, commit; write good commit messages; read `status`, `log`, `diff`, `show`.
8. Write correct `.gitignore` files; explain tracked/untracked/ignored.
9. Create, switch, merge, rename and delete branches; distinguish fast-forward from three-way merges.
10. Resolve merge conflicts by reading markers, and abort safely.
11. Work with remotes: add, fetch, pull, push, upstream tracking; explain fetch vs pull.

## Git professional (I→A→E)
12. Undo mistakes with `restore`, `reset` (all modes), `revert`, `reflog`; recover lost commits and deleted branches.
13. Use rebase (basic and interactive) and decide between merge and rebase using stated trade-offs.
14. Use tags (lightweight/annotated), semantic versioning, and explain tag vs GitHub Release.
15. Use stash, cherry-pick, bisect, blame, grep, clean, worktree, submodule/subtree, sparse/partial/shallow clone.
16. Explain Git's object model (blob, tree, commit, tag, refs, packfiles) and use plumbing commands to inspect it.
17. Configure hooks, aliases, attributes, credential helpers, signing, rerere, maintenance, LFS.
18. Choose and justify a workflow (GitHub Flow, Git Flow, trunk-based, fork-based, release branches).
19. Handle a leaked secret correctly (revoke first, then clean history), and explain why deleting the file is not enough.

## GitHub (B→I→A)
20. State the difference between Git and GitHub; create/secure an account (2FA, passkeys, recovery).
21. Authenticate using HTTPS + token/credential manager and SSH keys; explain public vs private key and authentication vs authorization.
22. Create and manage repositories, READMEs, licenses, topics, releases, visibility.
23. Use Issues, templates, labels, milestones, Projects, Discussions; choose between them.
24. Open, review, update and merge pull requests (merge/squash/rebase options); explain PR vs `git merge`.
25. Perform and receive constructive code review.
26. Collaborate: collaborators, teams, roles, forks, upstream sync, CODEOWNERS, community health files.
27. Configure branch protection/rulesets; explain the difference.
28. Write GitHub Actions workflows (triggers, jobs, steps, runners, secrets, variables, artifacts, caching, matrices, reusable workflows, environments, permissions) for testing, linting, building, deploying, releasing, scheduled tasks and issue automation.
29. Apply GitHub security features (Dependabot, code/secret scanning, push protection, advisories, security policy, least-privilege Actions permissions, OIDC concept).
30. Use Pages, Packages, Codespaces/dev containers, `gh` CLI, REST/GraphQL API basics, webhooks/Apps concepts; describe organisations and Enterprise at concept level.
31. Contribute to and create an open-source project with correct licensing.

## Independence (E)
32. Diagnose an unfamiliar Git/GitHub error using status, logs, reflog and documentation; select a safe fix; explain what was done.
33. Read official Git and GitHub documentation without help.
34. Design and defend a Git/GitHub workflow for a given team and project.
