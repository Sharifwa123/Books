#!/usr/bin/env python3
"""Checks statements that the Git chapters make against the Git 2.56.0 manual sources (Documentation/*.adoc at tag v2.56.0).
Each check is (ledger row, manual page, regular expression that must match the page text, what the chapter states).
The pages are fetched from raw.githubusercontent.com (and cached), and the fetched copies are recorded by tools/fetch_source.py.
It prints one line per check and exits 1 if a check fails. It checks that the *manual says* what the chapter attributes to it;
it does not run Git (the recordings do that).   usage: git-manual-checks.py [--json]"""
import json, os, re, sys, urllib.request
TAG = "v2.56.0"
BASE = f"https://raw.githubusercontent.com/git/git/{TAG}/Documentation/"
CACHE = os.environ.get("SOURCE_CACHE", "/tmp/git-manual-cache")
os.makedirs(CACHE, exist_ok=True)
def raw(name):
    p = os.path.join(CACHE, name + ".adoc")
    if not os.path.exists(p) or os.path.getsize(p) < 200:
        req = urllib.request.Request(BASE + name + ".adoc", headers={"User-Agent": "book-verification/1.0"})
        open(p, "wb").write(urllib.request.urlopen(req, timeout=60).read())
    return open(p, encoding="utf-8").read()
def page(name):
    """The page text with the pages it includes (one level, e.g. merge-options.adoc), backticks removed, whitespace collapsed."""
    t = raw(name)
    for inc in re.findall(r"^include::([\w./-]+?)\.adoc\[", t, flags=re.M):
        try: t += "\n" + raw(inc)
        except Exception: pass
    return re.sub(r"\s+", " ", t.replace("`", ""))
