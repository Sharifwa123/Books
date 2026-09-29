#!/usr/bin/env python3
"""Small, dependency-free scan for accidentally committed credentials.
Deliberate fake tokens used in exercises must contain the marker FAKE (e.g. FAKE_TOKEN_DO_NOT_USE_0000) and are ignored."""
import os, re, subprocess, sys
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PATTERNS = {
 "private key block": r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY",
 "GitHub token (ghp_/gho_/ghu_/ghs_/ghr_)": r"\bgh[pousr]_[A-Za-z0-9]{30,}",
 "GitHub fine-grained token": r"\bgithub_pat_[A-Za-z0-9_]{30,}",
 "AWS access key id": r"\bAKIA[0-9A-Z]{16}\b",
 "Slack token": r"\bxox[baprs]-[A-Za-z0-9-]{10,}",
 "generic assignment of long secret": r"(?i)\b(?:api[_-]?key|secret|token|passwd|password)\s*[:=]\s*['\"][A-Za-z0-9/+_\-]{24,}['\"]",
}
files = subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True, check=True).stdout.split("\n")
bad = 0
for f in files:
    if not f or f.endswith((".png", ".jpg", ".pdf")): continue
    try: text = open(os.path.join(root, f), errors="replace").read()
    except OSError: continue
    for name, rx in PATTERNS.items():
        for m in re.finditer(rx, text):
            line = text[max(0, text.rfind("\n", 0, m.start())):text.find("\n", m.end())]
            if "FAKE" in line.upper(): continue
            print(f"POSSIBLE SECRET ({name}): {f}: {m.group(0)[:12]}..."); bad += 1
print(f"files scanned: {len([f for f in files if f])}, findings: {bad}")
sys.exit(1 if bad else 0)
