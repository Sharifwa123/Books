# 02 — Table of Contents and Chapter Curriculum

Every chapter ends with the standard checkpoint: What You Learned · New Vocabulary · Commands Learned · Common Mistakes · Practice (5 levels: Guided, Partial, Independent, Professional, Troubleshooting) · Self-Test · Before Moving On. Exercise solutions are in a separate companion section.

## FRONT MATTER
Half title · Title page · Copyright page · Publisher & author information · Edition/version statement · Disclaimer · Trademark notice · Licensing statement · Dedication · Foreword (placeholder) · Preface · How to use this book · Who this is for · Learning roadmap · Prerequisites · Equipment/software · Table of contents.

## PART I — COMPUTERS AND DIGITAL PROJECTS
| Ch | Title | Teaches |
|----|-------|---------|
| 1 | What a Computer Is | hardware vs software, OS (Windows/macOS/Linux concepts), apps, installing software |
| 2 | Files, Folders and Paths | files, extensions, names, drives, absolute/relative paths, hidden files, copy/move/delete, permissions (intro) |
| 3 | Editors and Project Folders | text vs word processor, code editors, saving, what a "software project" is (website, app, docs), example project used in the book |
| 4 | The Internet, the Web and Servers | internet vs web, client/server, local vs remote, website vs web app, DNS/HTTP at a conceptual level |
| 5 | Accounts, Passwords and Trust | username, password, authentication vs authorization, 2FA, keys (intro), SSH concept |
| 6 | The Terminal Without Fear | shell/terminal, prompt, `pwd`, `ls`/`dir`, `cd`, `mkdir`, `cp`, `mv`, `rm` (with safety), reading errors, the sandbox `sharif-git-lab` |

## PART II — UNDERSTANDING VERSION CONTROL
| 7 | The Problem of Changing Files | `report_final_v3_REAL.docx`, collaboration collisions, lost work |
| 8 | A Short History of Version Control | local → centralized (e.g. CVS/SVN-style) → distributed; why Git was created and became widespread |
| 9 | Centralized vs Distributed | mental models, trade-offs, Git vs SVN |
| 10 | Git, GitHub, GitLab, Bitbucket | what each is/is not; platform vs tool; alternatives and trade-offs |

## PART III — LEARNING GIT
| 11 | Installing and Configuring Git | install per OS, `git --version`, `git config` (name, email, default branch, editor, line endings), `git help`, reading man pages |
| 12 | Git's Core Model | working tree, index/staging, repository, commit, HEAD, branch, tag, remote, remote-tracking branch; master diagram |
| 13 | Your First Repository | `git init`, `status`, `add`, `commit`; **Project 1** |
| 14 | Seeing Changes and History | `log` (formats/filters), `show`, `diff`, `diff --staged`, hashes, parents, relative refs (`HEAD~1`, `^`) |
| 15 | Tracking, Ignoring, Renaming, Deleting | file states, `.gitignore`, global ignore, `rm`, `mv`, secrets/env/build/deps/generated files |
| 16 | Writing Good Commits | message anatomy, atomic commits, `--amend`, empty commits, authorship/timestamps; **Project 2** (website) |
| 17 | Branching | create/switch (`switch`, `checkout`), list, rename, delete, naming, feature/release/hotfix, short vs long-lived |
| 18 | Merging | fast-forward, three-way, merge commits, divergence, `--no-ff`, `--squash`; **Project 4** |
| 19 | Merge Conflicts | why, markers, manual resolution, tools, abort, prevention; **Project 6** |
| 20 | Remotes | `remote` add/remove/rename/-v, `fetch`, `pull`, `push`, upstream, fetch vs pull, pull vs merge/rebase |
| 21 | Stash and Small Tools | `stash`, `tag` intro, `clean` (⚠️), `grep`, `blame` |

