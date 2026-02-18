# Workshop 1: Git Installation & Basic Setup

## Duration: 30-45 minutes

## Objective
By the end of this workshop, you will have Git installed and configured on your system, ready for development work.

## Prerequisites
- Computer with internet access
- Administrator privileges (for installation)
- Text editor (optional, for configuration)

## Materials Needed
- Computer (Windows, macOS, or Linux)
- Internet connection
- Command line terminal (built-in on all platforms)

---

## Part 1: Installing Git

### Step 1: Identify Your Operating System

**What you'll do:** Determine which installation guide to follow.

**Instructions:**
1. Check your operating system:
   - Windows: Press `Win + R`, type `winver`, press Enter
   - macOS: Click Apple menu → About This Mac
   - Linux: Open terminal and run `cat /etc/os-release`

2. Note your OS version for reference during troubleshooting

**Expected Result:**
You know your OS and version (e.g., "Windows 11", "macOS Ventura", "Ubuntu 22.04")

---

### Step 2: Download and Install Git

**Windows Users:**

1. Open your web browser and go to: https://git-scm.com/download/win
2. Click the download link (should start automatically)
3. Locate the downloaded file (usually in Downloads folder)
4. Double-click the `.exe` file to start installation
5. Follow the installation wizard:
   - Click "Next" on the information screen
   - Choose components (default is fine):
     - ☑ Git Bash Here
     - ☑ Git GUI Here
     - ☑ Git LFS (Large File Support)
     - ☑ Associate .git* files
     - ☑ Associate .sh files
   - Choose default editor or select your preferred one
   - **Important:** Select "Git from the command line and also from 3rd-party software", click "Next"
   - Choose HTTPS transport (default)
   - Configure line ending conversions (default is fine)
   - Choose terminal emulator (default MinTTY)
   - Choose default behavior of `git pull` (default)
   - Choose credential helper (default)
   - Configure extra options (default)
   - Click "Install"
6. Click "Finish" when installation completes

**macOS Users:**

**Option A: Using Homebrew (Recommended)**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Git
brew install git
```

**Option B: Using Xcode Command Line Tools**
```bash
xcode-select --install
```

**Option C: Download from website**
1. Go to: https://git-scm.com/download/mac
2. Download the latest version
3. Open the downloaded .dmg file
4. Drag Git to Applications folder

**Linux Users (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install git
```

**Linux Users (CentOS/RHEL/Fedora):**
```bash
# CentOS/RHEL
sudo yum install git

# Fedora
sudo dnf install git
```

---

### Step 3: Verify Installation

**Instructions:**
Open a terminal/command prompt and run:
```bash
git --version
```

**Expected Output:**
```
git version 2.34.1
```
(or similar version number)

**If you see an error:**
- Windows: Try opening "Git Bash" instead of Command Prompt
- macOS: Try opening Terminal app
- Linux: Check if Git is in your PATH

---

## Part 2: Basic Git Configuration

### Step 4: Configure Your Identity

**What you'll do:** Tell Git who you are for commit attribution.

**Instructions:**
```bash
# Set your name
git config --global user.name "Your Full Name"

# Set your email
git config --global user.email "your.email@example.com"
```

**Examples:**
```bash
git config --global user.name "John Doe"
git config --global user.email "john.doe@example.com"
```

### Step 5: Verify Configuration

**Instructions:**
```bash
git config --global --list
```

**Expected Output:**
```
user.name=Your Full Name
user.email=your.email@example.com
```

### Step 6: Configure Default Branch Name (Optional)

**Instructions:**
```bash
git config --global init.defaultBranch main
```

This sets `main` as the default branch name instead of `master`.

---

## Part 3: Testing Git Installation

### Step 7: Create a Test Repository

**Instructions:**
```bash
# Create a test directory
mkdir git-test
cd git-test

# Initialize Git repository
git init

# Check status
git status
```

**Expected Output:**
```
Initialized empty Git repository in /path/to/git-test/.git/
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

### Step 8: Create and Commit a Test File

**Instructions:**
```bash
# Create a test file
echo "# My First Git Repository" > README.md
echo "" >> README.md
echo "This is a test repository to verify Git installation." >> README.md

# Stage the file
git add README.md

