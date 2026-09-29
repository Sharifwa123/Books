#!/usr/bin/env python3
"""Run commands in an INTERACTIVE shell (via a pseudo-terminal) inside a throwaway HOME and print a transcript,
so output matches what a learner sees (interactive shells word errors differently from `sh -c`).
Usage: run_session.py <bash|zsh> <session.txt> [--check expected.txt]
Session file: one command per line; blank lines and lines starting '#' are ignored.
Normalisation: HOME -> /home/learner; `ls -l` owner/date masked; LC_ALL=C (so `ls` sorts in C order).
With --check, exits 1 and prints a diff if the transcript differs."""
import difflib, os, pty, re, select, sys, tempfile, time
shell, session = sys.argv[1], sys.argv[2]
check = sys.argv[sys.argv.index("--check") + 1] if "--check" in sys.argv else None
MARK = "@@READY@@ "
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GITMODE = open(session).readline().startswith("#!git")
# A FIXED home path (serialised with a lock) so that anything Git writes into commit messages (such as
# "Merge branch 'main' of <path>") is identical on every run and every machine, keeping commit hashes reproducible.
import fcntl, shutil
_lock = open(os.path.join(tempfile.gettempdir(), "sharif-session.lock"), "w"); fcntl.flock(_lock, fcntl.LOCK_EX)
tmp = os.path.join(tempfile.gettempdir(), "sharif-session-home")
shutil.rmtree(tmp, ignore_errors=True)
home = os.path.join(tmp, "learner"); os.makedirs(home)
argv = {"bash": ["bash", "--norc", "--noprofile", "--noediting", "-i"], "zsh": ["zsh", "-f", "-i", "-o", "no_zle", "-o", "no_prompt_sp"]}[shell]
env = {"HOME": home, "PATH": os.environ["PATH"], "LC_ALL": "C", "TERM": "dumb", "USER": "learner", "LOGNAME": "learner", "STARTER": os.path.join(root_dir, "companion", "sunrise-bakery-starter")}
if GITMODE:  # neutralise the host's Git setup and anything that would block a terminal session
    env.update({"GIT_CONFIG_SYSTEM": "/dev/null", "GIT_PAGER": "cat", "PAGER": "cat", "GIT_EDITOR": "true", "EDITOR": "true",
                "GIT_TERMINAL_PROMPT": "0"})
pid, fd = pty.fork()
if pid == 0:
    os.chdir(home); os.execvpe(argv[0], argv, env)
buf = b""
def read_until_prompt(timeout=15):
    global buf
    end = time.time() + timeout
    while time.time() < end:
        if buf.endswith(MARK.encode()): return
        r, _, _ = select.select([fd], [], [], 0.2)
        if r:
            try: d = os.read(fd, 65536)
            except OSError: return
            if not d: return
            buf += d
    raise SystemExit(f"timeout waiting for prompt; got: {buf[-200:]!r}")
time.sleep(0.3)
os.write(fd, (("PS1" if shell == "bash" else "PROMPT") + f"='{MARK}'\n").encode())
buf = b""; read_until_prompt()
buf = b""
if GITMODE:  # every git call gets a timestamp one minute after the previous call (deterministic): real, reproducible commit hashes and dates
    wrapper = ('git() { _n=$((_n+1)); local _t=$((1767603600 + _n*60)); '
               'GIT_AUTHOR_DATE="$_t +0000" GIT_COMMITTER_DATE="$_t +0000" command git "$@"; }')
    os.write(fd, (wrapper + "\n").encode()); read_until_prompt(); buf = b""
cmds = [l.rstrip("\n") for l in open(session) if l.strip() and not l.startswith("#")]
out = MARK
for c in cmds:
    silent = c.startswith("@ ")
    os.write(fd, ((c[2:] if silent else c) + "\n").encode()); read_until_prompt()
    chunk = buf.decode(errors="replace"); buf = b""
    if silent: chunk = MARK if False else ""; out = out  # setup step: neither echoed nor recorded
    else: out += chunk
os.write(fd, b"exit\n"); time.sleep(0.2)
out = re.sub(r"\x1b\[[0-9;?]*[A-Za-z]", "", out).replace("\r", "")
out = out.replace(MARK, "$ ")
out = out.replace(home, "/home/learner").replace(tmp, "/tmp/session")
if GITMODE:
    # progress meters differ from computer to computer (thread counts, speeds): drop them, keep the settled summary lines
    out = re.sub(r"(?m)^(Enumerating objects|Counting objects|Compressing objects|Writing objects|Receiving objects|Resolving deltas|Unpacking objects|Delta compression|Total \d+|remote: (Enumerating|Counting|Compressing|Total)).*\n", "", out)
    out = re.sub(r"git version \d+\.\d+\.\d+[^\n]*", "git version <version>", out)
out = re.sub(r"(?m)^([-dlrwxs]{10}) +(\d+) +\S+ +\S+ +(\d+) +[A-Z][a-z]{2} +\d+ +[\d:]+ ", r"\1 \2 learner learner \3 <date> ", out)
out = re.sub(r"\n\$ $", "\n", out)
out = out.rstrip("\n") + "\n"
if check:
    exp = open(check).read()
    if exp != out:
        sys.stdout.writelines(difflib.unified_diff(exp.splitlines(True), out.splitlines(True), "expected", "actual")); sys.exit(1)
    print(f"OK {shell} {os.path.basename(session)}"); sys.exit(0)
sys.stdout.write(out)
