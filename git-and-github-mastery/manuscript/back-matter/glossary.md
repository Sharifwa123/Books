# Glossary

Every term that the book defines, in alphabetical order. Each entry gives a simple definition, a technical one, an example, related terms and the chapter where the term is first explained.

## .

**.gitignore.** A text file listing patterns of files Git should ignore.

*Technically:* A file whose lines are patterns (with comments and negations) applied to paths under its directory; normally tracked. *Example:* *.log

*Related:* ignored file; core.excludesFile. *First explained in* Chapter 18<!--ref:tracking-->.

## A

**Absolute path.** A path that starts at the root and means the same wherever you are.

*Technically:* A path that begins at the file-system root (or a drive letter on Windows) and fully specifies a location. *Example:* /home/learner/sharif-git-lab/sunrise-bakery/menu.html

*Related:* relative path; root. *First explained in* Chapter 2<!--ref:files-->.

**Access token.** A password-like secret for programs.

*Technically:* A secret string that a program presents instead of a password, which can be limited in permissions and lifetime and revoked separately. *Example:* a personal access token

*Related:* secret; authentication. *First explained in* Chapter 38<!--ref:ghauth-->.

**Account.** A record a service keeps to represent you.

*Technically:* A stored identity with credentials, settings and permissions maintained by a service. *Example:* Your email account.

*Related:* username; authentication. *First explained in* Chapter 6<!--ref:accounts-->.

**Action.** A reusable piece of code that a step can use.

*Technically:* A predefined, reusable unit of code used in a workflow step to perform a task such as checking out a repository or setting up a toolchain. *Example:* actions/checkout@v6

*Related:* step; workflow. *First explained in* Chapter 54<!--ref:actions-->.

**Administrator.** An account or permission level allowed to change the computer's system settings.

*Technically:* A privileged user role that may modify system-wide configuration and install software for all users. *Example:* The prompt that asks whether to allow an installer to make changes.

*Related:* installer; permission. *First explained in* Chapter 1<!--ref:computer-->.

**Alias.** Your own short name for a Git command.

*Technically:* A name defined in configuration (alias.<name>) as a shortcut for another Git command, or for a shell command when it starts with !. *Example:* git config --global alias.st "status --short"

*Related:* configuration. *First explained in* Chapter 32<!--ref:custom-->.

**Annotated tag.** A tag with a message and tagger.

*Technically:* A tag stored as its own object with tagger, date and message; the usual choice for releases. *Example:* git tag -a v1.0 -m "First public menu"

*Related:* tag. *First explained in* Chapter 24<!--ref:stash-->.

**Apex domain.** A domain name with nothing in front of it, like example.com.

*Technically:* A domain without a subdomain, also called a bare or root domain. *Example:* example.com

*Related:* DNS; custom domain. *First explained in* Chapter 69<!--ref:pages-->.

**API.** A way for one program to ask another to do something.

*Technically:* An application programming interface: a defined set of requests and responses that programs use to communicate. *Example:* A script asking GitHub for a repository's issues.

*Related:* REST; GraphQL. *First explained in* Chapter 74<!--ref:api-->.

**Application (program).** Software that does a specific job for a person.

*Technically:* A program designed to perform a task for a user, running on top of an operating system. *Example:* A text editor, a browser, Git.

*Related:* software; operating system; installer. *First explained in* Chapter 1<!--ref:computer-->.

**Argument.** The thing a command acts on, such as a file name.

*Technically:* A value passed to a command on the command line. *Example:* notes.txt in ls -l notes.txt

*Related:* command; option. *First explained in* Chapter 7<!--ref:terminal-->.

**Artifact.** A file a workflow produces and keeps.

*Technically:* A file or collection of files produced during a workflow run and stored so that it persists after the job and can be shared with other jobs. *Example:* A built program or a test report.

*Related:* cache; workflow (GitHub Actions). *First explained in* Chapter 56<!--ref:workflows_practice-->.

**Asset.** A file attached to a release.

*Technically:* A file uploaded to a GitHub release, in addition to the automatic source archives. *Example:* A compiled program.

*Related:* release; artifact. *First explained in* Chapter 66<!--ref:releases-->.

**Atomic commit.** A commit containing one logical change.

*Technically:* A commit that is complete and self-contained, with a single purpose, that can be reviewed or reverted independently. *Example:* Raise the price of rolls

*Related:* commit. *First explained in* Chapter 19<!--ref:commits-->.

**Attestation.** A signed statement about where and how a file was built.

*Technically:* A signed record, for example made with Sigstore, linking an artifact to its source and build instructions. *Example:* A GitHub artifact attestation.

*Related:* artifact; signed commit. *First explained in* Chapter 63<!--ref:secpractice-->.

**Authentication.** Proving who you are.

*Technically:* The process of verifying the identity claimed by a user or program. *Example:* Entering a password and a code.

*Related:* authorization; account. *First explained in* Chapter 6<!--ref:accounts-->.

**Authorization.** Deciding what you are allowed to do once your identity is known.

*Technically:* The process of determining whether an authenticated identity may perform a requested action. *Example:* You can read a project but not delete it.

*Related:* authentication; least privilege. *First explained in* Chapter 6<!--ref:accounts-->.

## B

**Backup.** A copy of your files kept elsewhere so they can be restored after loss.

*Technically:* A duplicate of data stored separately from the original to allow recovery after loss or damage. *Example:* A nightly copy of a laptop to an external drive.

*Related:* version control; synchronised folder. *First explained in* Chapter 9<!--ref:problem-->.

**Bare repository.** A repository with no working files, used as a shared hub.

*Technically:* A repository holding only Git's database, with no checked-out working tree; the form used for shared remotes. *Example:* git init --bare shared/bakery.git

*Related:* remote; clone. *First explained in* Chapter 23<!--ref:remotes-->.

**Base branch.** The branch a pull request wants to change.

*Technically:* The branch into which the changes of a pull request are to be merged, usually the default branch. *Example:* main

*Related:* pull request; compare branch. *First explained in* Chapter 45<!--ref:pr-->.

**Base permission.** The lowest level of access every member of an organization has to its repositories.

*Technically:* An organization-wide default repository permission for members; it does not apply to outside collaborators. *Example:* Read.

*Related:* organization; repository role. *First explained in* Chapter 68<!--ref:orgs-->.

**Bash.** A widely used shell; the one this book uses for its examples.

*Technically:* The Bourne-Again Shell, a Unix command interpreter. *Example:* The shell in Git Bash.

*Related:* shell; Git Bash; zsh. *First explained in* Chapter 7<!--ref:terminal-->.

**Binary file.** A file that is not plain text, such as a photo or a word-processor document.

*Technically:* A file whose bytes are not a sequence of characters intended to be read as text. *Example:* logo.png, report.docx

*Related:* plain text; ZIP archive. *First explained in* Chapter 3<!--ref:editors-->.

**Bisect.** Find the commit that broke something by halving.

*Technically:* A binary search through history that repeatedly checks out the middle of the remaining range to find the first bad commit. *Example:* git bisect run ./test.sh

*Related:* commit. *First explained in* Chapter 28<!--ref:tools-->.

**Bitbucket.** Another hosting platform for Git repositories, from a different company.

*Technically:* A hosting platform for Git repositories with collaboration features. *Example:* A team's repository hosted outside GitHub.

*Related:* GitHub; hosting platform. *First explained in* Chapter 12<!--ref:platforms-->.

**Blob.** The stored contents of one file.

*Technically:* An object holding the contents of a single file, with no name, folder or date. *Example:* 28adfbf...

*Related:* tree; object. *First explained in* Chapter 30<!--ref:objects-->.

**Branch.** A movable name that points to a commit.

*Technically:* A reference under refs/heads that holds the identifier of a commit and moves forward with new commits. *Example:* main

*Related:* HEAD; commit. *First explained in* Chapter 15<!--ref:model-->.

**Branch protection rule.** A setting that protects chosen branches from risky changes.

*Technically:* A repository setting on a hosting platform that matches branch names by pattern and applies restrictions or requirements, such as required reviews and blocked force pushes. *Example:* A rule on main that requires one review.

*Related:* ruleset; pull request. *First explained in* Chapter 50<!--ref:protect-->.

**Browser.** An application for viewing web pages.

*Technically:* A client application that requests, interprets and displays web resources. *Example:* The program in which you open index.html.

*Related:* web; client. *First explained in* Chapter 5<!--ref:internet-->.

**Byte.** A unit for measuring stored information; enough for one English letter.

*Technically:* A unit of digital information made of eight bits. *Example:* The word 'Hi' takes two bytes in simple text.

*Related:* storage; file. *First explained in* Chapter 1<!--ref:computer-->.

## C

**cd.** Moves you into another folder.

*Technically:* Change directory: sets the shell's current working directory. *Example:* cd ..

*Related:* pwd; path. *First explained in* Chapter 7<!--ref:terminal-->.

**Centralised version control.** One server holds the only complete history; users hold working copies.

*Technically:* A version-control architecture with a single central repository that clients connect to. *Example:* A shared server everyone must reach to record work.

*Related:* distributed version control; single point of failure. *First explained in* Chapter 11<!--ref:distributed-->.

**Character.** A single unit of text: a letter, digit, symbol, emoji or space.

*Technically:* An abstract unit of written text identified by a Unicode code point. *Example:* a, é, 7, the space

*Related:* encoding; Unicode. *First explained in* Chapter 4<!--ref:text-->.

**Check.** A detailed result of an automated job, shown on a pull request.

*Technically:* A check run created by a GitHub App, including GitHub Actions, with output, annotations and messages. *Example:* The Checks tab of a pull request.

*Related:* commit status; workflow. *First explained in* Chapter 61<!--ref:externalci-->.

**Checksum.** A short fingerprint of a file that changes if the file changes.

*Technically:* A value computed from a file's bytes with a hash function such as SHA-256, used to detect change. *Example:* A 64-character SHA-256 value next to a download.

*Related:* hash; artifact. *First explained in* Chapter 63<!--ref:secpractice-->.

**Cherry-pick.** Copy one commit onto another branch.

