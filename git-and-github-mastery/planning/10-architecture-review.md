# 10 — Architecture Review (before any drafting)

Reviewed `02-table-of-contents-and-curriculum.md` against the master prompt and the latest instructions. Findings are grouped; **proposed changes are not yet applied to 02** — they are consolidated in the v2 outline below for approval.

## A. Gaps found
### Beginner computer concepts
1. **Plain text vs formatted text, character encoding, newlines** — needed for line-endings (Ch 15/29) and for Markdown. Missing.
2. **PATH / environment variables** — needed to understand "git is not recognized" and install checks. Only implied.
3. **Shell differences** (Command Prompt, PowerShell, Git Bash, bash/zsh) — cross-platform learners will hit these immediately. Missing.
4. **Downloading, zip files, installers, admin permission, package managers** — thin.
5. **Cloud-sync tools vs version control** (Dropbox/Drive/OneDrive) — the most common beginner alternative; missing from Part II.
6. **Markdown** — first used in README/Issues; was buried in Ch 37.

### Git
7. Bare repositories as local remotes (verified) — missing; would let Part III teach remotes without an account.
8. Git configuration scopes/includes (verified as a real source of confusion in the sandbox) — only implied.
9. Object-inspection commands (`ls-files`, `show-ref`, `fsck`, `archive`) — add to object-model chapter.
10. History-rewriting tools for secret removal (filter-repo/BFG vs discouraged filter-branch) — must be explicit and verified.
11. Reading official documentation (man pages, `-h`, reference manual) — an outcome (33) with no chapter.

### GitHub
12. **Notifications, stars, watching** — missing.
13. **Markdown on GitHub / README rendering** — missing as its own topic.
14. **Wiki, Deployments/Environments tab, repository Settings tour, Security tab tour** — listed in the prompt, not in the TOC.
15. **Actions expressions & contexts, conditionals, concurrency, timeouts, self-hosted runner risks, workflow debugging/re-runs** — missing details in Ch 48–51.
16. **Actions billing/usage limits** — needed for honest guidance; must be verified, else omitted.
17. Merge queue / auto-merge — verify existence and availability before mention.
18. Templates (repository templates), Gists — optional; decide after research.

### Structure / pedagogy
19. **Size risk:** ~72 chapters is very long. Recommendation: keep one book, tag every chapter **[Core]** (all readers) or **[Deep]** (skip on first read), and mark a "First-read path".
20. **Appendices A–L** were listed by reference only; now enumerated below.
21. **Exercises/solutions/diagrams** need persistent, separate folders (created now).
22. **Security is spread out** (Ch 15, 30, 34, 51, 53–54). Keep, but add a running "Security note" callout and one consolidated Appendix G.
23. Forward reference: Ch 12 previews remotes; Ch 15 mentions secrets before Ch 30 — flagged in 03; acceptable with one-line previews.

## B. Recommended additions / moves (v2)
| Change | Where |
|--------|-------|
| New: "Text, Encodings and Newlines" | Part I, after Ch 3 |
| New: "Markdown in Five Pages" | Part I (before Part II) |
| Expand Ch 6: shells (cmd/PowerShell/Git Bash/bash/zsh), PATH, environment variables, cross-shell command table | Part I |
| Expand Ch 7: cloud sync/backup vs version control | Part II |
| Ch 20 opens with **local bare-repo remote** exercise before GitHub | Part III |
| New short chapter: "Configuration Scopes and Includes" | Part III after Ch 11 (or merged into 11) |
| New: "Reading Git and GitHub Documentation" | end of Part IV; revisited in Part XIII |
| Ch 27 adds `ls-files`, `show-ref`, `fsck`, `archive` | Part IV |
| Ch 30 adds verified secret-removal tooling | Part IV |
| New: "Notifications, Stars and Watching" | Part V |
| New: "Repository Settings, Security Tab and Wiki Tour" | Part VI |
| Ch 49 split: (a) Expressions/contexts/conditionals, (b) practical workflows, (c) debugging and re-running workflows | Part VII |
| New: "Self-Hosted Runners, Concurrency and Limits" (only verified facts) | Part VII |
| Appendix list made explicit | Back matter |
| Chapter tags [Core]/[Deep] and first-read path | All |