## PART IV — PROFESSIONAL GIT
| 22 | Undoing Things Safely | `restore`, `reset` soft/mixed/hard (⚠️), `revert`, `checkout` legacy roles, restore vs checkout, reset vs revert |
| 23 | Recovery with the Reflog | `reflog`, detached HEAD, deleted branch, bad reset, lost commits, recovery decision tree |
| 24 | Rebase | concept, vs merge, interactive (squash/reword/edit/drop/reorder), conflicts, abort/continue/skip, shared-history danger (⚠️), `--force-with-lease` (⚠️) |
| 25 | Cherry-pick, Bisect and Patches | `cherry-pick`, `bisect`, `format-patch`, `apply`/`am`, advanced `diff` |
| 26 | Tags and Versioning | lightweight vs annotated, SemVer, push/delete tags, tag vs GitHub Release |
| 27 | Inside Git: The Object Model | blobs, trees, commits, tags, refs, packfiles, `cat-file`, `hash-object`, gc, maintenance |
| 28 | Big and Complex Repositories | worktree, submodule, subtree, sparse checkout, partial/shallow clone, LFS, monorepo vs multirepo, performance |
| 29 | Customising Git | aliases, hooks (client/server concepts), attributes, line-endings, credential helpers, rerere, merge strategies/drivers |
| 30 | Git Security | secrets in history, `.env`, key/token handling, SSH/HTTPS auth, GPG/SSH signing, removing secrets (revoke first!), force-push risks, supply chain, permissions, incident examples |
| 31 | Git Workflows | single-person, feature-branch, GitHub Flow, Git Flow, trunk-based, release branch, fork-based, open-source, team, monorepo, small vs large; comparison table |

## PART V — INTRODUCTION TO GITHUB
| 32 | What GitHub Is (and Is Not) | "Git is the version-control system; GitHub is an online platform built around Git repositories and collaboration" |
| 33 | Account and Profile | creating account, username, public/private, profile, profile README, pinned repos, contribution graph, organisations |
| 34 | Authentication in Depth | HTTPS vs SSH, key pairs, tokens, credential managers, 2FA, passkeys, recovery |
| 35 | Your First GitHub Repository | create, README/.gitignore/license, visibility, clone, connect existing repo, push/pull/fetch; **Project 3** |
| 36 | Touring the GitHub Interface | files, history, branches, tags, releases, tabs; UI-VERSION NOTE |

## PART VI — WORKING WITH GITHUB
| 37 | Professional Repositories and READMEs | README types (beginner, web app, mobile, OSS, library, API, CLI, business), About/topics; **Project 7** |
| 38 | Issues | anatomy, labels, assignees, milestones, references, templates, forms, closing keywords |
| 39 | Pull Requests | lifecycle, base/compare, draft, reviewers, merge options, conflicts, PR vs `git merge`; **Project 8** |
| 40 | Code Review | purpose, checklist, comments/suggestions, etiquette |
| 41 | GitHub Projects | tables, boards, roadmap, fields, iterations, automation |
| 42 | Discussions | vs Issues, categories, moderation |
| 43 | Collaboration and Access | collaborators, teams, roles, forks vs clones, upstream sync, CODEOWNERS, health files; **Project 5** |
| 44 | Branch Protection and Rulesets | what each does, differences, plan/visibility dependencies |
| 45 | Insights | traffic, contributors, commits, code frequency, network, forks, pulse, dependency graph — meaning and non-meaning |

## PART VII — AUTOMATION AND CI/CD
| 46 | CI/CD Concepts | build, test, lint, deploy, pipeline diagram |
| 47 | YAML for Beginners | indentation, maps, lists, strings, common errors |
| 48 | GitHub Actions Fundamentals | workflow, event, job, step, runner, action, `.github/workflows`, `on`/`jobs`/`runs-on`/`steps`/`uses`/`run` |
| 49 | Actions in Practice | env vars, variables, secrets, artifacts, caching, matrices, manual & scheduled triggers, PR automation; workflows: tests, format check, build, issue automation, scheduled maintenance; **Project 9** |
| 50 | Reusable Workflows, Environments and Deployments | reusable workflows, environments, approvals, deploy site, release automation; **Project 10** |
| 51 | Securing Workflows | permissions, `GITHUB_TOKEN`, third-party actions/pinning, secrets exposure, untrusted PR input, OIDC concept |
| 52 | Actions vs External CI | comparison and trade-offs |

