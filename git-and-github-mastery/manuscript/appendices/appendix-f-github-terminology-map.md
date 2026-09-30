# Appendix F — GitHub Terminology Map

The 107 terms first explained from Part V onwards (GitHub and what is built on it). **GitHub's names and features change**; where a term depends on the platform, the chapter says which documentation it was checked against. The full definitions are in the Glossary.

| Term | Meaning in one line | First explained |
|---|---|---|
| Access token | A password-like secret for programs. | Chapter 38<!--ref:ghauth--> |
| Action | A reusable piece of code that a step can use. | Chapter 54<!--ref:actions--> |
| Apex domain | A domain name with nothing in front of it, like example.com. | Chapter 69<!--ref:pages--> |
| API | A way for one program to ask another to do something. | Chapter 74<!--ref:api--> |
| Artifact | A file a workflow produces and keeps. | Chapter 56<!--ref:workflows_practice--> |
| Asset | A file attached to a release. | Chapter 66<!--ref:releases--> |
| Attestation | A signed statement about where and how a file was built. | Chapter 63<!--ref:secpractice--> |
| Base branch | The branch a pull request wants to change. | Chapter 45<!--ref:pr--> |
| Base permission | The lowest level of access every member of an organization has to its repositories. | Chapter 68<!--ref:orgs--> |
| Branch protection rule | A setting that protects chosen branches from risky changes. | Chapter 50<!--ref:protect--> |
| Check | A detailed result of an automated job, shown on a pull request. | Chapter 61<!--ref:externalci--> |
| Checksum | A short fingerprint of a file that changes if the file changes. | Chapter 63<!--ref:secpractice--> |
| Code of conduct | A written set of rules for how people behave in a project. | Chapter 64<!--ref:oss--> |
| Code owner | A person or team responsible for reviewing changes to certain files. | Chapter 49<!--ref:collab--> |
| Code review | Reading someone else's proposed change before it is merged. | Chapter 46<!--ref:review--> |
| Code scanning | Automatic analysis of your code for weaknesses. | Chapter 62<!--ref:ghsec--> |
| CodeQL | GitHub's code analysis engine. | Chapter 62<!--ref:ghsec--> |
| Codespace | A development environment that runs in the cloud and that you use through a browser or an editor. | Chapter 70<!--ref:codespaces--> |
| Commit status | A simple pass/fail label that a service attaches to a commit. | Chapter 61<!--ref:externalci--> |
| Compare branch | The branch that holds the changes in a pull request. | Chapter 45<!--ref:pr--> |
| Concurrency group | A name that lets only one run at a time use a shared resource. | Chapter 59<!--ref:runners--> |
| Container | An isolated, packaged environment that runs on a host computer. | Chapter 70<!--ref:codespaces--> |
| Container image | A packaged program together with everything it needs to run. | Chapter 71<!--ref:packages--> |
| Context | A collection of information that a workflow can read. | Chapter 55<!--ref:exprs--> |
| Continuous deployment | Deploying every change that passes the checks, automatically. | Chapter 72<!--ref:deploy--> |
| Continuous deployment (CD) | Publishing software automatically after it passes its checks. | Chapter 52<!--ref:cicd--> |
| Continuous integration (CI) | Checking every change automatically as soon as it is committed. | Chapter 52<!--ref:cicd--> |
| Contributor | A person who sends a change or report to a project. | Chapter 64<!--ref:oss--> |
| Copyleft | A licence rule that what you build from the code must be shared under the same licence. | Chapter 65<!--ref:licences--> |
| Copyright | The legal right of a creator over their work. | Chapter 65<!--ref:licences--> |
| Creative Commons | A family of licences for text, pictures and other non-software work. | Chapter 65<!--ref:licences--> |
| Cron | A compact way to write repeating times. | Chapter 56<!--ref:workflows_practice--> |
| Custom property | A label with a value that you attach to repositories in an organization. | Chapter 75<!--ref:platformextras--> |
| CVE | A public identification number for a known vulnerability. | Chapter 62<!--ref:ghsec--> |
| Dependabot | GitHub's helper that warns about vulnerable dependencies and opens pull requests to update them. | Chapter 62<!--ref:ghsec--> |
| Dependency graph | A list of the packages your project depends on. | Chapter 62<!--ref:ghsec--> |
| Deployment | Putting a version of your software where its users can use it. | Chapter 72<!--ref:deploy--> |
| Dev container | A container set up with the tools a project needs. | Chapter 70<!--ref:codespaces--> |
| Discussion | An open-ended conversation about a project, kept apart from the list of issues. | Chapter 48<!--ref:discussions--> |
| Docker | A popular tool for building and running containers. | Chapter 70<!--ref:codespaces--> |
| Dockerfile | A text file with instructions for building a container image. | Chapter 70<!--ref:codespaces--> |
| Enterprise account | An account that manages policy and billing for many organizations. | Chapter 68<!--ref:orgs--> |
| Environment | A named deployment target with its own rules and secrets. | Chapter 58<!--ref:wfadvanced--> |
| Event | Something that happens in a repository and can start a workflow. | Chapter 54<!--ref:actions--> |
| Expression | A small formula in a workflow that GitHub works out while running. | Chapter 55<!--ref:exprs--> |
| Fork | Your own hosted copy of someone else's repository. | Chapter 49<!--ref:collab--> |
| GitHub App | An integration with its own limited permissions that acts on GitHub. | Chapter 74<!--ref:api--> |
| GitHub CLI | A command-line program, gh, for working with GitHub. | Chapter 73<!--ref:ghcli--> |
| GitHub Pages | GitHub's service for publishing a static website from a repository. | Chapter 69<!--ref:pages--> |
| GitHub Sponsors | GitHub's way of supporting open-source maintainers with money. | Chapter 75<!--ref:platformextras--> |
| Governance | The written rules by which a group runs a project. | Chapter 75<!--ref:platformextras--> |
| GraphQL | An API where you send a query that names exactly the fields you want. | Chapter 74<!--ref:api--> |
| HMAC | A fingerprint that only someone with a secret key can produce. | Chapter 74<!--ref:api--> |
| Issue | A numbered item where a problem, idea or task is written down and discussed. | Chapter 44<!--ref:issues--> |
| Issue form | A form, defined in a file, that guides people to write a useful issue. | Chapter 44<!--ref:issues--> |
| Iteration | A block of time in which a team plans to finish some work. | Chapter 47<!--ref:projects--> |
| Job | A group of steps that run together on one machine. | Chapter 54<!--ref:actions--> |
| Licence | A written permission that says what others may do with a work. | Chapter 65<!--ref:licences--> |
| Lock file | A file that records the exact versions chosen. | Chapter 62<!--ref:ghsec--> |
| Machine user | A user account made for automation instead of a person. | Chapter 68<!--ref:orgs--> |
| Maintainer | A person who looks after a project and decides what is merged. | Chapter 64<!--ref:oss--> |
| Manifest | A file that lists the packages a project needs. | Chapter 62<!--ref:ghsec--> |
| Matrix | A way to run the same job in several configurations. | Chapter 56<!--ref:workflows_practice--> |
| Mixed content | An HTTPS page that loads some of its parts over plain HTTP. | Chapter 69<!--ref:pages--> |
| Notification | A message from a platform that something happened where you are subscribed. | Chapter 41<!--ref:notify--> |
| OAuth app | An integration that acts with the permissions a user gives it. | Chapter 74<!--ref:api--> |
| OIDC | A way for a workflow to get a short-lived cloud credential instead of storing a long-lived secret. | Chapter 60<!--ref:wfsec--> |
| Open source | Software whose code is public and whose licence lets others use, change and share it. | Chapter 64<!--ref:oss--> |
| Organization | A shared GitHub account that a group of people use to own repositories together. | Chapter 68<!--ref:orgs--> |
| Outside collaborator | Someone who is not a member of an organization but has access to some of its repositories. | Chapter 68<!--ref:orgs--> |
| Package | Software prepared so that a tool can install it. | Chapter 71<!--ref:packages--> |
| Pagination | Splitting a long list of results into pages. | Chapter 74<!--ref:api--> |
| Permissive licence | A licence that asks only for credit and notices. | Chapter 65<!--ref:licences--> |
| Pipeline | The ordered steps a change goes through automatically. | Chapter 52<!--ref:cicd--> |
| Pre-release | A release marked as not yet final. | Chapter 66<!--ref:releases--> |
| Project | A table, board or roadmap for planning work across issues and pull requests. | Chapter 47<!--ref:projects--> |
| Pull request | A proposal to merge one branch into another, with a place to discuss it first. | Chapter 45<!--ref:pr--> |
| Push protection | A block that stops a push containing a secret. | Chapter 62<!--ref:ghsec--> |
| Rate limit | A cap on how many requests you may make in a period. | Chapter 74<!--ref:api--> |
| README | A file that introduces a project to the people who arrive at it. | Chapter 42<!--ref:readme--> |
| Registry | A place that stores packages for download. | Chapter 71<!--ref:packages--> |
| Release | A named, downloadable version of a project on GitHub. | Chapter 66<!--ref:releases--> |
| Release notes | A description of what changed in a release. | Chapter 66<!--ref:releases--> |
| REST | A style of API where each kind of thing has an address and you ask with HTTP requests. | Chapter 74<!--ref:api--> |
| Reusable workflow | A workflow that other workflows can call as a whole. | Chapter 58<!--ref:wfadvanced--> |
| Rollback | Going back to the previous working version. | Chapter 72<!--ref:deploy--> |
| Ruleset | A named list of rules that a platform enforces on branches or tags. | Chapter 50<!--ref:protect--> |
| Runner | The machine that runs a job. | Chapter 54<!--ref:actions--> |
| Script injection | Someone else's text becoming part of your script and being run. | Chapter 60<!--ref:wfsec--> |
| Security advisory | A published notice about a vulnerability and its fix. | Chapter 62<!--ref:ghsec--> |
| Self-hosted runner | A machine you run yourself to do the jobs of a workflow. | Chapter 59<!--ref:runners--> |
| Sign-off | A line in a commit message saying the author has the right to submit the change. | Chapter 64<!--ref:oss--> |
| Source archive | A zip or tar file of the files at a tag, without history. | Chapter 66<!--ref:releases--> |
| SPDX identifier | A short standard name for a licence. | Chapter 65<!--ref:licences--> |
| Staging | A practice copy of production where you deploy first. | Chapter 72<!--ref:deploy--> |
| Static site | A website made of files that are sent to the browser exactly as they are. | Chapter 69<!--ref:pages--> |
| Step | One task inside a job. | Chapter 54<!--ref:actions--> |
| Subscription | An arrangement to be told about activity in one conversation or repository. | Chapter 41<!--ref:notify--> |
| Supply chain | Everything your software is made from and built with. | Chapter 63<!--ref:secpractice--> |
| Symbolic link | A file that points to another file or folder. | Chapter 72<!--ref:deploy--> |
| Team | A named group of people in an organization that shares access and mentions. | Chapter 68<!--ref:orgs--> |
| Telemetry | Usage information a program sends back to its maker. | Chapter 73<!--ref:ghcli--> |
| Topic | A short label that helps people find a repository. | Chapter 42<!--ref:readme--> |
| Webhook | A message GitHub sends to your web address when something happens. | Chapter 74<!--ref:api--> |
| Wiki | A section of a repository for long documentation, kept as its own Git repository. | Chapter 43<!--ref:settings--> |
| Workflow (GitHub Actions) | An automated process defined in a file in the repository. | Chapter 54<!--ref:actions--> |
| YAML | A readable text format for settings and lists, written with indentation. | Chapter 53<!--ref:yaml--> |