C = [
 ("R355", "git-fsck", r"--lost-found:: Write dangling objects into .git/lost-found/commit/ or .git/lost-found/other/, depending on type. If the object is a blob, the contents are written into the file", "fsck --lost-found writes dangling blobs into .git/lost-found/other/"),
 ("R355", "git-fsck", r"dangling:: --no-dangling:: Print objects that exist but that are never .directly. used", "fsck prints dangling objects by default"),
 ("R153", "gitrepository-layout", r"HEAD:: A symref \(see glossary\) to the refs/heads/ namespace describing the currently active branch", "the HEAD file is a symref to the current branch"),
 ("R153", "gitrepository-layout", r"HEAD can also record a specific commit directly", "HEAD can record a commit directly (detached)"),
 ("R141", "git-init", r"--bare", "git init --bare exists"),
 ("R154", "git-status", r"paths that have differences between the index file and the current HEAD commit", "status reports index-versus-HEAD differences"),
 ("R154", "git-status", r"paths in the working tree that are not tracked by Git", "status reports untracked files"),
 ("R155", "git-init", r"Create an empty Git repository", "git init creates an empty repository"),
 ("R155", "git-add", r"Add file contents to the index", "git add adds to the index"),
 ("R155", "git-commit", r"Record changes to the repository", "git commit records changes"),
 ("R155", "git-commit", r"Create a new commit containing the current contents of the index", "a commit records the index"),
 ("R159", "git-diff", r"Show changes between commits, commit and working tree", "git diff compares commits and the working tree"),
 ("R159", "git-diff", r"--staged", "--staged exists"),
 ("R159", "git-diff", r"--cached", "--cached is a synonym"),
 ("R163", "git-rm", r"--cached.{0,200}(only from the index|unstage and remove paths only from the index)", "rm --cached removes only from the index"),
 ("R163", "git-mv", r"Move or rename a file, a directory, or a symlink", "git mv renames"),
 ("R166", "git-commit", r"--amend", "--amend exists"),
 ("R166", "git-commit", r"Replace the tip of the current branch by creating a new commit", "amend replaces the tip by a new commit"),
 ("R166", "git-commit", r"--no-edit", "--no-edit exists"),
 ("R166", "git-reflog", r"reflogs.{0,80}record when the tips of branches", "the reflog records tips"),
 ("R167", "git-commit", r"--author=<author>", "--author exists"),
 ("R168", "git-commit", r"--allow-empty", "--allow-empty exists"),
 ("R172", "git-switch", r"local modifications", "switch mentions local modifications"),
 ("R172", "git-switch", r"refuses|refuse", "switch can refuse"),
 ("R173", "git-merge", r"fast-forward", "merge describes fast-forward"),
 ("R174", "git-merge", r"Incorporates changes from the named commits", "merge incorporates changes"),
 ("R175", "git-merge", r"--no-ff", "--no-ff exists"),
 ("R175", "git-merge", r"--squash.{0,600}do not actually make a commit", "--squash makes no commit"),
 ("R176", "git-merge", r"HOW CONFLICTS ARE PRESENTED", "conflict markers are documented"),
 ("R176", "git-merge", r"<<<<<<<", "the <<<<<<< marker is documented"),
 ("R176", "git-merge", r"git merge --abort", "merge --abort exists"),
 ("R178", "git-clone", r"Clone a repository into a new directory", "clone"),
 ("R178", "git-push", r"--set-upstream", "push -u sets upstream"),
 ("R178", "git-remote", r"Manage set of tracked repositories", "git remote manages remotes"),
 ("R179", "git-fetch", r"Download objects and refs from another repository", "fetch downloads"),
 ("R179", "git-pull", r"Fetch from and integrate with another repository or a local branch", "pull = fetch and integrate"),
 ("R181", "git-stash", r"Stash the changes in a dirty working directory away", "stash"),
 ("R181", "git-stash", r"--include-untracked", "stash -u includes untracked files"),
 ("R182", "git-tag", r"Create, list, delete or verify tags", "tag"),
 ("R182", "git-clean", r"Remove untracked files from the working tree", "clean removes untracked files"),
 ("R182", "git-clean", r"--dry-run", "clean -n is --dry-run"),
 ("R183", "git-grep", r"Print lines matching a pattern", "git grep"),
 ("R183", "git-blame", r"Show what revision and author last modified each line of a file", "git blame"),
 ("R183", "git-log", r"-S<string>", "log -S"),
 ("R184", "git-restore", r"Restore working tree files", "git restore"),
 ("R184", "git-restore", r"--staged", "restore --staged"),
 ("R185", "git-reset", r"Set HEAD or the index to a known state", "git reset"),
 ("R185", "git-reset", r"--hard", "reset --hard"),
 ("R185", "git-reset", r"--hard:: Overwrite all files and directories with the version from _?<commit>_?", "reset --hard overwrites files with the commit's version"),
 ("R187", "git-reflog", r"Manage reflog information", "git reflog"),
 ("R188", "git-switch", r"--detach", "switch --detach"),
 ("R188", "glossary-content", r"detached HEAD", "detached HEAD is defined in the glossary"),
 ("R190", "git-rebase", r"Reapply commits on top of another base tip", "rebase"),
 ("R193", "git-cherry-pick", r"Apply the changes introduced by some existing commits", "cherry-pick"),
 ("R199", "git-hash-object", r"Compute object ID and optionally create an object from a file", "hash-object"),
 ("R199", "git-cat-file", r"Provide contents or details of repository objects", "cat-file"),
 ("R200", "git-ls-tree", r"List the contents of a tree object", "ls-tree"),
 ("R200", "gitrepository-layout", r"HEAD", "HEAD is documented in the repository layout"),
 ("R203", "git-worktree", r"Manage multiple working trees", "worktree"),
 ("R203", "git-sparse-checkout", r"Reduce your working tree to a subset of tracked files", "sparse-checkout"),
 ("R203", "git-clone", r"--depth", "clone --depth"),
 ("R208", "git-rerere", r"Reuse recorded resolution of conflicted merges", "rerere"),
 ("R213", "gitignore", r"Specifies intentionally untracked files to ignore", "gitignore"),
 ("R226", "git-remote", r"git remote add ", "remote add"),
 ("R239", "git-ls-remote", r"List references in a remote repository", "ls-remote"),
 ("R240", "git-merge", r"--allow-unrelated-histories", "unrelated histories need --allow-unrelated-histories"),
 ("R243", "git-archive", r"Create an archive of files from a named tree", "archive"),
]
res = []
for row, pg, rx, what in C:
    try: ok = re.search(rx, page(pg), flags=re.I) is not None
    except Exception as e: ok = False; what += f" (fetch error {e})"
    res.append({"row": row, "page": pg, "regex": rx, "what": what, "ok": ok})
    print(("ok  " if ok else "FAIL"), row, pg, "-", what)
if "--json" in sys.argv: json.dump(res, open("git-manual-checks-result.json", "w"), indent=1)
bad = [r for r in res if not r["ok"]]
print(f"{len(res) - len(bad)} of {len(res)} checks matched")
sys.exit(1 if bad else 0)
