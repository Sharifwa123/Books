#!/bin/sh
# Creates the sandbox for the final assessment (Chapter 81).
# Usage: sh setup.sh        (default folder: $HOME/assessment; set ASSESS_DIR to change it)
set -e
A="${ASSESS_DIR:-$HOME/assessment}"
rm -rf "$A"
mkdir -p "$A"
cd "$A"
git init -q --bare remote.git
git -C remote.git symbolic-ref HEAD refs/heads/main
git clone -q remote.git seed 2>/dev/null
cd seed
git config user.name "Setup"
git config user.email "setup@example.org"
printf '# Sunrise Bakery menu\n\n- White loaf: 2.50\n- Rolls: 3.00\n' > menu.md
printf '# Bakery\n\nOpening hours: to be decided.\n' > README.md
mkdir docs src
printf 'Guide\n' > docs/guide.md
printf 'app\n' > src/app.txt
git add -A
git commit -q -m "Add the menu"
git tag -a v1.0.0 -m "Version 1.0.0"
printf 'API_KEY=not-a-real-key\n' > secrets.env
git add secrets.env
git commit -q -m "Add settings"
printf 'ok\n' > state.txt
git add state.txt
git commit -q -m "Add state"
for i in 1 2 3 4; do printf "%s\n" "$i" >> notes.txt; git add notes.txt; git commit -q -m "Note $i"; done
printf 'broken\n' > state.txt
git commit -q -am "Change state"
for i in 5 6 7; do printf "%s\n" "$i" >> notes.txt; git add notes.txt; git commit -q -m "Note $i"; done
sed -i 's/2.50/0.00/; s/3.00/0.00/' menu.md
git commit -q -am "Set prices to zero"
git push -q origin main
git push -q origin v1.0.0
git switch -q -c edit-a
printf '# Bakery\n\nOpening hours: 8 to 5.\n' > README.md
git commit -q -am "Opening hours: 8 to 5"
git push -q origin edit-a
git switch -q main
git switch -q -c edit-b
printf '# Bakery\n\nOpening hours: 9 to 6.\n' > README.md
git commit -q -am "Opening hours: 9 to 6"
git push -q origin edit-b
cd ..
rm -rf seed
git clone -q remote.git work 2>/dev/null
cd work
git config user.name "Setup"
git config user.email "setup@example.org"
git switch -q -c precious
printf 'precious\n' > precious.txt
git add precious.txt
git commit -q -m "Precious work"
git switch -q main
git branch -D precious > /dev/null
git config --unset user.name
git config --unset user.email
printf 'debug\n' > debug.log
echo "Assessment sandbox ready in $A/work"
