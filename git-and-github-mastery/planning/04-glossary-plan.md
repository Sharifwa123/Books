# 04 — Glossary Plan

## Entry format (every term)
**Term** · Simple definition · Technical definition · Example · Related terms · First introduced in (chapter).

## Process
1. Each chapter's "New Vocabulary" list is the source of truth; entries added to `glossary-master.csv` (to be created at drafting start) when a chapter is finished.
2. Editorial Pass 3 checks that every term used in prose is either previously introduced or defined inline.
3. Alphabetical, cross-referenced, generated from the CSV so print/PDF/EPUB/web stay consistent.

## Term families (seed list; will grow)
- **Computing:** hardware, software, OS, file, folder/directory, path (absolute/relative), extension, hidden file, permission, terminal, shell, prompt, command, argument, option/flag, environment variable, PATH, process, installer, package manager.
- **Networking:** internet, web, browser, URL, HTTP/HTTPS, server, client, local, remote, DNS (concept), port (concept), API, webhook, TLS (concept).
- **Security:** account, authentication, authorization, password, 2FA/MFA, passkey, public key, private key, SSH, token (PAT), scope, secret, credential helper, signing, GPG, least privilege, supply chain, vulnerability, advisory, CVE (concept), OIDC.
- **Git core:** version control, VCS, repository, working tree, index/staging area, commit, hash/SHA, parent, HEAD, branch, tag (lightweight/annotated), remote, origin, upstream, remote-tracking branch, clone, fetch, pull, push, merge, fast-forward, three-way merge, merge commit, conflict, rebase, cherry-pick, stash, reflog, detached HEAD, reset (soft/mixed/hard), revert, restore, ref, blob, tree, packfile, garbage collection, hook, alias, submodule, subtree, worktree, sparse checkout, shallow/partial clone, LFS, bisect, blame, rerere, patch, `.gitignore`, `.gitattributes`.
- **Workflows:** feature branch, GitHub Flow, Git Flow, trunk-based development, release branch, hotfix, fork workflow, monorepo, multirepo, SemVer.
- **GitHub:** account, organisation, repository (public/private/internal), fork, issue, label, milestone, assignee, pull request (draft), review, approval, CODEOWNERS, branch protection, ruleset, Project (table/board/roadmap), Discussion, Wiki, release, GitHub Pages, Packages, Codespaces, dev container, GitHub App, OAuth App, GitHub CLI, REST/GraphQL, Enterprise Cloud/Server, Insights, Sponsors, Marketplace.
- **Automation:** CI, CD, pipeline, workflow, event/trigger, job, step, runner (hosted/self-hosted), action, YAML, matrix, artifact, cache, environment, reusable workflow, `GITHUB_TOKEN`, secret vs variable.
- **Open source/legal:** copyright, licence, permissive, copyleft, MIT, Apache-2.0, GPL, LGPL, BSD, MPL, Creative Commons, maintainer, contributor, code of conduct, upstream/downstream.
- **Software development:** source code, build, test, lint, dependency, package, artifact, deploy, environment (dev/staging/production), container/image/registry (concept), regression.

## Term-map appendices
Appendix E (Git terminology map) and F (GitHub terminology map) are diagrams grouping the above by how terms relate.
