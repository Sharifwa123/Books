# Chapter 74 solutions

## Level 1
**1.1** REST exposes resources at addresses and returns a fixed structure for each request; GraphQL takes a query that names exactly the fields you want, at a single address, so one query can replace several REST requests.

**1.2** The response is paginated and there is a next page at that address; the script should request it, and continue until no `next` relation remains.

## Level 2
**2.1** `secret="It's a Secret to Everybody"; printf '%s' 'Hello, World!' | openssl dgst -sha256 -hmac "$secret"` prints a value ending with `757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17`.

**2.2** They look completely unrelated: a hash changes entirely when the input changes by one character. That is why a matching signature shows that the payload was not altered.

## Level 3
**3.1** For example, in Python: `import re, sys; print(dict((r, u) for u, r in re.findall(r'<([^>]+)>; rel="(\w+)"', sys.stdin.read())).get("next", "none"))`.

**3.2** A plain comparison can stop at the first difference, so the time it takes may leak how much of the guess was right. Use a constant-time comparison such as Python's `hmac.compare_digest`, Ruby's `Rack::Utils.secure_compare` or Node's `crypto.timingSafeEqual`.

## Level 4
**4.1** A personal access token is tied to a person and often broad; an OAuth app acts with a user's scopes; a GitHub App has fine-grained permissions, can be limited to chosen repositories, uses short-lived tokens and is not tied to a person. Recommend a GitHub App with only the permission to comment on pull requests, installed on the organisation's repositories.

## Level 5
**5.1** The endpoint paginates (30 items is a default page). Request a larger `per_page` if the endpoint supports it and follow the `next` link until it is absent.

**5.2** Check that you use the raw request body (not a re-serialised copy), that you handle it as UTF-8, that the secret in your server equals the one in the webhook's settings, that you compute HMAC-SHA-256 and prefix the hex digest with `sha256=`, and that you compare against the `X-Hub-Signature-256` header.
