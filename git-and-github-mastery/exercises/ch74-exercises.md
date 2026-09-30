# Chapter 74 exercises — APIs, Webhooks and Apps

Attempt each exercise before you open `solutions/ch74-solutions.md`. Exercises 2.1 and 2.2 need Python 3 or OpenSSL and no account or network. **Use only made-up secrets. Never paste a real token into a terminal, a script or a message.**

## Level 1 — Guided

**1.1 Two APIs.** Explain in one sentence each what REST and GraphQL are and one difference.

**1.2 The header.** A response contains `Link: <https://example.org/items?page=3>; rel="next"`. What does it tell a script?

## Level 2 — Partially guided

**2.1 A signature.** Using the documentation's test values (secret `It's a Secret to Everybody`, payload `Hello, World!`), compute the HMAC-SHA-256 of the payload with `openssl dgst -sha256 -hmac`. Compare it with the value in the chapter.

**2.2 Tamper.** Change one character of the payload and compute again. Do the two signatures look similar or completely different? What does that tell you?

## Level 3 — Independent

**3.1 A pager.** Write a short script (any language) that, given the text of a `Link` header, prints the address of the next page or `none`.

**3.2 Constant time.** Explain why the documentation says never to use a plain `==` to compare signatures, and name the function you would use in a language you know.

## Level 4 — Professional scenario

**4.1 Choose.** Your team wants a service that comments on pull requests in every repository of the organization. Compare a personal access token, an OAuth app and a GitHub App using the chapter, and recommend one.

## Level 5 — Troubleshooting

**5.1** Your script gets 30 items when the repository has hundreds. What is wrong and how do you fix it?

**5.2** Your webhook handler accepts a request but the signature check fails on every delivery, including genuine ones. List three things to check.