*Technically:* Apply the change introduced by an existing commit as a new commit on the current branch. *Example:* git cherry-pick drinks~1

*Related:* rebase; patch. *First explained in* Chapter 28<!--ref:tools-->.

**Client.** The computer or program that asks for something.

*Technically:* The party in a client-server exchange that initiates requests. *Example:* Your browser.

*Related:* server; HTTP. *First explained in* Chapter 5<!--ref:internet-->.

**Clone.** A complete copy of a repository, with all its history, made on another computer.

*Technically:* A full copy of a repository including history, produced by cloning. *Example:* Your copy of a project from a shared server.

*Related:* repository; remote. *First explained in* Chapter 11<!--ref:distributed-->.

**Code editor.** A text editor with extra help for writing structured text such as software.

*Technically:* A text editor providing features such as syntax highlighting, line numbers, multi-file search and folder navigation. *Example:* An editor showing your project's files in a side panel.

*Related:* text editor; syntax highlighting. *First explained in* Chapter 3<!--ref:editors-->.

**Code of conduct.** A written set of rules for how people behave in a project.

*Technically:* A document that defines standards of engagement in a community and procedures for problems. *Example:* A CODE_OF_CONDUCT file.

*Related:* CONTRIBUTING; community profile. *First explained in* Chapter 64<!--ref:oss-->.

**Code owner.** A person or team responsible for reviewing changes to certain files.

*Technically:* A user or team named in a CODEOWNERS file who is automatically requested to review pull requests that change matching files. *Example:* @ada owns menu.md.

*Related:* review; pull request. *First explained in* Chapter 49<!--ref:collab-->.

**Code review.** Reading someone else's proposed change before it is merged.

*Technically:* The practice of examining a proposed change to detect defects, share knowledge and decide whether it is ready to be integrated. *Example:* A colleague comments on three lines of your pull request.

*Related:* pull request; approval. *First explained in* Chapter 46<!--ref:review-->.

**Code scanning.** Automatic analysis of your code for weaknesses.

*Technically:* A GitHub feature that runs analysis tools such as CodeQL and shows alerts. *Example:* An alert on a pull request.

*Related:* CodeQL; check. *First explained in* Chapter 62<!--ref:ghsec-->.

**CodeQL.** GitHub's code analysis engine.

*Technically:* The analysis product maintained by GitHub that code scanning can use. *Example:* A CodeQL alert for a possible injection.

*Related:* code scanning. *First explained in* Chapter 62<!--ref:ghsec-->.

**Codespace.** A development environment that runs in the cloud and that you use through a browser or an editor.

*Technically:* A GitHub-hosted development environment in a Docker container on a virtual machine, created from a repository. *Example:* A codespace for the wordcount repository.

*Related:* dev container; container. *First explained in* Chapter 70<!--ref:codespaces-->.

**Command.** One instruction typed to the shell.

*Technically:* A line of input consisting of a program name followed by options and arguments, executed by the shell. *Example:* ls -l notes.txt

*Related:* option; argument; prompt. *First explained in* Chapter 7<!--ref:terminal-->.

**Commit.** A recorded snapshot with author, time, message and a link to the previous commit; also the action of making one.

*Technically:* A Git object recording a tree, parent commits, author and committer identities, timestamps and a message. *Example:* git commit -m "Add README"

*Related:* snapshot; hash; branch. *First explained in* Chapter 15<!--ref:model-->.

**Commit status.** A simple pass/fail label that a service attaches to a commit.

*Technically:* A state (such as success or failure) with a context name that an external service sets on a commit through GitHub's API. *Example:* An external build reporting success on the latest commit of a pull request.

*Related:* check; status check. *First explained in* Chapter 61<!--ref:externalci-->.

**CommonMark.** A precise written specification of the core Markdown syntax.

*Technically:* A standardised specification of Markdown syntax intended to make different implementations behave consistently. *Example:* The syntax taught in the Markdown chapter.

*Related:* Markdown. *First explained in* Chapter 8<!--ref:markdown-->.

**Compare branch.** The branch that holds the changes in a pull request.

*Technically:* The topic (head) branch of a pull request, whose commits are proposed for merging into the base branch. *Example:* add-tea

*Related:* pull request; base branch. *First explained in* Chapter 45<!--ref:pr-->.

**Computer.** A machine that follows instructions to take in, change, keep and show information.

*Technically:* A programmable electronic device that executes stored instructions to process data received as input, retain results in storage and present output. *Example:* A laptop, a phone, a cash machine.

*Related:* hardware; software; processor. *First explained in* Chapter 1<!--ref:computer-->.

**Concurrency group.** A name that lets only one run at a time use a shared resource.

*Technically:* A label under which the platform allows at most one workflow run or job to be running, with later runs waiting or earlier ones cancelled. *Example:* validate-refs/heads/main

*Related:* workflow (GitHub Actions). *First explained in* Chapter 59<!--ref:runners-->.

**Configuration (setting).** A named value that changes how Git behaves.

*Technically:* A key of the form section.name with a value, read from Git's configuration files, environment and command line. *Example:* user.email, init.defaultBranch

*Related:* scope; git config. *First explained in* Chapter 14<!--ref:config-->.

**Conflict markers.** The lines Git writes into a conflicted file.

*Technically:* The <<<<<<<, ======= and >>>>>>> lines that delimit the two versions; all must be removed before committing. *Example:* <<<<<<< HEAD

*Related:* merge conflict. *First explained in* Chapter 22<!--ref:conflicts-->.

**Container.** An isolated, packaged environment that runs on a host computer.

*Technically:* An isolated runtime environment with its own filesystem and tools, started from an image. *Example:* A Python environment in a container.

*Related:* Docker; dev container. *First explained in* Chapter 70<!--ref:codespaces-->.

**Container image.** A packaged program together with everything it needs to run.

*Technically:* A stored, layered file system and configuration from which containers are started. *Example:* An image in the container registry.

*Related:* container; Docker. *First explained in* Chapter 71<!--ref:packages-->.

**Context.** A collection of information that a workflow can read.

*Technically:* A named object, such as github, env, steps or runner, whose properties can be read in workflow expressions. *Example:* github.sha

*Related:* expression. *First explained in* Chapter 55<!--ref:exprs-->.

**Continuous deployment.** Deploying every change that passes the checks, automatically.

*Technically:* A practice in which each change that passes automated checks is deployed to production without a manual step. *Example:* A merge to main that goes live after the tests pass.

*Related:* continuous integration; deployment. *First explained in* Chapter 72<!--ref:deploy-->.

**Continuous deployment (CD).** Publishing software automatically after it passes its checks.

*Technically:* The practice of using automation to publish and deploy software updates, typically after the code has been built and tested automatically. *Example:* A merge to main publishes the website.

*Related:* continuous integration; pipeline. *First explained in* Chapter 52<!--ref:cicd-->.

**Continuous integration (CI).** Checking every change automatically as soon as it is committed.

*Technically:* The practice of frequently committing code to a shared repository and automatically building and testing each change to detect errors early. *Example:* A server runs the tests on every pull request.

*Related:* continuous deployment; pipeline. *First explained in* Chapter 52<!--ref:cicd-->.

**Contributor.** A person who sends a change or report to a project.

*Technically:* Someone who provides code, documentation, reports or other work to a project. *Example:* A stranger who fixes a typo through a pull request.

*Related:* maintainer; fork. *First explained in* Chapter 64<!--ref:oss-->.

**Copyleft.** A licence rule that what you build from the code must be shared under the same licence.

*Technically:* A licence condition requiring that distributed derivative works be licensed under the same or a compatible licence, with reach that varies (weak or strong). *Example:* The GNU General Public License.

*Related:* permissive licence. *First explained in* Chapter 65<!--ref:licences-->.

**Copyright.** The legal right of a creator over their work.

*Technically:* A legal right, differing by country, that lets the creator control copying, distribution and adaptation of a work. *Example:* The author of a program holds the copyright unless they transfer it.

*Related:* licence. *First explained in* Chapter 65<!--ref:licences-->.

**Creative Commons.** A family of licences for text, pictures and other non-software work.

*Technically:* Public licences built from elements such as Attribution, ShareAlike and NonCommercial. *Example:* CC-BY-4.0

*Related:* licence; SPDX identifier. *First explained in* Chapter 65<!--ref:licences-->.

**Credential helper.** A program that remembers passwords for Git.

*Technically:* A program that Git asks to store, return or delete the username and password or token for a remote address. *Example:* credential.helper

*Related:* remote. *First explained in* Chapter 32<!--ref:custom-->.

**Cron.** A compact way to write repeating times.

*Technically:* A five-field notation (minute, hour, day of month, month, day of week) with the operators *, comma, hyphen and slash that describes when a scheduled task runs. *Example:* 20 8 * * * means 08:20 every day.

*Related:* schedule; workflow (GitHub Actions). *First explained in* Chapter 56<!--ref:workflows_practice-->.

**CSS.** A text format that describes how web pages look.

*Technically:* Cascading Style Sheets: a language for describing the presentation of documents written in a markup language. *Example:* css/style.css

*Related:* HTML. *First explained in* Chapter 3<!--ref:editors-->.

**Current directory (working directory).** The folder that counts as 'here' when you give a relative path.

*Technically:* The directory against which a process resolves relative paths. *Example:* sunrise-bakery after you have moved into it.

*Related:* relative path; path. *First explained in* Chapter 2<!--ref:files-->.

**Custom property.** A label with a value that you attach to repositories in an organization.

*Technically:* Organization-defined metadata on repositories that can be used, for example, to target rulesets. *Example:* criticality = high

*Related:* ruleset; organization. *First explained in* Chapter 75<!--ref:platformextras-->.

**CVE.** A public identification number for a known vulnerability.

*Technically:* Common Vulnerabilities and Exposures identifier assigned by a numbering authority. *Example:* An advisory that carries a CVE number.

*Related:* security advisory. *First explained in* Chapter 62<!--ref:ghsec-->.

## D

**Dangling object.** A stored object nothing points to.

