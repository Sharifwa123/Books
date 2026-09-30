# Part XII review (Chapters 78-79), 2026-09-30

## 1. Technical review
- **78 Troubleshooting Handbook:** fifteen Git errors reproduced offline, each with meaning, cause, diagnosis, safe fix, dangerous fix and prevention. Recordings keep only `fatal:`/`error:` or first lines because `hint:` lines vary between versions. A final table lists errors that need a network or account and were **not** reproduced.
- **79 Recovery Playbooks:** five recorded recoveries (pushed secret, hard reset, bad merge, failed rebase, wrong branch). The secret playbook follows GitHub's documentation on removing sensitive data: revoke first; `git filter-repo --sensitive-data-removal` (2.47 or later); force push with `--mirror`; what remains in clones, forks, cached views and pull requests; the Support step (not exercised). The revert-then-remerge caveat was read in Git's howto, not run.

## 2. Beginner comprehension review
The method (first line, last line, `git status`, safe copy) is stated once and reused. Dangerous fixes are named beside safe ones.

## 3. Command verification
All recordings pass in Bash and zsh locally. Message wording differs between Git versions; CI on newer Git will show which recordings need `.alt` files.

## 4. Cross-references
No problems reported by the checkers.

## 5. Research / source review
R350-R352. The GitHub statements come from `github/docs` at commit `2eaab0b`. The table of unreproduced errors is unverified common patterns and says so.

## 6. Security review
Made-up secrets only. The chapters state that a rewrite is large and incomplete and that revocation is the real fix.

## 7. Editorial review
Consistent entry layout; British spelling.

## Open items
1. Confirm message wording on newer Git in CI.
2. Reproduce the network and authentication errors when an authenticated pass is possible (gate D).
