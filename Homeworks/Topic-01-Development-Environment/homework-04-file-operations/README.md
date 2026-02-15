# Homework 04: File Operations & Remote Repositories

## 📋 Overview

This homework focuses on advanced file operations in Git and working with remote repositories. You'll learn how to effectively manage files, push changes to remotes, and collaborate using Git.

## 🎯 Learning Objectives

By completing this homework, you will be able to:

- Master selective file staging and committing
- Work with multiple files and complex changes
- Push local changes to remote repositories
- Pull updates from remote repositories
- Handle file renaming, moving, and deletion with Git
- Understand remote repository workflows

## 📝 Assignment Tasks

### Part 1: Advanced File Staging

1. **Create a project repository**:
   ```bash
   mkdir file-ops-project
   cd file-ops-project
   git init
   ```

2. **Set up initial project structure**:
   ```bash
   echo "# File Operations Project" > README.md
   echo "print('Main script')" > main.py
   mkdir utils
   echo "def helper(): pass" > utils/helpers.py
   mkdir tests
   echo "# Test file" > tests/test_main.py
   ```

3. **Practice different staging methods**:
   ```bash
   # Stage all files
   git add .

   # Check status
   git status

   # Commit initial structure
   git commit -m "Initial project structure"
   ```

### Part 2: Selective Staging and Complex Changes

1. **Make multiple changes across files**:
   ```bash
   # Update main script
   echo "from utils.helpers import helper" >> main.py
   echo "helper()" >> main.py
   echo "print('Enhanced main script')" >> main.py

   # Update helper
   echo "def helper():" > utils/helpers.py
   echo "    return 'Helper function'" >> utils/helpers.py

   # Add new test
   echo "def test_helper():" > tests/test_utils.py
   echo "    assert helper() == 'Helper function'" >> tests/test_utils.py
   ```

2. **Use interactive staging**:
   ```bash
   git add -p
   # Review each hunk and decide whether to stage it
   ```

3. **Commit selectively**:
   ```bash
   git commit -m "Add helper function and basic implementation"
   git status  # Check what remains unstaged
   ```

### Part 3: File Management Operations

1. **Rename files with Git**:
   ```bash
   git mv main.py app.py
   git status
   git commit -m "Rename main.py to app.py"
   ```

2. **Move files between directories**:
   ```bash
   mkdir src
   git mv app.py src/
   git mv utils/* src/
   git status
   git add .
   git commit -m "Reorganize code into src directory"
   ```

3. **Remove files properly**:
   ```bash
   # Remove from working directory and staging
   git rm tests/test_main.py

   # Remove from staging only (keep in working directory)
   echo "Temporary file" > temp.txt
   git add temp.txt
   git rm --cached temp.txt
   rm temp.txt
   ```

### Part 4: Working with Remote Repositories

1. **Create a GitHub repository**:
   - Go to GitHub and create a new repository
   - Name it `file-ops-project` or similar
   - Keep it empty (don't initialize with README)

2. **Connect local repository to remote**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/file-ops-project.git
   git remote -v
   ```

3. **Push your work to GitHub**:
   ```bash
   git push -u origin main
   ```

4. **Verify on GitHub**:
   - Check that all files are uploaded
   - Review commit history
   - Try editing a file directly on GitHub

### Part 5: Remote Workflow Practice

1. **Make changes locally**:
   ```bash
   echo "# Project configuration" > config.py
   echo "DEBUG = True" >> config.py
   git add config.py
   git commit -m "Add project configuration"
   git push
   ```

2. **Simulate collaboration**:
   - Edit a file directly on GitHub
   - Pull the changes locally:
   ```bash
   git pull origin main
   ```

3. **Handle merge scenarios**:
   ```bash
   # Make local changes
   echo "# Local changes" >> README.md
   git add README.md
   git commit -m "Update README locally"

   # Pull remote changes
   git pull origin main  # May create a merge commit
   ```

### Part 6: File History and Diff Analysis

1. **View detailed commit information**:
   ```bash
   git show HEAD
   git show HEAD~1
   ```

2. **Compare different versions**:
   ```bash
   git diff HEAD~2 HEAD
   git log --oneline --graph
   ```

3. **Track file changes over time**:
   ```bash
   git log --follow -- src/app.py
   ```

## 📊 Deliverables

### Repository Structure
Your repository should contain:
```
file-ops-project/
├── .git/
├── README.md
├── config.py
├── src/
│   ├── app.py
│   └── helpers.py (in utils/)
└── tests/
    └── test_utils.py
```

### Git History
Your repository should show a clear progression:
- Initial commit with basic structure
- Multiple commits showing file operations
- Commits demonstrating remote operations
- Clear, descriptive commit messages

### Remote Repository
- Public GitHub repository with all files
- Multiple commits visible in history
- Proper repository description and README

## ✅ Verification Checklist

- [ ] Repository created and initialized
- [ ] Multiple files staged and committed selectively
- [ ] Interactive staging (`git add -p`) practiced
- [ ] Files renamed and moved using Git commands
- [ ] Files properly removed with `git rm`
- [ ] Remote repository created on GitHub
- [ ] Local repository connected to remote
- [ ] Changes pushed to remote successfully
- [ ] Remote changes pulled locally
- [ ] Commit history reviewed and understood
- [ ] File changes tracked over time

## 🆘 Troubleshooting Guide

### "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin <new-url>
```

### "failed to push some refs"
```bash
git pull --rebase origin main
git push
```

### "Changes not staged for commit"
```bash
git add .
# or
git add <specific-files>
```

### Interactive add not working
Use regular `git add` commands instead of `-p` flag.

## 📚 Additional Resources

- [Git File Operations Documentation](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
- [GitHub Guides](https://guides.github.com/)

## 🎯 Success Criteria

Your homework is complete when:
- You can confidently stage files selectively
- You understand when to use different Git commands for file operations
- Your repository is properly connected to GitHub
- You can push and pull changes effectively
- Your commit history tells a clear story of your development process

**Estimated completion time: 90-120 minutes**