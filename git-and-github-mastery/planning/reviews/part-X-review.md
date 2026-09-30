# Part X review (Chapters 68-75), 2026-09-30

All eight chapters are `status: draft` and tagged [Deep], first read "later".

## 1. Technical review
- **68 Organizations and Enterprise Concepts:** account types, roles, teams, repository roles and base permissions, plans without figures, Enterprise Cloud vs Server.
- **69 GitHub Pages:** site types, publishing sources, limits and rules, custom domains, HTTPS; local pre-publication check for mixed content and root-absolute paths.
- **70 Codespaces and Dev Containers:** configuration as code, `.devcontainer` layout, lifecycle, cost model, security; local layout and strict-JSON check.
- **71 GitHub Packages and Containers:** registries, npm scope and name rules, permissions models, containers at concept level; local scope-mapping and token-placement check.
- **72 Deployment Pipelines:** pipeline steps, release directories with a switching link and rollback (local), environments and deployment secrets.
- **73 GitHub CLI:** `gh` 2.102.0 (checksum-verified download; CI installs the same pinned version) — alias, config, unauthenticated behaviour and exit statuses, telemetry log and disabled modes.
- **74 APIs, Webhooks and Apps:** REST vs GraphQL, pagination, versions, rate limits, webhook signature verification with the documented test vector (Python `hmac` and `openssl`), GitHub Apps vs OAuth apps. Also **observed live once**: a paginated endpoint's `Link` header, the default API version header and a 400 for a bogus version (through an authenticating proxy; not re-run in CI).
- **75 Other Platform Features:** Sponsors and `FUNDING.yml` (local check), Marketplace, AI assistance (neutral), custom properties, governance.

## 2. Beginner comprehension review
Deep chapters can be skipped on a first read. They repeat the security rules of Part VIII (least privilege, keep secrets out, verify before trusting) rather than introducing new ones. Chapters 70-72 use Linux/container vocabulary that is only introduced; a pilot read is needed.

## 3. Command verification
New recordings in Bash and zsh: `ch69-pages`, `ch70-codespaces`, `ch71-packages`, `ch72-deploy`, `ch73-ghcli`, `ch74-api`, `ch75-platformextras`. Chapter 73 required a new CI step (pinned `gh`, SHA-256 checked). Not run: `npm`, Docker, any hosted deployment, any command that needs a GitHub login.

## 4. Cross-references
`resolve_refs.py --check`, `check_links.py`, `check_refs`: no problems.

## 5. Research / source review
Ledger rows R325-R347, checked against `github/docs` at commit `2eaab0b` (the read-only clone's sparse checkout was extended for Codespaces, Packages, REST, webhooks, apps, Sponsors, GitHub CLI, Pages reusables and Copilot). Quantities, prices, regional lists and plan availability are deliberately **not** stated. **Open:** organisation creation steps and custom-role details were not read; `410 Gone` for a formerly supported API version was not observed; replay protection advice for webhooks not verified; token scope names for packages not copied.

## 6. Security review
Every token in the recordings is made up (`not-a-real-token`) or a published test value. The `gh` binary was checked against its release checksum. Live API observations did not reproduce identifiers or rate-limit numbers from the proxy. The chapters repeat: never commit tokens; pin actions; verify webhook signatures in constant time; treat marketplace listings and extensions as third-party code.

## 7. Editorial review
British spelling; no banned filler phrases; neutral treatment of AI tools, sponsorship and vendors; every plan-dependent statement carries a caveat.

## Open items
1. Live-account pass for organisations, Pages, Codespaces, Packages, Sponsors (gate D).
2. Plan availability and current limits for every feature.
3. Pilot read of Chapters 70-72.
