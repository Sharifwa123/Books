# Chapter 70 exercises — Codespaces and Dev Containers

Attempt each exercise before you open `solutions/ch70-solutions.md`. Exercises 2.1 and 2.2 use your terminal; nothing needs a GitHub account or Docker.

## Level 1 — Guided

**1.1 Definition.** In two sentences, explain what a codespace is and what configuration as code means here.

**1.2 Where?** Where must `devcontainer.json` be, and where do you put a second configuration?

## Level 2 — Partially guided

**2.1 Lay it out.** In a sandbox repository, create `.devcontainer/devcontainer.json` with `name` and `image` keys, add it and commit it. Show `git ls-files`.

**2.2 Comments.** Add a `//` comment to the file and check it with `python3 -m json.tool`. What happens? What does the chapter say about it?

## Level 3 — Independent

**3.1 Customisation or personalisation?** Sort into the file or your own settings: a linter everyone must use, your favourite colour theme, the language version, your shell aliases.

**3.2 Cost note.** Write a short note for your team that says how they should stop wasting codespace quota, using only what the chapter says.

## Level 4 — Professional scenario

**4.1 Onboarding.** Your open-source project needs new contributors to start in minutes. Write the proposal: what goes in `.devcontainer`, what you would test first, and what the security cautions are.

## Level 5 — Troubleshooting

**5.1** You deleted a codespace and lost an afternoon's work. What did the chapter say you should have done?

**5.2** A colleague made a forwarded port public "just for a minute". List the risks and what resets it.
