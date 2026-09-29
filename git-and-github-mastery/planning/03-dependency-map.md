# 03 — Technical Dependency Map

Rule: no chapter may use a term or skill not taught in an earlier chapter (or defined inline at first use with a forward pointer).

| Section | Requires (chapters) | Key prerequisite concepts |
|---------|--------------------|---------------------------|
| Ch 2 Files & paths | 1 | OS, app |
| Ch 3 Editors | 2 | file, extension |
| Ch 4 Internet | 1 | computer, app |
| Ch 5 Accounts | 4 | server, client |
| Ch 6 Terminal | 2, 3 | path, folder |
| Ch 7–10 Version-control concepts | 2, 4 | files, server |
| Ch 11 Install/config | 5, 6 | terminal, admin permission |
| Ch 12 Core model | 7–10, 11 | history, snapshot idea |
| Ch 13–16 First commits | 6, 11, 12 | terminal, identity config, model |
| Ch 17–19 Branch/merge/conflicts | 13–16 | commit, HEAD, history |
| Ch 20 Remotes | 4, 5, 17 | server, auth, branch |
| Ch 21 Stash/tools | 13–18 | working tree, index |
| Ch 22–23 Undo/reflog | 12, 14, 16–18 | HEAD, hashes, reset targets |
| Ch 24 Rebase | 18, 19, 22, 23 | merge, conflicts, reflog safety net |
| Ch 25 Cherry-pick/bisect | 14, 18, 22 | commit ranges |
| Ch 26 Tags | 14, 20 | refs, remotes |
| Ch 27 Object model | 12–18 | commit, tree idea (introduced informally earlier) |
| Ch 28 Big repos | 20, 27 | clone, objects |
| Ch 29 Customising | 11, 15, 27 | config, hooks need shell scripts (introduced briefly) |
| Ch 30 Git security | 5, 15, 20, 22–24 | auth, ignore, history rewriting |
| Ch 31 Workflows | 17–20, 24, 26 | branching, merging, tags |
| Ch 32–36 GitHub intro | 20, 30 (auth), 5 | remotes, tokens/SSH |
| Ch 37–38 Repos/Issues | 35, 36 | README, Markdown (introduced in Ch 37) |
| Ch 39–40 PRs/Review | 17–19, 20, 37, 38 | branches, merge, remotes, issues |
| Ch 41–42 Projects/Discussions | 38, 39 | issues, PRs |
| Ch 43–44 Collaboration/protection | 39, 40 | PRs, review |
| Ch 45 Insights | 35–39 | commits, PRs |
| Ch 46–47 CI/CD, YAML | 6, 39 | terminal, PR |
| Ch 48–52 Actions | 46, 47, 44 | YAML, PR events, protections |
| Ch 53–54 GitHub security | 30, 48–51 | secrets, workflows |
| Ch 55–58 Open source/licences/releases | 26, 37–40, 43 | fork, PR, tag |
| Ch 59–62 Org/Pages/Codespaces/Packages | 43, 48–50 | roles, workflows |
| Ch 63 Deployment | 4, 48–51 | servers, secrets, environments |
| Ch 64–65 CLI/API | 6, 34, 38–39 | terminal, tokens |
| Ch 66 Other features | 59 | organisations |
| Ch 67–68 Scenarios/capstone | Parts I–X | everything |
| Ch 69–70 Troubleshooting | Parts III–VIII | error vocabulary |
| Ch 71–72 Mastery | all | all |

## Known forward-reference risks to manage
1. Ch 12 (core model) mentions remotes before Ch 20 — resolved by a one-paragraph "preview" flagged as such.
2. Ch 15 (`.gitignore`) mentions secrets before Ch 30 — brief warning, full treatment later.
3. Ch 14 needs "hash" — defined informally at first use, formally in Ch 27.
4. Ch 30 (Git security) references GitHub tokens before Part V — teach credentials at Git level first; GitHub specifics in Ch 34.
5. Ch 37 needs Markdown — taught inside Ch 37 before README work.
