---
key: platformextras
number: 75
tag: Deep
first_read: later
status: draft
requires: [orgs]
ledger: [R344, R345, R346, R347]
---
# Chapter 75 — Other Platform Features [Deep]

**In this chapter**

- GitHub Sponsors and the sponsor button (`FUNDING.yml`)
- GitHub Marketplace
- AI assistance in the workflow, described neutrally
- custom properties and governance
- how to keep up with a platform that keeps changing

> **How to read this chapter.** This is a **Deep** chapter and can be read later. It is a tour of features you may meet, not a guide to using them. Statements about GitHub come from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026) and **were not run on a live account**; no sponsorship, listing, subscription or setting was created. **Prices, eligibility, supported regions and availability by plan change and are not stated.** The one recording is local: it checks a `FUNDING.yml` file written from the documentation's example. This book takes **no position** on AI tools, sponsorship or any product: it says what the documentation says, and what you must decide for yourself.

**Before you start.** Chapter 68<!--ref:orgs-->.

---

## 75.1 GitHub Sponsors

GitHub's documentation says that anyone can sponsor open-source maintainers on GitHub: "Anyone in any region can sponsor eligible maintainers, but you must reside in a supported region to receive funds." When you become a sponsored developer or sponsored organization, "additional terms" apply, and a matching programme exists with its own conditions, for example that "payments to sponsored organizations and payments from organizations are not eligible". **The details of eligibility, regions, fees and matching are on GitHub's pages and change**; read them before you rely on Sponsors for income or plan a budget around it.

**The sponsor button.** A repository can show a **Sponsor** button. The documentation: "You can configure your sponsor button by editing a `FUNDING.yml` file in your repository's `.github` folder, on the default branch." Rules stated there: "one username, package name, or project name per external funding platform and up to four custom URLs", and "one organization and up to four sponsored developers" on GitHub Sponsors. Each platform goes on its own line. Anyone with admin permissions can enable the button in the repository settings, and you can also set a default for your organization or account (Chapter 64<!--ref:oss--> on default community health files). **Funding links are for supporting open-source projects**: the documentation says they are not supported for other purposes such as advertising or for political, community or charity groups.

The recording writes the documentation's example file and reads it with PyYAML (Chapter 53<!--ref:yaml-->), counting entries per key:

```text
$ mkdir -p .github
$ printf 'github: [octocat, surftocat]\npatreon: octocat\ntidelift: npm/octo-package\ncustom: ["https://www.paypal.me/octocat", octocat.com]\n' > .github/FUNDING.yml
$ cat .github/FUNDING.yml
github: [octocat, surftocat]
patreon: octocat
tidelift: npm/octo-package
custom: ["https://www.paypal.me/octocat", octocat.com]
$ python3 fund.py .github/FUNDING.yml
github 2
patreon 1
tidelift 1
custom 2
problems: none
```

*Recorded in Bash; `ch75-platformextras/expected-funding.bash.txt`.*

`github` has two entries, `custom` has two, and the other keys one each, so the file respects the stated limits. The script does **not** contact GitHub and does not know which platforms GitHub supports: it only counts.

Now two variations:

```text
$ printf 'custom: [https://www.paypal.me/octocat, octocat.com]\n' > unquoted.yml
$ python3 fund.py unquoted.yml
custom 2
problems: none
$ printf 'custom: [a.example, b.example, c.example, d.example, e.example]\n' > toomany.yml
$ python3 fund.py toomany.yml
custom 5
problems: ['more than four custom URLs']
```

*Recorded in Bash; `ch75-platformextras/expected-funding.bash.txt`.*