## PART VIII — SECURITY
| 53 | GitHub Security Features | Dependabot (alerts/security updates/version updates), code scanning/CodeQL concept, secret scanning, push protection, advisories, SECURITY.md, private vulnerability reporting, security overview, dependency graph |
| 54 | Repository Security Practice | least privilege, secrets scopes (repository/environment/organisation), signed commits, artifact security, supply chain; Git security vs GitHub security |

## PART IX — OPEN SOURCE AND PROFESSIONAL DEVELOPMENT
| 55 | How Open Source Works | meaning, roles, contribution flow, CONTRIBUTING, code of conduct, good first issues, responsible contribution |
| 56 | Copyright and Licences | copyright ≠ licence; public ≠ free to reuse; MIT, Apache-2.0, GPL family, LGPL, BSD, MPL, Creative Commons (non-software); not legal advice |
| 57 | Creating an Open-Source Project | structure, docs, releases, versioning, maintenance; **Project 11** |
| 58 | Releases | GitHub Releases, notes, artifacts, source archives, release automation |

## PART X — ADVANCED GITHUB
| 59 | Organisations and Enterprise Concepts | members/owners/teams, policies, billing concepts, Enterprise Cloud vs Server |
| 60 | GitHub Pages | static sites, publishing, custom domains, HTTPS, limits, Actions deploys |
| 61 | Codespaces and Dev Containers | what/why, `devcontainer.json`, costs, security, local vs cloud |
| 62 | GitHub Packages and Containers | registries, publishing/installing, auth, visibility, ecosystems; Docker relationship (concept only) |
| 63 | Deployment Pipelines | static, Node.js, Python, container, VPS, cloud; deployment secrets |
| 64 | GitHub CLI | `gh auth login`, `gh repo`, `gh issue`, `gh pr`, `gh workflow`, `gh release`; `gh` vs `git` |
| 65 | APIs, Webhooks, Apps | REST, GraphQL concept, tokens, scripts, GitHub Apps vs OAuth Apps, webhooks |
| 66 | Other Platform Features | Sponsors, Marketplace, Copilot-related repository workflows, custom properties, governance |

## PART XI — MASTER PROJECTS
| 67 | Scenarios 1–12 | walk-throughs listed in 05 |
| 68 | Capstone | 23-step professional simulation |

## PART XII — TROUBLESHOOTING AND RECOVERY
| 69 | Troubleshooting Handbook | each error: meaning, cause, diagnose, safe fix, dangerous fix, prevention |
| 70 | Recovery Playbooks | secrets, lost commits, bad merges, failed rebase, wrong branch |

## PART XIII — MASTERY
| 71 | Advanced Challenges | multi-repo, history surgery, large-repo problems, workflow design |
| 72 | Final Mastery Assessment | practical; rubric and answer key separate |

## BACK MATTER
Appendices A–L (see 04/06) · Glossary · Sources and Further Reading · Author biography (placeholder) · SHARIF TECHNOLOGIES publisher section · Final competency checklist · Index plan.

---

## Cross-cutting requirements per chapter
- Compare related concepts (per the master list in the prompt: Git vs GitHub, merge vs rebase, reset vs revert, restore vs checkout, fetch vs pull, fork vs clone, issue vs discussion, tag vs release, SSH vs HTTPS, secret scopes, branch protection vs rulesets, LFS vs regular Git, monorepo vs multirepo, etc.) at the chapter where each first becomes relevant.
- Realistic example project progression: personal notes folder → small business website → documentation repo → small API/library → team mobile-app repo → security tool → open-source library.
- No "etc."/"and so on" in place of teaching.
