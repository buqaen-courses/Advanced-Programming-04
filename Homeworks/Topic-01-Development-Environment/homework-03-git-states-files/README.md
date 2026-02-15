# Homework 03: Git States Mastery

## 📋 Overview

This homework focuses on mastering Git's three-area architecture (working directory, staging area, repository) and understanding how files move between different states during development.

## 🎯 Learning Objectives

By completing this homework, you will be able to:

- Understand Git's three main areas and their purposes
- Track files through all possible states (untracked, modified, staged, committed)
- Use appropriate commands to move files between states
- Apply selective staging techniques
- Troubleshoot and resolve state-related issues

## 📝 Assignment Tasks

### Part 1: Exploring File States

1. **Create a practice repository**:
   ```bash
   mkdir git-states-practice
   cd git-states-practice
   git init
   echo "# Git States Practice" > README.md
   git add README.md
   git commit -m "Initial commit"
   ```

2. **Demonstrate all file states**:
   - **Untracked**: Create new files and observe `git status`
   - **Modified**: Edit existing files and see changes
   - **Staged**: Add files to staging area with `git add`
   - **Committed**: Commit staged changes

### Part 2: State Transitions

1. **Working Directory → Staging Area**:
   ```bash
   # Create/modify files
   echo "New content" > newfile.txt
   echo "More content" >> README.md

   # Stage changes
   git add newfile.txt
   git add README.md
   git status
   ```

2. **Staging Area → Repository**:
   ```bash
   git commit -m "Add new file and update README"
   git status
   ```

3. **Repository → Modified (Working Directory)**:
   ```bash
   echo "Additional changes" >> newfile.txt
   git status
   ```

### Part 3: Advanced State Management

1. **Selective staging with `git add -p`**:
   ```bash
   # Make multiple changes to a file
   echo "Change 1" >> README.md
   echo "Change 2" >> README.md
   echo "Change 3" >> README.md

   # Stage interactively
   git add -p README.md
   ```

2. **Unstaging changes**:
   ```bash
   git reset HEAD <filename>
   git status
   ```

3. **Discarding working directory changes**:
   ```bash
   git checkout -- <filename>
   ```

### Part 4: Complex State Scenarios

1. **Files in multiple states simultaneously**:
   ```bash
   # Modify a staged file
   git add README.md
   echo "Unstaged change" >> README.md
   git status
   git diff     # Shows unstaged changes
   git diff --staged  # Shows staged changes
   ```

2. **Compare different state combinations**:
   ```bash
   git diff HEAD  # Working directory vs last commit
   ```

### Part 5: State Troubleshooting

1. **Recover accidentally staged files**:
   ```bash
   echo "Secret data" > sensitive.txt
   git add sensitive.txt
   git reset HEAD sensitive.txt
   rm sensitive.txt
   ```

2. **Use reflog to recover lost changes**:
   ```bash
   git reflog
   git checkout <commit-hash> -- <filename>
   ```
   - Delete a file from working directory
   - Stage the deletion
   - Commit the removal

4. **Rename/move files**:
   - Rename a file using `git mv`
   - Move files between directories
   - Commit the changes

### Part 3: Advanced Operations

1. **Unstage changes**:
   ```bash
   git reset HEAD <file>
   ```

2. **Discard working directory changes**:
   ```bash
   git checkout -- <file>
   # or
   git restore <file>
   ```

3. **View detailed history**:
   ```bash
   git log --stat
   git show <commit-hash>
   ```

## 📁 Submission Requirements

Create the following files in this folder:

```
homework-03-git-states-files/
├── README.md                    # This file (update with your work)
├── git-states-demo.txt         # Commands demonstrating the three areas
├── file-operations.txt         # File creation, modification, deletion commands
├── advanced-operations.txt     # Unstaging, discarding, and history commands
└── repository-snapshot/        # Copy of your repository at completion
    ├── .git/                   # Git repository data
    └── ...                     # Your project files
```

## ✅ Verification Checklist

- [ ] Understand and can explain Git's three areas
- [ ] Can move files between different Git states
- [ ] Proficient with staging and unstaging operations
- [ ] Can handle file additions, modifications, and deletions
- [ ] Know how to discard unwanted changes
- [ ] Can view detailed commit history

## 📚 Resources

- [Tutorial: Understanding Git States](../sections/section-03/tutorial.md)
- [Workshop: File Operations Workshop](../sections/section-03/workshop.md)