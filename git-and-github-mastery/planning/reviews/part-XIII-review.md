# Part XIII review (Chapters 80-81), 2026-09-30

## 1. Technical review
- **80 Advanced Challenges:** six challenges (submodule pointer, subdirectory split, shallow and sparse clone, workflow design on paper, automated bisect, dangling-commit rescue) with recorded reference solutions kept out of the chapter text; solutions and extensions in a separate file.
- **81 Final Mastery Assessment:** a sandbox setup script and a checker script (`companion/assessment/`), fifteen tasks in two levels, rubric and answer key separate. The reference solution (author-side, `verification/ch81-assessment/`) scores 0 of 15 before and 15 of 15 after.

## 2. Beginner comprehension review
Challenges are Deep and optional. The assessment states its limits: a self-check, open book, not a certificate.

## 3. Command verification
Recordings pass locally in Bash and zsh. Defects found while building: `grep -q ok` matching `broken` (fixed with `-x`); the sensitive-data removal mode of `git-filter-repo` restructures local refs (branches that exist only locally are lost), so the assessment tells learners to push first and do that task last; cone-mode sparse checkout keeps top-level files, so the check tests for a folder instead.

## 4. Cross-references
No problems reported by the checkers.

## 5. Research / source review
R353-R354 are locally tested. No GitHub claim.

## 6. Security review
Made-up secrets; the checker never reads real credentials; the setup script only deletes its own sandbox folder (`ASSESS_DIR`). **Caution recorded:** while developing, a destructive command was once run in the wrong folder because a shell variable had not persisted between tool calls; it failed harmlessly. The scripts guard against a missing sandbox (`No sandbox found`) but the reader should read a script before running it.

## 7. Editorial review
British spelling; no banned phrases.

## Open items
1. The checker may misjudge unusual valid solutions; more reference solutions should be tried.
2. Pilot use by real learners.