*Technically:* An object in the database that no ref leads to; removed by garbage collection eventually. *Example:* dangling commit ee9eec6

*Related:* reflog; garbage collection. *First explained in* Chapter 30<!--ref:objects-->.

**Dependabot.** GitHub's helper that warns about vulnerable dependencies and opens pull requests to update them.

*Technically:* A set of features: alerts, security updates and version updates. *Example:* A pull request that raises a package to a fixed version.

*Related:* dependency graph; pull request. *First explained in* Chapter 62<!--ref:ghsec-->.

**Dependency graph.** A list of the packages your project depends on.

*Technically:* GitHub's map of a repository's dependencies built from manifests and lock files. *Example:* Packages listed in a manifest file.

*Related:* Dependabot; manifest. *First explained in* Chapter 62<!--ref:ghsec-->.

**Deployment.** Putting a version of your software where its users can use it.

*Technically:* The process of releasing a build to an environment where it runs, such as a server or a hosting platform. *Example:* Copying a new site version to a web host.

*Related:* pipeline; environment. *First explained in* Chapter 72<!--ref:deploy-->.

**Detached HEAD.** HEAD points directly at a commit instead of a branch.

*Technically:* A state in which HEAD contains a commit identifier rather than a symbolic reference to a branch. *Example:* HEAD detached at 9f10b43

*Related:* HEAD; branch. *First explained in* Chapter 20<!--ref:branching-->.

**Dev container.** A container set up with the tools a project needs.

*Technically:* A Docker container configured for development, described by devcontainer.json in a .devcontainer folder. *Example:* .devcontainer/devcontainer.json

*Related:* codespace; Dockerfile. *First explained in* Chapter 70<!--ref:codespaces-->.

**Diff.** A report of the differences between two versions, line by line.

*Technically:* A description of changes between two file or tree states, shown as removed (-) and added (+) lines in hunks. *Example:* git diff

*Related:* hunk; git show. *First explained in* Chapter 17<!--ref:history_view-->.

**Discussion.** An open-ended conversation about a project, kept apart from the list of issues.

*Technically:* A hosting-platform forum thread, filed in a category, used for questions, ideas, announcements and polls that are not yet tracked work. *Example:* A Q&A thread asking how to install the tool.

*Related:* issue; category. *First explained in* Chapter 48<!--ref:discussions-->.

**Distributed version control.** Every user holds a complete copy of the repository and its history.

*Technically:* A version-control architecture in which each participant has a full repository, and repositories exchange history peer to peer. *Example:* Git

*Related:* centralised version control; clone. *First explained in* Chapter 11<!--ref:distributed-->.

**Diverged.** Each branch has commits the other lacks.

*Technically:* Two branches have diverged when neither tip is an ancestor of the other, so a fast-forward is impossible. *Example:* Hours added on main while tea is added on add-tea.

*Related:* merge; fast-forward. *First explained in* Chapter 21<!--ref:merging-->.

**DNS (domain name system).** The internet's phone book: it turns names into numbers.

*Technically:* A distributed naming system that resolves domain names to IP addresses and other records. *Example:* Turning example.org into an address.

*Related:* domain name; IP address. *First explained in* Chapter 5<!--ref:internet-->.

**Docker.** A popular tool for building and running containers.

*Technically:* A platform for building container images and running containers. *Example:* A Dockerfile builds an image.

*Related:* container; Dockerfile. *First explained in* Chapter 70<!--ref:codespaces-->.

**Dockerfile.** A text file with instructions for building a container image.

*Technically:* A text file of instructions such as FROM, COPY and RUN that create a Docker image. *Example:* FROM an existing image, then RUN an install command.

*Related:* Docker; dev container. *First explained in* Chapter 70<!--ref:codespaces-->.

**Domain name.** A human-friendly name, such as example.org, for a host on the internet.

*Technically:* A hierarchical name registered in the domain name system that resolves to network addresses. *Example:* example.org

*Related:* DNS; URL. *First explained in* Chapter 5<!--ref:internet-->.

## E

**Empty commit.** A commit with a message but no file change.

*Technically:* A commit whose tree is identical to its parent's, created with --allow-empty. *Example:* Mark the start of the spring menu

*Related:* commit. *First explained in* Chapter 19<!--ref:commits-->.

**Encoding.** The rule that turns characters into bytes and back.

*Technically:* A mapping between sequences of characters and sequences of bytes used to store or transmit text. *Example:* UTF-8

*Related:* Unicode; UTF-8; mojibake. *First explained in* Chapter 4<!--ref:text-->.

**Enterprise account.** An account that manages policy and billing for many organizations.

*Technically:* An account type that centrally manages multiple organizations; it does not directly own repositories. *Example:* A large company with many organizations.

*Related:* organization. *First explained in* Chapter 68<!--ref:orgs-->.

**Environment.** A named deployment target with its own rules and secrets.

*Technically:* A named target such as staging or production, configured with protection rules, secrets and variables, that a workflow job can reference. *Example:* github-pages

*Related:* deployment; reusable workflow. *First explained in* Chapter 58<!--ref:wfadvanced-->.

**Environment variable.** A variable that programs started from the shell can read.

*Technically:* A variable exported into the environment inherited by child processes. *Example:* HOME, PATH

*Related:* variable; PATH. *First explained in* Chapter 7<!--ref:terminal-->.

**Event.** Something that happens in a repository and can start a workflow.

*Technically:* An activity in a repository, such as a push, pull request or issue, or a schedule or manual request, that triggers a workflow run. *Example:* push

*Related:* workflow. *First explained in* Chapter 54<!--ref:actions-->.

**Expression.** A small formula in a workflow that GitHub works out while running.

*Technically:* A construct written between ${{ and }} in a workflow file that GitHub evaluates using literals, operators, functions and contexts. *Example:* ${{ github.ref == 'refs/heads/main' }}

*Related:* context; workflow (GitHub Actions). *First explained in* Chapter 55<!--ref:exprs-->.

**Extension.** The letters after the last dot in a file name; a label for the kind of contents.

*Technically:* A suffix of a file name, conventionally indicating the file's format; it does not change the contents. *Example:* .html in menu.html

*Related:* file. *First explained in* Chapter 2<!--ref:files-->.

## F

**Fast-forward.** A merge that only moves a branch pointer forward.

*Technically:* A merge in which the receiving branch has not diverged, so Git moves its pointer to the source commit and creates no merge commit. *Example:* main moves to add-tea's commit.

*Related:* merge; merge commit. *First explained in* Chapter 21<!--ref:merging-->.

**Fetch.** Download new commits without changing your branches.

*Technically:* Retrieve objects and update remote-tracking branches, leaving local branches and the working tree untouched. *Example:* git fetch

*Related:* pull; remote-tracking branch. *First explained in* Chapter 23<!--ref:remotes-->.

**File.** A named collection of information kept in storage.

*Technically:* A named sequence of bytes stored in a file system, with associated metadata. *Example:* menu.html

*Related:* folder; extension; metadata. *First explained in* Chapter 2<!--ref:files-->.

**Folder (directory).** A container that holds files and other folders.

*Technically:* A file-system object that contains references to files and other directories. *Example:* sunrise-bakery

*Related:* file; path; root. *First explained in* Chapter 2<!--ref:files-->.

**Fork.** Your own hosted copy of someone else's repository.

*Technically:* A copy of a hosted repository owned by another account, connected to the original (the upstream), used to propose changes back through pull requests without write access to the original. *Example:* Your copy of an open-source project on the platform.

*Related:* clone; upstream; pull request. *First explained in* Chapter 49<!--ref:collab-->.

## G

**Garbage collection.** Git's housekeeping of stored objects.

*Technically:* git gc packs loose objects into packfiles and removes unreachable objects after a safety period. *Example:* git gc

*Related:* packfile; dangling object. *First explained in* Chapter 30<!--ref:objects-->.

**Git.** A free, open-source version-control system that runs on your computer.

*Technically:* A distributed version-control system that records the history of a project in a repository. *Example:* The program you use to record versions of sunrise-bakery.

*Related:* GitHub; repository. *First explained in* Chapter 12<!--ref:platforms-->.

**git add.** Stages files so they are part of the next commit.

*Technically:* Updates the index with the current content of the given paths. *Example:* git add notes.md

*Related:* stage; index. *First explained in* Chapter 16<!--ref:firstrepo-->.

**Git Bash.** A Bash environment for Windows that is installed with Git for Windows; it is not Git itself.

*Technically:* A terminal providing a Bash shell and Unix-style utilities on Windows, distributed with Git for Windows. *Example:* The window you open to type Git commands on Windows.

*Related:* Bash; Git; terminal. *First explained in* Chapter 7<!--ref:terminal-->.

**git branch.** Lists, creates, renames and deletes branches.

*Technically:* Manages branch references under refs/heads. *Example:* git branch add-tea

*Related:* branch; git switch. *First explained in* Chapter 20<!--ref:branching-->.

**git commit.** Records the staged snapshot with a message.

*Technically:* Creates a commit object from the index and advances the current branch. *Example:* git commit -m "Add notes"

*Related:* commit; stage. *First explained in* Chapter 16<!--ref:firstrepo-->.

**git commit --amend.** Replaces the last commit with a new one, to fix its message or add forgotten changes.

*Technically:* Creates a new commit from the index and message that replaces the tip commit; the replaced commit is left unreferenced. *Example:* git commit --amend --no-edit

*Related:* commit; reflog. *First explained in* Chapter 19<!--ref:commits-->.

**git config.** The command that reads and changes Git's settings.

*Technically:* Reads, writes and lists Git configuration values across system, global, local and worktree scopes. *Example:* git config user.email

*Related:* configuration; scope. *First explained in* Chapter 13<!--ref:install-->.

**git init.** Creates a new repository in the current folder.

*Technically:* Initialises an empty Git repository by creating the .git directory. *Example:* git init

*Related:* repository; git status. *First explained in* Chapter 16<!--ref:firstrepo-->.

**Git LFS.** A way to keep large files outside the history.

*Technically:* An extension that stores large file contents on a separate server and leaves small pointer files in the repository. *Example:* git lfs track "*.png"

