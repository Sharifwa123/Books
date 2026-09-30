# Appendix C — Common Git Errors

A quick index to Chapter 78<!--ref:trouble--> and Chapter 79<!--ref:playbooks-->. For each message: what it means in a phrase, the **safe** first step, and the chapter that explains it. Messages are shortened; your Git may add "hint:" lines or change the wording.

| Message (shortened) | Meaning | Safe first step | Where |
|---|---|---|---|
| `fatal: not a git repository` | no repository in this folder or its parents | check the folder with `pwd`; `cd` to the project | 78<!--ref:trouble--> |
| `fatal: pathspec 'x' did not match` | Git cannot find that file or branch | `git status`, `git branch -a` | 78<!--ref:trouble--> |
| `Author identity unknown` | no name and email configured | `git config --global user.name` and `user.email` | 14<!--ref:config-->, 78<!--ref:trouble--> |
| `nothing to commit` / `no changes added to commit` | nothing staged | `git status`, then `git add` | 78<!--ref:trouble--> |
| `Your local changes ... would be overwritten by checkout` | uncommitted edits would be lost | commit or `git stash` | 78<!--ref:trouble-->, 24<!--ref:stash--> |
| `! [rejected] ... (fetch first)` / `non-fast-forward` | the remote has commits you lack | `git fetch`, read, merge or rebase | 78<!--ref:trouble-->, 23<!--ref:remotes--> |
| `fatal: refusing to merge unrelated histories` | no common ancestor | clone instead of `init`; decide the base | 78<!--ref:trouble--> |
| `error: remote origin already exists` | that remote name is taken | `git remote -v`; use another name or `set-url` | 78<!--ref:trouble--> |
| `does not appear to be a git repository` | wrong or unreachable address | `git remote -v`; check the address | 78<!--ref:trouble--> |
| `fatal: a branch named 'x' already exists` | the name is taken | choose another name | 78<!--ref:trouble--> |
| `error: the branch 'x' is not fully merged` | unmerged commits would be lost | check `git log main..x` before `-D` | 78<!--ref:trouble--> |
| `fatal: ambiguous argument 'x'` | Git cannot tell what `x` is | `git branch -a`, `git log --oneline` | 78<!--ref:trouble--> |
| `Unable to create '.git/index.lock': File exists` | another Git process, or a leftover lock | make sure nothing is running, then remove the file | 78<!--ref:trouble--> |
| `.gitignore` seems ignored | the file is already tracked | `git rm --cached FILE` | 78<!--ref:trouble-->, 18<!--ref:tracking--> |
| `HEAD detached at ...` | you are on a commit, not a branch | `git switch -c NAME` to keep work | 78<!--ref:trouble--> |
| `CONFLICT (content): Merge conflict in ...` | both sides changed the same lines | edit, `git add`, commit; or `git merge --abort` | 78<!--ref:trouble-->, 22<!--ref:conflicts--> |
| `Need to specify how to reconcile divergent branches` | local and remote each have new commits | choose merge or rebase | 78<!--ref:trouble-->, 23<!--ref:remotes--> |
| `Permission denied (publickey)` | SSH key missing or not registered | check the key on your account | 38<!--ref:ghauth--> (not reproduced) |
| push rejected for a secret | push protection found a credential | remove it; revoke if exposed | 62<!--ref:ghsec--> (not reproduced) |

**The dangerous "fixes" to avoid** (see each entry for the safer alternative): `git push --force`, `git reset --hard`, `git checkout -f`, `git branch -D`, `git clean -fd`, deleting `.git`, and `--allow-unrelated-histories` used blindly.
