# 03 — Technical Dependency Map (v2, generated)

**Generated from `tools/toc_data.py`; ordering is machine-checked (every prerequisite appears earlier).** Rule: no chapter may use a term or skill not taught earlier, unless defined inline at first use with a pointer forward.

| Chapter | Requires |
|---|---|
| 1 What a Computer Is | — |
| 2 Files, Folders and Paths | 1 What a Computer Is |
| 3 Editors and Project Folders | 2 Files, Folders and Paths |
| 4 Text, Encodings and Newlines | 3 Editors and Project Folders |
| 5 The Internet, the Web and Servers | 1 What a Computer Is |
| 6 Accounts, Passwords and Trust | 5 The Internet, the Web and Servers |
| 7 The Terminal Without Fear | 2 Files, Folders and Paths, 4 Text, Encodings and Newlines |
| 8 Markdown in Five Pages | 3 Editors and Project Folders, 4 Text, Encodings and Newlines |
| 9 The Problem of Changing Files | 2 Files, Folders and Paths, 3 Editors and Project Folders, 7 The Terminal Without Fear |
| 10 A Short History of Version Control | 9 The Problem of Changing Files |
| 11 Centralized vs Distributed | 9 The Problem of Changing Files, 5 The Internet, the Web and Servers |
| 12 Git, GitHub, GitLab, Bitbucket | 11 Centralized vs Distributed |
| 13 Installing Git | 7 The Terminal Without Fear, 6 Accounts, Passwords and Trust, 12 Git, GitHub, GitLab, Bitbucket |
| 14 Configuration Scopes and Environments | 13 Installing Git |
| 15 Git's Core Model | 14 Configuration Scopes and Environments, 9 The Problem of Changing Files |
| 16 Your First Repository | 15 Git's Core Model |
| 17 Seeing Changes and History | 16 Your First Repository |
| 18 Tracking, Ignoring, Renaming, Deleting | 16 Your First Repository, 4 Text, Encodings and Newlines |
| 19 Writing Good Commits | 17 Seeing Changes and History, 18 Tracking, Ignoring, Renaming, Deleting |
| 20 Branching | 19 Writing Good Commits |
| 21 Merging | 20 Branching |
| 22 Merge Conflicts | 21 Merging |
| 23 Remotes | 20 Branching, 5 The Internet, the Web and Servers, 14 Configuration Scopes and Environments |
| 24 Stash and Small Tools | 21 Merging |
| 25 Undoing Things Safely | 19 Writing Good Commits, 21 Merging |
| 26 Recovery with the Reflog | 25 Undoing Things Safely |
| 27 Rebase | 22 Merge Conflicts, 26 Recovery with the Reflog, 23 Remotes |
| 28 Cherry-pick, Bisect and Patches | 21 Merging, 25 Undoing Things Safely |
| 29 Tags and Versioning | 23 Remotes, 17 Seeing Changes and History |
| 30 Inside Git: The Object Model | 19 Writing Good Commits, 20 Branching |
| 31 Big and Complex Repositories | 23 Remotes, 30 Inside Git: The Object Model |
| 32 Customising Git | 14 Configuration Scopes and Environments, 30 Inside Git: The Object Model |
| 33 Git Security | 18 Tracking, Ignoring, Renaming, Deleting, 23 Remotes, 26 Recovery with the Reflog, 6 Accounts, Passwords and Trust |
| 34 Git Workflows | 20 Branching, 21 Merging, 23 Remotes, 29 Tags and Versioning |
| 35 Reading Official Documentation | 13 Installing Git, 15 Git's Core Model |
| 36 What GitHub Is (and Is Not) | 12 Git, GitHub, GitLab, Bitbucket, 23 Remotes |
| 37 Account and Profile | 36 What GitHub Is (and Is Not), 6 Accounts, Passwords and Trust |
| 38 Authentication in Depth | 37 Account and Profile, 33 Git Security |
| 39 Your First GitHub Repository | 38 Authentication in Depth, 23 Remotes |
| 40 Touring the GitHub Interface | 39 Your First GitHub Repository |
| 41 Notifications, Stars and Watching | 40 Touring the GitHub Interface |
| 42 Professional Repositories and READMEs | 39 Your First GitHub Repository, 8 Markdown in Five Pages |
| 43 Repository Settings, Security Tab and Wiki Tour | 40 Touring the GitHub Interface |
| 44 Issues | 39 Your First GitHub Repository, 8 Markdown in Five Pages |
| 45 Pull Requests | 20 Branching, 21 Merging, 23 Remotes, 44 Issues |
| 46 Code Review | 45 Pull Requests |
| 47 GitHub Projects | 44 Issues, 45 Pull Requests |
| 48 GitHub Discussions | 44 Issues |
| 49 Collaboration and Access | 45 Pull Requests, 46 Code Review |
| 50 Branch Protection and Rulesets | 45 Pull Requests, 49 Collaboration and Access |
| 51 Insights | 39 Your First GitHub Repository, 45 Pull Requests |
| 52 CI/CD Concepts | 45 Pull Requests, 7 The Terminal Without Fear |
| 53 YAML for Beginners | 52 CI/CD Concepts, 4 Text, Encodings and Newlines |
| 54 GitHub Actions Fundamentals | 53 YAML for Beginners, 45 Pull Requests |
| 55 Expressions, Contexts and Conditionals | 54 GitHub Actions Fundamentals |
| 56 Practical Workflows | 54 GitHub Actions Fundamentals |
| 57 Debugging and Re-running Workflows | 56 Practical Workflows |
| 58 Reusable Workflows, Environments and Deployments | 56 Practical Workflows, 50 Branch Protection and Rulesets |
| 59 Self-Hosted Runners, Concurrency and Limits | 54 GitHub Actions Fundamentals |
| 60 Securing Workflows | 56 Practical Workflows, 33 Git Security |
| 61 Actions vs External CI | 54 GitHub Actions Fundamentals |
| 62 GitHub Security Features | 33 Git Security, 60 Securing Workflows |
| 63 Repository Security Practice | 62 GitHub Security Features, 49 Collaboration and Access |
| 64 How Open Source Works | 45 Pull Requests, 49 Collaboration and Access |
| 65 Copyright and Licences | 64 How Open Source Works |
| 66 Releases | 29 Tags and Versioning, 39 Your First GitHub Repository |
| 67 Creating an Open-Source Project | 65 Copyright and Licences, 42 Professional Repositories and READMEs, 66 Releases |
| 68 Organizations and Enterprise Concepts | 49 Collaboration and Access |
| 69 GitHub Pages | 56 Practical Workflows |
| 70 Codespaces and Dev Containers | 39 Your First GitHub Repository |
| 71 GitHub Packages and Containers | 56 Practical Workflows |
| 72 Deployment Pipelines | 58 Reusable Workflows, Environments and Deployments, 5 The Internet, the Web and Servers |
| 73 GitHub CLI | 38 Authentication in Depth, 7 The Terminal Without Fear, 45 Pull Requests |
| 74 APIs, Webhooks and Apps | 38 Authentication in Depth, 73 GitHub CLI |
| 75 Other Platform Features | 68 Organizations and Enterprise Concepts |
| 76 Professional Scenarios 1-12 | 45 Pull Requests, 60 Securing Workflows, 66 Releases, 26 Recovery with the Reflog |
| 77 Capstone Project | 76 Professional Scenarios 1-12 |
| 78 Troubleshooting Handbook | 77 Capstone Project |
| 79 Recovery Playbooks | 78 Troubleshooting Handbook |
| 80 Advanced Challenges | 79 Recovery Playbooks |
| 81 Final Mastery Assessment | 79 Recovery Playbooks |

## Known forward-reference risks (managed deliberately)
1. Ch 15 previews remotes before Ch 23 — a flagged one-paragraph preview.
2. Ch 18 mentions secrets before Ch 33 — brief warning now, full treatment later.
3. Ch 17 uses 'hash' — informal definition first, formal in Ch 30.
4. Ch 33 covers credentials at Git level; GitHub-specific tokens and keys wait for Ch 38.
5. Ch 42 needs Markdown — taught earlier in Ch 8.
6. Ch 29 previews GitHub Releases before Ch 66 — one-line pointer only.
7. Ch 23 teaches remotes with a local bare repository, so it does not depend on any GitHub chapter.