- The unquoted URL was **accepted** by PyYAML 6.0.1, although the documentation notes that "If a custom URL in an array includes `:`, you must wrap the URL in quotes". The documentation's rule is stricter than this parser. **Follow the documentation**: the parser that matters is GitHub's, and a rule that one tool tolerates can break in another. (Chapter 53<!--ref:yaml--> showed PyYAML reading `no` as false, another case where one tool's reading is not the whole story.)
- The five custom URLs were flagged by the script, which mirrors the documented limit of four.

> **Checked against GitHub's documentation (R344) and locally tested.** "About GitHub Sponsors" and "Displaying a sponsor button in your repository". The list of supported funding platforms in the documentation is not reproduced here.

---

## 75.2 GitHub Marketplace

The **Marketplace** is a directory of tools that extend GitHub's workflows. The documentation: it "connects you to developers who want to extend and improve their GitHub workflows. You can list free and paid tools for developers to use in GitHub." It has two kinds of listing: **GitHub Actions** (Chapter 54<!--ref:actions-->) and **apps** (Chapter 74<!--ref:api-->).

Points from the documentation about *publishing*: "Anyone can share their apps with other users for free on GitHub Marketplace but only apps owned by organizations can sell their app." Paid plans need "publisher verification" of the organization and a financial onboarding process. Free listings need to meet the general requirements for listing.

For a **user** of the Marketplace, the rules of Chapter 60<!--ref:wfsec--> and Chapter 74<!--ref:api--> apply: an entry in the Marketplace is not a guarantee of safety. Before you install an app, look at the permissions it asks for (least privilege), who publishes it, and whether the publisher is verified; before you use an action, pin it to a commit and read its source.

> **Checked against GitHub's documentation (R345).** "About GitHub Marketplace for apps".

---

## 75.3 AI assistance in the development workflow

GitHub documents an AI assistant, Copilot, as part of the platform. **This section describes what the documentation says and gives no recommendation.** The documentation describes it as "an AI assistant that helps you write, understand, and ship software" that "suggests code as you type, answers questions about a codebase, reviews your changes, and works on tasks you assign it", working "within the development workflow you already use": your code, issues and pull requests, and repository automations. It groups the capabilities into categories, among them **assistive** (it suggests and you "review and apply each suggestion") and **agentic** (you describe a goal and it "can work through multiple steps", with the statement "You remain responsible for reviewing and approving"), plus **customisations** such as instructions and reusable prompts.

What does not change, whatever tool produced a change:

- **A person is accountable** for what is merged. Review (Chapter 46<!--ref:review-->) and branch protection (Chapter 50<!--ref:protect-->) apply to every pull request, including one that a tool opened.
- **Licences and provenance still matter** (Chapter 65<!--ref:licences-->): do not submit what you do not have the right to submit, and do not submit what you cannot explain (Chapter 64<!--ref:oss-->).
- **Secrets stay out of prompts, code and logs** (Chapter 33<!--ref:gitsec-->).
- **Least privilege** applies to any tool's access to your repositories (Chapter 63<!--ref:secpractice-->).
- **Tests and checks** (Chapter 52<!--ref:cicd-->) are the same for human and machine changes.

Plans, features, limits and policies for these tools differ by account and change often; read the current documentation and your organization's policy.

> **Checked against GitHub's documentation (R346).** "About GitHub Copilot" (first sections only). The claims about Copilot were not checked by using it.

---

## 75.4 Custom properties and governance

In an organization with many repositories, you need to organise and control them. **Custom properties** are one tool. The documentation: "With custom properties, you can add metadata to repositories in your organization. You can use those properties to target repositories with rulesets." Organization owners can define the properties (and, where the plan supports it, people with a specific permission). Other points: the visibility of a property matches the repository's visibility, so on a public repository anyone can see its custom properties; a REST API endpoint exists for managing them; and properties can be synced with an external system.

A small example of the idea: define a property such as "team" or "criticality", set it on each repository, then write a ruleset (Chapter 50<!--ref:protect-->) that applies to all repositories with `criticality = high`. That gives **one rule for many repositories**.

**Governance** means the decisions and rules by which a group runs its projects. On GitHub they are made of parts you have already met:

| Governance question | Where it lives |
|---|---|
| Who may do what? | repository roles and base permissions (Chapter 68<!--ref:orgs-->) |
| Which changes may merge, and after what? | branch protection and rulesets (Chapter 50<!--ref:protect-->) |
| Who reviews which files? | code owners (Chapter 50<!--ref:protect-->) |
| How do we behave? | code of conduct (Chapter 64<!--ref:oss-->) |
| How do we contribute and report problems? | `CONTRIBUTING.md`, `SECURITY.md`, templates (Chapters 64<!--ref:oss-->, 62<!--ref:ghsec-->) |
| Which licence? | `LICENSE` (Chapter 65<!--ref:licences-->) |
| What is scanned and blocked? | security features (Chapter 62<!--ref:ghsec-->) |
| Who can be reached in an emergency? | ownership with more than one owner (Chapter 68<!--ref:orgs-->) |

Write the rules down in the repository, so that they are versioned and reviewed like code.

> **Checked against GitHub's documentation (R347).** "Managing custom properties for repositories in your organization". Rulesets that target properties were not examined in detail.

---

## 75.5 Keeping up with a platform that changes

This whole Part depends on a platform that changes faster than a book. Habits that help:

1. **Read the source of truth**: GitHub's documentation, with the version for your plan selected (Chapter 35<!--ref:readdocs-->).
2. **Read the changelog** for features you depend on.
3. **Test on a repository you can afford to break.**
4. **Keep notes** of what you observed and when, as this book does in its ledger: a fact without a date is a rumour.
5. **Prefer principles** (least privilege, verify before trusting, keep secrets out, write it down) to memorised screens.

---

## Checkpoint

## What You Learned

- Sponsors: anyone can sponsor; receiving funds depends on region and terms; the sponsor button is configured with `.github/FUNDING.yml`, with documented limits.
- A tool can accept what documentation forbids (unquoted URL): follow the documentation.
- The Marketplace lists actions and apps; only organizations can sell apps; a listing is not a safety guarantee.
- AI tools do not change accountability, licensing, secrets or review rules.
- Custom properties add metadata to repositories and can target rulesets; governance is written down in the repository.

## New Vocabulary

**GitHub Sponsors**, **custom property**, **governance** (see the glossary).

## Commands Learned

No new commands.

## Common Mistakes

1. **Relying on Sponsors income without reading the current terms.**
2. **Trusting a Marketplace listing without checking permissions.**
3. **Merging a machine-made change without review.**
4. **Assuming a parser's tolerance equals the platform's.**
5. **Keeping governance in people's heads.**

## Practice

Do the exercises in [`exercises/ch75-exercises.md`](../../../exercises/ch75-exercises.md).

## Self-Test

1. Where does `FUNDING.yml` live?
2. How many custom URLs does the documentation allow?
3. Who can sell an app on the Marketplace?
4. Does an AI tool change who is accountable for a merged change?
5. What can custom properties be used for?

## Before Moving On

You are ready for Part XI if you can:

- [ ] explain what each feature in this chapter is for, without assuming it is right for you
- [ ] list where a project's governance rules live

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Counting entries in `FUNDING.yml`; PyYAML accepts an unquoted URL | Locally tested: Bash 5.2 and zsh 5.9, Python 3, PyYAML 6.0.1; CI | R344 (local side) |
| Sponsors, Marketplace, AI assistant description, custom properties | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account**; eligibility, prices and plans not stated | R344-R347 |
| Governance table | The author's summary of earlier chapters | none |

## Where this leads

Part XI, "Master Projects", puts everything together: Chapter 76<!--ref:scenarios--> has twelve professional scenarios, and Chapter 77<!--ref:capstone--> is the capstone.
