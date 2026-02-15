# Workshop 2: Creating Your First Git Repository

## Duration: 45-60 minutes

## Objective
By the end of this workshop, you will create your first Git repository, understand repository structure, and perform basic repository operations like cloning and inspecting repositories.

## Prerequisites
- Git installed and configured ([Workshop 1](workshop-01-basic-setup.md))
- Basic understanding of command line/terminal
- Familiarity with file operations

## Materials Needed
- Computer with Git installed
- Terminal/command prompt
- Text editor
- Internet connection (for cloning)

---

## Part 1: Understanding Repositories

### Step 1: What is a Git Repository?

**Discussion Points:**
- A repository (repo) is a directory tracked by Git
- Contains your project files plus Git's internal data
- Every Git project is a repository
- Can be local (on your computer) or remote (on servers like GitHub)

**Key Components:**
- **Working Directory**: Files you edit
- **.git folder**: Git's internal data (don't modify manually!)
- **Config files**: Repository settings
- **Commit history**: All changes made to the project

### Step 2: Repository Types

**Local Repository:**
- Exists only on your computer
- Perfect for personal projects
- No internet connection required

**Remote Repository:**
- Hosted on servers (GitHub, GitLab, etc.)
- Enables collaboration
- Acts as backup and sharing point

---

## Part 2: Creating a Local Repository

### Step 3: Initialize a New Repository

**What you'll do:** Create a brand new Git repository from scratch.

**Instructions:**
```bash
# Create a new directory for your project
mkdir my-first-repo
cd my-first-repo

# Initialize Git repository
git init
```

**Expected Output:**
```
Initialized empty Git repository in /path/to/my-first-repo/.git/
```

**Verification:**
```bash
# Check what Git created
ls -la
```

**Expected Output:**
```
drwxr-xr-x  .git/
-rw-r--r--  (other files if any)
```

### Step 4: Explore the .git Folder

**Instructions:**
```bash
# Look inside Git's internal folder (don't modify files here!)
ls -la .git/
```

**Key Files/Folders:**
- `HEAD` - Points to current branch
- `config` - Repository configuration
- `refs/` - Branch and tag references
- `objects/` - Git's internal object storage

**Important:** Never manually edit files in `.git/` folder!

### Step 5: Check Repository Status

**Instructions:**
```bash
git status
```

**Expected Output:**
```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

**Discussion:**
- You're on the `main` branch (default)
- No commits yet (repository is empty)
- No files are being tracked

---

## Part 3: Adding Files and Making Your First Commit

### Step 6: Create Project Files

**Instructions:**
```bash
# Create a README file
echo "# My First Git Repository" > README.md
echo "" >> README.md
echo "This is my first Git project!" >> README.md

# Create a simple script
echo "print('Hello from Git!')" > hello.py

# Check status again
git status
```

**Expected Output:**
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        hello.py

nothing added to commit but untracked files present (use "git add" to track)
```

### Step 7: Stage Files

**Instructions:**
```bash
# Stage all files
git add .

# Check status
git status
```

**Expected Output:**
```
On branch main

No commits yet

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   README.md
        new file:   hello.py
```

### Step 8: Make Your First Commit

**Instructions:**
```bash
git commit -m "Initial commit: Add README and hello script"
```

**Expected Output:**
```
[main (root-commit) 1a2b3c4] Initial commit: Add README and hello script
 2 files changed, 3 insertions(+)
 create mode 100644 README.md
 create mode 100644 hello.py
```

### Step 9: View Commit History

**Instructions:**
```bash
# View commit history
git log

# View compact history
git log --oneline
```

**Expected Output:**
```
commit 1a2b3c4... (HEAD -> main)
Author: Your Name <your.email@example.com>
Date:   [timestamp]

    Initial commit: Add README and hello script
```

---

## Part 4: Working with Existing Repositories

### Step 10: Clone a Repository

**What you'll do:** Copy an existing repository to your computer.

