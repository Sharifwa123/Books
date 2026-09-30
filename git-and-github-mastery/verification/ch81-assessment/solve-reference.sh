#!/bin/sh
# AUTHOR-SIDE reference solution for the assessment; not part of the learner's companion files.
set -e
A="${ASSESS_DIR:-$HOME/assessment}"
cd "$A/work"
git config --local user.name "Ada Learner"
git config --local user.email "ada@example.org"
git switch -q -c feature/tea
printf -- '- Tea: 1.50\n' >> menu.md
git commit -q -am "Add tea"
git push -q -u origin feature/tea
git switch -q main
printf '*.log\n' > .gitignore
git add .gitignore
git commit -q -m "Ignore log files"
git fetch -q
git switch -q -c combined origin/edit-a
git -c advice.mergeConflict=false merge origin/edit-b >/dev/null 2>&1 || true
printf '# Bakery\n\nOpening hours: 8 to 6.\n' > README.md
git add README.md
git commit -q --no-edit
git switch -q main
sha=$(git reflog --format='%H %gs' | grep 'commit: Precious work' | awk '{print $1}')
git branch precious "$sha"
git revert --no-edit "$(git log --format=%H --grep='Set prices to zero' -1 main)" >/dev/null
printf '# Security policy\n\nReport vulnerabilities privately to security@example.org.\n' > SECURITY.md
printf '# Contributing\n\nOpen an issue first.\n' > CONTRIBUTING.md
mkdir -p .github/workflows
printf 'name: ci\non: [pull_request]\npermissions:\n  contents: read\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803\n      - run: sh check.sh\n' > .github/workflows/ci.yml
git add SECURITY.md CONTRIBUTING.md .github
git commit -q -m "Add community files and a workflow"
git push -q origin main
git tag -a v1.1.0 -m "Version 1.1.0"
git push -q origin v1.1.0
git push -q origin combined precious
git bisect start HEAD "$(git rev-list --max-parents=0 HEAD | tail -1)" >/dev/null
printf 'grep -qx ok state.txt\n' > "$A/test.sh"
git bisect run sh "$A/test.sh" >/dev/null 2>&1 || true
git log -1 --format=%s refs/bisect/bad > "$A/work/bisect-answer.txt"
git bisect reset >/dev/null 2>&1
git log --format='- %s' v1.0.0..v1.1.0 > RELEASE_NOTES.md
printf '%s' 'Order 42 shipped' | openssl dgst -sha256 -hmac 'bakery-test-secret' | awk '{print $NF}' > signature.txt
git clone -q --depth 1 --no-checkout "file://$A/remote.git" "$A/slim"
git -C "$A/slim" sparse-checkout set docs
git -C "$A/slim" checkout -q main
git filter-repo --sensitive-data-removal --invert-paths --path secrets.env --force >/dev/null 2>&1
git push -q --force --mirror origin
