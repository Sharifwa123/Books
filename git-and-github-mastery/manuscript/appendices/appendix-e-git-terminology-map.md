# Appendix E — Git Terminology Map

The 180 terms first explained in Parts I to IV (computers, version control, Git itself), with a one-line meaning and the chapter to read. Terms about GitHub are in Appendix F. The full definitions are in the Glossary.

| Term | Meaning in one line | First explained |
|---|---|---|
| .gitignore | A text file listing patterns of files Git should ignore. | Chapter 18<!--ref:tracking--> |
| Absolute path | A path that starts at the root and means the same wherever you are. | Chapter 2<!--ref:files--> |
| Account | A record a service keeps to represent you. | Chapter 6<!--ref:accounts--> |
| Administrator | An account or permission level allowed to change the computer's system settings. | Chapter 1<!--ref:computer--> |
| Alias | Your own short name for a Git command. | Chapter 32<!--ref:custom--> |
| Annotated tag | A tag with a message and tagger. | Chapter 24<!--ref:stash--> |
| Application (program) | Software that does a specific job for a person. | Chapter 1<!--ref:computer--> |
| Argument | The thing a command acts on, such as a file name. | Chapter 7<!--ref:terminal--> |
| Atomic commit | A commit containing one logical change. | Chapter 19<!--ref:commits--> |
| Authentication | Proving who you are. | Chapter 6<!--ref:accounts--> |
| Authorization | Deciding what you are allowed to do once your identity is known. | Chapter 6<!--ref:accounts--> |
| Backup | A copy of your files kept elsewhere so they can be restored after loss. | Chapter 9<!--ref:problem--> |
| Bare repository | A repository with no working files, used as a shared hub. | Chapter 23<!--ref:remotes--> |
| Bash | A widely used shell; the one this book uses for its examples. | Chapter 7<!--ref:terminal--> |
| Binary file | A file that is not plain text, such as a photo or a word-processor document. | Chapter 3<!--ref:editors--> |
| Bisect | Find the commit that broke something by halving. | Chapter 28<!--ref:tools--> |
| Bitbucket | Another hosting platform for Git repositories, from a different company. | Chapter 12<!--ref:platforms--> |
| Blob | The stored contents of one file. | Chapter 30<!--ref:objects--> |
| Branch | A movable name that points to a commit. | Chapter 15<!--ref:model--> |
| Browser | An application for viewing web pages. | Chapter 5<!--ref:internet--> |
| Byte | A unit for measuring stored information; enough for one English letter. | Chapter 1<!--ref:computer--> |
| cd | Moves you into another folder. | Chapter 7<!--ref:terminal--> |
| Centralised version control | One server holds the only complete history; users hold working copies. | Chapter 11<!--ref:distributed--> |
| Character | A single unit of text: a letter, digit, symbol, emoji or space. | Chapter 4<!--ref:text--> |
| Cherry-pick | Copy one commit onto another branch. | Chapter 28<!--ref:tools--> |
| Client | The computer or program that asks for something. | Chapter 5<!--ref:internet--> |
| Clone | A complete copy of a repository, with all its history, made on another computer. | Chapter 11<!--ref:distributed--> |
| Code editor | A text editor with extra help for writing structured text such as software. | Chapter 3<!--ref:editors--> |
| Command | One instruction typed to the shell. | Chapter 7<!--ref:terminal--> |
| Commit | A recorded snapshot with author, time, message and a link to the previous commit; also the action of making one. | Chapter 15<!--ref:model--> |
| CommonMark | A precise written specification of the core Markdown syntax. | Chapter 8<!--ref:markdown--> |
| Computer | A machine that follows instructions to take in, change, keep and show information. | Chapter 1<!--ref:computer--> |
| Configuration (setting) | A named value that changes how Git behaves. | Chapter 14<!--ref:config--> |
| Conflict markers | The lines Git writes into a conflicted file. | Chapter 22<!--ref:conflicts--> |
| Credential helper | A program that remembers passwords for Git. | Chapter 32<!--ref:custom--> |
| CSS | A text format that describes how web pages look. | Chapter 3<!--ref:editors--> |
| Current directory (working directory) | The folder that counts as 'here' when you give a relative path. | Chapter 2<!--ref:files--> |
| Dangling object | A stored object nothing points to. | Chapter 30<!--ref:objects--> |
| Detached HEAD | HEAD points directly at a commit instead of a branch. | Chapter 20<!--ref:branching--> |
| Diff | A report of the differences between two versions, line by line. | Chapter 17<!--ref:history_view--> |
| Distributed version control | Every user holds a complete copy of the repository and its history. | Chapter 11<!--ref:distributed--> |
| Diverged | Each branch has commits the other lacks. | Chapter 21<!--ref:merging--> |
| DNS (domain name system) | The internet's phone book: it turns names into numbers. | Chapter 5<!--ref:internet--> |
| Domain name | A human-friendly name, such as example.org, for a host on the internet. | Chapter 5<!--ref:internet--> |
| Empty commit | A commit with a message but no file change. | Chapter 19<!--ref:commits--> |
| Encoding | The rule that turns characters into bytes and back. | Chapter 4<!--ref:text--> |
| Environment variable | A variable that programs started from the shell can read. | Chapter 7<!--ref:terminal--> |
| Extension | The letters after the last dot in a file name; a label for the kind of contents. | Chapter 2<!--ref:files--> |
| Fast-forward | A merge that only moves a branch pointer forward. | Chapter 21<!--ref:merging--> |
| Fetch | Download new commits without changing your branches. | Chapter 23<!--ref:remotes--> |
| File | A named collection of information kept in storage. | Chapter 2<!--ref:files--> |
| Folder (directory) | A container that holds files and other folders. | Chapter 2<!--ref:files--> |
| Garbage collection | Git's housekeeping of stored objects. | Chapter 30<!--ref:objects--> |
| Git | A free, open-source version-control system that runs on your computer. | Chapter 12<!--ref:platforms--> |
| git add | Stages files so they are part of the next commit. | Chapter 16<!--ref:firstrepo--> |
| Git Bash | A Bash environment for Windows that is installed with Git for Windows; it is not Git itself. | Chapter 7<!--ref:terminal--> |
| git branch | Lists, creates, renames and deletes branches. | Chapter 20<!--ref:branching--> |
| git commit | Records the staged snapshot with a message. | Chapter 16<!--ref:firstrepo--> |
| git commit --amend | Replaces the last commit with a new one, to fix its message or add forgotten changes. | Chapter 19<!--ref:commits--> |
| git config | The command that reads and changes Git's settings. | Chapter 13<!--ref:install--> |
| git init | Creates a new repository in the current folder. | Chapter 16<!--ref:firstrepo--> |
| Git LFS | A way to keep large files outside the history. | Chapter 31<!--ref:bigrepos--> |
| git log | Shows the history of commits, newest first. | Chapter 17<!--ref:history_view--> |
| git mv | Renames or moves a file and stages the change. | Chapter 18<!--ref:tracking--> |
| git reset | Move the current branch to another commit. | Chapter 25<!--ref:undo--> |
| git restore | Bring a file back from the index or an older commit. | Chapter 25<!--ref:undo--> |
| git revert | Undo a commit by adding a new one. | Chapter 25<!--ref:undo--> |
| git rm | Deletes a file and stages the deletion. | Chapter 18<!--ref:tracking--> |
| git show | Displays one commit: its message and changes. | Chapter 17<!--ref:history_view--> |
| git status | Shows which files are untracked, modified or staged, and the current branch. | Chapter 16<!--ref:firstrepo--> |
| git switch | Changes the current branch. | Chapter 20<!--ref:branching--> |
| GitHub | A widely used online platform for hosting Git repositories and collaborating on software. | Chapter 12<!--ref:platforms--> |
| GitLab | Another hosting platform for Git repositories. | Chapter 12<!--ref:platforms--> |
| Global setting | A Git setting that applies to your user account in every repository. | Chapter 13<!--ref:install--> |
| Hardware | The physical parts of a computer. | Chapter 1<!--ref:computer--> |
| Hash (commit identifier) | The long code that uniquely identifies a commit. | Chapter 15<!--ref:model--> |
| HEAD | The pointer that says which commit you are currently on. | Chapter 15<!--ref:model--> |
| Hidden file | A file that ordinary listings do not show unless asked. | Chapter 2<!--ref:files--> |
| History | The recorded sequence of versions of a project, with reasons and authors. | Chapter 9<!--ref:problem--> |
| Home folder | The folder that belongs to your user account. | Chapter 2<!--ref:files--> |
| Hook | A script Git runs at a fixed moment. | Chapter 32<!--ref:custom--> |
| Hosting platform | An online service that stores shared repositories and adds collaboration features. | Chapter 12<!--ref:platforms--> |
| HTML | A text format that marks up web pages so a browser knows how to show them. | Chapter 3<!--ref:editors--> |
| HTTP | The rules web clients and servers follow to exchange requests and replies. | Chapter 5<!--ref:internet--> |
| HTTPS | HTTP with encryption and a check of the server's identity. | Chapter 5<!--ref:internet--> |
| Hunk | One contiguous chunk of changes in a diff. | Chapter 17<!--ref:history_view--> |
| Ignored file | A file Git has been told to leave alone. | Chapter 18<!--ref:tracking--> |
| Index (staging area) | The holding area that lists exactly what the next commit will contain. | Chapter 15<!--ref:model--> |
| Installer | A file or program that puts an application on your computer. | Chapter 1<!--ref:computer--> |
| Internet | The worldwide system of connected networks. | Chapter 5<!--ref:internet--> |
| IP address | A number that identifies a computer on a network. | Chapter 5<!--ref:internet--> |
| Key pair | A shareable public key and a private key that never leaves your computer. | Chapter 6<!--ref:accounts--> |
| Least privilege | Giving only the access that is needed, and no more. | Chapter 6<!--ref:accounts--> |
| Lightweight tag | A tag that is just a name. | Chapter 24<!--ref:stash--> |
| Line ending (newline) | The invisible character or characters that end a line of text. | Chapter 4<!--ref:text--> |
| Local | On the computer you are using. | Chapter 5<!--ref:internet--> |
| Local repository | The complete history, kept in the hidden .git folder on your computer. | Chapter 15<!--ref:model--> |
| Lock | A marker that stops others from changing a file until you release it. | Chapter 10<!--ref:history--> |
| Markdown | A way of writing formatted text using plain-text marks. | Chapter 8<!--ref:markdown--> |
| Memory (RAM) | Fast, temporary working space that is emptied when the power goes off. | Chapter 1<!--ref:computer--> |
| Merge | To combine two sets of changes into one. | Chapter 10<!--ref:history--> |
| Merge commit | A commit that joins two lines of work. | Chapter 21<!--ref:merging--> |
| Merge conflict | Git cannot combine two changes by itself. | Chapter 22<!--ref:conflicts--> |
| Metadata | Information about a file, such as its size, dates, owner and permissions. | Chapter 2<!--ref:files--> |
| mkdir | Creates a new folder. | Chapter 7<!--ref:terminal--> |
| Mojibake | Garbled text caused by reading with the wrong encoding. | Chapter 4<!--ref:text--> |
| Network | Computers connected so that they can exchange information. | Chapter 5<!--ref:internet--> |
| Object | Any item in Git's database. | Chapter 30<!--ref:objects--> |
| Operating system (OS) | The main software that manages the computer, its files and the other programs. | Chapter 1<!--ref:computer--> |
| Option (flag) | A word that changes how a command behaves. | Chapter 7<!--ref:terminal--> |
| Override | To replace a setting's value for one command or one shell. | Chapter 14<!--ref:config--> |
| Package manager | A program that installs and updates applications from a trusted collection. | Chapter 1<!--ref:computer--> |
| Packfile | One file holding many objects compactly. | Chapter 30<!--ref:objects--> |
| Password | A secret string you present to prove you own an account. | Chapter 6<!--ref:accounts--> |
| Password manager | An application that stores all your passwords securely and fills them in. | Chapter 6<!--ref:accounts--> |
| Patch | A text file that describes a change. | Chapter 28<!--ref:tools--> |
| Path | A written description of where a file or folder is in the tree. | Chapter 2<!--ref:files--> |
| PATH (environment variable) | The list of folders the shell searches for programs. | Chapter 7<!--ref:terminal--> |
| Permission | A rule about who may read, change or run a file. | Chapter 2<!--ref:files--> |
| Phishing | Tricking someone into giving away a secret by pretending to be trusted. | Chapter 6<!--ref:accounts--> |
| Plain text | Information stored as ordinary characters with no fonts, colours or layout. | Chapter 3<!--ref:editors--> |
| Processor (CPU) | The part that carries out instructions. | Chapter 1<!--ref:computer--> |
| Prompt | The text the shell shows when it is waiting for you to type. | Chapter 7<!--ref:terminal--> |
| Pull | Fetch, then merge into your current branch. | Chapter 23<!--ref:remotes--> |
| pwd | Prints the folder you are currently in. | Chapter 7<!--ref:terminal--> |
| Rebase | Replay your commits on top of another commit. | Chapter 27<!--ref:rebase--> |
| Ref | A name that points to an object. | Chapter 30<!--ref:objects--> |
| Reflog | Git's private diary of where HEAD has been. | Chapter 26<!--ref:reflog--> |
| Relative path | A path that starts from where you are now. | Chapter 2<!--ref:files--> |
| Remote | On a different computer, reached over a network. | Chapter 5<!--ref:internet--> |
| Remote-tracking branch | Your note of where a remote branch was when you last looked. | Chapter 23<!--ref:remotes--> |
| Renderer | A program that turns marked-up text into a formatted result. | Chapter 8<!--ref:markdown--> |
| Repository | A project together with the complete record of its history. | Chapter 11<!--ref:distributed--> |
| rerere | Git remembers how you resolved a conflict. | Chapter 32<!--ref:custom--> |
| Revision | Any way of naming a commit: a hash, a branch name, HEAD, HEAD~2. | Chapter 17<!--ref:history_view--> |
| Root | The top folder of a tree; everything else is inside it. | Chapter 2<!--ref:files--> |
| Scope | The level at which a setting is stored: system, global, local or worktree. | Chapter 14<!--ref:config--> |
| Secret | A value that gives access if someone else has it. | Chapter 33<!--ref:gitsec--> |
| Semantic versioning | A convention for MAJOR.MINOR.PATCH release numbers. | Chapter 29<!--ref:tags--> |
| Server | A computer or program that answers requests. | Chapter 5<!--ref:internet--> |
| Shallow clone | A clone with only the recent history. | Chapter 31<!--ref:bigrepos--> |
| Shell | The program that reads your commands and has them carried out. | Chapter 7<!--ref:terminal--> |
| Signed commit | A commit that carries a verifiable signature. | Chapter 33<!--ref:gitsec--> |
| Single point of failure | A part whose failure stops everything or loses something irreplaceable. | Chapter 11<!--ref:distributed--> |
| Snapshot | A complete picture of all the files of a project at one moment. | Chapter 15<!--ref:model--> |
| Software | Instructions that tell hardware what to do. | Chapter 1<!--ref:computer--> |
| Software project | The folder of files that makes up one piece of work. | Chapter 3<!--ref:editors--> |
| Source code (source files) | The human-written files from which a project is made. | Chapter 3<!--ref:editors--> |
| Squash | Turn many commits into one. | Chapter 21<!--ref:merging--> |
| SSH (Secure Shell) | A secure way to connect to another computer, which can use a key pair to prove your identity. | Chapter 6<!--ref:accounts--> |
| Stage | To add a file's current contents to the index so the next commit includes them. | Chapter 15<!--ref:model--> |
| Stash | A shelf for unfinished changes. | Chapter 24<!--ref:stash--> |
| Storage | Slower, permanent space that keeps information when the power is off. | Chapter 1<!--ref:computer--> |
| Submodule | A repository pinned inside another repository. | Chapter 31<!--ref:bigrepos--> |
| Synchronised (cloud) folder | A folder whose contents are kept the same across computers or an online service. | Chapter 9<!--ref:problem--> |
| Synopsis | The short line showing how to write a command. | Chapter 35<!--ref:readdocs--> |
| Syntax highlighting | Colouring parts of text according to their role so the structure is easy to see. | Chapter 3<!--ref:editors--> |
| Tag | A fixed name for one commit. | Chapter 24<!--ref:stash--> |
| Tag object | The object an annotated tag creates. | Chapter 30<!--ref:objects--> |
| Terminal | A window in which you type commands and read text replies. | Chapter 7<!--ref:terminal--> |
| Text editor | A program for creating and changing plain text files. | Chapter 3<!--ref:editors--> |
| Token | A limited stand-in for a password; still a secret. | Chapter 6<!--ref:accounts--> |
| touch | Creates an empty file, or updates a file's last-changed time. | Chapter 7<!--ref:terminal--> |
| Tracked file | A file Git knows about, because it is in the last commit or in the index. | Chapter 15<!--ref:model--> |
| Tree | A stored list of a folder's contents. | Chapter 30<!--ref:objects--> |
| Two-factor authentication (2FA) | Proving who you are with two proofs from different families. | Chapter 6<!--ref:accounts--> |
| Unicode | A universal list that gives every character a number. | Chapter 4<!--ref:text--> |
| Upstream branch | The remote branch a local branch follows. | Chapter 23<!--ref:remotes--> |
| URL | The written address of a page or resource on the internet. | Chapter 5<!--ref:internet--> |
| Username | The name that identifies your account. | Chapter 6<!--ref:accounts--> |
| UTF-8 | The most widely used way to store Unicode text as bytes. | Chapter 4<!--ref:text--> |
| Variable | A named piece of text the shell remembers. | Chapter 7<!--ref:terminal--> |
| Version | One particular state of a file or project at a point in time. | Chapter 9<!--ref:problem--> |
| Version control | A system that records a project's history so changes can be seen, reversed and combined. | Chapter 9<!--ref:problem--> |
| Web (World Wide Web) | Linked pages and applications you view with a browser. | Chapter 5<!--ref:internet--> |
| Word processor | A program for writing formatted documents, saved in a packaged format. | Chapter 3<!--ref:editors--> |
| Workflow | The agreed way a team uses Git. | Chapter 34<!--ref:workflows--> |
| Working tree | The folder of files you see and edit. | Chapter 15<!--ref:model--> |
| Worktree | An extra working folder for the same repository. | Chapter 31<!--ref:bigrepos--> |
| ZIP archive | One file that holds other files in compressed form. | Chapter 3<!--ref:editors--> |