**Instructions:**
```bash
# Go back to parent directory
cd ..

# Clone a public repository (replace with any public repo URL)
git clone https://github.com/octocat/Hello-World.git cloned-repo

# Enter the cloned repository
cd cloned-repo
```

**Expected Output:**
```
Cloning into 'cloned-repo'...
remote: Enumerating objects: 123, done.
remote: Counting objects: 100% (123/123), done.
remote: Compressing objects: 100% (78/78), done.
remote: Total 123 (delta 42), done.
Receiving objects: 100% (123/123), 12.34 KiB | 1.23 MiB/s, done.
Resolving deltas: 100% (42/42), done.
```

### Step 11: Explore Cloned Repository

**Instructions:**
```bash
# Check the repository
git status

# View commit history
git log --oneline

# See remote repositories
git remote -v

# Check current branch
git branch
```

**Expected Output:**
```
On branch main
Your branch is up to date with 'origin/main'.

origin  https://github.com/octocat/Hello-World.git (fetch)
origin  https://github.com/octocat/Hello-World.git (push)
```

### Step 12: Understand Remote Tracking

**Discussion:**
- `origin` is the default name for the remote repository
- `origin/main` is the remote main branch
- Your local `main` branch tracks `origin/main`
- `git pull` gets latest changes from remote
- `git push` sends your changes to remote

---

## Part 5: Repository Configuration

### Step 13: View Repository Configuration

**Instructions:**
```bash
# View all configuration
git config --list

# View repository-specific config
git config --local --list

# View global config
git config --global --list
```

### Step 14: Repository-Specific Settings

**Instructions:**
```bash
# Set repository-specific user info (if different from global)
git config user.name "Project-Specific Name"
git config user.email "project@example.com"

# Check what changed
git config --local --list
```

### Step 15: Repository Maintenance

**Instructions:**
```bash
# Check repository health
git fsck

# Compress repository (optimize storage)
git gc

# View repository size
du -sh .git
```

---

## Part 6: Multiple Repository Scenarios

### Step 16: Working with Multiple Repositories

**Instructions:**
```bash
# Go back to projects directory
cd ..

# Create another repository
mkdir project-two
cd project-two
git init
echo "# Second Project" > README.md
git add README.md
git commit -m "Start second project"

# List all repositories in parent directory
cd ..
ls -la */.git
```

### Step 17: Repository Organization

**Best Practices:**
```bash
# Organize repositories in a dedicated directory
mkdir ~/projects
cd ~/projects

# Clone repositories here
git clone <repo-url> project-name

# Keep repositories organized by purpose
mkdir personal-work
mkdir open-source
mkdir work-projects
```

---

## Part 7: Repository Troubleshooting

### Step 18: Common Repository Issues

**Issue: "Not a git repository"**
```bash
# Check if you're in the right directory
pwd
ls -la

# If .git folder is missing, re-initialize (CAUTION: loses history)
git init
```

**Issue: "Remote origin already exists"**
```bash
# Remove existing remote
git remote remove origin

# Add new remote
git remote add origin <new-url>
```

**Issue: "Repository is empty" after clone**
```bash
# Check the URL
git remote -v

# Try HTTPS instead of SSH or vice versa
git remote set-url origin <new-url>
```

**Issue: Permission denied**
```bash
# For HTTPS: Use personal access token instead of password
# For SSH: Check SSH key setup
ssh -T git@github.com
```

---

## Part 8: Repository Best Practices

### Step 19: Repository Structure Guidelines

**Recommended Structure:**
```
my-project/
├── .git/              # Git internal (auto-created)
├── README.md          # Project description
├── .gitignore         # Files to ignore
├── src/               # Source code
├── tests/             # Test files
├── docs/              # Documentation
└── LICENSE            # License file
```

### Step 20: Initial Repository Setup

