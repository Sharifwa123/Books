# 05 — Practical Project Plan, Scenarios and Assessment (v2, generated)

Chapter numbers come from `tools/toc_data.py`. Every project has: goal, prerequisites, steps, expected result, checkpoint questions and a reference solution (in `solutions/`). **An exercise or project may not be published until its commands have been run and its expected results recorded** (see `exercises/registry.csv`).

## The twelve projects

| # | Project | After | Realistic content | Skills |
|---|---|---|---|---|
| 1 | Track a simple folder | Ch 16 Your First Repository | personal study-notes folder | init, add, commit, status, log |
| 2 | Build and version a website | Ch 19 Writing Good Commits | 3-page small-business site (HTML/CSS provided; no coding needed) | commits, diff, .gitignore, good messages |
| 3 | Publish to GitHub | Ch 39 Your First GitHub Repository | the website | account, remote, push, clone |
| 4 | Work with branches | Ch 21 Merging | 'contact page' and 'pricing' branches | branch, merge, fast-forward vs three-way |
| 5 | Collaborate with another person | Ch 49 Collaboration and Access | two-person site update (partner, or two clones on one machine if solo) | remotes, pull/push, forks |
| 6 | Resolve a merge conflict | Ch 22 Merge Conflicts | both people edit the same heading | conflict markers, abort/continue |
| 7 | Professional GitHub repository | Ch 42 Professional Repositories and READMEs | README, licence, topics, templates, CONTRIBUTING | repository quality |
| 8 | Create a pull request | Ch 45 Pull Requests | proposed change to the Project 7 repository | PR lifecycle, review |
| 9 | Automated tests with Actions | Ch 56 Practical Workflows | tiny library with provided tests | workflow, jobs, matrix, cache |
| 10 | Deploy with Actions | Ch 58 Reusable Workflows, Environments and Deployments | website to GitHub Pages | deploy workflow, environment |
| 11 | Create an open-source project | Ch 67 Creating an Open-Source Project | small documented library | licence, releases, community files |
| 12 | Full professional workflow | Ch 77 Capstone Project | capstone | everything |

## Capstone (Ch 77, 23 steps)
Create project → init Git → .gitignore → meaningful commits → branches → features → merges → resolve conflict → create GitHub repo → push → Issues → Project → PR → code review → Actions → automated tests → security controls (only features verified for the learner's account type and repository visibility) → release → documentation → prepare for another contributor → simulate production problem → recover from a Git mistake → final professional repository. Reference implementation in `solutions/capstone-reference/`.

## Twelve scenarios (Ch 76)
1 Student's first project · 2 Solo developer builds a website · 3 Two developers collaborate · 4 Team mobile-app development · 5 Company manages production software · 6 Open-source contributor submits a change · 7 Security researcher reports a vulnerability · 8 Company deploys automatically from GitHub · 9 Developer accidentally deletes work · 10 Secret accidentally pushed (fake token only) · 11 Team hits a merge conflict · 12 Project needs a release.

## Exercise levels (every chapter)
L1 Guided · L2 Partially guided · L3 Independent · L4 Professional scenario · L5 Troubleshooting. Solutions separate.

## Final Mastery Assessment (Ch 81)
Practical, not multiple-choice. Six practical tasks + one troubleshooting lab + one written design memo, scored on a rubric (Not yet / Developing / Proficient / Expert) with observable criteria. Areas: concepts, commands, troubleshooting, branches, collaboration, GitHub repository management, pull requests, code review, Actions, security, releases, deployment, open-source contribution. Instructor key and rubric are separate.

## Safety rules for exercises
- Fake secrets only (e.g. `FAKE_TOKEN_DO_NOT_USE_0000`); never a real credential.
- All exercises run in the sandbox folder; destructive commands only on sandbox repositories.
- Exercises that need a GitHub account state that clearly, and offer a local bare-repository alternative wherever the concept allows.
