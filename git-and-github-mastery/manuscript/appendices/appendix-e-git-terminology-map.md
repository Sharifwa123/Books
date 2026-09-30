# Appendix E — Git Terminology Map

The 180 terms first explained in Parts I to IV (computers, version control, Git itself), with a one-line meaning and the chapter to read. Terms about GitHub are in Appendix F. The full definitions are in the Glossary.

| Term | Meaning in one line | First explained |
|---|---|---|
| .gitignore | A text file listing patterns of files Git should ignore. | Chapter [[tracking]] |
| Absolute path | A path that starts at the root and means the same wherever you are. | Chapter [[files]] |
| Account | A record a service keeps to represent you. | Chapter [[accounts]] |
| Administrator | An account or permission level allowed to change the computer's system settings. | Chapter [[computer]] |
| Alias | Your own short name for a Git command. | Chapter [[custom]] |
| Annotated tag | A tag with a message and tagger. | Chapter [[stash]] |
| Application (program) | Software that does a specific job for a person. | Chapter [[computer]] |
| Argument | The thing a command acts on, such as a file name. | Chapter [[terminal]] |
| Atomic commit | A commit containing one logical change. | Chapter [[commits]] |
| Authentication | Proving who you are. | Chapter [[accounts]] |
| Authorization | Deciding what you are allowed to do once your identity is known. | Chapter [[accounts]] |
| Backup | A copy of your files kept elsewhere so they can be restored after loss. | Chapter [[problem]] |
| Bare repository | A repository with no working files, used as a shared hub. | Chapter [[remotes]] |
| Bash | A widely used shell; the one this book uses for its examples. | Chapter [[terminal]] |
| Binary file | A file that is not plain text, such as a photo or a word-processor document. | Chapter [[editors]] |
| Bisect | Find the commit that broke something by halving. | Chapter [[tools]] |
| Bitbucket | Another hosting platform for Git repositories, from a different company. | Chapter [[platforms]] |
| Blob | The stored contents of one file. | Chapter [[objects]] |
| Branch | A movable name that points to a commit. | Chapter [[model]] |
| Browser | An application for viewing web pages. | Chapter [[internet]] |
| Byte | A unit for measuring stored information; enough for one English letter. | Chapter [[computer]] |
| cd | Moves you into another folder. | Chapter [[terminal]] |
| Centralised version control | One server holds the only complete history; users hold working copies. | Chapter [[distributed]] |
| Character | A single unit of text: a letter, digit, symbol, emoji or space. | Chapter [[text]] |
| Cherry-pick | Copy one commit onto another branch. | Chapter [[tools]] |
| Client | The computer or program that asks for something. | Chapter [[internet]] |
| Clone | A complete copy of a repository, with all its history, made on another computer. | Chapter [[distributed]] |
| Code editor | A text editor with extra help for writing structured text such as software. | Chapter [[editors]] |
| Command | One instruction typed to the shell. | Chapter [[terminal]] |
| Commit | A recorded snapshot with author, time, message and a link to the previous commit; also the action of making one. | Chapter [[model]] |
| CommonMark | A precise written specification of the core Markdown syntax. | Chapter [[markdown]] |
| Computer | A machine that follows instructions to take in, change, keep and show information. | Chapter [[computer]] |
| Configuration (setting) | A named value that changes how Git behaves. | Chapter [[config]] |
| Conflict markers | The lines Git writes into a conflicted file. | Chapter [[conflicts]] |
| Credential helper | A program that remembers passwords for Git. | Chapter [[custom]] |
| CSS | A text format that describes how web pages look. | Chapter [[editors]] |
| Current directory (working directory) | The folder that counts as 'here' when you give a relative path. | Chapter [[files]] |
| Dangling object | A stored object nothing points to. | Chapter [[objects]] |
| Detached HEAD | HEAD points directly at a commit instead of a branch. | Chapter [[branching]] |
| Diff | A report of the differences between two versions, line by line. | Chapter [[history_view]] |
| Distributed version control | Every user holds a complete copy of the repository and its history. | Chapter [[distributed]] |
| Diverged | Each branch has commits the other lacks. | Chapter [[merging]] |
| DNS (domain name system) | The internet's phone book: it turns names into numbers. | Chapter [[internet]] |
| Domain name | A human-friendly name, such as example.org, for a host on the internet. | Chapter [[internet]] |
| Empty commit | A commit with a message but no file change. | Chapter [[commits]] |
| Encoding | The rule that turns characters into bytes and back. | Chapter [[text]] |
| Environment variable | A variable that programs started from the shell can read. | Chapter [[terminal]] |
| Extension | The letters after the last dot in a file name; a label for the kind of contents. | Chapter [[files]] |
| Fast-forward | A merge that only moves a branch pointer forward. | Chapter [[merging]] |
| Fetch | Download new commits without changing your branches. | Chapter [[remotes]] |
| File | A named collection of information kept in storage. | Chapter [[files]] |
| Folder (directory) | A container that holds files and other folders. | Chapter [[files]] |
| Garbage collection | Git's housekeeping of stored objects. | Chapter [[objects]] |
| Git | A free, open-source version-control system that runs on your computer. | Chapter [[platforms]] |
| git add | Stages files so they are part of the next commit. | Chapter [[firstrepo]] |
| Git Bash | A Bash environment for Windows that is installed with Git for Windows; it is not Git itself. | Chapter [[terminal]] |
| git branch | Lists, creates, renames and deletes branches. | Chapter [[branching]] |
| git commit | Records the staged snapshot with a message. | Chapter [[firstrepo]] |
| git commit --amend | Replaces the last commit with a new one, to fix its message or add forgotten changes. | Chapter [[commits]] |
| git config | The command that reads and changes Git's settings. | Chapter [[install]] |
| git init | Creates a new repository in the current folder. | Chapter [[firstrepo]] |
| Git LFS | A way to keep large files outside the history. | Chapter [[bigrepos]] |
| git log | Shows the history of commits, newest first. | Chapter [[history_view]] |
| git mv | Renames or moves a file and stages the change. | Chapter [[tracking]] |
| git reset | Move the current branch to another commit. | Chapter [[undo]] |
| git restore | Bring a file back from the index or an older commit. | Chapter [[undo]] |
| git revert | Undo a commit by adding a new one. | Chapter [[undo]] |
| git rm | Deletes a file and stages the deletion. | Chapter [[tracking]] |
| git show | Displays one commit: its message and changes. | Chapter [[history_view]] |
| git status | Shows which files are untracked, modified or staged, and the current branch. | Chapter [[firstrepo]] |
| git switch | Changes the current branch. | Chapter [[branching]] |
| GitHub | A widely used online platform for hosting Git repositories and collaborating on software. | Chapter [[platforms]] |
| GitLab | Another hosting platform for Git repositories. | Chapter [[platforms]] |
| Global setting | A Git setting that applies to your user account in every repository. | Chapter [[install]] |
| Hardware | The physical parts of a computer. | Chapter [[computer]] |
| Hash (commit identifier) | The long code that uniquely identifies a commit. | Chapter [[model]] |
| HEAD | The pointer that says which commit you are currently on. | Chapter [[model]] |
| Hidden file | A file that ordinary listings do not show unless asked. | Chapter [[files]] |
| History | The recorded sequence of versions of a project, with reasons and authors. | Chapter [[problem]] |
| Home folder | The folder that belongs to your user account. | Chapter [[files]] |
| Hook | A script Git runs at a fixed moment. | Chapter [[custom]] |
| Hosting platform | An online service that stores shared repositories and adds collaboration features. | Chapter [[platforms]] |
| HTML | A text format that marks up web pages so a browser knows how to show them. | Chapter [[editors]] |
| HTTP | The rules web clients and servers follow to exchange requests and replies. | Chapter [[internet]] |
| HTTPS | HTTP with encryption and a check of the server's identity. | Chapter [[internet]] |
| Hunk | One contiguous chunk of changes in a diff. | Chapter [[history_view]] |
| Ignored file | A file Git has been told to leave alone. | Chapter [[tracking]] |
| Index (staging area) | The holding area that lists exactly what the next commit will contain. | Chapter [[model]] |
| Installer | A file or program that puts an application on your computer. | Chapter [[computer]] |
| Internet | The worldwide system of connected networks. | Chapter [[internet]] |
| IP address | A number that identifies a computer on a network. | Chapter [[internet]] |
| Key pair | A shareable public key and a private key that never leaves your computer. | Chapter [[accounts]] |
| Least privilege | Giving only the access that is needed, and no more. | Chapter [[accounts]] |
| Lightweight tag | A tag that is just a name. | Chapter [[stash]] |
| Line ending (newline) | The invisible character or characters that end a line of text. | Chapter [[text]] |
| Local | On the computer you are using. | Chapter [[internet]] |
| Local repository | The complete history, kept in the hidden .git folder on your computer. | Chapter [[model]] |
| Lock | A marker that stops others from changing a file until you release it. | Chapter [[history]] |
| Markdown | A way of writing formatted text using plain-text marks. | Chapter [[markdown]] |
| Memory (RAM) | Fast, temporary working space that is emptied when the power goes off. | Chapter [[computer]] |
| Merge | To combine two sets of changes into one. | Chapter [[history]] |
| Merge commit | A commit that joins two lines of work. | Chapter [[merging]] |
| Merge conflict | Git cannot combine two changes by itself. | Chapter [[conflicts]] |
| Metadata | Information about a file, such as its size, dates, owner and permissions. | Chapter [[files]] |
| mkdir | Creates a new folder. | Chapter [[terminal]] |
| Mojibake | Garbled text caused by reading with the wrong encoding. | Chapter [[text]] |
| Network | Computers connected so that they can exchange information. | Chapter [[internet]] |
| Object | Any item in Git's database. | Chapter [[objects]] |
| Operating system (OS) | The main software that manages the computer, its files and the other programs. | Chapter [[computer]] |
| Option (flag) | A word that changes how a command behaves. | Chapter [[terminal]] |
| Override | To replace a setting's value for one command or one shell. | Chapter [[config]] |
| Package manager | A program that installs and updates applications from a trusted collection. | Chapter [[computer]] |
| Packfile | One file holding many objects compactly. | Chapter [[objects]] |
| Password | A secret string you present to prove you own an account. | Chapter [[accounts]] |
| Password manager | An application that stores all your passwords securely and fills them in. | Chapter [[accounts]] |
| Patch | A text file that describes a change. | Chapter [[tools]] |
| Path | A written description of where a file or folder is in the tree. | Chapter [[files]] |
| PATH (environment variable) | The list of folders the shell searches for programs. | Chapter [[terminal]] |
| Permission | A rule about who may read, change or run a file. | Chapter [[files]] |
| Phishing | Tricking someone into giving away a secret by pretending to be trusted. | Chapter [[accounts]] |
| Plain text | Information stored as ordinary characters with no fonts, colours or layout. | Chapter [[editors]] |
| Processor (CPU) | The part that carries out instructions. | Chapter [[computer]] |
| Prompt | The text the shell shows when it is waiting for you to type. | Chapter [[terminal]] |
| Pull | Fetch, then merge into your current branch. | Chapter [[remotes]] |
| pwd | Prints the folder you are currently in. | Chapter [[terminal]] |
| Rebase | Replay your commits on top of another commit. | Chapter [[rebase]] |
| Ref | A name that points to an object. | Chapter [[objects]] |
| Reflog | Git's private diary of where HEAD has been. | Chapter [[reflog]] |
| Relative path | A path that starts from where you are now. | Chapter [[files]] |
| Remote | On a different computer, reached over a network. | Chapter [[internet]] |
| Remote-tracking branch | Your note of where a remote branch was when you last looked. | Chapter [[remotes]] |
| Renderer | A program that turns marked-up text into a formatted result. | Chapter [[markdown]] |
| Repository | A project together with the complete record of its history. | Chapter [[distributed]] |
| rerere | Git remembers how you resolved a conflict. | Chapter [[custom]] |
| Revision | Any way of naming a commit: a hash, a branch name, HEAD, HEAD~2. | Chapter [[history_view]] |
| Root | The top folder of a tree; everything else is inside it. | Chapter [[files]] |
| Scope | The level at which a setting is stored: system, global, local or worktree. | Chapter [[config]] |
| Secret | A value that gives access if someone else has it. | Chapter [[gitsec]] |
| Semantic versioning | A convention for MAJOR.MINOR.PATCH release numbers. | Chapter [[tags]] |
| Server | A computer or program that answers requests. | Chapter [[internet]] |
| Shallow clone | A clone with only the recent history. | Chapter [[bigrepos]] |
| Shell | The program that reads your commands and has them carried out. | Chapter [[terminal]] |
| Signed commit | A commit that carries a verifiable signature. | Chapter [[gitsec]] |
| Single point of failure | A part whose failure stops everything or loses something irreplaceable. | Chapter [[distributed]] |
| Snapshot | A complete picture of all the files of a project at one moment. | Chapter [[model]] |
| Software | Instructions that tell hardware what to do. | Chapter [[computer]] |
| Software project | The folder of files that makes up one piece of work. | Chapter [[editors]] |
| Source code (source files) | The human-written files from which a project is made. | Chapter [[editors]] |
| Squash | Turn many commits into one. | Chapter [[merging]] |
| SSH (Secure Shell) | A secure way to connect to another computer, which can use a key pair to prove your identity. | Chapter [[accounts]] |
| Stage | To add a file's current contents to the index so the next commit includes them. | Chapter [[model]] |
| Stash | A shelf for unfinished changes. | Chapter [[stash]] |
| Storage | Slower, permanent space that keeps information when the power is off. | Chapter [[computer]] |
| Submodule | A repository pinned inside another repository. | Chapter [[bigrepos]] |
| Synchronised (cloud) folder | A folder whose contents are kept the same across computers or an online service. | Chapter [[problem]] |
| Synopsis | The short line showing how to write a command. | Chapter [[readdocs]] |
| Syntax highlighting | Colouring parts of text according to their role so the structure is easy to see. | Chapter [[editors]] |
| Tag | A fixed name for one commit. | Chapter [[stash]] |
| Tag object | The object an annotated tag creates. | Chapter [[objects]] |
| Terminal | A window in which you type commands and read text replies. | Chapter [[terminal]] |
| Text editor | A program for creating and changing plain text files. | Chapter [[editors]] |
| Token | A limited stand-in for a password; still a secret. | Chapter [[accounts]] |
| touch | Creates an empty file, or updates a file's last-changed time. | Chapter [[terminal]] |
| Tracked file | A file Git knows about, because it is in the last commit or in the index. | Chapter [[model]] |
| Tree | A stored list of a folder's contents. | Chapter [[objects]] |
| Two-factor authentication (2FA) | Proving who you are with two proofs from different families. | Chapter [[accounts]] |
| Unicode | A universal list that gives every character a number. | Chapter [[text]] |
| Upstream branch | The remote branch a local branch follows. | Chapter [[remotes]] |
| URL | The written address of a page or resource on the internet. | Chapter [[internet]] |
| Username | The name that identifies your account. | Chapter [[accounts]] |
| UTF-8 | The most widely used way to store Unicode text as bytes. | Chapter [[text]] |
| Variable | A named piece of text the shell remembers. | Chapter [[terminal]] |
| Version | One particular state of a file or project at a point in time. | Chapter [[problem]] |
| Version control | A system that records a project's history so changes can be seen, reversed and combined. | Chapter [[problem]] |
| Web (World Wide Web) | Linked pages and applications you view with a browser. | Chapter [[internet]] |
| Word processor | A program for writing formatted documents, saved in a packaged format. | Chapter [[editors]] |
| Workflow | The agreed way a team uses Git. | Chapter [[workflows]] |
| Working tree | The folder of files you see and edit. | Chapter [[model]] |
| Worktree | An extra working folder for the same repository. | Chapter [[bigrepos]] |
| ZIP archive | One file that holds other files in compressed form. | Chapter [[editors]] |