**Complete Setup Checklist:**
```bash
# 1. Create project directory
mkdir my-project
cd my-project

# 2. Initialize repository
git init

# 3. Create initial files
echo "# My Project" > README.md
echo "node_modules/" > .gitignore

# 4. Make initial commit
git add .
git commit -m "Initial project setup"

# 5. Connect to remote (optional)
git remote add origin <repository-url>
git push -u origin main
```

---

## Practice Exercises

### Exercise 1: Repository Creation
1. Create a new directory called `git-exercise`
2. Initialize it as a Git repository
3. Create at least 3 files (README.md, script file, config file)
4. Add and commit all files
5. View the commit history

### Exercise 2: Repository Cloning
1. Find a public repository on GitHub
2. Clone it to your local machine
3. Explore the repository structure
4. Check the commit history
5. View the remote configuration

### Exercise 3: Multiple Repositories
1. Create two separate repositories in different directories
2. Add different files to each
3. Make commits in both
4. Compare their histories
5. Practice switching between repositories

### Exercise 4: Repository Configuration
1. Set repository-specific user information
2. Configure a custom remote name
3. Add multiple remotes to one repository
4. View and compare different configuration levels

---

## Verification Checklist

- [ ] Created local repository with `git init`
- [ ] Added files and made initial commit
- [ ] Cloned existing repository
- [ ] Explored repository structure (.git folder)
- [ ] Configured repository settings
- [ ] Understood local vs remote repositories
- [ ] Practiced repository maintenance commands

---

## Key Concepts Covered

✅ **Repository Creation:** `git init` for new repos, `git clone` for existing ones
✅ **Repository Structure:** Understanding .git folder and working directory
✅ **Basic Operations:** status, add, commit, log
✅ **Remote Repositories:** Cloning and remote configuration
✅ **Repository Configuration:** Local vs global settings
✅ **Repository Maintenance:** Health checks and optimization

---

## What You've Accomplished

You've successfully:
- Created your first Git repository from scratch
- Added files and made your first commit
- Cloned an existing repository
- Explored Git's internal structure
- Configured repository settings
- Understood the difference between local and remote repositories

---

## Repository Commands Mastered

```bash
git init                    # Create new repository
git clone <url>             # Copy existing repository
git status                  # Check repository state
git add <files>             # Stage files for commit
git commit -m "message"     # Save changes permanently
git log                     # View commit history
git remote -v               # View remote repositories
git config --list           # View configuration
git fsck                    # Check repository health
git gc                      # Optimize repository
```

---

## Next Steps

Now that you have repository basics, you can:

1. [Master Git's state management](workshop-03-git-states.md)
2. [Learn file operations](workshop-04-file-operations.md)
3. [Explore branching](workshop-05-branching.md)
4. [Practice with repository homework](../homeworks/homework-02-repository-management.md)

---

## Reflection Questions

1. What's the difference between `git init` and `git clone`?
2. Why is the .git folder important? What happens if you delete it?
3. How do local and remote repositories work together?
4. Why should you make frequent commits?
5. How do repository-specific settings differ from global settings?

---

## Troubleshooting

### Repository Issues
- **"fatal: not a git repository"**: Check if you're in the correct directory with `ls -la`
- **"Permission denied"**: Verify repository URL and authentication
- **"Repository not found"**: Check if repository exists and is public
- **"Already exists"**: Choose a different local directory name

### Commit Issues
- **"nothing to commit"**: Add files first with `git add`
- **"empty commit"**: Make sure you've made changes to tracked files

---

## Workshop Complete! 🎉

You've created your first Git repositories! You now understand:

- **Repository Creation:** How to start new projects with Git
- **Repository Cloning:** How to work with existing projects
- **Repository Structure:** What's inside a Git repository
- **Basic Workflow:** Add, commit, and track changes
- **Remote Operations:** Working with GitHub/GitLab repositories

**Repository Skills:**
- Local repository creation and management
- Remote repository cloning and configuration
- Repository inspection and maintenance
- Basic Git workflow implementation