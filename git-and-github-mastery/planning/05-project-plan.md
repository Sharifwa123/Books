# 05 — Practical Project Plan, Scenarios and Assessment

All projects use the running example progression in 02. Every project has: goal, prerequisites, steps, expected result, checkpoint questions, and a reference solution (separate section).

## The twelve projects
| # | Project | After chapter | Realistic content | Skills |
|---|---------|--------------|-------------------|--------|
| 1 | Track a simple folder | 13 | personal study-notes folder | init, add, commit, status, log |
| 2 | Build and version a website | 16 | 3-page small-business site (HTML/CSS given; no coding knowledge needed) | commits, diff, `.gitignore`, good messages |
| 3 | Publish to GitHub | 35 | the website | account, remote, push, clone |
| 4 | Work with branches | 18 | add "contact page" and "pricing" branches | branch, merge, FF vs 3-way |
| 5 | Collaborate with another person | 43 | two-person site update (partner, or two clones on one machine if solo) | remotes, pull/push, forks |
| 6 | Resolve a merge conflict | 19 | both edits to the same heading | conflict markers, abort/continue |
| 7 | Professional repository | 37 | README, licence, topics, templates, CONTRIBUTING | repository quality |
| 8 | Create a pull request | 39 | change proposed to project 7 repo | PR lifecycle, review |
| 9 | Automated tests with Actions | 49 | tiny library with tests provided | workflow, jobs, matrix, cache |
| 10 | Deploy with Actions | 50 | site to GitHub Pages | deploy workflow, environment |
| 11 | Create an open-source project | 57 | small documented library | licence, releases, community files |
| 12 | Full professional workflow | 68 | capstone | everything |

## Capstone (23 steps)
Create project → init Git → `.gitignore` → meaningful commits → branches → features → merges → resolve conflict → create GitHub repo → push → Issues → Project → PR → code review → Actions → automated tests → security controls (Dependabot, secret scanning/push protection as available, least-privilege permissions, rules) → release → documentation → prepare for another contributor → simulate production problem → recover from a Git mistake → final professional repository. Reference implementation published separately in `companion/capstone-reference/`.

## Twelve scenarios (each step-by-step)
1 Student's first project · 2 Solo developer builds a website · 3 Two developers collaborate · 4 Team mobile-app development · 5 Company manages production software · 6 Open-source contributor submits a change · 7 Security researcher reports a vulnerability · 8 Company deploys automatically from GitHub · 9 Developer accidentally deletes work · 10 Secret accidentally pushed (fake token in exercises) · 11 Team hits a merge conflict · 12 Project needs a release.

## Exercise levels (used in every chapter)
L1 Guided · L2 Partially guided · L3 Independent · L4 Professional scenario · L5 Troubleshooting. Solutions in a separate companion section.

## Final Mastery Assessment (practical, not multiple-choice)
Learner delivers a repository and short written answers. Areas: concepts, command knowledge, troubleshooting, branches, collaboration, GitHub repo management, PRs, code review, Actions, security, releases, deployment, open-source contribution.

Format: 6 practical tasks + 1 troubleshooting lab + 1 written design memo. Each task scored on a rubric (Not yet / Developing / Proficient / Expert) with observable criteria (e.g. "recovers deleted branch using reflog without data loss"). Instructor answer key and rubric in a separate file, not bundled in the learner edition.

## Companion material (planned)
`companion/` : sandbox setup scripts, sample project files, broken-repo labs for troubleshooting exercises, capstone reference, solutions, assessment key.