*Related:* object. *First explained in* Chapter 31<!--ref:bigrepos-->.

**git log.** Shows the history of commits, newest first.

*Technically:* Lists commits reachable from the current revision in reverse chronological order, with options for format and filtering. *Example:* git log --oneline

*Related:* commit; revision. *First explained in* Chapter 17<!--ref:history_view-->.

**git mv.** Renames or moves a file and stages the change.

*Technically:* Moves a file in the working tree and index in one operation. *Example:* git mv menu.html carte.html

*Related:* git rm; rename. *First explained in* Chapter 18<!--ref:tracking-->.

**git reset.** Move the current branch to another commit.

*Technically:* Moves the current branch to a commit; --soft keeps index and working tree, the default resets the index, --hard resets both. *Example:* git reset --soft HEAD~1

*Related:* git revert; reflog. *First explained in* Chapter 25<!--ref:undo-->.

**git restore.** Bring a file back from the index or an older commit.

*Technically:* Restores content into the working tree or, with --staged, into the index, from the index or a named commit. *Example:* git restore menu.md

*Related:* git reset; index. *First explained in* Chapter 25<!--ref:undo-->.

**git revert.** Undo a commit by adding a new one.

*Technically:* Creates a new commit that applies the inverse of an earlier commit, leaving history intact. *Example:* git revert --no-edit HEAD

*Related:* git reset. *First explained in* Chapter 25<!--ref:undo-->.

**git rm.** Deletes a file and stages the deletion.

*Technically:* Removes a path from the working tree and the index; with --cached only from the index. *Example:* git rm contact.html

*Related:* git mv; git restore. *First explained in* Chapter 18<!--ref:tracking-->.

**git show.** Displays one commit: its message and changes.

*Technically:* Shows a commit's metadata and diff (or other objects). *Example:* git show HEAD~1

*Related:* git log; diff. *First explained in* Chapter 17<!--ref:history_view-->.

**git status.** Shows which files are untracked, modified or staged, and the current branch.

*Technically:* Reports the state of the working tree and index relative to HEAD; read-only. *Example:* git status

*Related:* working tree; index. *First explained in* Chapter 16<!--ref:firstrepo-->.

**git switch.** Changes the current branch.

*Technically:* Moves HEAD to another branch and updates the index and working tree to match. *Example:* git switch add-tea

*Related:* branch; HEAD. *First explained in* Chapter 20<!--ref:branching-->.

**GitHub.** A widely used online platform for hosting Git repositories and collaborating on software.

*Technically:* A hosting platform built around Git repositories with collaboration and automation features. *Example:* github.com

*Related:* Git; hosting platform. *First explained in* Chapter 12<!--ref:platforms-->.

**GitHub App.** An integration with its own limited permissions that acts on GitHub.

*Technically:* An integration that uses fine-grained permissions and short-lived tokens and is not tied to a user account. *Example:* An app that comments on pull requests.

*Related:* OAuth app; token. *First explained in* Chapter 74<!--ref:api-->.

**GitHub CLI.** A command-line program, gh, for working with GitHub.

*Technically:* GitHub's official command-line tool for pull requests, issues, releases, workflow runs, codespaces and more. *Example:* gh pr create

*Related:* Git; command line. *First explained in* Chapter 73<!--ref:ghcli-->.

**GitHub Pages.** GitHub's service for publishing a static website from a repository.

*Technically:* A static site hosting service that takes files from a repository, optionally builds them, and publishes a website. *Example:* https://ada.github.io/notes

*Related:* static site; workflow. *First explained in* Chapter 69<!--ref:pages-->.

**GitHub Sponsors.** GitHub's way of supporting open-source maintainers with money.

*Technically:* A GitHub program through which people and organizations sponsor maintainers, with additional terms and regional eligibility for those who receive funds. *Example:* A sponsor button on a repository.

*Related:* open source; FUNDING.yml. *First explained in* Chapter 75<!--ref:platformextras-->.

**GitLab.** Another hosting platform for Git repositories.

*Technically:* A hosting platform for Git repositories with collaboration and automation features. *Example:* A team's self-hosted code server.

*Related:* GitHub; hosting platform. *First explained in* Chapter 12<!--ref:platforms-->.

**Global setting.** A Git setting that applies to your user account in every repository.

*Technically:* A configuration value stored in the user's global file (~/.gitconfig) and applied to all repositories of that user. *Example:* user.name set with --global

*Related:* scope; configuration. *First explained in* Chapter 13<!--ref:install-->.

**Governance.** The written rules by which a group runs a project.

*Technically:* The decisions, roles and rules of a project or organisation, expressed on GitHub through permissions, rulesets, code owners and community files. *Example:* A CONTRIBUTING file and a ruleset.

*Related:* organization; code of conduct. *First explained in* Chapter 75<!--ref:platformextras-->.

**GraphQL.** An API where you send a query that names exactly the fields you want.

*Technically:* A query language for APIs served at one endpoint that returns the requested structure. *Example:* A query that asks for the logins of your followers.

*Related:* API; REST. *First explained in* Chapter 74<!--ref:api-->.

## H

**Hardware.** The physical parts of a computer.

*Technically:* The tangible components of a computing system, such as the processor, memory, storage devices, display and network adapter. *Example:* A solid-state drive.

*Related:* software; processor; memory; storage. *First explained in* Chapter 1<!--ref:computer-->.

**Hash (commit identifier).** The long code that uniquely identifies a commit.

*Technically:* A cryptographic hash of an object's content, used as its identifier; usually abbreviated. *Example:* c3c1c38

*Related:* commit; branch. *First explained in* Chapter 15<!--ref:model-->.

**HEAD.** The pointer that says which commit you are currently on.

*Technically:* A reference, normally symbolic, to the current branch or commit; the parent of the next commit. *Example:* HEAD -> main

*Related:* branch; commit. *First explained in* Chapter 15<!--ref:model-->.

**Hidden file.** A file that ordinary listings do not show unless asked.

*Technically:* A file whose name (on Unix-like systems, a leading dot) or attribute marks it to be omitted from default listings. *Example:* .git, .gitignore

*Related:* file; .git. *First explained in* Chapter 2<!--ref:files-->.

**History.** The recorded sequence of versions of a project, with reasons and authors.

*Technically:* The ordered record of a project's versions together with metadata such as author, date and description. *Example:* Every recorded change to the bakery menu.

*Related:* version; version control. *First explained in* Chapter 9<!--ref:problem-->.

**HMAC.** A fingerprint that only someone with a secret key can produce.

*Technically:* A keyed hash message authentication code, here HMAC-SHA-256, used to check that a message is genuine and unaltered. *Example:* The X-Hub-Signature-256 header of a webhook delivery.

*Related:* webhook; checksum. *First explained in* Chapter 74<!--ref:api-->.

**Home folder.** The folder that belongs to your user account.

*Technically:* The directory assigned to a user account for that user's files and settings; often written ~ in a shell. *Example:* /home/learner

*Related:* path; folder. *First explained in* Chapter 2<!--ref:files-->.

**Hook.** A script Git runs at a fixed moment.

*Technically:* A script in .git/hooks that Git runs at a specific moment, such as before a commit; a failing exit status stops the operation. *Example:* .git/hooks/pre-commit

*Related:* configuration. *First explained in* Chapter 32<!--ref:custom-->.

**Hosting platform.** An online service that stores shared repositories and adds collaboration features.

*Technically:* A web service providing remote repository storage and collaboration tools such as issue tracking and review. *Example:* GitHub, GitLab, Bitbucket

*Related:* Git; remote. *First explained in* Chapter 12<!--ref:platforms-->.

**HTML.** A text format that marks up web pages so a browser knows how to show them.

*Technically:* HyperText Markup Language: a markup language using tags to describe the structure of a web page. *Example:* <h1>Sunrise Bakery</h1>

*Related:* CSS; web page. *First explained in* Chapter 3<!--ref:editors-->.

**HTTP.** The rules web clients and servers follow to exchange requests and replies.

*Technically:* HyperText Transfer Protocol: an application-layer protocol of requests and responses carrying methods, status codes, headers and bodies. *Example:* Status 200 OK.

*Related:* HTTPS; server; client. *First explained in* Chapter 5<!--ref:internet-->.

**HTTPS.** HTTP with encryption and a check of the server's identity.

*Technically:* HTTP carried over an encrypted, authenticated TLS connection. *Example:* https://example.org

*Related:* HTTP; authentication. *First explained in* Chapter 5<!--ref:internet-->.

**Hunk.** One contiguous chunk of changes in a diff.

*Technically:* A group of adjacent changed lines with context in a unified diff, introduced by an @@ header. *Example:* @@ -1,4 +1,4 @@

*Related:* diff. *First explained in* Chapter 17<!--ref:history_view-->.

## I

**Ignored file.** A file Git has been told to leave alone.

*Technically:* A file matching an ignore pattern that Git omits from untracked listings and from git add of directories. *Example:* build.log

*Related:* .gitignore; untracked file. *First explained in* Chapter 18<!--ref:tracking-->.

**Index (staging area).** The holding area that lists exactly what the next commit will contain.

*Technically:* Git's staging area (index): a file in .git recording the content that will form the next commit. *Example:* Files after git add.

*Related:* stage; commit. *First explained in* Chapter 15<!--ref:model-->.

**Installer.** A file or program that puts an application on your computer.

*Technically:* A program or package that copies an application's files to the correct locations and registers it with the operating system. *Example:* A Git setup file downloaded from the maker's site.

*Related:* package manager; administrator. *First explained in* Chapter 1<!--ref:computer-->.

**Internet.** The worldwide system of connected networks.

*Technically:* The global interconnection of networks that use common protocols to exchange data. *Example:* The connection between your laptop and a server in another country.

*Related:* web; network. *First explained in* Chapter 5<!--ref:internet-->.

**IP address.** A number that identifies a computer on a network.

*Technically:* A numeric identifier assigned to a network interface, used to route packets. *Example:* 127.0.0.1 means this computer.

