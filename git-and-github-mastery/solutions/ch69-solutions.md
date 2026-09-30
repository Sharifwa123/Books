# Chapter 69 solutions

## Level 1
**1.1** (a) `https://ada.github.io` (the repository is named `ada.github.io`); (b) `https://ada.github.io/notes`.

**1.2** Deploy from a branch (with an optional folder), or a custom GitHub Actions workflow.

## Level 2
**2.1** `git grep -n 'http://'` finds the image line; `git grep -n -E '(href|src)="/'` finds the stylesheet line.

**2.2** Nothing is printed, and `git grep` exits with a failure status. Add `|| echo "none left"` to print a message.

## Level 3
**3.1** For example: `if git grep -q 'http://' -- '*.html'; then echo "mixed content found"; exit 1; fi`.

**3.2** `www.example.com`: CNAME. `example.com`: A, ALIAS or ANAME. The actual values are on GitHub's current page for managing a custom domain, not in this book.

## Level 4
**4.1** For example: "GitHub's documentation says Pages is not intended for or allowed to be used as a free web-hosting service for an online business or an e-commerce site, so a shop is not a good fit. You could use Pages for a catalogue and link to a proper shop service. Check the current rules page, because they can change."

## Level 5
**5.1** A root-absolute path such as `/style.css` on a project site (confirm by looking at the requested address in the browser's developer tools or by searching with `git grep`), or a stylesheet loaded over `http://` from an HTTPS site (mixed content; confirm by searching for `http://`).

**5.2** GitHub checks the DNS settings, then requests a certificate from Let's Encrypt, which may take some time. If it does not finish several minutes after saving, remove the custom domain, type it again and save, which restarts the process.
