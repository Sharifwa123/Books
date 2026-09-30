# Appendix N — Sources and Verification Log

This book separates what was **checked** from what was **assumed**. Every claim that could be wrong was entered in a research ledger with an evidence class. This appendix summarises the ledger and lists what remains open. The full ledger is the file `research/research-ledger.csv` in the book's companion repository (https://github.com/Sharifwa123/Books, folder `git-and-github-mastery`), and the list of fetched sources with their SHA-256 values is `research/sources-manifest.csv` in the same place.

## N.1 Evidence classes

| Evidence class | Rows | Meaning |
|---|---|---|
| Both officially verified and locally tested | 127 | compared with an official source and run in the authoring environment |
| Officially verified (docs only) | 113 | compared with an official source; not run |
| Time-sensitive (unverified) | 56 | about a platform that changes; not yet checked |
| Locally tested | 34 | run in the authoring environment; no official source consulted |
| Needs re-verification | 23 | checked once; must be checked again before publication |
| Not applicable | 3 | a general concept with no product claim |

Total rows: 356.

## N.2 What was tested, and where

- **Git:** every command shown was run in Bash and zsh on Git 2.43.0 (the Linux package in the authoring environment, a sandbox used by the author and the AI assistant) and re-run in continuous integration on the runner's Git (2.55.0) and on Git 2.56.0 built from source. Where newer versions print different text, alternate recordings are kept and noted.
- **GitHub:** statements were compared with the `github/docs` repository at commit `2eaab0b` (29 September 2026) and the `github/site-policy` repository, both read from their public sources. **No statement about GitHub was checked on a live account**; the book says so wherever it matters (a signed-in account of the plan).
- **Licences:** licence summaries come from GitHub's `choosealicense.com` data and the SPDX licence list (secondary sources); the official pages could not be read. The book's own licences (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International for the text, the MIT License for code samples) are stated on its copyright page; the official Creative Commons pages could not be read from the testing computer, and the complete legal code is not reproduced in the book.
- **Quotations:** short quotations from GitHub's documentation are used with attribution; that documentation is published under the Creative Commons Attribution 4.0 licence (as stated in its repository), and the quoted passages stay under it, not under this book's licence. Quotations from other sources stay under their own terms.
- **Other tools:** the GitHub CLI 2.102.0 (checksum-verified download), `git-filter-repo` 2.47.0, PyYAML 6.0.1, OpenSSL.

## N.3 Where the sources came from

| Host | Files fetched |
|---|---|
| raw.githubusercontent.com | 138 |

Files fetched with the book's tool are hashed in the manifest, so a reader can check that a source has not changed since it was read.

## N.4 What is still open (79 ledger rows)

These rows were planned during research and could not be verified from an official source at the time (the official hosts were blocked, or the claim needs a live account). Many are covered in part by later, chapter-level rows; they remain open until each claim is checked. Treat each as an **individual dependency**, not as a reason to distrust the rest.