*Related:* DNS; network. *First explained in* Chapter 5<!--ref:internet-->.

**Issue.** A numbered item where a problem, idea or task is written down and discussed.

*Technically:* A tracked item in a hosted repository with a title, description, discussion and open or closed state, identified by a number unique within the repository. *Example:* Issue #12: rolls price is wrong.

*Related:* pull request; label; milestone. *First explained in* Chapter 44<!--ref:issues-->.

**Issue form.** A form, defined in a file, that guides people to write a useful issue.

*Technically:* A YAML template stored under .github/ISSUE_TEMPLATE that defines input fields whose values are converted into a Markdown issue. *Example:* .github/ISSUE_TEMPLATE/bug.yml

*Related:* issue; YAML. *First explained in* Chapter 44<!--ref:issues-->.

**Iteration.** A block of time in which a team plans to finish some work.

*Technically:* A repeating, fixed-length period of planned work; in GitHub Projects, a field type that groups items by such periods. *Example:* A two-week iteration.

*Related:* project. *First explained in* Chapter 47<!--ref:projects-->.

## J

**Job.** A group of steps that run together on one machine.

*Technically:* A set of steps in a workflow executed on the same runner; jobs run in parallel unless one declares a dependency on another. *Example:* check

*Related:* workflow; step; runner. *First explained in* Chapter 54<!--ref:actions-->.

## K

**Key pair.** A shareable public key and a private key that never leaves your computer.

*Technically:* A matched public/private cryptographic key pair in which data signed or locked with one key is verified or unlocked with the other. *Example:* An SSH key pair.

*Related:* SSH; authentication. *First explained in* Chapter 6<!--ref:accounts-->.

## L

**Least privilege.** Giving only the access that is needed, and no more.

*Technically:* A design principle that grants a subject the minimum permissions required for its task. *Example:* A token that can read one project only.

*Related:* authorization; token. *First explained in* Chapter 6<!--ref:accounts-->.

**Licence.** A written permission that says what others may do with a work.

*Technically:* A document in which the rights holder grants permissions, subject to conditions and with stated limitations. *Example:* A LICENSE file in the root of a repository.

*Related:* copyright; open source. *First explained in* Chapter 65<!--ref:licences-->.

**Lightweight tag.** A tag that is just a name.

*Technically:* A tag that is only a reference to a commit, with no tagger, date or message of its own. *Example:* git tag v0.1

*Related:* tag; annotated tag. *First explained in* Chapter 24<!--ref:stash-->.

**Line ending (newline).** The invisible character or characters that end a line of text.

*Technically:* A control character sequence marking a line break: LF on Unix-like systems, CRLF traditionally on Windows. *Example:* \n (LF) or \r\n (CRLF)

*Related:* plain text; whitespace. *First explained in* Chapter 4<!--ref:text-->.

**Local.** On the computer you are using.

*Technically:* Residing on, or executing on, the machine at hand rather than reached over a network. *Example:* A file in your sharif-git-lab folder.

*Related:* remote. *First explained in* Chapter 5<!--ref:internet-->.

**Local repository.** The complete history, kept in the hidden .git folder on your computer.

*Technically:* The .git directory holding a project's objects, references and configuration. *Example:* sunrise-bakery/.git

*Related:* repository; working tree. *First explained in* Chapter 15<!--ref:model-->.

**Lock.** A marker that stops others from changing a file until you release it.

*Technically:* A mechanism preventing concurrent modification of a resource by others. *Example:* Checking out a file exclusively.

*Related:* merge. *First explained in* Chapter 10<!--ref:history-->.

**Lock file.** A file that records the exact versions chosen.

*Technically:* A file generated by a package manager pinning resolved versions. *Example:* A file that fixes each package to one version.

*Related:* manifest. *First explained in* Chapter 62<!--ref:ghsec-->.

## M

**Machine user.** A user account made for automation instead of a person.

*Technically:* A user account created to automate activity, such as continuous integration. *Example:* An account a build system uses.

*Related:* user account; bot. *First explained in* Chapter 68<!--ref:orgs-->.

**Maintainer.** A person who looks after a project and decides what is merged.

*Technically:* A person who reviews and merges changes, triages issues and manages releases of a project. *Example:* The person who approves a pull request.

*Related:* contributor; pull request. *First explained in* Chapter 64<!--ref:oss-->.

**Manifest.** A file that lists the packages a project needs.

*Technically:* A dependency definition file read by package managers and by GitHub's dependency graph. *Example:* A file that names packages and version ranges.

*Related:* lock file; dependency graph. *First explained in* Chapter 62<!--ref:ghsec-->.

**Markdown.** A way of writing formatted text using plain-text marks.

*Technically:* A lightweight markup language whose plain-text syntax is converted to structured documents such as HTML. *Example:* # Heading, *emphasis*

*Related:* renderer; CommonMark; plain text. *First explained in* Chapter 8<!--ref:markdown-->.

**Matrix.** A way to run the same job in several configurations.

*Technically:* A job strategy that defines variables with lists of values and runs the job once for each combination. *Example:* Three versions on two systems gives six jobs.

*Related:* job; workflow (GitHub Actions). *First explained in* Chapter 56<!--ref:workflows_practice-->.

**Memory (RAM).** Fast, temporary working space that is emptied when the power goes off.

*Technically:* Random-access memory: volatile, fast storage used for the data and instructions a computer is currently using. *Example:* The words you have typed but not yet saved.

*Related:* storage; processor. *First explained in* Chapter 1<!--ref:computer-->.

**Merge.** To combine two sets of changes into one.

*Technically:* The operation of integrating changes from two lines of work into a single version. *Example:* Joining Alice's cake addition and Bob's price change.

*Related:* branch; conflict. *First explained in* Chapter 10<!--ref:history-->.

**Merge commit.** A commit that joins two lines of work.

*Technically:* A commit with two or more parents, recording where lines of work were combined. *Example:* Merge branch 'add-tea'.

*Related:* merge; diverged. *First explained in* Chapter 21<!--ref:merging-->.

**Merge conflict.** Git cannot combine two changes by itself.

*Technically:* A situation in which both sides changed the same part of a file differently, so Git stops the merge and asks the user to decide. *Example:* Two branches set the white loaf price differently.

*Related:* merge; conflict markers. *First explained in* Chapter 22<!--ref:conflicts-->.

**Metadata.** Information about a file, such as its size, dates, owner and permissions.

*Technically:* Attributes a file system records about a file separately from the file's contents. *Example:* The size and last-changed date shown in a detailed listing.

*Related:* file; permission. *First explained in* Chapter 2<!--ref:files-->.

**Mixed content.** An HTTPS page that loads some of its parts over plain HTTP.

*Technically:* Assets such as images, style sheets or scripts referenced with http:// from a page served over HTTPS. *Example:* An image with a src that begins http://

*Related:* HTTPS; static site. *First explained in* Chapter 69<!--ref:pages-->.

**mkdir.** Creates a new folder.

*Technically:* Make directory: creates directories; -p also creates missing parent directories. *Example:* mkdir -p sunrise-bakery/css

*Related:* cd; rmdir. *First explained in* Chapter 7<!--ref:terminal-->.

**Mojibake.** Garbled text caused by reading with the wrong encoding.

*Technically:* Incorrect characters displayed when bytes are decoded using an encoding different from the one used to encode them. *Example:* cafÃ© instead of café

*Related:* encoding; UTF-8. *First explained in* Chapter 4<!--ref:text-->.

## N

**Network.** Computers connected so that they can exchange information.

*Technically:* A set of computing devices linked by communication channels. *Example:* Your home Wi-Fi network.

*Related:* internet. *First explained in* Chapter 5<!--ref:internet-->.

**Notification.** A message from a platform that something happened where you are subscribed.

*Technically:* An update delivered to a notifications inbox, a mobile app or email because of activity in a conversation or repository to which a user is subscribed. *Example:* A message that someone commented on your pull request.

*Related:* subscription; watching; inbox. *First explained in* Chapter 41<!--ref:notify-->.

## O

**OAuth app.** An integration that acts with the permissions a user gives it.

*Technically:* An app that a user authorises to act on GitHub within granted scopes; generally less preferred than a GitHub App. *Example:* A third-party tool you sign in to with GitHub.

*Related:* GitHub App; token. *First explained in* Chapter 74<!--ref:api-->.

**Object.** Any item in Git's database.

*Technically:* One of the four kinds of stored item in Git's object database: blob, tree, commit or tag, each named by a hash. *Example:* a commit

*Related:* blob; tree. *First explained in* Chapter 30<!--ref:objects-->.

**OIDC.** A way for a workflow to get a short-lived cloud credential instead of storing a long-lived secret.

*Technically:* OpenID Connect: the workflow requests a short-lived access token from a cloud provider that trusts GitHub. *Example:* A deployment job that receives a token valid for one job.

*Related:* secret; token. *First explained in* Chapter 60<!--ref:wfsec-->.

**Open source.** Software whose code is public and whose licence lets others use, change and share it.

*Technically:* Software distributed under a licence that grants permissions to use, study, modify and redistribute the source. *Example:* A library with a licence file that permits reuse.

*Related:* licence; public repository. *First explained in* Chapter 64<!--ref:oss-->.

**Operating system (OS).** The main software that manages the computer, its files and the other programs.

*Technically:* System software that manages hardware resources, provides services such as file storage and process scheduling, and hosts applications. *Example:* Windows, macOS, Linux.

*Related:* application; hardware; distribution. *First explained in* Chapter 1<!--ref:computer-->.

**Option (flag).** A word that changes how a command behaves.

*Technically:* A command-line parameter, usually prefixed with one or two dashes, that modifies a command's behaviour. *Example:* -l in ls -l

*Related:* command; argument. *First explained in* Chapter 7<!--ref:terminal-->.

**Organization.** A shared GitHub account that a group of people use to own repositories together.

*Technically:* An account type that can own repositories, packages and projects; people access it through their own user accounts and hold roles in it. *Example:* A company account with several teams.

*Related:* team; enterprise account. *First explained in* Chapter 68<!--ref:orgs-->.

