# Part V review (Chapters 36-51), 2026-09-30

Chapters 36-40 were drafted earlier and re-verified this session; chapters 41-51 were drafted this session. All sixteen are `status: draft`. Chapters 47, 48, 50 and 51 are tagged [Deep] with first read "later"; Chapters 41, 43, 49 have first read "part".

## 1. Technical review
- **Sources.** Every statement about GitHub is checked against the open source of GitHub's documentation (`github/docs`, commit `2eaab0b`, 29 September 2026) or, for terms, `site-policy` (commit `b9578b5`). Both commit ids are in `research/sources-manifest.csv`. No live account was used: interface *layouts* are described by idea, and the chapters say so.
- **Git behind the platform, recorded.** Relative links and renames (42), a wiki as a second Git repository (43), issue forms and closing keywords in commit messages (44), three-dot vs two-dot diff, merge/squash/rebase results and the `refs/pull` namespace on a stand-in server (45), `Co-authored-by` trailers (46), the fork and upstream workflow (49), server-side refusal of force pushes and deletions (50), commit counting with `shortlog`, `--no-merges` and `.mailmap` (51). Each recording is Bash and zsh, re-run in CI on the runner's Git and on Git v2.56.0 built from source.
- **Stand-ins.** Bare repositories play the platform. The chapters say wherever a recording is a stand-in, and none claims to show GitHub's own implementation.
- **A finding from the sources.** The Git 2.55+ `git pull` manual says `--ff-only` is the default, but `builtin/pull.c` (v2.56.0) still stops with "Need to specify how to reconcile divergent branches". Chapter 23 states both and follows the behaviour (R180).
- **Version differences noted in the text and handled with `.alt` recordings:** extra `advice.mergeConflict` hint and quoting in bisect (Git 2.55+), `blame -s` hash length (2.56), `upstream/HEAD` label (2.55+).

## 2. Beginner comprehension review
- Every chapter states at the top how it was checked and what was not seen on a live account. The [Deep] chapters say they can be read later.
- `check_term_order.py` reports many warnings, nearly all ordinary words (*project*, *issue*, *fork*, *pull request*) used in Chapters 36-43 before the formal definitions in Chapters 44-49. Chapters 12 and 36 explain these words in place and point forward with explicit chapter references. **Open:** decide whether the glossary should record an earlier `first_chapter_key` for *pull request*, *issue* and *fork*.
- A pilot read by a beginner is still needed for Chapters 45 and 49, which carry the most new ideas.

## 3. Command verification
All transcripts pass in Bash and zsh locally. CI results are recorded on the pull request. Not run: anything on a live GitHub account (creating a repository, opening a pull request, merging, notifications, projects, discussions, rulesets).

## 4. Cross-references
`resolve_refs.py --check`, `check_links.py` and `check_refs`: no problems.

## 5. Research / source review
Ledger rows R224-R278 cover Part V. GitHub rows are `Officially verified (docs only)` or `Both`, with `needs_reverification = yes`, because the service changes. **Open dependencies (each independent):** GitHub plan and price availability of features (R214, R275, R276 partly); username character rules (R228); whether `.git` is optional in a GitHub address (R226); the exact wording and layout of buttons on a live account; trunk-based and `develop` workflow models (R219); incident examples (R217).

## 6. Security review
- All credentials, addresses and names in recordings are made up. `check_secrets.py` finds nothing.
- Chapters 37-38 state token, SSH-key and two-factor guidance from the documentation. Chapter 47 warns that a public project exposes what is written in it. Chapter 50 shows server-side refusal and warns about bypass lists.

## 7. Editorial review
British spelling; no banned filler phrases; consistent callouts; quotations from GitHub's documentation are short and attributed. Part V is complete at Chapter 51.

## Open items
1. Re-verify every GitHub row before release (the source commit id will have moved).
2. A live-account pass for interface layouts, if a human with an account can do it (gate D).
3. Pilot read.
