# Appendix B — GitHub and CLI Reference

This appendix maps GitHub features to the chapters that describe them, and lists the GitHub CLI (`gh`) commands from Chapter 73<!--ref:ghcli-->. **GitHub changes often**: everything here comes from the documentation as read on 29 September 2026 (`github/docs` at commit `2eaab0b`) and was **not run on a live account** except where a chapter says so. Interface labels are deliberately not listed, because they change; look for the idea, not the label.

## B.1 GitHub features and where they are taught

| Feature | What it is for | Chapter |
|---|---|---|
| Account, profile, two-factor authentication | who you are on the platform | 37<!--ref:ghaccount-->, 38<!--ref:ghauth--> |
| Repository (visibility, README, licence, topics) | the project's home | 39<!--ref:ghrepo-->, 42<!--ref:readme--> |
| Settings, Security tab, wiki | control and documentation | 43<!--ref:settings--> |
| Issues, labels, milestones, forms | tracking work | 44<!--ref:issues--> |
| Pull requests and merge strategies | proposing and merging changes | 45<!--ref:pr--> |
| Code review, suggestions, approvals | quality control | 46<!--ref:review--> |
| Projects, Discussions | planning and conversation | 47<!--ref:projects-->, 48<!--ref:discussions--> |
| Collaborators, forks, teams | access | 49<!--ref:collab--> |
| Branch protection, rulesets, code owners | rules for branches | 50<!--ref:protect--> |
| Insights, graphs | activity data | 51<!--ref:insights--> |
| Actions: workflows, runners, environments | automation | 54<!--ref:actions-->, 58<!--ref:wfadvanced-->, 59<!--ref:runners--> |
| Dependabot, secret scanning, code scanning, advisories | security features | 62<!--ref:ghsec--> |
| Releases | named versions | 66<!--ref:releases--> |
| Pages | static websites | 69<!--ref:pages--> |
| Codespaces | cloud development environments | 70<!--ref:codespaces--> |
| Packages | package registries | 71<!--ref:packages--> |
| Organizations, enterprise accounts | groups | 68<!--ref:orgs--> |
| REST and GraphQL APIs, webhooks, Apps | programmatic access | 74<!--ref:api--> |
| Sponsors, Marketplace, custom properties | other features | 75<!--ref:platformextras--> |

## B.2 Special files and folders

| Path | Purpose | Chapter |
|---|---|---|
| `README.md` | the front page of a repository | 42<!--ref:readme--> |
| `LICENSE` | the licence (the owner's decision) | 65<!--ref:licences--> |
| `CONTRIBUTING.md` | how to contribute | 64<!--ref:oss--> |
| `CODE_OF_CONDUCT.md` | expected behaviour | 64<!--ref:oss--> |
| `SECURITY.md` | how to report vulnerabilities | 62<!--ref:ghsec--> |
| `.github/workflows/*.yml` | workflows | 54<!--ref:actions--> |
| `.github/dependabot.yml` | dependency update settings | 62<!--ref:ghsec--> |
| `.github/FUNDING.yml` | sponsor button | 75<!--ref:platformextras--> |
| `.github/release.yml` | release-note categories | 66<!--ref:releases--> |
| `.devcontainer/devcontainer.json` | cloud development environment | 70<!--ref:codespaces--> |
| `.gitignore`, `.gitattributes` | what Git ignores; how it treats files | 18<!--ref:tracking-->, 32<!--ref:custom--> |

## B.3 GitHub CLI commands

Run with `gh`; add `--help` to any command. The commands below were described in Chapter 73<!--ref:ghcli-->; only those marked "run" were executed for the book (with `gh` 2.102.0).

| Command | What it does | Status |
|---|---|---|
| `gh --version` | prints the version | run |
| `gh alias set NAME "..."`, `gh alias list`, `gh alias delete NAME` | shortcuts | run (`set`, `list`) |
| `gh config set KEY VALUE`, `gh config get KEY` | settings | run |
| `gh auth status`, `gh auth login`, `gh auth switch` | sign in and out | `status` run without login |
| `gh status` | your work across repositories | documented, not run |
| `gh repo view`, `clone`, `create` | repositories | documented, not run |
| `gh issue list`, `create` | issues | documented, not run |
| `gh pr list`, `create`, `checkout` | pull requests | `list` run only to show the login message |
| `gh search prs --review-requested=@me` | search | documented, not run |
| `gh release create TAG` | releases | documented, not run |
| `gh run rerun`, `gh run watch` | workflow runs | documented, not run |
| `gh codespace create`, `list` | codespaces | documented, not run |
| `gh api PATH` | a request to the API | mentioned only |

Environment variables: `GH_TOKEN` (a token instead of a login), `GH_TELEMETRY` (`log`, or a falsy value to disable), `DO_NOT_TRACK`.

## B.4 API details worth remembering

- `Link` header: pagination; follow `rel="next"` until it is absent (74<!--ref:api-->).
- `X-GitHub-Api-Version`: pin a version.
- `X-Hub-Signature-256`: webhook signature, `sha256=` plus an HMAC hex digest; compare in constant time.
- Rate-limit headers start with `X-RateLimit-`.
