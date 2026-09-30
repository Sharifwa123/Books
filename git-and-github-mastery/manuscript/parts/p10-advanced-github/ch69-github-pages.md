---
key: pages
number: 69
tag: Deep
first_read: later
status: draft
requires: [workflows_practice]
ledger: [R328, R329, R330]
---
# Chapter 69 — GitHub Pages [Deep]

**In this chapter**

- what GitHub Pages is, and the two kinds of site
- publishing from a branch, or with a workflow
- custom domains, DNS records and HTTPS
- limits and rules of use
- a local pre-publication check for links, mixed content and paths

> **How to read this chapter.** This is a **Deep** chapter and can be read later. GitHub statements come from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026) and were **not run on a live account**: no site was published, and no domain was configured. The pre-publication check is a local recording (Bash and zsh, Git 2.43.0). Limits and rules change; read the current page before you rely on a number.

**Before you start.** Chapter 56<!--ref:workflows_practice-->. Chapter 58<!--ref:wfadvanced--> built the workflow that deploys a Pages artifact (Project 10); this chapter explains the service itself.

---

## 69.1 What Pages is

GitHub's documentation: "GitHub Pages is a static site hosting service that takes HTML, CSS, and JavaScript files straight from a repository on GitHub, optionally runs the files through a build process, and publishes a website."

**Static** means the files are sent to the browser as they are (Chapter 5<!--ref:internet-->): there is no program running on the server that builds each page for each visitor. A site whose pages depend on a database or a login needs a different kind of hosting (Chapter 72<!--ref:deploy-->).

There are two types of site:

| | User and organization sites | Project sites |
|---|---|---|
| Source files | in a repository named `<owner>.github.io`, where `<owner>` is the account name | in a folder within the repository that holds the project's code |
| Limit | one site per account | one site per repository |
| Default address | `http(s)://<owner>.github.io` | `http(s)://<owner>.github.io/<repositoryname>` |

**Note the last line for project sites**: the address has a repository-name *folder* after the domain. That matters for links, below.

> **Checked against GitHub's documentation (R328).** "What is GitHub Pages?".

---

## 69.2 Two ways to publish

In the repository's Pages settings you choose a **publishing source**:

1. **Deploy from a branch.** You choose a branch and, optionally, a folder (the documentation mentions `/(root)` and `/docs`). The files in it are the site. If you choose `/docs` and later remove that folder, the site "won't build" and you will get a build error.
2. **A custom GitHub Actions workflow.** Chapter 58<!--ref:wfadvanced--> used it: a workflow builds the site and deploys it as an artifact. Some limits do not apply to workflow builds (see 69.4).

The documentation adds that Pages "will always be deployed with a GitHub Actions workflow run, even if you've configured your GitHub Pages site to be built using a different CI tool", and that external CI tools typically "deploy" by committing the build output to a `gh-pages` branch, "and typically include a `.nojekyll` file". A `.nojekyll` file (an empty file with that name) is the way to tell Pages that the files need no build step. You can look at the workflow run for your site in the repository's workflow runs when something fails (Chapter 57<!--ref:wfdebug-->).

Pages also supports building with **Jekyll**, a static site generator, which turns Markdown pages and templates into HTML. It is a subject of its own; this book uses plain HTML.

> **Checked against GitHub's documentation (R329).** "Configuring a publishing source for your GitHub Pages site".

---

## 69.3 A check before you publish

Pages serves what you give it. Two problems appear again and again, and both can be found on your computer before publishing.

**Problem 1: mixed content.** If the site is served over HTTPS but a page still loads an image, style sheet or script through `http://`, the documentation says you are "serving *mixed content*", which "may make your site less secure and cause trouble loading assets". Its advice: change `http://` to `https://`, and "search your site's source files for `http://`".

**Problem 2: absolute paths on a project site.** A link that starts with a slash, such as `/style.css`, means "from the root of the domain". On a project site at `<owner>.github.io/<repositoryname>`, the root of the domain is not your site's folder, so `/style.css` asks for a file that is not there. This follows from how addresses work (Chapter 5<!--ref:internet-->) and from the project-site address above. Relative links (`style.css`) keep working.

The recording makes a two-line mistake, finds it with `git grep`, fixes it, and adds `.nojekyll`:

```text
$ git init -q site && cd site
$ printf '<link rel="stylesheet" href="/style.css">\n<img src="http://example.com/logo.png">\n<a href="about.html">About</a>\n' > index.html
$ printf 'body { margin: 0; }\n' > style.css
$ git add . && git commit -q -m "First version of the site"
$ git grep -n 'http://'
index.html:2:<img src="http://example.com/logo.png">
$ git grep -n -E '(href|src)="/'
index.html:1:<link rel="stylesheet" href="/style.css">
$ printf '<link rel="stylesheet" href="style.css">\n<img src="https://example.com/logo.png">\n<a href="about.html">About</a>\n' > index.html
$ git grep -n 'http://' || echo "no http:// left"
no http:// left
$ git grep -n -E '(href|src)="/' || echo "no root-absolute paths left"
no root-absolute paths left
```

*Recorded in Bash; `ch69-pages/expected-check.bash.txt`.*

The first search found the `http://` image; the second found the root-absolute stylesheet. After the fix, both searches found nothing (`git grep` exits with a failure code when it finds nothing, so the `||` part prints the message). This check finds only what the patterns match; it does not test the site. Chapter 57<!--ref:wfdebug--> and your browser's address bar are the real test, after publishing.

