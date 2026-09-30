# Appendix I — Open-Source Project Checklist

For someone who is about to publish a project for others to use. Chapter 67<!--ref:ossproject--> builds one; Chapters 64<!--ref:oss-->, 65<!--ref:licences--> and 66<!--ref:releases--> explain the parts. **This book gives no legal advice; the licence is your decision.**

## I.1 Before you publish

- [ ] I own the work, or have the right to publish it (employer, contributors, copied code) (Chapter 65<!--ref:licences-->).
- [ ] I have removed secrets and personal data, including from history (Chapters 33<!--ref:gitsec--> and 79<!--ref:playbooks-->).
- [ ] I decided what others may do with the code, and chose a licence from an official text, with my own name and the correct year.
- [ ] The licences of everything I include are compatible with mine (a question for a qualified person if unsure).
- [ ] I read the rules of any platform I publish on (for example rules of use for Pages, Chapter 69<!--ref:pages-->).

## I.2 What visitors need

- [ ] What it is, how to install and use it, one true example, how to run the tests.
- [ ] Status: "early development" or "stable", and the versioning scheme.
- [ ] How to report a bug and how to ask for help.
- [ ] How to contribute; whether sign-off is required (Chapter 64<!--ref:oss-->).
- [ ] How to report a security problem privately (Chapter 62<!--ref:ghsec-->).

## I.3 Health of the project

- [ ] Tests exist and run on each pull request.
- [ ] Releases have notes, checksums and tags; old versions stay available (Chapter 66<!--ref:releases-->).
- [ ] I have said what I will not do, and how much time I have.
- [ ] I can hand over or close the project honestly if I can no longer maintain it (Chapter 67<!--ref:ossproject-->).

## I.4 Contributing to someone else's project

- [ ] I read the README, `CONTRIBUTING.md`, the code of conduct and the licence first.
- [ ] I asked before starting anything large.
- [ ] My change is small, tested and explained; one purpose per pull request.
- [ ] I did not include anything I have no right to submit, and no secrets.
- [ ] I respond politely to review, and accept the maintainers' decision.