**Outside collaborator.** Someone who is not a member of an organization but has access to some of its repositories.

*Technically:* A person given access to specific repositories of an organization without being a member. *Example:* A contractor.

*Related:* organization; base permission. *First explained in* Chapter 68<!--ref:orgs-->.

**Override.** To replace a setting's value for one command or one shell.

*Technically:* To supply a value that takes precedence over stored configuration, for example with git -c or an environment variable. *Example:* git -c commit.gpgsign=false commit

*Related:* scope; configuration. *First explained in* Chapter 14<!--ref:config-->.

## P

**Package.** Software prepared so that a tool can install it.

*Technically:* A versioned, packaged unit of software distributed through a registry and installed by a package manager. *Example:* @ada/wordcount version 0.1.0

*Related:* registry; package manager. *First explained in* Chapter 71<!--ref:packages-->.

**Package manager.** A program that installs and updates applications from a trusted collection.

*Technically:* A tool that resolves, retrieves, installs, updates and removes software packages from configured repositories. *Example:* apt on Ubuntu.

*Related:* installer; application. *First explained in* Chapter 1<!--ref:computer-->.

**Packfile.** One file holding many objects compactly.

*Technically:* A file that stores many objects together, using differences between similar objects; created by git gc and by network transfers. *Example:* .git/objects/pack

*Related:* garbage collection; object. *First explained in* Chapter 30<!--ref:objects-->.

**Pagination.** Splitting a long list of results into pages.

*Technically:* Returning results in subsets with links (the Link header) to further pages. *Example:* 30 issues per page by default.

*Related:* API; rate limit. *First explained in* Chapter 74<!--ref:api-->.

**Password.** A secret string you present to prove you own an account.

*Technically:* A memorised secret used as a credential in authentication. *Example:* A long passphrase of unrelated words.

*Related:* password manager; two-factor authentication. *First explained in* Chapter 6<!--ref:accounts-->.

**Password manager.** An application that stores all your passwords securely and fills them in.

*Technically:* Software that keeps credentials in an encrypted vault protected by a master secret. *Example:* An app protected by one strong master password.

*Related:* password. *First explained in* Chapter 6<!--ref:accounts-->.

**Patch.** A text file that describes a change.

*Technically:* A text file describing changes to files so that they can be applied elsewhere, for example with git apply or git am. *Example:* 0001-Add-tea.patch

*Related:* diff; cherry-pick. *First explained in* Chapter 28<!--ref:tools-->.

**Path.** A written description of where a file or folder is in the tree.

*Technically:* A sequence of directory names, separated by a separator character, identifying a location in a file system. *Example:* css/style.css

*Related:* absolute path; relative path. *First explained in* Chapter 2<!--ref:files-->.

**PATH (environment variable).** The list of folders the shell searches for programs.

*Technically:* An environment variable containing an ordered list of directories searched to resolve command names. Not to be confused with a file path. *Example:* A tool in a folder not on PATH gives 'command not found'.

*Related:* environment variable; command; path. *First explained in* Chapter 7<!--ref:terminal-->.

**Permission.** A rule about who may read, change or run a file.

*Technically:* An access-control attribute governing read, write and execute rights of users on a file or directory. *Example:* -rw-r--r-- on a text file

*Related:* administrator; metadata. *First explained in* Chapter 2<!--ref:files-->.

**Permissive licence.** A licence that asks only for credit and notices.

*Technically:* A licence whose main condition is preserving copyright and licence notices; derived works may use other terms. *Example:* MIT and BSD licences.

*Related:* copyleft; licence. *First explained in* Chapter 65<!--ref:licences-->.

**Phishing.** Tricking someone into giving away a secret by pretending to be trusted.

*Technically:* A social-engineering attack that impersonates a trusted party to obtain credentials or induce harmful actions. *Example:* An urgent email with a link to a lookalike site.

*Related:* password; account. *First explained in* Chapter 6<!--ref:accounts-->.

**Pipeline.** The ordered steps a change goes through automatically.

*Technically:* An ordered sequence of automated stages, such as lint, test, build and deploy, in which a failure normally stops later stages. *Example:* Lint, then test, then build.

*Related:* continuous integration; exit code. *First explained in* Chapter 52<!--ref:cicd-->.

**Plain text.** Information stored as ordinary characters with no fonts, colours or layout.

*Technically:* A sequence of encoded characters with no formatting metadata, stored as bytes according to a character encoding. *Example:* A .txt or .md file.

*Related:* text editor; binary file. *First explained in* Chapter 3<!--ref:editors-->.

**Pre-release.** A release marked as not yet final.

*Technically:* A release flagged as a pre-release, for example a beta. *Example:* v1.3.2 (beta)

*Related:* release. *First explained in* Chapter 66<!--ref:releases-->.

**Processor (CPU).** The part that carries out instructions.

*Technically:* The central processing unit: the hardware component that executes program instructions. *Example:* The chip that runs your browser's instructions.

*Related:* memory; hardware. *First explained in* Chapter 1<!--ref:computer-->.

**Project.** A table, board or roadmap for planning work across issues and pull requests.

*Technically:* A hosting-platform planning tool that presents issues, pull requests and draft items in table, board and roadmap layouts with custom fields, filters and automation. *Example:* A board with the columns Todo, In progress and Done.

*Related:* issue; pull request; iteration. *First explained in* Chapter 47<!--ref:projects-->.

**Prompt.** The text the shell shows when it is waiting for you to type.

*Technically:* A string printed by the shell to indicate readiness for input. *Example:* $ 

*Related:* shell; command. *First explained in* Chapter 7<!--ref:terminal-->.

**Pull.** Fetch, then merge into your current branch.

*Technically:* git fetch followed by integrating the upstream branch into the current branch, by default with a merge. *Example:* git pull

*Related:* fetch; merge. *First explained in* Chapter 23<!--ref:remotes-->.

**Pull request.** A proposal to merge one branch into another, with a place to discuss it first.

*Technically:* A hosting-platform feature that records a request to merge a compare branch into a base branch and collects discussion, reviews and automated check results; it is not a Git object. *Example:* A pull request from add-tea into main.

*Related:* branch; merge; review. *First explained in* Chapter 45<!--ref:pr-->.

**Push protection.** A block that stops a push containing a secret.

*Technically:* A secret scanning feature that rejects pushes with detected secrets before they reach the repository. *Example:* A refused push with a message naming the secret type.

*Related:* secret scanning; secret. *First explained in* Chapter 62<!--ref:ghsec-->.

**pwd.** Prints the folder you are currently in.

*Technically:* Print working directory: outputs the absolute path of the current directory. *Example:* /home/learner

*Related:* current directory; cd. *First explained in* Chapter 7<!--ref:terminal-->.

## R

**Rate limit.** A cap on how many requests you may make in a period.

*Technically:* A limit on API requests within a time window, reported in response headers. *Example:* The X-RateLimit-Remaining header.

*Related:* API. *First explained in* Chapter 74<!--ref:api-->.

**README.** A file that introduces a project to the people who arrive at it.

*Technically:* A documentation file, conventionally named README.md, placed at the root (or in a .github or docs folder) of a repository and displayed on its front page by hosting platforms. *Example:* README.md

*Related:* repository; markdown; topic. *First explained in* Chapter 42<!--ref:readme-->.

**Rebase.** Replay your commits on top of another commit.

*Technically:* Reapply the commits of a branch, one by one, on a new base, producing new commits with new hashes. *Example:* git rebase main

*Related:* merge; squash. *First explained in* Chapter 27<!--ref:rebase-->.

**Ref.** A name that points to an object.

*Technically:* A named pointer, stored as a small file under .git/refs, holding a hash or another ref's name; branches and tags are refs. *Example:* refs/heads/main

*Related:* branch; tag. *First explained in* Chapter 30<!--ref:objects-->.

**Reflog.** Git's private diary of where HEAD has been.

*Technically:* A local, temporary log of the positions of HEAD and each branch, used to recover commits that are no longer reachable. *Example:* git reflog

*Related:* HEAD; git reset. *First explained in* Chapter 26<!--ref:reflog-->.

**Registry.** A place that stores packages for download.

*Technically:* A service that hosts packages and serves them to package managers. *Example:* GitHub's npm registry.

*Related:* package; package manager. *First explained in* Chapter 71<!--ref:packages-->.

**Relative path.** A path that starts from where you are now.

*Technically:* A path interpreted relative to the current working directory. *Example:* ../images/logo.svg

*Related:* absolute path; current directory. *First explained in* Chapter 2<!--ref:files-->.

**Release.** A named, downloadable version of a project on GitHub.

*Technically:* A GitHub page built on a Git tag, with a title, notes and attached files. *Example:* Release v1.2.0 with a zip file and a notes page.

*Related:* tag; release notes. *First explained in* Chapter 66<!--ref:releases-->.

**Release notes.** A description of what changed in a release.

*Technically:* Text attached to a release, written by hand or generated from merged pull requests. *Example:* A list of merged pull requests and contributors.

*Related:* release; changelog. *First explained in* Chapter 66<!--ref:releases-->.

**Remote.** On a different computer, reached over a network.

*Technically:* Residing on another machine, accessed through a network connection. *Example:* A page on example.org; later, a repository on GitHub.

*Related:* local; server. *First explained in* Chapter 5<!--ref:internet-->.

**Remote-tracking branch.** Your note of where a remote branch was when you last looked.

*Technically:* A read-only local reference such as origin/main that Git updates on fetch, pull and push. *Example:* origin/main

*Related:* remote; upstream branch. *First explained in* Chapter 23<!--ref:remotes-->.

**Renderer.** A program that turns marked-up text into a formatted result.

*Technically:* Software that parses a markup language and produces a presentation, such as HTML, from it. *Example:* The preview in your editor.

*Related:* Markdown. *First explained in* Chapter 8<!--ref:markdown-->.

**Repository.** A project together with the complete record of its history.

*Technically:* A store containing a project's files and the full history of changes to them; in Git, the project folder plus its .git directory. *Example:* The sunrise-bakery folder after Git is started in it.

