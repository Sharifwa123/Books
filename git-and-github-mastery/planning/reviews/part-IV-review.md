# Part IV review (Chapters 25-35), 2026-09-30

All eleven chapters are `status: draft`. Chapters 25-35 were drafted from recorded Bash and zsh sessions (`verification/ch25-*` to `ch35-*`); every `$ ` line in the manuscript is checked against those recordings, and the recordings are re-run in CI on the runner's Git (2.55.0). Chapters 27, 28, 30, 31, 32 and 33 are tagged [Deep] or contain [Deep] material as the outline says.

## 1. Technical review
- **Undo, reflog, rebase, tools (25-28):** restore, reset (three strengths), revert, reflog recovery, detached HEAD, rebase (with conflicts and interactive squash driven by `GIT_SEQUENCE_EDITOR`), cherry-pick, bisect run, format-patch/apply --check/am. The empty-commit revert exercise stays **blocked** and is not used.
- **Objects and big repositories (30-31):** blob/tree/commit/tag objects, refs, packfiles, gc, fsck, archive; worktree, shallow clone, sparse checkout, submodule (including the recorded refusal of the `file` transport), Git LFS pointer files. The object name was recomputed independently with `sha1sum`.
- **Customising and security (32-33):** aliases, a `pre-commit` hook, attributes and line endings, `credential.helper store` with a made-up credential, rerere; secrets in history, `git filter-repo` (no remote), GPG-signed commits.
- **Defects found by CI on Git 2.55.0, all handled with `.alt` recordings and noted in the text, none behavioural:** `git branch -d` advice, invalid-branch-name hints (Ch 20), rebase-conflict advice and `# ` in the subject (Ch 27), bisect quoting (Ch 28), `worktree list` padding (Ch 31), ignored-file hint (Ch 33).
- **CI environment defects, fixed:** `git-filter-repo` was invisible to the recording tool because the tool uses its own `HOME`; the workflow now uses a wrapper pointing at the module folder.

## 2. Beginner comprehension review
- Every chapter follows the pattern: motivation, a small recorded demonstration read line by line, a caution, a summary. [Deep] chapters say so at the top and can be skipped on a first read.
- `check_term_order.py` shows only forward pointers with chapter references, plus the front-matter key `tag:` (false positive).
- Chapters 30-31 are dense and need a pilot read by a beginner.

## 3. Command verification
`verification/run_all.sh`: all transcripts (Bash and zsh) pass locally and in CI. The following were **not run** and are marked in the text: `git pull --rebase`, `--force-with-lease`, other interactive-rebase actions, cherry-pick and patch conflicts, manual bisect, `git apply` without `--check`, partial clone, subtree, submodule clone/update/removal, hook types other than `pre-commit`, merge strategies and drivers, `git maintenance`, OS credential helpers, SSH-key signing (ssh-keygen was unavailable on the test computer).

## 4. Cross-references
`resolve_refs.py --check`, `check_links.py`, `check_refs`: no problems. Forward references to Part V (`whatgh`, `ghauth`, `ghsec`, `pr`, `actions`, `collab`, `oss`, `releases`) use `Chapter [[key]]`.

## 5. Research / source review
Ledger rows R173-R223 cover Part IV. Locally tested rows have no official-source verification because the official hosts are blocked. **Open, unverified:** reflog expiry (R189), `pull --rebase`/`--force-with-lease` (R191), semantic-versioning rules (R198), default hash function (R202), partial clone/subtree/monorepo (R204), submodule transport rule (R205), platform secret scanning and branch protection (R214), filter-repo recommendation and remote behaviour (R215), SSH signing and "Verified" marks (R216), supply-chain guidance, named workflow models (R219), manual pages and platform documentation (R221-R223).

## 6. Security review
- Every secret in the recordings is made up (`not-a-real-key`, `not-a-real-password`); `check_secrets.py` finds nothing.
- Chapter 32 warns that `credential.helper store` writes plain text; Chapter 33 states the revoke-first order and that a history rewrite does not un-leak a secret; Chapter 33 names **no** real incident (none was verified from a primary source).
- The recorded submodule refusal and the caution against a permanent `protocol.file.allow=always` are in Chapter 31.

## 7. Editorial review
British spelling; no banned filler phrases; consistent callouts. Chapters 27, 28, 30-32 are [Deep] and first-read "later". Projects 1-6 are embedded in Chapters 16-24; no new project was added in Part IV.

## Open items
1. Determine the current upstream Git release; re-run every test on it.
2. Verify the open rows above when official hosts are reachable.
3. Windows and macOS runs; SSH-based checks need `ssh-keygen`.
4. Pilot read (especially Chapters 30-31).
5. `EX-revert-empty-commit` stays blocked.
