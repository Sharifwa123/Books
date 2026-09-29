"""Single source of truth for the book outline (v2).
Chapter numbers are DERIVED from order here. Never hard-code a chapter number elsewhere:
use the key (e.g. {ch:reflog}) and let tools/build_planning.py render it.
tag: Core | Deep.  first: full | part | later  (First-Read Path membership).
req: keys of chapters whose content is needed first (validated: must appear earlier).
"""
PARTS = [
 ("I","Computers and Digital Projects"),("II","Understanding Version Control"),("III","Learning Git"),
 ("IV","Professional Git"),("V","Introduction to GitHub"),("VI","Working with GitHub"),
 ("VII","Automation and CI/CD"),("VIII","Security on GitHub"),("IX","Open Source and Professional Development"),
 ("X","Advanced GitHub"),("XI","Master Projects"),("XII","Troubleshooting and Recovery"),("XIII","Mastery"),
]
# (part_index, key, title, tag, first, req, teaches)
C = [
# ---- Part I
(0,"computer","What a Computer Is","Core","full",[],"hardware vs software; operating system (Windows, macOS, Linux at concept level); applications; installing software; administrator permission; package managers (concept)"),
(0,"files","Files, Folders and Paths","Core","full",["computer"],"files, folders/directories, names, extensions, drives, absolute vs relative paths, hidden files, copy/move/delete, permissions (introduction)"),
(0,"editors","Editors and Project Folders","Core","full",["files"],"text editor vs word processor, code editors, saving/opening, what a software project is (website, app, docs), the running example project"),
(0,"text","Text, Encodings and Newlines","Core","full",["editors"],"plain vs formatted text; characters and encodings (UTF-8 concept); line endings (LF vs CRLF) and why they matter to Git; invisible characters; binary vs text files"),
(0,"internet","The Internet, the Web and Servers","Core","full",["computer"],"internet vs web; browser; URL; client/server; local vs remote; website vs web application; DNS and HTTP/HTTPS at concept level"),
(0,"accounts","Accounts, Passwords and Trust","Core","full",["internet"],"account, username, password, authentication vs authorization, two-factor authentication, keys (introduction), SSH concept, phishing basics"),
(0,"terminal","The Terminal Without Fear","Core","full",["files","text"],"terminal/shell/prompt/command/argument/option; Command Prompt, PowerShell, Git Bash, bash, zsh; Git is not Git Bash; PATH; environment variables; navigating (pwd, ls, cd, mkdir, cp, mv, rm with safety); reading errors; the sandbox folder"),
(0,"markdown","Markdown in Five Pages","Core","full",["editors","text"],"headings, lists, links, code blocks, tables, images; README-style documents; why Markdown suits version control"),
# ---- Part II
(1,"problem","The Problem of Changing Files","Core","full",["files","editors"],"report_final_v3 problem; collaboration collisions; lost work; cloud sync and backup vs version control (what each does and does not do)"),
(1,"history","A Short History of Version Control","Core","later",["problem"],"local → centralized → distributed; why Git was created; why it became widely used"),
(1,"distributed","Centralized vs Distributed","Core","full",["problem","internet"],"mental models; trade-offs; Git vs SVN-style systems"),
(1,"platforms","Git, GitHub, GitLab, Bitbucket","Core","full",["distributed"],"what each is and is not; tool vs platform; alternatives and trade-offs"),
# ---- Part III
(2,"install","Installing Git","Core","full",["terminal","accounts","platforms"],"install per OS (Git for Windows/Git Bash, macOS, Linux); verify with git --version; PATH problems; git help and reading built-in help"),
(2,"config","Configuration Scopes and Environments","Core","full",["install"],"system/global/local/worktree scopes; precedence; --show-origin; includes/includeIf [Deep]; identity, default branch, editor, line endings; how environment variables and inherited configuration change Git behaviour; isolated test environments"),
(2,"model","Git's Core Model","Core","full",["config","problem"],"working tree, index/staging area, repository, commit, HEAD, branch, tag, remote, remote-tracking branch; master diagram; preview of remotes"),
(2,"firstrepo","Your First Repository","Core","full",["model"],"git init, status, add, commit"),
(2,"history_view","Seeing Changes and History","Core","full",["firstrepo"],"log formats/filters, show, diff, diff --staged, hashes (informal), parents, relative refs"),
(2,"tracking","Tracking, Ignoring, Renaming, Deleting","Core","full",["firstrepo","text"],"untracked/tracked/modified/staged/committed/ignored; .gitignore; global ignore; rm, mv; secrets, env files, build artifacts, dependencies, generated files"),
(2,"commits","Writing Good Commits","Core","full",["history_view","tracking"],"message anatomy; atomic commits; amend (local only); empty commits; authorship and timestamps"),
(2,"branching","Branching","Core","full",["commits"],"create/switch, list, rename, delete, naming; feature/release/hotfix; short vs long-lived"),
(2,"merging","Merging","Core","full",["branching"],"fast-forward; three-way; merge commits; divergence; --no-ff; --squash"),
(2,"conflicts","Merge Conflicts","Core","full",["merging"],"why they happen; markers; manual resolution; tools; abort; prevention"),
(2,"remotes","Remotes","Core","full",["branching","internet","config"],"FIRST with a local bare repository (no account); remote add/remove/rename/-v; fetch, pull, push; upstream and tracking; fetch vs pull; pull vs merge/rebase; push vs fetch"),
(2,"stash","Stash and Small Tools","Core","part",["merging"],"stash; introduction to tags; clean (caution); grep; blame"),
# ---- Part IV
(3,"undo","Undoing Things Safely","Core","full",["commits","merging"],"restore; reset soft/mixed/hard (caution); revert; checkout legacy roles; restore vs checkout; reset vs revert"),
(3,"reflog","Recovery with the Reflog","Core","full",["undo"],"reflog; detached HEAD; deleted branch; bad reset; lost commits; recovery decision tree"),
(3,"rebase","Rebase","Deep","later",["conflicts","reflog","remotes"],"why rebase exists; rebase vs merge; interactive (squash, reword, edit, drop, reorder); conflicts; abort/continue/skip; shared-history danger; --force-with-lease (caution)"),
(3,"tools","Cherry-pick, Bisect and Patches","Deep","later",["merging","undo"],"cherry-pick; bisect; format-patch, apply, am; advanced diff"),
(3,"tags","Tags and Versioning","Core","part",["remotes","history_view"],"lightweight vs annotated; semantic versioning; push/delete tags; tag vs GitHub Release (preview)"),
(3,"objects","Inside Git: The Object Model","Deep","later",["commits","branching"],"blobs, trees, commits, tags, refs, packfiles; cat-file, hash-object, ls-files, show-ref, fsck, archive; gc and maintenance"),
(3,"bigrepos","Big and Complex Repositories","Deep","later",["remotes","objects"],"worktree; submodule; subtree; sparse checkout; partial and shallow clone; Git LFS; monorepo vs multirepo; performance"),
(3,"custom","Customising Git","Deep","later",["config","objects"],"aliases; hooks (client and server concepts); attributes; line-ending normalisation; credential helpers; rerere; merge strategies and drivers; maintenance"),
(3,"gitsec","Git Security","Core","part",["tracking","remotes","reflog","accounts"],"secrets in history; .env; tokens and keys; SSH vs HTTPS; signing (SSH and GPG); removing secrets (revoke first; verified tools); force-push risks; supply chain; incident examples"),
(3,"workflows","Git Workflows","Core","part",["branching","merging","remotes","tags"],"single-person; feature branch; GitHub Flow; Git Flow; trunk-based; release branch; fork-based; open-source; team; monorepo; small vs large; comparison table"),
(3,"readdocs","Reading Official Documentation","Core","part",["install","model"],"man pages and git help; command synopsis notation; reference manual vs guides; release notes; reading GitHub Docs; checking a source's version and date"),
# ---- Part V
(4,"whatgh","What GitHub Is (and Is Not)","Core","full",["platforms","remotes"],"Git is the version-control system; GitHub is an online platform built around Git repositories and collaboration"),
(4,"ghaccount","Account and Profile","Core","full",["whatgh","accounts"],"creating an account; username; public/private; profile; profile README; pinned repositories; contribution graph; organisations"),
(4,"ghauth","Authentication in Depth","Core","full",["ghaccount","gitsec"],"HTTPS vs SSH; key pairs; tokens; credential managers; 2FA; passkeys; recovery"),
(4,"ghrepo","Your First GitHub Repository","Core","full",["ghauth","remotes"],"create; README/.gitignore/licence; visibility; clone; connect existing repo; push/pull/fetch"),
(4,"ghtour","Touring the GitHub Interface","Core","full",["ghrepo"],"files, history, branches, tags, releases, tabs; UI paths flagged version-dependent"),
(4,"notify","Notifications, Stars and Watching","Core","part",["ghtour"],"what each does; controlling notification volume; stars vs watching vs following"),
# ---- Part VI
(5,"readme","Professional Repositories and READMEs","Core","full",["ghrepo","markdown"],"README types (beginner, web app, mobile, open source, library, API, CLI, business); About and topics"),
(5,"settings","Repository Settings, Security Tab and Wiki Tour","Core","part",["ghtour"],"Settings; Security tab; Wiki; Deployments and Environments views; what depends on plan/visibility/role"),
(5,"issues","Issues","Core","full",["ghrepo","markdown"],"anatomy; labels; assignees; milestones; references; templates and forms; closing keywords; automation"),
(5,"pr","Pull Requests","Core","full",["branching","merging","remotes","issues"],"lifecycle; base/compare; draft; reviewers; merge options; conflicts; PR vs git merge"),
(5,"review","Code Review","Core","full",["pr"],"purpose; checklist; comments and suggestions; etiquette; receiving review"),
(5,"projects","GitHub Projects","Deep","later",["issues","pr"],"tables; boards; roadmap; fields; iterations; filters; automation"),
(5,"discussions","GitHub Discussions","Deep","later",["issues"],"vs Issues; categories; moderation"),
(5,"collab","Collaboration and Access","Core","part",["pr","review"],"collaborators; teams; roles; forks vs clones; upstream sync; CODEOWNERS; community health files"),
(5,"protect","Branch Protection and Rulesets","Deep","later",["pr","collab"],"what each does; differences; plan/visibility dependencies"),
(5,"insights","Insights","Deep","later",["ghrepo","pr"],"traffic; contributors; commits; code frequency; network; forks; pulse; dependency graph - what each does and does not mean"),
# ---- Part VII
(6,"cicd","CI/CD Concepts","Core","full",["pr","terminal"],"build; test; lint; deploy; pipeline"),
(6,"yaml","YAML for Beginners","Core","full",["cicd","text"],"indentation; maps; lists; strings; common errors"),
(6,"actions","GitHub Actions Fundamentals","Core","full",["yaml","pr"],"workflow; event; job; step; runner; action; .github/workflows; on/jobs/runs-on/steps/uses/run"),
(6,"exprs","Expressions, Contexts and Conditionals","Deep","later",["actions"],"${{ }} expressions; contexts; if conditions; status functions; outputs"),
(6,"workflows_practice","Practical Workflows","Core","full",["actions"],"env vars; variables; secrets; artifacts; caching; matrices; manual and scheduled triggers; PR automation; tests; format check; build; issue automation; scheduled maintenance"),
(6,"wfdebug","Debugging and Re-running Workflows","Core","full",["workflows_practice"],"reading logs; re-running; debug logging; common YAML and permission failures"),
(6,"wfadvanced","Reusable Workflows, Environments and Deployments","Deep","later",["workflows_practice","protect"],"reusable workflows; environments; approvals; deploy a site; release automation"),
(6,"runners","Self-Hosted Runners, Concurrency and Limits","Deep","later",["actions"],"hosted vs self-hosted; security of self-hosted; concurrency; timeouts; usage limits (verified facts only)"),
(6,"wfsec","Securing Workflows","Core","part",["workflows_practice","gitsec"],"permissions; GITHUB_TOKEN; third-party actions and pinning; secrets exposure; untrusted PR input; OIDC concept"),
(6,"externalci","Actions vs External CI","Deep","later",["actions"],"comparison and trade-offs"),
# ---- Part VIII
(7,"ghsec","GitHub Security Features","Core","part",["gitsec","wfsec"],"Dependabot (alerts, security updates, version updates); dependency graph; code scanning and CodeQL concept; secret scanning; push protection; advisories; SECURITY.md; private vulnerability reporting; security overview"),
(7,"secpractice","Repository Security Practice","Core","part",["ghsec","collab"],"least privilege; secret scopes (repository/environment/organisation); signed commits; artifact security; supply chain; Git security vs GitHub security"),
# ---- Part IX
(8,"oss","How Open Source Works","Core","part",["pr","collab"],"meaning; roles; contribution flow; CONTRIBUTING; code of conduct; good first issues; responsible contribution"),
(8,"licences","Copyright and Licences","Core","part",["oss"],"copyright vs licence; public vs reusable; MIT; Apache-2.0; GPL family; LGPL; BSD; MPL; Creative Commons incl. the licence used by this book; not legal advice"),
(8,"releases","Releases","Core","part",["tags","ghrepo"],"GitHub Releases; notes; artifacts; source archives; release automation"),
(8,"ossproject","Creating an Open-Source Project","Deep","later",["licences","readme","releases"],"structure; docs; releases; versioning; maintenance"),
# ---- Part X
(9,"orgs","Organizations and Enterprise Concepts","Deep","later",["collab"],"members/owners/teams; policies; billing concepts; Enterprise Cloud vs Server"),
(9,"pages","GitHub Pages","Deep","later",["workflows_practice"],"static sites; publishing; custom domains; HTTPS; limits; Actions deploys"),
(9,"codespaces","Codespaces and Dev Containers","Deep","later",["ghrepo"],"what and why; devcontainer.json; costs; security; local vs cloud"),
(9,"packages","GitHub Packages and Containers","Deep","later",["workflows_practice"],"registries; publishing and installing; auth; visibility; ecosystems; Docker relationship (concept only)"),
(9,"deploy","Deployment Pipelines","Deep","later",["wfadvanced","internet"],"static; Node.js; Python; container; VPS; cloud; deployment secrets"),
(9,"ghcli","GitHub CLI","Deep","later",["ghauth","terminal","pr"],"gh auth login, gh repo, gh issue, gh pr, gh workflow, gh release; gh vs git"),
(9,"api","APIs, Webhooks and Apps","Deep","later",["ghauth","ghcli"],"REST; GraphQL concept; tokens; scripts; GitHub Apps vs OAuth apps; webhooks"),
(9,"platformextras","Other Platform Features","Deep","later",["orgs"],"Sponsors; Marketplace; Copilot-related repository workflows (neutral); custom properties; governance"),
# ---- Part XI
(10,"scenarios","Professional Scenarios 1-12","Core","later",["pr","wfsec","releases","reflog"],"twelve step-by-step scenarios"),
(10,"capstone","Capstone Project","Core","later",["scenarios"],"23-step professional simulation"),
# ---- Part XII
(11,"trouble","Troubleshooting Handbook","Core","later",["capstone"],"meaning, cause, diagnosis, safe fix, dangerous fix, prevention for each error"),
(11,"playbooks","Recovery Playbooks","Core","later",["trouble"],"secrets; lost commits; bad merges; failed rebase; wrong branch"),
# ---- Part XIII
(12,"challenges","Advanced Challenges","Deep","later",["playbooks"],"multi-repo; history surgery; large-repo problems; workflow design"),
(12,"assessment","Final Mastery Assessment","Core","later",["playbooks"],"practical tasks; two levels: Proficient (Core material) and Mastery (adds tasks tagged Deep); rubric and key separate"),
]
# Projects/scenarios anchored to the chapter after which they appear
PROJECTS = [
 (1,"Track a simple folder","firstrepo","personal study-notes folder","init, add, commit, status, log"),
 (2,"Build and version a website","commits","3-page small-business site (HTML/CSS provided; no coding needed)","commits, diff, .gitignore, good messages"),
 (3,"Publish to GitHub","ghrepo","the website","account, remote, push, clone"),
 (4,"Work with branches","merging","'contact page' and 'pricing' branches","branch, merge, fast-forward vs three-way"),
 (5,"Collaborate with another person","collab","two-person site update (partner, or two clones on one machine if solo)","remotes, pull/push, forks"),
 (6,"Resolve a merge conflict","conflicts","both people edit the same heading","conflict markers, abort/continue"),
 (7,"Professional GitHub repository","readme","README, licence, topics, templates, CONTRIBUTING","repository quality"),
 (8,"Create a pull request","pr","proposed change to the Project 7 repository","PR lifecycle, review"),
 (9,"Automated tests with Actions","workflows_practice","tiny library with provided tests","workflow, jobs, matrix, cache"),
 (10,"Deploy with Actions","wfadvanced","website to GitHub Pages","deploy workflow, environment"),
 (11,"Create an open-source project","ossproject","small documented library","licence, releases, community files"),
 (12,"Full professional workflow","capstone","capstone","everything"),
]
APPENDICES = [
 ("A","Git Command Reference"),("B","GitHub and CLI Reference"),("C","Common Git Errors"),("D","GitHub Actions YAML Reference"),
 ("E","Git Terminology Map"),("F","GitHub Terminology Map"),("G","Security Checklist"),("H","Professional Repository Checklist"),
 ("I","Open-Source Project Checklist"),("J","Deployment Checklist"),("K","Git Recovery Decision Tree"),("L","Learning Roadmap After the Book"),
 ("M","Git Bash / PowerShell / Command Prompt Equivalence Guide"),("N","Sources and Verification Log"),
]
