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
tmp = tempfile.mkdtemp(prefix="session-")
home = os.path.join(tmp, "home", "learner"); os.makedirs(home)
argv = {"bash": ["bash", "--norc", "--noprofile", "--noediting", "-i"], "zsh": ["zsh", "-f", "-i", "-o", "no_zle", "-o", "no_prompt_sp"]}[shell]
env = {"HOME": home, "PATH": os.environ["PATH"], "LC_ALL": "C", "TERM": "dumb", "USER": "learner", "LOGNAME": "learner"}
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
cmds = [l.rstrip("\n") for l in open(session) if l.strip() and not l.startswith("#")]
out = MARK
for c in cmds:
    os.write(fd, (c + "\n").encode()); read_until_prompt()
    chunk = buf.decode(errors="replace"); buf = b""
    out += chunk
os.write(fd, b"exit\n"); time.sleep(0.2)
out = re.sub(r"\x1b\[[0-9;?]*[A-Za-z]", "", out).replace("\r", "")
out = out.replace(MARK, "$ ")
out = out.replace(home, "/home/learner").replace(tmp, "/tmp/session")
out = re.sub(r"(?m)^([-dlrwxs]{10}) +(\d+) +\S+ +\S+ +(\d+) +[A-Z][a-z]{2} +\d+ +[\d:]+ ", r"\1 \2 learner learner \3 <date> ", out)
out = re.sub(r"\n\$ $", "\n", out)
out = out.rstrip("\n") + "\n"
if check:
    exp = open(check).read()
    if exp != out:
        sys.stdout.writelines(difflib.unified_diff(exp.splitlines(True), out.splitlines(True), "expected", "actual")); sys.exit(1)
    print(f"OK {shell} {os.path.basename(session)}"); sys.exit(0)
sys.stdout.write(out)