# Commit the file
git commit -m "Initial commit: Test Git installation"
```

**Expected Output:**
```
[main (root-commit) abc1234] Initial commit: Test Git installation
 1 file changed, 3 insertions(+)
 create mode 100644 README.md
```

### Step 9: View Repository History

**Instructions:**
```bash
git log --oneline
```

**Expected Output:**
```
abc1234 Initial commit: Test Git installation
```

---

## Part 4: Git Help System

### Step 10: Access Git Help

**Instructions:**
```bash
# General help
git help

# Command-specific help
git help config
git help init
git help add

# Or use --help flag
git config --help
```

---



## Part 6: Cleanup

### Step 11: Remove Test Repository

**Instructions:**
```bash
# Go back to parent directory
cd ..

# Remove test repository
rm -rf git-test
```

---

## Verification Checklist

- [ ] Git installed successfully (`git --version` works)
- [ ] User name configured
- [ ] User email configured
- [ ] Default branch set to `main`
- [ ] Test repository created successfully
- [ ] Test file committed
- [ ] Git help system accessible
- [ ] Preferred editor configured (optional)

---

## Troubleshooting Common Issues

### "git: command not found"
**Windows:**
- Make sure you installed Git correctly
- Try using "Git Bash" instead of Command Prompt
- Add Git to your PATH during installation

**macOS:**
- Try reinstalling with Homebrew: `brew install git`
- Check if Xcode Command Line Tools are installed

**Linux:**
- Try: `sudo apt install git` (Ubuntu/Debian)
- Or: `sudo yum install git` (CentOS/RHEL)

### "Please tell me who you are"
**Solution:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### "warning: LF will be replaced by CRLF"
**Solution:** This is normal on Windows, no action needed.

### Permission denied errors
**Solution:** Make sure you're running terminal/command prompt as administrator (Windows) or with sudo (macOS/Linux) for installation.

### Git Bash won't open (Windows)
**Solution:** Reinstall Git and make sure to select "Git Bash Here" during installation.

---

## What You've Accomplished

✅ **Git Installation:** Successfully installed Git on your system
✅ **Configuration:** Set up user identity and preferences
✅ **Verification:** Confirmed Git is working properly
✅ **Repository Creation:** Created and used your first repository
✅ **Basic Workflow:** Experienced add → commit cycle
✅ **Help System:** Learned how to access Git documentation

---

## Git Configuration Levels

| Level | Command | Scope |
|-------|---------|-------|
| System | `git config --system` | All users on machine |
| Global | `git config --global` | All repositories for current user |
| Local | `git config --local` | Current repository only |
| Worktree | `git config --worktree` | Current worktree |

**Recommendation:** Use `--global` for personal settings, `--local` for repository-specific settings.

---

## Essential Git Commands Learned

```bash
git --version          # Check Git version
git config --global    # Configure Git settings
git init               # Create new repository
git status             # Check repository status
git add <file>         # Stage files for commit
git commit -m "msg"    # Commit staged changes
git log --oneline      # View commit history
git help               # Access help system
```

---

## Next Steps

Now that Git is installed and configured, you can:

1. [Create your first repository](workshop-02-first-repo.md)
2. [Learn about Git states](workshop-03-git-states.md)
3. [Master file operations](workshop-04-file-operations.md)
4. [Explore branching](workshop-05-branching.md)
5. Complete [homework assignments](../homeworks/)

---

## Reflection Questions

1. Why is it important to configure your Git identity?
2. What's the difference between global and local Git configuration?
3. Why should you test your Git installation after setup?
4. How does Git's help system help with learning?

---

## Help & Support

- **Installation Issues:** Check the [official Git documentation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- **Configuration Problems:** Run `git config --global -e` to edit config file directly
- **Version Issues:** Always use the latest stable version of Git
- **OS-specific Help:** Check Git documentation for your operating system

---

## Workshop Complete! 🎉

Git is now installed and ready! You've:

- **Installed Git** on your system
- **Configured** your identity and preferences
- **Verified** everything works correctly
- **Created** your first test repository
- **Experienced** basic Git workflow

**Your development environment is ready for:**
- Repository creation and management
- File tracking and version control
- Collaboration and remote work
- Professional development workflows

**Next:** [Create your first repository](workshop-02-first-repo.md) to start building projects with Git!