| Row | Topic | Claim to verify |
|---|---|---|
| R032 | Git versions | current stable Git version at edition date; planned breaking changes (e.g. future default branch / hash changes) - confi |
| R034 | Git vs GitHub definition | GitHub's own description of itself relative to Git |
| R035 | Account creation & username rules | steps, username constraints, email handling, plan defaults |
| R036 | 2FA / passkeys / recovery | supported methods, mandatory-2FA policy, recovery codes, passkey behaviour |
| R037 | Repository visibility | public/private/internal definitions; who can see; plan dependencies |
| R038 | Repository creation options | README, .gitignore templates, licence templates, default branch name setting |
| R039 | Profiles & profile README | special repo naming rule, pinned repos, contribution graph counting rules |
| R040 | README rendering & Markdown (GFM) | supported syntax, README locations/precedence, alerts, Mermaid support |
| R041 | Issues | labels, assignees, milestones, closing keywords, issue forms/templates, sub-issues, issue types |
| R042 | Discussions | enablement, categories, Q&A/answers, plan/visibility conditions |
| R043 | Projects | current Projects product (views, fields, iterations, automations, roadmap), limits |
| R044 | Wikis | availability by plan/visibility |
| R045 | Pull requests | draft PRs, reviews, suggested changes, merge methods, auto-merge, merge queue availability |
| R046 | Branch protection vs rulesets | capabilities, differences, plan/visibility availability, bypass |
| R047 | CODEOWNERS | file locations, syntax, review enforcement |
| R048 | Releases & tags | release creation, notes generation, assets, immutability options, source archives |
| R049 | Notifications, stars, watching | current behaviour and settings |
| R050 | Insights | Pulse, Contributors, Traffic, Commits, Code frequency, Dependency graph, Network, Forks - definitions and retention |
| R051 | Actions overview | workflow syntax basics, events, jobs, steps, contexts/expressions |
| R052 | Actions runners | GitHub-hosted labels/images, self-hosted security notes, larger runners |
| R053 | Actions limits & billing | included minutes, storage, concurrency limits by plan/visibility, pricing |
| R054 | Actions secrets & variables | repository/environment/organization scope, naming, availability to forks |
| R055 | Actions environments | required reviewers, protection rules, secrets scoping, plan limits |
| R056 | Actions permissions & GITHUB_TOKEN | default permissions, permissions key, fork PR restrictions |
| R057 | Actions artifacts & caching | retention, size limits, actions/cache & actions/upload-artifact current major versions |
| R058 | Actions matrix, concurrency, timeouts | syntax and limits |
| R059 | Reusable workflows & composite actions | workflow_call syntax, limits, nesting |
| R060 | Actions security hardening | pinning to SHA, script injection, pull_request_target risks, OIDC |
| R061 | Actions workflow events | schedule, workflow_dispatch, pull_request, push, release, issues triggers - exact semantics |
| R062 | Dependabot | alerts, security updates, version updates config file, availability |
| R063 | Dependency graph & dependency review | availability, supported ecosystems |
| R064 | Secret scanning & push protection | availability by visibility/plan, default behaviour for public repos, supported patterns |
| R065 | Code scanning & CodeQL | availability by visibility/plan, supported languages, default setup |
| R066 | Security advisories & private vulnerability reporting | enablement and workflow |
| R067 | SECURITY.md & community health files | recognised files and locations, .github repo defaults |
| R068 | Organizations, teams, roles | role names, base permissions, repository roles, custom roles availability |
| R069 | Forks & upstream sync | fork behaviour, sync fork button, private-fork rules |
| R070 | Packages | supported registries, auth, permissions, visibility, current limits/pricing |
| R071 | Container registry | ghcr.io usage and auth |
| R072 | GitHub Pages | publishing sources, Actions-based deploy, custom domain, HTTPS, limits, plan/visibility |
| R073 | Codespaces | quotas, pricing, machine types, dev container config, security, availability by plan |
| R074 | Dev containers | devcontainer.json spec status and GitHub support |
| R075 | GitHub CLI | install, gh auth login, gh repo/issue/pr/workflow/release command list and flags |
| R076 | REST API | versioning header, auth, rate limits, pagination |
| R077 | GraphQL API | endpoint, auth, rate limit model |
| R078 | Webhooks | events, secrets, signature verification |
| R079 | GitHub Apps vs OAuth apps | differences and recommendations |
| R080 | Personal access tokens | fine-grained vs classic status, scopes, expiry policy |
| R081 | SSH keys on GitHub | supported key types, host fingerprints, setup steps, SSH over HTTPS port |
| R082 | HTTPS auth for Git | password auth removed - token/credential manager requirement |
| R083 | Commit signature verification | 'Verified' badge rules, SSH/GPG/S/MIME support, vigilant mode |
| R084 | GitHub Enterprise | Cloud vs Server vs data residency naming and concepts |
| R085 | Sponsors / Marketplace | current availability and terms (neutral description only) |
| R086 | Copilot-related repository features | only neutral description of repo-level features - verify names |
| R087 | Plans and pricing | Free/Team/Enterprise feature matrix - only cite if verified; otherwise omit |
| R088 | UI navigation labels | names/locations of tabs, buttons, settings pages used in tutorials |
| R093 | Apache-2.0, GPL family, LGPL, BSD, MPL | Key conditions summarised accurately |
| R102 | GitHub terms vs repository licence | What rights GitHub's own Terms give other users of a public repo independent of the repo's licence (view/fork) |
| R103 | Git for Windows / Git Bash | What Git for Windows installs, what Git Bash is (a shell/environment, not Git), installer options incl. line-ending and  |
| R104 | PowerShell and Command Prompt equivalents | Correct cmdlets/commands for Appendix M (pwd/ls/cd/mkdir/cp/mv/rm equivalents; aliases) |
| R105 | macOS default shell | Current default shell on macOS (zsh?) and Terminal app behaviour |
| R106 | Installing Git on Linux/macOS | Package-manager install commands per platform and current versions |
| R107 | Newlines and encodings facts | LF/CRLF conventions per OS; UTF-8 statements used in the text chapter |
| R108 | Current Git release and supported versions | Latest stable version and release date at publication; deprecations / planned breaking changes |
| R109 | Git secret-removal tools | Current recommended tool(s) for purging secrets from history and their install/usage syntax (git-filter-repo, BFG) and G |
| R111 | Operating-system families | Who makes Windows/macOS; Linux distributions; Unix-like relationship (Ch 1) |
| R113 | Path separators and drive letters | Windows uses drive letters and backslash in native tools; macOS/Linux use a single tree and slash (Ch 2); Bash, Git Bash |
| R114 | File-name case sensitivity | Linux file systems here are case-sensitive (tested); Windows and macOS defaults are usually case-insensitive but case-pr |
| R115 | Hidden files | Unix-like: leading dot hides a file from plain ls (tested); Windows uses a hidden attribute (Ch 2) |
| R122 | Reserved example domains | example.org/example.com are reserved for documentation (Ch 5) |
| R123 | HTTPS meaning | Encryption in transit and server identity; not a guarantee of trustworthiness (Ch 5) |
| R124 | Authentication vs authorization; 2FA; keys | General security concepts used in Ch 6 |
| R128 | macOS Terminal default shell | macOS Terminal uses zsh by default (Ch 7) |
| R134 | Backups, synchronised folders and tracked changes: general behaviour | General descriptions of what backups, synchronised/cloud folders and word-processor tracked changes do and do not record |
| R136 | History of version-control systems | Eras (manual copies, local file-versioning tools, centralised systems, distributed systems) and example systems (Ch 10) |
| R138 | Why Git became widely used | Causes given in Ch 10: speed, distributed design, cheap branching, integrity, hosting platforms |
| R139 | Centralised versus distributed version control | Definitions, trade-offs, and classification of example systems (Subversion-style centralised; Git and Mercurial distribu |
| R140 | Git, GitHub, GitLab, Bitbucket: what each is | Git is a version-control tool; GitHub, GitLab and Bitbucket are hosting platforms built around Git repositories with col |
| R217 | Supply-chain guidance and incidents | general practice about hooks, submodules and dependencies; no incident examples verified (Ch 33) |

## N.5 AI assistance

This book was written with an AI assistant, Claude (made by Anthropic, used through Claude Code), working with the author. The assistant drafted the text, exercises, solutions, glossary, appendices and code; ran the commands and recorded their output in a sandbox (the "authoring environment"); fetched and read the sources and kept the ledger summarised here; read the whole book for errors; built the PDF and EPUB editions and the checks; drew the draft cover; and drafted the author and licensing information. The author set the goals and rules, chose the licences and imprint name, approved the plan and is responsible for the book. The recorded output is real output from that sandbox; nothing was run by hand on a live GitHub account, on Windows or on macOS. The repository lists Claude as a contributor and co-author of its commits. The full statement, area by area, is the file `AI-ASSISTANCE.md` in the companion repository.

## N.6 How to use this log

1. Before relying on a fact about GitHub, find its chapter's ledger row and read its status and date.
2. Prefer GitHub's current documentation for your plan over this book for anything time-sensitive.
3. If you find an error, the ledger tells you where the claim came from, so it can be corrected at the source.