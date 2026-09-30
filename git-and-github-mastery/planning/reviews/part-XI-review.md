# Part XI review (Chapters 76-77), 2026-09-30

Both chapters are `status: draft` and Core, first read "later".

## 1. Technical review
- **76 Professional Scenarios 1-12:** twelve recorded sessions using a local bare repository: topic-branch merge, amend, revert, reflog recovery, conflict resolution, contribution with sign-off, soft-reset squash, committed secret (before and after the search), hotfix from a tag with `cherry-pick -x`, pickaxe search, stash, local review.
- **77 Capstone (Project 12):** one recorded session of 23 steps from an empty repository to an audited release, with a GitHub column per step described from earlier chapters. The project has **no licence**, deliberately.

## 2. Beginner comprehension review
Each scenario follows one layout (situation, goal, steps, what happened, if it goes wrong). The capstone repeats earlier commands in context; a first attempt can take two to three hours.

## 3. Command verification
Recordings in Bash and zsh (Git 2.43.0, Python 3), re-run in CI on newer Git. Two defects found while recording and fixed: an accidental conflict in step 12 of the capstone (both edits appended to the same file), and a test that passed wrongly because `grep ok` matched `broken`. Both became teaching points (Chapters 77 and 80).

## 4. Cross-references
`resolve_refs.py --check`, `check_links.py`, `check_refs`: no problems.

## 5. Research / source review
Ledger rows R348-R349 are locally tested only; no GitHub claim is made beyond earlier chapters. **Nothing ran on GitHub**; the GitHub columns are unverified by live use (gate D).

## 6. Security review
The only secrets are made up (`not-a-real-key`, `not-a-real-token`). The scenarios state that revocation comes first and that a later commit does not remove a secret from history. A forced add of an ignored file is called a warning sign.

## 7. Editorial review
British spelling; no banned phrases. Titles use ASCII hyphens where the outline uses them.

## Open items
1. Live-account run of the capstone's GitHub column.
2. Pilot read of the capstone.
3. Licence for the capstone project stays undecided by design.
