#!/bin/sh
# Checks your work in the assessment sandbox (Chapter 81). Usage: sh check.sh
A="${ASSESS_DIR:-$HOME/assessment}"
W="$A/work"
R="$A/remote.git"
[ -d "$W/.git" ] || { echo "No sandbox found in $A: run setup.sh first."; exit 2; }
cd "$W" || exit 2
p=0; m=0
res() { # res LEVEL ID DESCRIPTION STATUS
  if [ "$4" = 0 ]; then echo "PASS $2 $3"; if [ "$1" = P ]; then p=$((p+1)); else m=$((m+1)); fi; else echo "FAIL $2 $3"; fi
}
t() { level=$1; id=$2; desc=$3; shift 3; ( "$@" ) >/dev/null 2>&1; res "$level" "$id" "$desc" $?; }

c_p1() { [ -n "$(git config --local user.name)" ] && [ -n "$(git config --local user.email)" ]; }
c_p2() { git rev-parse -q --verify refs/heads/feature/tea >/dev/null && git show feature/tea:menu.md | grep -q 'Tea' && [ -n "$(git log --format=%s main..feature/tea)" ]; }
c_p3() { git -C "$R" rev-parse -q --verify refs/heads/feature/tea; }
c_p4() { git check-ignore -q debug.log && ! git status --short | grep -q 'debug.log'; }
c_p5() { git rev-parse -q --verify refs/heads/combined >/dev/null && ! git show combined:README.md | grep -q '<<<<<<<\|>>>>>>>\|=======' && git show combined:README.md | grep -q '^Opening hours' && git log --format=%s combined | grep -qF 'Opening hours: 8 to 5' && git log --format=%s combined | grep -qF 'Opening hours: 9 to 6'; }
c_p6() { git log --format=%s main | grep -q 'Set prices to zero' && git show main:menu.md | grep -q '2.50' && git -C "$R" show main:menu.md | grep -q '2.50'; }
c_p7() { [ "$(git cat-file -t refs/tags/v1.1.0)" = tag ] && [ "$(git rev-parse v1.1.0^{commit})" = "$(git rev-parse main)" ] && git -C "$R" rev-parse -q --verify refs/tags/v1.1.0; }
c_p8() { git rev-parse -q --verify refs/heads/precious >/dev/null && [ "$(git log -1 --format=%s precious)" = "Precious work" ]; }
c_p9() { git show main:SECURITY.md | grep -q . && git show main:CONTRIBUTING.md | grep -q .; }
c_p10() { git show main:.github/workflows/ci.yml > "$A/ci.yml.tmp" && python3 - "$A/ci.yml.tmp" <<'PY'
import re, sys, yaml
d = yaml.safe_load(open(sys.argv[1]))
assert ("on" in d or True in d) and "permissions" in d
assert "jobs" in d and d["jobs"]
uses = re.findall(r"uses:\s*(\S+)", open(sys.argv[1]).read())
assert uses and all(re.search(r"@[0-9a-f]{40}$", u) for u in uses)
PY
}
c_m1() { [ -z "$(git log --all --format=%h -S'not-a-real-key')" ] && [ -z "$(git -C "$R" log --all --format=%h -S'not-a-real-key')" ]; }
c_m2() { [ "$(cat "$A/work/bisect-answer.txt" 2>/dev/null)" = "Change state" ] || [ "$(cat "$A/bisect-answer.txt" 2>/dev/null)" = "Change state" ]; }
c_m3() { [ "$(git -C "$A/slim" rev-list --count HEAD)" = 1 ] && [ -d "$A/slim/docs" ] && [ ! -e "$A/slim/src" ]; }
c_m4() { f="$A/work/RELEASE_NOTES.md"; [ -f "$f" ] || f="$A/RELEASE_NOTES.md"; [ -f "$f" ] && git log --format=%s v1.0.0..v1.1.0 | while IFS= read -r s; do grep -qF -- "$s" "$f" || exit 1; done; }
c_m5() { exp=$(printf '%s' 'Order 42 shipped' | openssl dgst -sha256 -hmac 'bakery-test-secret' | awk '{print $NF}'); f="$A/work/signature.txt"; [ -f "$f" ] || f="$A/signature.txt"; [ -f "$f" ] && [ "$(tr -d ' \n' < "$f" | sed 's/^sha256=//')" = "$exp" ]; }

echo "== Proficient level"
t P P1 "identity set in this repository" c_p1
t P P2 "branch feature/tea with a commit adding tea" c_p2
t P P3 "branch feature/tea pushed to the remote" c_p3
t P P4 "debug.log ignored and not shown by status" c_p4
t P P5 "conflict resolved on branch combined" c_p5
t P P6 "bad commit reverted on main and pushed" c_p6
t P P7 "annotated tag v1.1.0 at the tip of main, pushed" c_p7
t P P8 "deleted branch precious recovered" c_p8
t P P9 "SECURITY.md and CONTRIBUTING.md on main" c_p9
t P P10 "workflow file with permissions, jobs and pinned actions" c_p10
echo "== Mastery level (extra)"
t M M1 "secret removed from all history, local and remote" c_m1
t M M2 "first bad commit found and written down" c_m2
t M M3 "shallow, sparse clone in slim" c_m3
t M M4 "release notes for v1.0.0..v1.1.0" c_m4
t M M5 "webhook signature computed" c_m5
echo "Proficient: $p of 10. Mastery extras: $m of 5."
if [ "$p" -ge 9 ]; then echo "Proficient level reached."; else echo "Proficient level not yet reached (9 of 10 needed)."; fi
if [ "$p" -eq 10 ] && [ "$m" -ge 4 ]; then echo "Mastery level reached."; fi