```text
$ : > .nojekyll
$ git add -A && git commit -q -m "Fix mixed content and paths; add .nojekyll"
$ git ls-files
.nojekyll
index.html
style.css
```

*Recorded in Bash; `ch69-pages/expected-check.bash.txt`.*

---

## 69.4 Limits and rules of use

Read the current page ("GitHub Pages limits"). At the time of the commit used for this book, the documentation said:

- Pages "is not intended for or allowed to be used as a free web-hosting service to run your online business, e-commerce site, or any other website that is primarily directed at either facilitating commercial transactions or providing commercial software as a service (SaaS)".
- Use is subject to the Terms of Service.
- Usage limits are listed: one user or organization site per account, a recommended size for source repositories, a maximum size for published sites, a timeout for deployments, "soft" limits on bandwidth and on builds per hour (the build limit "does not apply if you build and publish your site with a custom GitHub Actions workflow"), and rate limiting, with HTTP status `429`. **The numbers are not repeated here because they change.**
- **Do not put sensitive data on a Pages site.** The documentation repeats this warning in several places. The documentation describes **privately published** sites, which only people with read access to the repository can open, as an option for organizations on Enterprise Cloud (Chapter 68<!--ref:orgs-->). Without that option, **treat any published site as public, whatever the visibility of the repository** (Chapter 39<!--ref:ghrepo-->).
- A "copy of an existing website as a learning exercise" is allowed only under conditions: you write the code yourself, the site collects no user data, and it carries "a prominent disclaimer" that it is unaffiliated and educational.

> **Checked against GitHub's documentation (R330).** "GitHub Pages limits" and "Securing your GitHub Pages site with HTTPS" (visibility and sensitive-data warnings).

---

## 69.5 Custom domains and HTTPS

By default your site lives at `github.io`. You can use your own domain. The documentation lists the types it supports: a `www` subdomain (`www.example.com`), a custom subdomain (`blog.example.com`) and an **apex domain** (`example.com`, with no subdomain). It recommends "always using a `www` subdomain, even if you also use an apex domain", and says `www` subdomains "are the most stable type of custom domain because `www` subdomains are not affected by changes to the IP addresses of GitHub's servers".

At your **DNS provider** (Chapter 5<!--ref:internet--> introduced DNS), you make records:

| Domain type | Record type the documentation names |
|---|---|
| Subdomain (such as `www`) | `CNAME` |
| Apex domain | `A`, `ALIAS` or `ANAME` |

By default, a custom domain set for a user or organization site is used for all project sites of the same account (the documentation's example: `www.octocat.com/octo-project`). **The exact records and values are on the managing-a-custom-domain page and change; copy them from there, not from a book.** The documentation also describes **verifying** a domain, to stop others from taking it over. Do that.

**HTTPS.** "All GitHub Pages sites, including sites that are correctly configured with a custom domain, support HTTPS and HTTPS enforcement." Sites on `github.io` created after 15 June 2016 are served over HTTPS automatically. Admins of the repository can select **Enforce HTTPS**. For a custom domain, GitHub checks your DNS settings and then requests a certificate from Let's Encrypt; this "may take some time", and the documentation gives a troubleshooting step if the certificate is not created. The whole domain name must be shorter than 64 characters for a certificate to be created.

---

## 69.6 A publishing checklist

1. Are the files static, and is there nothing secret in them (or in the history that a private repository hides)?
2. Do the local checks pass: no `http://` references, no root-absolute paths on a project site?
3. Which publishing source: branch or workflow? Is `.nojekyll` needed?
4. Are you within the rules of use?
5. If you use a custom domain: DNS records copied from the current page, domain verified, HTTPS enforced.
6. Open the published address in a private window and click every link.

---

## Checkpoint

## What You Learned

- Pages publishes static files from a repository; user/organization sites and project sites differ in address.
- You publish from a branch (and folder) or with a workflow.
- Mixed content and root-absolute paths are the common faults; search for them locally.
- Rules of use forbid running a commercial business on Pages; limits change, so read them.
- Custom domains use CNAME (subdomains) or A/ALIAS/ANAME (apex) records; HTTPS is supported and can be enforced.

## New Vocabulary

**Static site**, **GitHub Pages**, **apex domain**, **mixed content** (see the glossary).

## Commands Learned

`git grep -n -E`, and `: > .nojekyll` to create an empty file.

## Common Mistakes

1. **Using `/style.css` on a project site.**
2. **Loading assets over `http://` from an HTTPS site.**
3. **Publishing secrets or personal data.**
4. **Trusting DNS values from memory.**
5. **Assuming a private repository makes the site private.**

## Practice

Do the exercises in [`exercises/ch69-exercises.md`](../../../exercises/ch69-exercises.md).

## Self-Test

1. What is a static site?
2. What is the address of a project site?
3. Which two publishing sources exist?
4. Why does `/style.css` fail on a project site?
5. Which DNS record types does the documentation name for an apex domain?

## Before Moving On

You are ready for Chapter 70<!--ref:codespaces--> if you can:

- [ ] explain user sites versus project sites
- [ ] find mixed content and absolute paths with `git grep`
- [ ] list the steps before publishing

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The local checks with `git grep` and the creation of `.nojekyll` | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R329, R330 (local side) |
| Site types, publishing sources, limits, rules of use, custom domains, HTTPS | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account** | R328-R330 |
| Why a root-absolute path fails on a project site | Reasoning from URL rules and the documented project-site address; not observed on GitHub | none |

## Where this leads

Chapter 70<!--ref:codespaces--> moves the development environment itself into the cloud.
