# Appendix F — GitHub Terminology Map

The 107 terms first explained from Part V onwards (GitHub and what is built on it). **GitHub's names and features change**; where a term depends on the platform, the chapter says which documentation it was checked against. The full definitions are in the Glossary.

| Term | Meaning in one line | First explained |
|---|---|---|
| Access token | A password-like secret for programs. | Chapter [[ghauth]] |
| Action | A reusable piece of code that a step can use. | Chapter [[actions]] |
| Apex domain | A domain name with nothing in front of it, like example.com. | Chapter [[pages]] |
| API | A way for one program to ask another to do something. | Chapter [[api]] |
| Artifact | A file a workflow produces and keeps. | Chapter [[workflows_practice]] |
| Asset | A file attached to a release. | Chapter [[releases]] |
| Attestation | A signed statement about where and how a file was built. | Chapter [[secpractice]] |
| Base branch | The branch a pull request wants to change. | Chapter [[pr]] |
| Base permission | The lowest level of access every member of an organization has to its repositories. | Chapter [[orgs]] |
| Branch protection rule | A setting that protects chosen branches from risky changes. | Chapter [[protect]] |
| Check | A detailed result of an automated job, shown on a pull request. | Chapter [[externalci]] |
| Checksum | A short fingerprint of a file that changes if the file changes. | Chapter [[secpractice]] |
| Code of conduct | A written set of rules for how people behave in a project. | Chapter [[oss]] |
| Code owner | A person or team responsible for reviewing changes to certain files. | Chapter [[collab]] |
| Code review | Reading someone else's proposed change before it is merged. | Chapter [[review]] |
| Code scanning | Automatic analysis of your code for weaknesses. | Chapter [[ghsec]] |
| CodeQL | GitHub's code analysis engine. | Chapter [[ghsec]] |
| Codespace | A development environment that runs in the cloud and that you use through a browser or an editor. | Chapter [[codespaces]] |
| Commit status | A simple pass/fail label that a service attaches to a commit. | Chapter [[externalci]] |
| Compare branch | The branch that holds the changes in a pull request. | Chapter [[pr]] |
| Concurrency group | A name that lets only one run at a time use a shared resource. | Chapter [[runners]] |
| Container | An isolated, packaged environment that runs on a host computer. | Chapter [[codespaces]] |
| Container image | A packaged program together with everything it needs to run. | Chapter [[packages]] |
| Context | A collection of information that a workflow can read. | Chapter [[exprs]] |
| Continuous deployment | Deploying every change that passes the checks, automatically. | Chapter [[deploy]] |
| Continuous deployment (CD) | Publishing software automatically after it passes its checks. | Chapter [[cicd]] |
| Continuous integration (CI) | Checking every change automatically as soon as it is committed. | Chapter [[cicd]] |
| Contributor | A person who sends a change or report to a project. | Chapter [[oss]] |
| Copyleft | A licence rule that what you build from the code must be shared under the same licence. | Chapter [[licences]] |
| Copyright | The legal right of a creator over their work. | Chapter [[licences]] |
| Creative Commons | A family of licences for text, pictures and other non-software work. | Chapter [[licences]] |
| Cron | A compact way to write repeating times. | Chapter [[workflows_practice]] |
| Custom property | A label with a value that you attach to repositories in an organisation. | Chapter [[platformextras]] |
| CVE | A public identification number for a known vulnerability. | Chapter [[ghsec]] |
| Dependabot | GitHub's helper that warns about vulnerable dependencies and opens pull requests to update them. | Chapter [[ghsec]] |
| Dependency graph | A list of the packages your project depends on. | Chapter [[ghsec]] |
| Deployment | Putting a version of your software where its users can use it. | Chapter [[deploy]] |
| Dev container | A container set up with the tools a project needs. | Chapter [[codespaces]] |
| Discussion | An open-ended conversation about a project, kept apart from the list of issues. | Chapter [[discussions]] |
| Docker | A popular tool for building and running containers. | Chapter [[codespaces]] |
| Dockerfile | A text file with instructions for building a container image. | Chapter [[codespaces]] |
| Enterprise account | An account that manages policy and billing for many organizations. | Chapter [[orgs]] |
| Environment | A named deployment target with its own rules and secrets. | Chapter [[wfadvanced]] |
| Event | Something that happens in a repository and can start a workflow. | Chapter [[actions]] |
| Expression | A small formula in a workflow that GitHub works out while running. | Chapter [[exprs]] |
| Fork | Your own hosted copy of someone else's repository. | Chapter [[collab]] |
| GitHub App | An integration with its own limited permissions that acts on GitHub. | Chapter [[api]] |
| GitHub CLI | A command-line program, gh, for working with GitHub. | Chapter [[ghcli]] |
| GitHub Pages | GitHub's service for publishing a static website from a repository. | Chapter [[pages]] |
| GitHub Sponsors | GitHub's way of supporting open-source maintainers with money. | Chapter [[platformextras]] |
| Governance | The written rules by which a group runs a project. | Chapter [[platformextras]] |
| GraphQL | An API where you send a query that names exactly the fields you want. | Chapter [[api]] |
| HMAC | A fingerprint that only someone with a secret key can produce. | Chapter [[api]] |
| Issue | A numbered item where a problem, idea or task is written down and discussed. | Chapter [[issues]] |
| Issue form | A form, defined in a file, that guides people to write a useful issue. | Chapter [[issues]] |
| Iteration | A block of time in which a team plans to finish some work. | Chapter [[projects]] |
| Job | A group of steps that run together on one machine. | Chapter [[actions]] |
| Licence | A written permission that says what others may do with a work. | Chapter [[licences]] |
| Lock file | A file that records the exact versions chosen. | Chapter [[ghsec]] |
| Machine user | A user account made for automation instead of a person. | Chapter [[orgs]] |
| Maintainer | A person who looks after a project and decides what is merged. | Chapter [[oss]] |
| Manifest | A file that lists the packages a project needs. | Chapter [[ghsec]] |
| Matrix | A way to run the same job in several configurations. | Chapter [[workflows_practice]] |
| Mixed content | An HTTPS page that loads some of its parts over plain HTTP. | Chapter [[pages]] |
| Notification | A message from a platform that something happened where you are subscribed. | Chapter [[notify]] |
| OAuth app | An integration that acts with the permissions a user gives it. | Chapter [[api]] |
| OIDC | A way for a workflow to get a short-lived cloud credential instead of storing a long-lived secret. | Chapter [[wfsec]] |
| Open source | Software whose code is public and whose licence lets others use, change and share it. | Chapter [[oss]] |
| Organization | A shared GitHub account that a group of people use to own repositories together. | Chapter [[orgs]] |
| Outside collaborator | Someone who is not a member of an organization but has access to some of its repositories. | Chapter [[orgs]] |
| Package | Software prepared so that a tool can install it. | Chapter [[packages]] |
| Pagination | Splitting a long list of results into pages. | Chapter [[api]] |
| Permissive licence | A licence that asks only for credit and notices. | Chapter [[licences]] |
| Pipeline | The ordered steps a change goes through automatically. | Chapter [[cicd]] |
| Pre-release | A release marked as not yet final. | Chapter [[releases]] |
| Project | A table, board or roadmap for planning work across issues and pull requests. | Chapter [[projects]] |
| Pull request | A proposal to merge one branch into another, with a place to discuss it first. | Chapter [[pr]] |
| Push protection | A block that stops a push containing a secret. | Chapter [[ghsec]] |
| Rate limit | A cap on how many requests you may make in a period. | Chapter [[api]] |
| README | A file that introduces a project to the people who arrive at it. | Chapter [[readme]] |
| Registry | A place that stores packages for download. | Chapter [[packages]] |
| Release | A named, downloadable version of a project on GitHub. | Chapter [[releases]] |
| Release notes | A description of what changed in a release. | Chapter [[releases]] |
| REST | A style of API where each kind of thing has an address and you ask with HTTP requests. | Chapter [[api]] |
| Reusable workflow | A workflow that other workflows can call as a whole. | Chapter [[wfadvanced]] |
| Rollback | Going back to the previous working version. | Chapter [[deploy]] |
| Ruleset | A named list of rules that a platform enforces on branches or tags. | Chapter [[protect]] |
| Runner | The machine that runs a job. | Chapter [[actions]] |
| Script injection | Someone else's text becoming part of your script and being run. | Chapter [[wfsec]] |
| Security advisory | A published notice about a vulnerability and its fix. | Chapter [[ghsec]] |
| Self-hosted runner | A machine you run yourself to do the jobs of a workflow. | Chapter [[runners]] |
| Sign-off | A line in a commit message saying the author has the right to submit the change. | Chapter [[oss]] |
| Source archive | A zip or tar file of the files at a tag, without history. | Chapter [[releases]] |
| SPDX identifier | A short standard name for a licence. | Chapter [[licences]] |
| Staging | A practice copy of production where you deploy first. | Chapter [[deploy]] |
| Static site | A website made of files that are sent to the browser exactly as they are. | Chapter [[pages]] |
| Step | One task inside a job. | Chapter [[actions]] |
| Subscription | An arrangement to be told about activity in one conversation or repository. | Chapter [[notify]] |
| Supply chain | Everything your software is made from and built with. | Chapter [[secpractice]] |
| Symbolic link | A file that points to another file or folder. | Chapter [[deploy]] |
| Team | A named group of people in an organization that shares access and mentions. | Chapter [[orgs]] |
| Telemetry | Usage information a program sends back to its maker. | Chapter [[ghcli]] |
| Topic | A short label that helps people find a repository. | Chapter [[readme]] |
| Webhook | A message GitHub sends to your web address when something happens. | Chapter [[api]] |
| Wiki | A section of a repository for long documentation, kept as its own Git repository. | Chapter [[settings]] |
| Workflow (GitHub Actions) | An automated process defined in a file in the repository. | Chapter [[actions]] |
| YAML | A readable text format for settings and lists, written with indentation. | Chapter [[yaml]] |