*Related:* clone; version control. *First explained in* Chapter 11<!--ref:distributed-->.

**rerere.** Git remembers how you resolved a conflict.

*Technically:* A feature (reuse recorded resolution) that records a conflict resolution and applies it when the same conflict recurs. *Example:* git config rerere.enabled true

*Related:* merge conflict. *First explained in* Chapter 32<!--ref:custom-->.

**REST.** A style of API where each kind of thing has an address and you ask with HTTP requests.

*Technically:* An API style organised by resources addressed with URLs and HTTP methods, returning structured responses. *Example:* GET /repos/OWNER/REPO/issues

*Related:* API; GraphQL. *First explained in* Chapter 74<!--ref:api-->.

**Reusable workflow.** A workflow that other workflows can call as a whole.

*Technically:* A workflow whose on key includes workflow_call, so that a job in another workflow can run it using the uses keyword, passing inputs and secrets. *Example:* A shared deploy workflow.

*Related:* workflow (GitHub Actions); environment. *First explained in* Chapter 58<!--ref:wfadvanced-->.

**Revision.** Any way of naming a commit: a hash, a branch name, HEAD, HEAD~2.

*Technically:* A specifier that resolves to a commit (or other object), as defined by Git's revision syntax. *Example:* HEAD~1

*Related:* hash; HEAD. *First explained in* Chapter 17<!--ref:history_view-->.

**Rollback.** Going back to the previous working version.

*Technically:* Restoring the previously deployed version after a failed or faulty deployment. *Example:* Pointing the current link back at the old release folder.

*Related:* deployment; release. *First explained in* Chapter 72<!--ref:deploy-->.

**Root.** The top folder of a tree; everything else is inside it.

*Technically:* The topmost directory of a file-system hierarchy, written / on Unix-like systems. *Example:* /

*Related:* path; folder. *First explained in* Chapter 2<!--ref:files-->.

**Ruleset.** A named list of rules that a platform enforces on branches or tags.

*Technically:* A set of rules applied by a hosting platform to selected branches or tags, layered with other rulesets so that the most restrictive version of each rule applies. *Example:* A ruleset that blocks force pushes to release branches.

*Related:* branch protection rule. *First explained in* Chapter 50<!--ref:protect-->.

**Runner.** The machine that runs a job.

*Technically:* A virtual machine or container, hosted by the platform or by the user, that executes the jobs of a workflow. *Example:* ubuntu-latest

*Related:* job; workflow. *First explained in* Chapter 54<!--ref:actions-->.

## S

**Scope.** The level at which a setting is stored: system, global, local or worktree.

*Technically:* The configuration file level (system, global, local, worktree) at which a value is stored, determining its reach and precedence. *Example:* A local value beats a global one in that repository.

*Related:* configuration; override. *First explained in* Chapter 14<!--ref:config-->.

**Script injection.** Someone else's text becoming part of your script and being run.

*Technically:* An attack in which untrusted input is substituted into the text of a script so that it is interpreted as commands. *Example:* A pull request title that closes a quotation and adds a command.

*Related:* least privilege; workflow. *First explained in* Chapter 60<!--ref:wfsec-->.

**Secret.** A value that gives access if someone else has it.

*Technically:* A password, token, API key, private key or file containing them, which gives access to a system when held by someone else. *Example:* API_KEY=...

*Related:* credential helper. *First explained in* Chapter 33<!--ref:gitsec-->.

**Security advisory.** A published notice about a vulnerability and its fix.

*Technically:* A report describing a vulnerability, affected versions and fixed versions, drafted privately and then published. *Example:* An advisory with a CVE number.

*Related:* CVE; SECURITY.md. *First explained in* Chapter 62<!--ref:ghsec-->.

**Self-hosted runner.** A machine you run yourself to do the jobs of a workflow.

*Technically:* A machine deployed and maintained by the user that executes GitHub Actions jobs instead of a machine provided by the platform. *Example:* A server in your own office.

*Related:* runner; security. *First explained in* Chapter 59<!--ref:runners-->.

**Semantic versioning.** A convention for MAJOR.MINOR.PATCH release numbers.

*Technically:* A versioning convention in which MAJOR changes for incompatible changes, MINOR for compatible additions and PATCH for compatible fixes; a hyphenated label marks a pre-release. *Example:* v1.4.2

*Related:* tag. *First explained in* Chapter 29<!--ref:tags-->.

**Server.** A computer or program that answers requests.

*Technically:* A process (or the computer running it) that listens for and responds to requests from clients. *Example:* The program that sends you a web page.

*Related:* client; remote. *First explained in* Chapter 5<!--ref:internet-->.

**Shallow clone.** A clone with only the recent history.

*Technically:* A clone limited to a given number of recent commits, with older history cut off (grafted) until fetched. *Example:* git clone --depth 1

*Related:* clone. *First explained in* Chapter 31<!--ref:bigrepos-->.

**Shell.** The program that reads your commands and has them carried out.

*Technically:* A command interpreter that reads input, parses commands and asks the operating system to execute them. *Example:* Bash, zsh, PowerShell.

*Related:* terminal; command. *First explained in* Chapter 7<!--ref:terminal-->.

**Sign-off.** A line in a commit message saying the author has the right to submit the change.

*Technically:* A Signed-off-by trailer added with git commit -s; it is text, not a cryptographic signature. *Example:* Signed-off-by: Ada Learner <ada@example.org>

*Related:* signed commit; trailer. *First explained in* Chapter 64<!--ref:oss-->.

**Signed commit.** A commit that carries a verifiable signature.

*Technically:* A commit carrying a cryptographic signature made with the author's private key, which others can check against the public key. *Example:* git commit -S

*Related:* commit. *First explained in* Chapter 33<!--ref:gitsec-->.

**Single point of failure.** A part whose failure stops everything or loses something irreplaceable.

*Technically:* A component in a system whose failure causes the entire system to fail. *Example:* A single central server with no backup.

*Related:* centralised version control. *First explained in* Chapter 11<!--ref:distributed-->.

**Snapshot.** A complete picture of all the files of a project at one moment.

*Technically:* The state of the tracked files at a point in time, as recorded by a commit's tree. *Example:* The whole bakery site as it was when you committed.

*Related:* commit; working tree. *First explained in* Chapter 15<!--ref:model-->.

**Software.** Instructions that tell hardware what to do.

*Technically:* Programs and data that direct the operation of hardware. *Example:* A web browser.

*Related:* application; operating system; hardware. *First explained in* Chapter 1<!--ref:computer-->.

**Software project.** The folder of files that makes up one piece of work.

*Technically:* A set of files, typically under one directory, that together form a program, website, document set or tool. *Example:* sunrise-bakery

*Related:* source code; folder. *First explained in* Chapter 3<!--ref:editors-->.

**Source archive.** A zip or tar file of the files at a tag, without history.

*Technically:* An archive of a tagged commit's tree, made by GitHub for each release or locally with git archive. *Example:* proj-1.0.0.tar.gz

*Related:* tag; release. *First explained in* Chapter 66<!--ref:releases-->.

**Source code (source files).** The human-written files from which a project is made.

*Technically:* Human-readable files that specify a program, website or document set and from which deliverables are produced. *Example:* index.html, style.css

*Related:* software project. *First explained in* Chapter 3<!--ref:editors-->.

**SPDX identifier.** A short standard name for a licence.

*Technically:* A short identifier from the SPDX licence list, such as MIT or Apache-2.0. *Example:* CC-BY-NC-SA-4.0

*Related:* licence. *First explained in* Chapter 65<!--ref:licences-->.

**Squash.** Turn many commits into one.

*Technically:* Combine the changes of several commits into a single new commit, leaving no link to the originals. *Example:* git merge --squash add-juice.

*Related:* merge commit. *First explained in* Chapter 21<!--ref:merging-->.

**SSH (Secure Shell).** A secure way to connect to another computer, which can use a key pair to prove your identity.

*Technically:* A cryptographic network protocol for secure remote login and command execution, supporting public-key authentication. *Example:* Connecting to a server without sending a password.

*Related:* key pair; remote. *First explained in* Chapter 6<!--ref:accounts-->.

**Stage.** To add a file's current contents to the index so the next commit includes them.

*Technically:* To record a file's current state in the index (git add). *Example:* git add menu.md

*Related:* index; commit. *First explained in* Chapter 15<!--ref:model-->.

**Staging.** A practice copy of production where you deploy first.

*Technically:* An environment that mirrors production and is used to check a release before it goes live. *Example:* A staging site that the team can test.

*Related:* environment; deployment. *First explained in* Chapter 72<!--ref:deploy-->.

**Stash.** A shelf for unfinished changes.

*Technically:* A stack of saved working-tree and index states that lets you return to a clean tree and reapply the changes later. *Example:* git stash

*Related:* working tree. *First explained in* Chapter 24<!--ref:stash-->.

**Static site.** A website made of files that are sent to the browser exactly as they are.

*Technically:* A site consisting of HTML, CSS and JavaScript files served without server-side code generating each page. *Example:* A bakery page with a few HTML files.

*Related:* GitHub Pages; server. *First explained in* Chapter 69<!--ref:pages-->.

**Step.** One task inside a job.

*Technically:* A single command (run) or action (uses) executed in order within a job, in its own process. *Example:* run: sh ci.sh

*Related:* job; action. *First explained in* Chapter 54<!--ref:actions-->.

**Storage.** Slower, permanent space that keeps information when the power is off.

*Technically:* Non-volatile data storage, such as a solid-state drive or hard disk, that retains data without power. *Example:* A saved document.

*Related:* memory; file. *First explained in* Chapter 1<!--ref:computer-->.

**Submodule.** A repository pinned inside another repository.

*Technically:* A repository at a fixed path in another repository; the outer one records one commit of the inner one (mode 160000), described in .gitmodules. *Example:* vendor/lib

*Related:* repository. *First explained in* Chapter 31<!--ref:bigrepos-->.

**Subscription.** An arrangement to be told about activity in one conversation or repository.

