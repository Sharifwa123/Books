---
key: api
number: 74
tag: Deep
first_read: later
status: draft
requires: [ghauth, ghcli]
ledger: [R341, R342, R343]
---
# Chapter 74 — APIs, Webhooks and Apps [Deep]

**In this chapter**

- what an API is, and GitHub's REST and GraphQL APIs
- requests, pagination, versions and rate limits
- webhooks: GitHub calling you, and verifying the call is genuine
- GitHub Apps versus OAuth apps
- tokens for scripts

> **How to read this chapter.** This is a **Deep** chapter and can be read later. Two kinds of evidence are used, and the text says which. **Recorded and re-run in CI:** the verification of a webhook signature (using the test values published in GitHub's documentation) and the reading of a pagination header, both with no network and no account. **Observed live, once:** a few requests to GitHub's API made on 30 September 2026 from the authoring environment, through a proxy that authenticates the requests on the session's behalf, so **the rate-limit numbers seen there are not typical and are not quoted**; these observations are not re-run in CI. **Everything else** comes from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026) and was not run.

**Before you start.** Chapter 38<!--ref:ghauth--> (tokens) and Chapter 73<!--ref:ghcli-->.

---

## 74.1 What an API is

An **API** (application programming interface) is a way for one program to ask another to do something. GitHub's web pages are for people; its **API** is for programs. GitHub's documentation: "You can use GitHub's API to build scripts and applications that automate processes, integrate with GitHub, and extend GitHub. For example, you could use the API to triage issues, build an analytics dashboard, or manage releases."

GitHub offers **two APIs**: "a REST API and a GraphQL API. You can interact with both APIs using GitHub CLI, curl, the official Octokit libraries, and third party libraries. Occasionally, a feature may be supported on one API but not the other."

- **REST** is organised by **resources** with an address for each; you ask with an HTTP request (Chapter 5<!--ref:internet-->): for example, a request to get the issues of a repository. Each endpoint returns a fixed structure. The documentation says that REST "returns more data than you requested and returns it in a pre-determined structure".
- **GraphQL** is one address to which you send a **query** naming exactly the fields you want. "The GraphQL API returns exactly the data that you request" and "you can also accomplish the equivalent of multiple REST API request in a single GraphQL request". Node IDs let you move between the two.

"You should use the API that best aligns with your needs and that you are most comfortable using. You don't need to exclusively use one API over the other." This chapter uses REST for its examples.

> **Checked against GitHub's documentation (R341).** "About the REST API" and "Comparing GitHub's REST API and GraphQL API".

---

## 74.2 A REST request, as observed

A request has a method (`GET` reads), an address, and headers; the answer has a status code, headers and a body, normally JSON (Chapter 5<!--ref:internet--> on status codes). The documentation's example asks for a repository's issues:

```shell
curl --include --request GET \
  --url "https://api.github.com/repos/OWNER/REPO/issues" \
  --header "Accept: application/vnd.github+json"
```

`--include` shows the response headers, which matter, as the next sections show. **I made an equivalent read-only request for the commits of this book's repository, asking for one item per page** (the API was reached through the session's proxy). Observed:

- Status **200** and a JSON list with one item; each item had the keys `sha`, `commit`, `author`, `committer`, `parents`, `url`, `html_url` and others.
- A **`Link`** header holding a `rel="next"` and a `rel="last"` address, because there were more pages than the one that was returned (section 74.3).
- **`X-GitHub-Api-Version-Selected: 2022-11-28`** although I sent no version (section 74.4).
- Headers whose names start with `X-RateLimit-` (section 74.5).
- A `Cache-Control` and an `ETag`, which a client can use to avoid re-downloading unchanged data.

Anything that could identify the session (token expiry, client identifiers) was in the headers too and is not reproduced. **Never publish raw headers or logs without reading them first**: they can contain identifiers, and in some tools, credentials (Chapter 63<!--ref:secpractice-->).

---

## 74.3 Pagination

"When a response from the REST API would include many results, GitHub will paginate the results and return a subset." The documentation's example: a request for a repository's issues "will only return 30 issues ... even though the repository includes over 1600 open issues". You ask for more with the **`Link` header**, which gives the URLs of the previous, next, first and last pages, and you can choose the page size with **`per_page`** on endpoints that support it. "If the endpoint does not support pagination, or if all results fit on a single page, the `link` header will be omitted."

The recording parses the documentation's example header with a short script (`link.py`) and prints each relation:

```text
$ printf '%s\n' '<https://api.github.com/repositories/1300192/issues?page=2>; rel="prev", <https://api.github.com/repositories/1300192/issues?page=4>; rel="next", <https://api.github.com/repositories/1300192/issues?page=515>; rel="last", <https://api.github.com/repositories/1300192/issues?page=1>; rel="first"' | python3 link.py
first -> https://api.github.com/repositories/1300192/issues?page=1
prev -> https://api.github.com/repositories/1300192/issues?page=2
next -> https://api.github.com/repositories/1300192/issues?page=4
last -> https://api.github.com/repositories/1300192/issues?page=515
$ printf '%s\n' '<https://api.github.com/repositories/1300192/issues?page=2>; rel="next"' | python3 link.py
first -> (none)
prev -> (none)
next -> https://api.github.com/repositories/1300192/issues?page=2
last -> (none)
```

*Recorded in Bash; `ch74-api/expected-verify.bash.txt`.*

The second call shows an answer with only a `next` relation: the rest are `(none)`. A script that follows `next` until it is absent has fetched everything, with no need to count pages. **The script reads a header that is pasted in; it makes no request.**

> **Checked against GitHub's documentation (R342).** "Using pagination in the REST API". The live observation in section 74.2 confirmed the header's presence and the `next`/`last` relations for one endpoint.

---

## 74.4 Versions and rate limits

**API versions.** The documentation says to "use the `X-GitHub-Api-Version` header to specify an API version", that requests without it use a default version, and that versions are supported for a period after a newer one is released; asking for an unsupported version "will receive a `410 Gone` response". **Observed:** with no header, the answer carried `X-GitHub-Api-Version-Selected: 2022-11-28`; with `X-GitHub-Api-Version: 2022-11-28` the same; with `X-GitHub-Api-Version: 2019-01-01`, a version that (as far as this book knows) never existed, the answer was **400 Bad Request**, not 410. The 410 case (a version that *was* supported) was not observed. Pin a version in your scripts so that a change of default does not break them silently.

**Rate limits.** "GitHub limits the number of REST API requests that you can make within a specific amount of time. This limit helps prevent abuse and denial-of-service attacks." Some endpoints, such as search, are stricter, and GraphQL has its own limit. Limits depend on how you authenticate; the numbers are on the documentation page and change, so they are not repeated here. The headers `X-RateLimit-Limit`, `-Remaining`, `-Used`, `-Reset` and `-Resource` tell you where you stand; the documentation says that a rate-limit error is typically **403 or 429**, and that an integration "should wait before making another request". A good script reads these headers, backs off, and caches with `ETag`.

---

## 74.5 Webhooks: GitHub calls you

Polling asks "anything new?" again and again. A **webhook** reverses it: "Webhooks let you subscribe to events happening in a software system and automatically receive a delivery of data to your server whenever those events occur." You give GitHub a URL and choose the events (a push, a pull request opened, a Pages build, a new team member); when one occurs GitHub "will send an HTTP request with data about the event to the URL that you specified". Uses listed in the documentation: triggering CI on an external server (Chapter 61<!--ref:externalci-->), notifying a chat service, updating an issue tracker, deploying (Chapter 72<!--ref:deploy-->), and audit logging.

Webhooks belong to a **repository**, an **organisation** or another installation point, and only see what is there. "You cannot create webhooks for individual user accounts." Creating one in a repository needs admin access; in an organisation, an owner. A limit exists per event type and changes.

**Verify what you receive.** Your webhook URL is public: anyone can send a request to it. GitHub's documentation therefore says you should "validate the webhook signature before processing the delivery further". You create a **secret token** (a random, high-entropy string), store it securely ("Never hardcode a token into an application or push a token to any repository"), and GitHub sends, with each delivery, a header `X-Hub-Signature-256`. It is computed as an **HMAC** (a keyed hash: a fingerprint that only someone with the secret can produce) with SHA-256 over the payload. Points from the documentation: "The hash signature always starts with `sha256=`", it is a hex digest, handle the payload as UTF-8, and "Never use a plain `==` operator": use a **constant-time comparison**, so that the time taken does not leak information.

