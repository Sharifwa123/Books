# Chapter 81 solutions: rubric and answer key

**Do not read this before you have tried the assessment.**

## Rubric

| Level | Requirement |
|---|---|
| Proficient | at least 9 of the 10 tasks P1 to P10 pass |
| Mastery | all ten Proficient tasks and at least 4 of the 5 tasks M1 to M5 pass |

Beyond the checker, a reviewer can ask you to explain: why P6 is a revert and not a reset; what the tag in P7 names; why M1 needs a forced push; why the test in M2 matches a whole line.

## Answer key

Commit names in your repository differ from anything printed here.

| Task | One way to do it | Chapters to revisit |
|---|---|---|
| P1 | `git config user.name "Your Name"` and `git config user.email "you@example.org"` (no `--global`) | 14<!--ref:config--> |
| P2 | `git switch -c feature/tea`, append the line, `git commit -am "Add tea"` | 20<!--ref:branching-->, 19<!--ref:commits--> |
| P3 | `git push -u origin feature/tea` | 23<!--ref:remotes--> |
| P4 | write `*.log` in `.gitignore`, `git add .gitignore`, commit | 18<!--ref:tracking--> |
| P5 | `git fetch`, `git switch -c combined origin/edit-a`, `git merge origin/edit-b`, edit `README.md`, `git add`, `git commit` | 22<!--ref:conflicts--> |
| P6 | `git revert COMMIT` (find it with `git log --grep`), then `git push origin main` | 25<!--ref:undo-->, 76<!--ref:scenarios--> |
| P7 | `git tag -a v1.1.0 -m "Version 1.1.0"` on the final tip of `main`, then `git push origin v1.1.0` | 29<!--ref:tags-->, 66<!--ref:releases--> |
| P8 | `git reflog`, find "Precious work", `git branch precious NAME` | 26<!--ref:reflog-->, 79<!--ref:playbooks--> |
| P9 | write both files, `git add`, commit, push | 64<!--ref:oss-->, 62<!--ref:ghsec--> |
| P10 | a file with `on:`, `permissions:`, `jobs:` and `uses: actions/checkout@<40 hex characters>` | 54<!--ref:actions-->, 60<!--ref:wfsec--> |
| M1 | push `combined`, `precious` and the tag; then `git filter-repo --sensitive-data-removal --invert-paths --path secrets.env --force` and `git push --force --mirror origin` | 33<!--ref:gitsec-->, 79<!--ref:playbooks--> |
| M2 | `git bisect start HEAD FIRST-COMMIT`, then `git bisect run sh test.sh` with `grep -qx ok state.txt`; write the subject "Change state" into `bisect-answer.txt`; `git bisect reset` | 28<!--ref:tools-->, 80<!--ref:challenges--> |
| M3 | `git clone --depth 1 --no-checkout file:///PATH/remote.git slim`, then `git sparse-checkout set docs` and `git checkout main` in `slim` | 31<!--ref:bigrepos--> |
| M4 | `git log --format='- %s' v1.0.0..v1.1.0 > RELEASE_NOTES.md` | 66<!--ref:releases--> |
| M5 | `printf '%s' 'Order 42 shipped' \| openssl dgst -sha256 -hmac 'bakery-test-secret'`, keep only the hexadecimal digest | 74<!--ref:api--> |

**Note on M3.** The `sparse-checkout set` command works in "cone" mode by default, which always keeps the files at the top level of the repository; that is why the check tests for the absence of the `src` folder and not of top-level files.

**Reflection answers.**

1.1 Compare your prediction with the result; large gaps show topics that you overestimate.

2.1 One order: P1, P2, P3, P4, P5, P8, P6, P9, P10, then push `main`, then P7. P7 depends on all changes to `main`; M1 depends on everything being pushed.

3.1 Record the pages you needed; they are your revision list.

4.1 A good explanation states purpose, command and pitfall; for example P6: purpose "undo a public mistake without disturbing others", command `git revert`, pitfall "resetting and force-pushing rewrites what colleagues already have".

5.1 The tag is lightweight and not annotated; it points to a commit that is no longer the tip of `main`; it was not pushed; or the name differs (for example `v1.1` or `V1.1.0`). Use `git cat-file -t v1.1.0`, `git rev-parse v1.1.0^{commit} main` and `git ls-remote --tags origin`.
