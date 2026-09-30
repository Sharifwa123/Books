# Chapter 31 exercises — Big and Complex Repositories

Attempt each exercise before you open `solutions/ch31-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed), and local bare repositories as remotes (Chapter 23<!--ref:remotes-->). For Level 4, git-lfs must be installed.

## Level 1 — Guided

**1.1 A second folder.** Run `git worktree add ../bakery-hotfix -b hotfix`. What does `git worktree list` show?

**1.2 Work in it.** Commit a change in the new folder, then look at `git log --oneline --all --graph` from the first folder.

## Level 2 — Partially guided

**2.1 Clean up.** Remove the worktree with `git worktree remove`. Does the `hotfix` branch still exist?

**2.2 A shallow clone.** Make a bare copy with `git clone --bare`, then clone it with `--depth 1` using a `file://` address. How many commits does `git log` show?

## Level 3 — Independent

**3.1 Complete it.** Run `git fetch --unshallow` and count the commits again. Check `git rev-parse --is-shallow-repository` before and after.

**3.2 Sparse.** Add `docs` and `src` folders and commit. Use `git sparse-checkout set docs`, then `ls`, then `git sparse-checkout disable`.

## Level 4 — Professional scenario

**4.1 Pointer files.** Set up `git lfs track "*.png"`, add a small fake `logo.png`, and commit. Use `git cat-file -p HEAD:logo.png` to read what Git stored. What is in it, and where is the real file?

**4.2 A submodule.** Create a second repository `lib-repo` with one commit. Add it as a submodule of `bakery-menu` at `vendor/lib`. Read what Git says when it refuses, and explain why you may use `-c protocol.file.allow=always` for this demonstration but should not set it permanently.

## Level 5 — Troubleshooting

**5.1** A learner deleted the extra worktree folder with `rm -r` and now `git worktree list` still shows it. What should they do?

**5.2** A learner made a shallow clone and `git blame` stops at the first commit. Why, and what is the fix?

**5.3** A learner added a 300 MB video, then set up LFS. The repository is still huge. Why?