The documentation publishes test values: secret `It's a Secret to Everybody` and payload `Hello, World!` must give `757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17`. The recording computes it two independent ways (Python's `hmac` and the `openssl` command), compares with `hmac.compare_digest`, and shows a changed payload being rejected:

```text
$ python3 sig.py
sha256=757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17
genuine delivery accepted: True
tampered payload accepted: False
$ secret="It's a Secret to Everybody"
$ printf '%s' 'Hello, World!' | openssl dgst -sha256 -hmac "$secret" | awk '{print $NF}'
757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17
```

*Recorded in Bash; `ch74-api/expected-verify.bash.txt`.*

Both methods printed the documented value; the genuine delivery was accepted and a payload with one changed character was not. **These are public test values; never use a value from a book as your real secret.** Also: a valid signature proves the payload came from someone with the secret and was not altered; it does not prove the *event* is one you should trust (validate the content too), and an attacker who copies an old signed delivery could replay it (the documentation's best-practice page discusses handling deliveries; this book did not verify its replay advice).

> **Checked against GitHub's documentation (R343) and locally tested.** "About webhooks", "Types of webhooks", "Validating webhook deliveries". No webhook was created and no delivery was received.

---

## 74.6 GitHub Apps and OAuth apps

Sometimes your program must act on GitHub for other people or for an organisation. GitHub distinguishes:

- **GitHub Apps**: "tools that extend GitHub's functionality. GitHub Apps can do things on GitHub like open issues, comment on pull requests, and manage projects. They can also do things outside of GitHub based on events that happen on GitHub." (For example, post to a chat service when an issue is opened.)
- **OAuth apps**: an older way, where a user authorises an app to act with the user's scopes.

The documentation's advice: "In general, GitHub Apps are preferred over OAuth apps. GitHub Apps use fine-grained permissions, give the user more control over which repositories the app can access, and use short-lived tokens. These properties can harden the security of the app by limiting the damage that could be done if the app's credentials were leaked." This is Chapter 63<!--ref:secpractice-->'s least-privilege principle applied to integrations. An app is also not tied to a person, so it keeps working if someone leaves (Chapter 68<!--ref:orgs-->).

Apps receive **webhooks** for their events, and call the API with tokens that GitHub issues to them. Building one is a software project of its own; the documentation has guides for it.

---

## 74.7 Tokens for scripts

1. **Inside a workflow**, use the built-in `GITHUB_TOKEN` (Chapter 60<!--ref:wfsec-->) with the smallest permissions; it is what the documentation recommends before creating any token.
2. **From your computer**, prefer `gh` (Chapter 73<!--ref:ghcli-->), which keeps your login, over pasting tokens into scripts.
3. **For an integration**, prefer a GitHub App.
4. **If you must use a personal access token**: choose the fewest scopes, an expiry, store it in a secret manager or a secret, never in the repository, and revoke it when it is no longer needed (Chapter 33<!--ref:gitsec-->).
5. **Handle failures**: check the status code, respect rate limits, and log without printing tokens.

---

## Checkpoint

## What You Learned

- GitHub has a REST API (fixed structures at resource addresses) and a GraphQL API (ask for the fields you want).
- Large results are paginated; follow the `Link` header's `next` until it is absent.
- Pin an API version; watch rate-limit headers and back off.
- Webhooks push events to your URL; verify the `X-Hub-Signature-256` HMAC with a constant-time comparison.
- Prefer GitHub Apps (fine-grained, short-lived tokens) to OAuth apps; use `GITHUB_TOKEN` in workflows.

## New Vocabulary

**API**, **REST**, **GraphQL**, **webhook**, **HMAC**, **rate limit**, **GitHub App**, **OAuth app**, **pagination** (see the glossary).

## Commands Learned

`curl --include`, `openssl dgst -sha256 -hmac`, `python3 -c` helpers as in the recordings.

## Common Mistakes

1. **Trusting a webhook without verifying its signature.**
2. **Comparing signatures with `==`.**
3. **Ignoring pagination and using only the first page.**
4. **Not pinning an API version.**
5. **Hard-coding a token in a script.**
6. **Publishing raw headers or logs.**

## Practice

Do the exercises in [`exercises/ch74-exercises.md`](../../../exercises/ch74-exercises.md).

## Self-Test

1. What is the difference between REST and GraphQL in one sentence?
2. What does the `Link` header contain?
3. What does a webhook signature prove?
4. Why is `==` a poor way to compare signatures?
5. Why are GitHub Apps preferred to OAuth apps?

## Before Moving On

You are ready for Chapter 75<!--ref:platformextras--> if you can:

- [ ] follow `next` links to fetch all pages
- [ ] verify a webhook signature
- [ ] choose a token type for a script

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The HMAC signature values, the rejection of a changed payload, and the reading of a `Link` header | Locally tested: Bash 5.2 and zsh 5.9, Python 3, OpenSSL; CI | R342, R343 (local side) |
| Observations of one paginated endpoint, the default version header, a 400 for a bogus version | Observed live once on 2026-09-30 from the authoring environment, through an authenticating proxy; not re-run in CI; rate-limit values not quoted | R342 |
| REST vs GraphQL, pagination, versions, rate limits, webhooks, apps | Checked against `github/docs` (commit `2eaab0b`); not otherwise run | R341-R343 |
| The 410 response for a formerly supported version; replay protection advice | **Not observed / not checked** | none |

## Where this leads

Chapter 75<!--ref:platformextras--> covers the remaining platform features: Sponsors, the Marketplace, custom properties and governance.
