#!/usr/bin/env python3
"""Check book claims against the upstream Git documentation SHIPPED WITH GIT 2.43.0.

Docs source: Ubuntu packages `git-doc` and `git-man` (built from upstream Git sources), extracted with
    apt-get download git-doc git-man git-lfs && dpkg-deb -x <each>.deb $DOCS
This is version-bound documentation (Git 2.43.0), NOT the current git-scm.com reference manual (unreachable
when written). Ledger classification: "official docs (packaged upstream docs, 2.43.0)".
Config-variable reference is checked in git-config.html (the .txt files only contain include:: directives).
Usage: DOCS=/path/to/extracted python3 verify-against-docs.py
"""
import os, re, sys, html
DOCS = os.environ.get("DOCS", "/tmp/claude-0/-home-user-Books/dd64ee17-5257-5272-b4ad-575dbe6858f1/scratchpad/gitdocs")
D = f"{DOCS}/usr/share/doc/git-doc"
_cache = {}
def load(name):
    if name in _cache: return _cache[name]
    p = f"{D}/{name}"
    if not os.path.exists(p): _cache[name] = None; return None
    t = open(p, errors="replace").read()
    if name.endswith(".html"):
        t = html.unescape(re.sub(r"<[^>]+>", "", t))
    _cache[name] = t; return t
fails = 0
def chk(cid, doc, pattern, note="", absent=False):
    global fails
    t = load(doc)
    if t is None: print(f"MISSING-DOC {cid} {doc}"); fails += 1; return
    found = re.search(pattern, t, re.I | re.M) is not None
    ok = (not found) if absent else found
    print(f"{'PASS' if ok else 'FAIL'}  {cid:<26} {doc:<28} {'ABSENT ' if absent else ''}/{pattern}/ {('-- ' + note) if note else ''}")
    if not ok: fails += 1
