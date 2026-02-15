# Homework 02: Creating Your First Repository

## 📋 Overview

This homework focuses on creating and understanding Git repositories, both local and remote. You'll learn how to initialize repositories, make your first commits, and understand repository structure.

## 🎯 Learning Objectives

By completing this homework, you will be able to:

- Create and initialize new Git repositories
- Understand repository structure and the `.git` folder
- Make commits and view repository history
- Clone existing repositories
- Configure repository settings

## 📝 Assignment Tasks

### Part 1: Creating Local Repositories

1. **Create a new project directory**:
   ```bash
   mkdir my-git-project
   cd my-git-project
   ```

2. **Initialize Git repository**:
   ```bash
   git init
   ```

3. **Explore repository structure**:
   ```bash
   ls -la
   ls -la .git/
   git status
   ```

### Part 2: Making Your First Commits

1. **Create initial files**:
   ```bash
   echo "# My Git Project" > README.md
   echo "print('Hello from Git!')" > hello.py
   mkdir docs
   echo "# Project Documentation" > docs/guide.md
   ```

2. **Stage and commit files**:
   ```bash
   git add README.md
   git commit -m "Add project README"

   git add hello.py
   git commit -m "Add main script"

   git add docs/
   git commit -m "Add documentation folder"
   ```

3. **View commit history**:
   ```bash
   git log --oneline
   git log --oneline --graph
   ```

### Part 3: Working with Existing Repositories

1. **Clone the course repository**:
   ```bash
   cd ..
   git clone https://github.com/buqaen-courses/Advanced-Programming-04.git course-repo
   cd course-repo
   ```

2. **Explore cloned repository**:
   ```bash
   git remote -v
   git branch -a
   git log --oneline -5
   ```

### Part 4: Repository Configuration

1. **Check current configuration**:
   ```bash
   git config --list
   git config user.name
   git config user.email
   ```

2. **Set repository-specific settings** (optional):
   ```bash
   git config user.name "Project Author"
   git config user.email "project@example.com"
   ```

### Part 3: Remote Operations

1. **Check remote status**:
   ```bash
   git status
   git remote -v
   ```

2. **Pull latest changes** (if any):
   ```bash
   git pull origin main
   ```

3. **Push your branch**:
   ```bash
   git push -u origin homework-topic-01
   ```

## 📁 Submission Requirements

Create the following files in this folder:

```
homework-02-repository-management/
├── README.md                    # This file (update with your work)
├── clone-commands.txt          # Commands and output from cloning
├── branch-operations.txt       # Branch creation and switching commands
├── remote-operations.txt       # Remote repository operations
└── repository-state.txt        # Final repository status and branch info
```

## ✅ Verification Checklist

- [ ] Successfully cloned the course repository
- [ ] Created and switched to a new branch
- [ ] Made commits on your branch
- [ ] Understood remote repository operations
- [ ] Can push changes to remote repository

## 📚 Resources

- [Tutorial: Repository Basics](../sections/section-02/tutorial.md)
- [Workshop: Repository Workshop](../sections/section-02/workshop.md)