## C. Enumerated appendices
A Git command reference · B GitHub/CLI reference · C Common Git errors · D GitHub Actions YAML reference · E Git terminology map · F GitHub terminology map · G Security checklist · H Professional repository checklist · I Open-source project checklist · J Deployment checklist · K Git recovery decision tree · L Learning roadmap after the book. Plus: M (proposed) Shell command equivalence table; N (proposed) Sources log / verification dates.

## D. v2 outline (titles only; detail stays in 02 unless noted)
**Part I — Computers and Digital Projects**: 1 What a Computer Is · 2 Files, Folders and Paths · 3 Editors and Project Folders · **3A Text, Encodings and Newlines** · 4 Internet, Web and Servers · 5 Accounts, Passwords and Trust · 6 The Terminal Without Fear (shells, PATH, env vars) · **6A Markdown in Five Pages**
**Part II — Version Control**: 7 The Problem of Changing Files (incl. cloud sync ≠ version control) · 8 Short History · 9 Centralized vs Distributed · 10 Git, GitHub, GitLab, Bitbucket
**Part III — Learning Git**: 11 Install and Configure (incl. scopes/includes) · 12 Core Model · 13 First Repository · 14 History and Diffs · 15 Tracking/Ignoring · 16 Good Commits · 17 Branching · 18 Merging · 19 Conflicts · 20 Remotes (**local bare remote first**) · 21 Stash and Small Tools
**Part IV — Professional Git**: 22 Undoing · 23 Reflog Recovery · 24 Rebase · 25 Cherry-pick/Bisect/Patches · 26 Tags/Versioning · 27 Object Model · 28 Big Repos (worktree, submodule, subtree, sparse/partial/shallow, LFS, monorepo) · 29 Customising Git · 30 Git Security · 31 Workflows · **31A Reading Documentation**
**Part V — GitHub Intro**: 32 What GitHub Is · 33 Account and Profile · 34 Authentication · 35 First GitHub Repo · 36 Interface Tour · **36A Notifications, Stars, Watching**
**Part VI — Working with GitHub**: 37 Professional Repos and READMEs · **37A Repository Settings, Security Tab, Wiki Tour** · 38 Issues · 39 Pull Requests · 40 Code Review · 41 Projects · 42 Discussions · 43 Collaboration and Access · 44 Protection and Rulesets · 45 Insights
**Part VII — Automation**: 46 CI/CD Concepts · 47 YAML · 48 Actions Fundamentals · **48A Expressions, Contexts, Conditionals** · 49 Practical Workflows · **49A Debugging and Re-running Workflows** · 50 Reusable Workflows, Environments, Deployments · **50A Self-Hosted Runners, Concurrency, Limits** · 51 Securing Workflows · 52 Actions vs External CI
**Parts VIII–XIII** unchanged from 02 (Ch 53–72).

Chapter count: 72 → 81 (no renumbering yet; "A" chapters renumber at finalisation).

## E. Coverage check against the prompt
All prompt topics map to a chapter. Items now explicitly homed: Markdown, encodings, PATH, shells, notifications, Wiki, Deployments/Environments tab, expressions/contexts, debugging, self-hosted runners, docs reading, bare remote. Items still conditional on research: merge queue, Gists, repository templates, LFS quotas, Actions limits/pricing, plan matrices, current UI labels.

## F. Decisions I recommend (need your OK; defaults applied if you don't object)
1. **Shell convention:** teach Git commands identically everywhere; show file-system commands in bash/zsh with a PowerShell column in Appendix M; on Windows, use Git Bash as the primary shell for consistency (to be confirmed once Git for Windows docs are verified).
2. **One book, tagged [Core]/[Deep]**, rather than splitting into volumes.
3. **Chapter numbering** finalised only after research changes the list.