*Technically:* A recorded preference that causes a platform to send notifications about a specific conversation or repository to a user until the user unsubscribes. *Example:* Commenting on an issue subscribes you to it.

*Related:* notification; watching. *First explained in* Chapter 41<!--ref:notify-->.

**Supply chain.** Everything your software is made from and built with.

*Technically:* The code, dependencies, tools, build systems and people involved in producing software. *Example:* A dependency that an attacker changes.

*Related:* dependency graph; Dependabot. *First explained in* Chapter 63<!--ref:secpractice-->.

**Symbolic link.** A file that points to another file or folder.

*Technically:* A file-system entry that names another path; reading through it reads the target. *Example:* current pointing to releases/v1

*Related:* path; deployment. *First explained in* Chapter 72<!--ref:deploy-->.

**Synchronised (cloud) folder.** A folder whose contents are kept the same across computers or an online service.

*Technically:* A directory whose contents are replicated automatically between devices or a service. *Example:* A folder that appears on your laptop and phone.

*Related:* backup; version control. *First explained in* Chapter 9<!--ref:problem-->.

**Synopsis.** The short line showing how to write a command.

*Technically:* The compact notation at the start of a command's usage or manual page that shows its options and arguments, with brackets for optional parts and angle brackets for placeholders. *Example:* git tag -d <tagname>...

*Related:* command; option. *First explained in* Chapter 35<!--ref:readdocs-->.

**Syntax highlighting.** Colouring parts of text according to their role so the structure is easy to see.

*Technically:* Display of tokens of structured text in different colours or styles according to their syntactic category. *Example:* Tags in HTML shown in one colour and words in another.

*Related:* code editor. *First explained in* Chapter 3<!--ref:editors-->.

## T

**Tag.** A fixed name for one commit.

*Technically:* A reference that names a commit and, unlike a branch, does not move when new commits are made. *Example:* v1.0

*Related:* branch; annotated tag. *First explained in* Chapter 24<!--ref:stash-->.

**Tag object.** The object an annotated tag creates.

*Technically:* An object naming another object with a type, tag name, tagger and message. *Example:* git cat-file -p v1.0

*Related:* annotated tag; ref. *First explained in* Chapter 30<!--ref:objects-->.

**Team.** A named group of people in an organization that shares access and mentions.

*Technically:* A group of organization members used to grant repository access and to mention people together; teams can be nested. *Example:* A documentation team.

*Related:* organization. *First explained in* Chapter 68<!--ref:orgs-->.

**Telemetry.** Usage information a program sends back to its maker.

*Technically:* Data about how software is used, collected and sent by the software, which may be inspected or disabled where the software allows. *Example:* GH_TELEMETRY=log prints what gh would send.

*Related:* GitHub CLI; privacy. *First explained in* Chapter 73<!--ref:ghcli-->.

**Terminal.** A window in which you type commands and read text replies.

*Technically:* A text-based interface (terminal emulator) through which a user interacts with a shell. *Example:* The Terminal application or Git Bash window.

*Related:* shell; prompt; command. *First explained in* Chapter 7<!--ref:terminal-->.

**Text editor.** A program for creating and changing plain text files.

*Technically:* An application that edits plain text without adding formatting information. *Example:* Any editor that saves only characters.

*Related:* code editor; word processor; plain text. *First explained in* Chapter 3<!--ref:editors-->.

**Token.** A limited stand-in for a password; still a secret.

*Technically:* A credential string that grants specified, often time-limited, permissions to its holder. *Example:* A personal access token used by a tool.

*Related:* password; least privilege. *First explained in* Chapter 6<!--ref:accounts-->.

**Topic.** A short label that helps people find a repository.

*Technically:* A lowercase label attached to a hosted repository to classify its purpose, subject area, community or language, and to enable search and browsing by that label. *Example:* static-site

*Related:* README; repository. *First explained in* Chapter 42<!--ref:readme-->.

**touch.** Creates an empty file, or updates a file's last-changed time.

*Technically:* Creates an empty file if it does not exist, or updates its timestamps. *Example:* touch .hidden-note

*Related:* file. *First explained in* Chapter 7<!--ref:terminal-->.

**Tracked file.** A file Git knows about, because it is in the last commit or in the index.

*Technically:* A file present in the index or in HEAD's tree. *Example:* README.md after the first commit.

*Related:* untracked file; staged. *First explained in* Chapter 15<!--ref:model-->.

**Tree.** A stored list of a folder's contents.

*Technically:* An object listing the entries of one folder, each with a mode, type, hash and name. *Example:* drinks/

*Related:* blob; commit. *First explained in* Chapter 30<!--ref:objects-->.

**Two-factor authentication (2FA).** Proving who you are with two proofs from different families.

*Technically:* Authentication requiring two distinct factors: something known, something held, or something inherent. *Example:* Password plus a code from a phone app.

*Related:* authentication; password. *First explained in* Chapter 6<!--ref:accounts-->.

## U

**Unicode.** A universal list that gives every character a number.

*Technically:* A standard that assigns a unique code point to each character of the world's writing systems and many symbols. *Example:* U+00E9 is é

*Related:* UTF-8; encoding. *First explained in* Chapter 4<!--ref:text-->.

**Upstream branch.** The remote branch a local branch follows.

*Technically:* The branch named by branch.<name>.remote and branch.<name>.merge, used by plain push, pull and status. *Example:* main follows origin/main

*Related:* remote-tracking branch. *First explained in* Chapter 23<!--ref:remotes-->.

**URL.** The written address of a page or resource on the internet.

*Technically:* Uniform Resource Locator: a string that identifies a resource by scheme, host, optional port, path, optional query and optional fragment. *Example:* https://example.org/menu/cakes?sort=price#top

*Related:* domain name; HTTP. *First explained in* Chapter 5<!--ref:internet-->.

**Username.** The name that identifies your account.

*Technically:* A unique identifier for an account within a service. *Example:* sharif-example

*Related:* account. *First explained in* Chapter 6<!--ref:accounts-->.

**UTF-8.** The most widely used way to store Unicode text as bytes.

*Technically:* A variable-width encoding of Unicode that uses one to four bytes per character and is backward compatible with ASCII for basic English characters. *Example:* é is stored as the two bytes c3 a9.

*Related:* Unicode; encoding. *First explained in* Chapter 4<!--ref:text-->.

## V

**Variable.** A named piece of text the shell remembers.

*Technically:* A named storage location in a shell holding a string value that can be referenced in later commands. *Example:* name="Sunrise Bakery"

*Related:* environment variable. *First explained in* Chapter 7<!--ref:terminal-->.

**Version.** One particular state of a file or project at a point in time.

*Technically:* A distinct recorded state of a file or project. *Example:* The menu as it was on Monday.

*Related:* history; version control. *First explained in* Chapter 9<!--ref:problem-->.

**Version control.** A system that records a project's history so changes can be seen, reversed and combined.

*Technically:* A system that records changes to files over time, supporting retrieval of earlier versions, comparison, and collaborative work. *Example:* Git

*Related:* history; repository. *First explained in* Chapter 9<!--ref:problem-->.

## W

**Web (World Wide Web).** Linked pages and applications you view with a browser.

*Technically:* A system of interlinked resources, identified by URLs and transferred using HTTP, accessed with browsers over the internet. *Example:* The Sunrise Bakery menu page.

*Related:* internet; browser; URL. *First explained in* Chapter 5<!--ref:internet-->.

**Webhook.** A message GitHub sends to your web address when something happens.

*Technically:* An HTTP request with event data that a service sends to a URL you registered when an event you subscribed to occurs. *Example:* A push triggering a request to your server.

*Related:* API; HMAC. *First explained in* Chapter 74<!--ref:api-->.

**Wiki.** A section of a repository for long documentation, kept as its own Git repository.

*Technically:* A documentation area attached to a hosted repository, stored as a separate Git repository (addressed with a .wiki.git suffix on GitHub) with its own history. *Example:* bakery-menu.wiki.git

*Related:* README; repository. *First explained in* Chapter 43<!--ref:settings-->.

**Word processor.** A program for writing formatted documents, saved in a packaged format.

*Technically:* An application that edits formatted documents, storing styles and layout along with the text, normally in a binary or packaged format. *Example:* A program that produces .docx files.

*Related:* text editor; binary file. *First explained in* Chapter 3<!--ref:editors-->.

**Workflow.** The agreed way a team uses Git.

*Technically:* The agreed way a person or team uses branches, commits, reviews, merges and releases to get changes into a project. *Example:* feature-branch workflow

*Related:* branch; merge. *First explained in* Chapter 34<!--ref:workflows-->.

**Workflow (GitHub Actions).** An automated process defined in a file in the repository.

*Technically:* A configurable automated process defined by a YAML file in .github/workflows that runs one or more jobs when triggered by an event. *Example:* .github/workflows/check.yml

*Related:* event; job; step; runner. *First explained in* Chapter 54<!--ref:actions-->.

**Working tree.** The folder of files you see and edit.

*Technically:* The checked-out files of a repository on disk, including changes not yet staged or committed. *Example:* The sunrise-bakery folder.

*Related:* index; repository. *First explained in* Chapter 15<!--ref:model-->.

**Worktree.** An extra working folder for the same repository.

*Technically:* An additional working directory linked to one repository, with its own checked-out branch and shared history. *Example:* git worktree add ../hotfix -b hotfix

*Related:* branch; working tree. *First explained in* Chapter 31<!--ref:bigrepos-->.

## Y

**YAML.** A readable text format for settings and lists, written with indentation.

*Technically:* A human-readable data-serialisation format that represents scalars, sequences and mappings using indentation (spaces only) and simple punctuation; used for configuration such as GitHub Actions workflows. *Example:* name: Sunrise Bakery

*Related:* workflow; indentation. *First explained in* Chapter 53<!--ref:yaml-->.

## Z

**ZIP archive.** One file that holds other files in compressed form.

*Technically:* A container format that stores multiple files, optionally compressed, in a single file. *Example:* Many word-processor documents are ZIP archives internally.

*Related:* binary file. *First explained in* Chapter 3<!--ref:editors-->.