CFG = "git-config.html"
A = [
("restore.staged","git-restore.txt",r"--staged"),
("restore.source","git-restore.txt",r"--source=<tree>"),
("restore.experimental","git-restore.txt",r"EXPERIMENTAL","docs label restore experimental in 2.43.0"),
("switch.experimental","git-switch.txt",r"EXPERIMENTAL","docs label switch experimental in 2.43.0"),
("switch.create","git-switch.txt",r"-c <new-branch>"),
("reset.soft","git-reset.txt",r"--soft"),("reset.mixed","git-reset.txt",r"--mixed"),("reset.hard","git-reset.txt",r"--hard"),
("revert.no-commit","git-revert.txt",r"--no-commit"),("revert.mainline","git-revert.txt",r"--mainline"),
("revert.no-quiet","git-revert.txt",r"(^|\s)(-q|--quiet)\b","-q NOT documented for revert","absent"),
("revert.empty-undocumented","git-revert.txt",r"empty","revert doc does not discuss empty commits","absent"),
("cherrypick.empty","git-cherry-pick.txt",r"cherry-picking an empty commit will fail"),
("push.fwl","git-push.txt",r"--force-with-lease"),("push.fio","git-push.txt",r"--force-if-includes"),
("push.delete","git-push.txt",r"--delete"),("push.tags","git-push.txt",r"--tags"),
("rebase.abort","git-rebase.txt",r"--abort"),("rebase.continue","git-rebase.txt",r"--continue"),("rebase.skip","git-rebase.txt",r"--skip"),
("rebase.autosquash","git-rebase.txt",r"--autosquash"),("rebase.merges","git-rebase.txt",r"--rebase-merges"),
("rebase.todo.edit","git-rebase.txt",r'"edit"',"todo command documented in prose"),
("rebase.todo.reword","git-rebase.txt",r'"reword"',"todo command documented in prose"),
("rebase.todo.squash","git-rebase.txt",r'"squash"|`squash`',"todo command documented in prose"),
("rebase.todo.fixup","git-rebase.txt",r'"fixup"|`fixup`',"todo command documented in prose"),
("rebase.todo.drop","git-rebase.txt",r'"drop"',"todo command documented in prose"),
("rebase.todo.exec","git-rebase.txt",r'"exec"|`exec`',"todo command documented in prose"),
("rebase.recovering","git-rebase.txt",r"RECOVERING FROM UPSTREAM REBASE","docs warn about rewriting published history"),
("clean.dryrun","git-clean.txt",r"--dry-run"),("clean.requireforce","git-clean.txt",r"clean\.requireForce"),
("config.system","git-config.txt",r"--system"),("config.global","git-config.txt",r"--global"),("config.local","git-config.txt",r"--local"),
("config.worktree","git-config.txt",r"--worktree"),("config.showorigin","git-config.txt",r"--show-origin"),("config.showscope","git-config.txt",r"--show-scope"),
("cfg.includeif",CFG,r"includeIf"),("cfg.defaultbranch",CFG,r"init\.defaultBranch"),
("cfg.gpg.format",CFG,r"gpg\.format"),("cfg.gpg.ssh.allowed",CFG,r"gpg\.ssh\.allowedSignersFile"),
("cfg.commit.gpgsign",CFG,r"commit\.gpgSign"),("cfg.gc.reflogexpire",CFG,r"gc\.reflogExpire\b"),
("cfg.pull.rebase",CFG,r"pull\.rebase"),("cfg.pull.ff",CFG,r"pull\.ff"),("cfg.hookspath",CFG,r"core\.hooksPath"),
("cfg.autocrlf",CFG,r"core\.autocrlf"),("cfg.worktreeconfig",CFG,r"extensions\.worktreeConfig"),
("cfg.credential.helper",CFG,r"credential\.helper"),
("attr.eol","gitattributes.txt",r"^`eol`"),("attr.text","gitattributes.txt",r"^`text`"),("attr.filter","gitattributes.txt",r"^`filter`"),
("hooks.precommit","githooks.txt",r"^pre-commit"),("hooks.commitmsg","githooks.txt",r"^commit-msg"),("hooks.prepush","githooks.txt",r"^pre-push"),
("hooks.prereceive","githooks.txt",r"^pre-receive"),("hooks.postreceive","githooks.txt",r"^post-receive"),
("clone.depth","git-clone.txt",r"--depth"),("clone.filter","git-clone.txt",r"--filter=<filter-spec>"),("clone.single","git-clone.txt",r"--single-branch"),
("sparse.cone","git-sparse-checkout.txt",r"cone mode"),("worktree.add","git-worktree.txt",r"git worktree add"),
("stash.push","git-stash.txt",r"push \["),("stash.untracked","git-stash.txt",r"--include-untracked"),
("tag.annotate","git-tag.txt",r"--annotate"),("merge.noff","git-merge.txt",r"--no-ff"),("merge.squash","git-merge.txt",r"--squash"),
("merge.ffonly","git-merge.txt",r"--ff-only"),("merge.abort","git-merge.txt",r"--abort"),("pull.ffonly","git-pull.html",r"--ff-only"),
("commit.amend","git-commit.txt",r"--amend"),("commit.allowempty","git-commit.txt",r"--allow-empty\b"),
("init.bare","git-init.txt",r"--bare"),("init.initialbranch","git-init.txt",r"--initial-branch"),
("reflog.expire","git-reflog.txt",r"expire"),
("filterbranch.filter-repo","git-filter-branch.txt",r"filter-repo","docs point to git-filter-repo"),
("filterbranch.pitfalls","git-filter-branch.txt",r"pitfalls|WARNING","docs warn about filter-branch"),
("credentials.helper","gitcredentials.txt",r"credential\.helper"),
("maintenance.start","git-maintenance.txt",r"\bstart\b"),
("init.objectformat","git-init.txt",r"--object-format=<format>"),
("bisect.start","git-bisect.txt",r"git bisect start"),("gitignore.patterns","gitignore.txt",r"PATTERN FORMAT"),
]
for a in A:
    cid, doc, pat = a[:3]; note = a[3] if len(a) > 3 else ""; absent = len(a) > 4 and a[4] == "absent"
    chk(cid, doc, pat, note, absent)
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
