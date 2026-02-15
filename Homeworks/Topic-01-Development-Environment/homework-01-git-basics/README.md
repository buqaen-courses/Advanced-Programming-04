# Homework 01: Git Installation & Basic Setup

## 📋 Overview

This homework focuses on getting Git installed and configured on your system, and learning the fundamental Git operations for version control.

## 🎯 Learning Objectives

By completing this homework, you will be able to:

- Install Git on your operating system (Windows, macOS, or Linux)
- Configure Git with your personal information
- Create and initialize a Git repository
- Perform basic Git operations (status, add, commit)
- Understand Git's three-area structure

## 📝 Assignment Tasks

### Part 1: Git Installation & Configuration

1. **Install Git** on your system following the appropriate guide for your OS:
   - [Windows Installation Guide](../installation/windows-setup.md)
   - [macOS Installation Guide](../installation/macos-setup.md)
   - [Linux Installation Guide](../installation/linux-setup.md)

2. **Verify Installation**:
   ```bash
   git --version
   ```

3. **Configure Git** with your information:
   ```bash
   git config --global user.name "Your Full Name"
   git config --global user.email "your.email@example.com"
   ```

4. **Verify Configuration**:
   ```bash
   git config --global --list
   ```

### Part 2: Creating Your First Repository

1. **Create a project directory**:
   ```bash
   mkdir my-first-git-project
   cd my-first-git-project
   ```

2. **Initialize Git repository**:
   ```bash
   git init
   ```

3. **Create a README file**:
   ```bash
   echo "# My First Git Project" > README.md
   echo "This is my first Git repository!" >> README.md
   ```

4. **Check repository status**:
   ```bash
   git status
   ```

5. **Stage and commit your changes**:
   ```bash
   git add README.md
   git commit -m "Initial commit: Add README file"
   ```

### Part 3: Basic Git Operations

1. **Modify the README file**:
   ```bash
   echo "## Features" >> README.md
   echo "- Version control with Git" >> README.md
   echo "- Basic repository management" >> README.md
   ```

2. **Check the changes**:
   ```bash
   git status
   git diff
   ```

3. **Stage and commit the changes**:
   ```bash
   git add README.md
   git commit -m "Add features section to README"
   ```

4. **View commit history**:
   ```bash
   git log --oneline
   ```

## 📁 Submission Requirements

Create the following files in this folder:

```
homework-01-git-basics/
├── README.md                    # This file (update with your work)
├── installation-verification.txt # Output of git --version
├── git-config.txt              # Output of git config --global --list
├── repository-setup.txt        # Commands and output from repository creation
├── basic-operations.txt        # Commands and output from Part 3
└── project-files/              # Your my-first-git-project folder
    ├── .git/                   # Git repository (should be included)
    ├── README.md               # Your created README file
    └── ...                     # Any other files you created
```

## ✅ Verification Checklist

- [ ] Git is installed and `git --version` works
- [ ] Git is configured with your name and email
- [ ] Created a Git repository with `git init`
- [ ] Created and committed at least one file
- [ ] Made modifications and created additional commits
- [ ] Can view commit history with `git log`
- [ ] Understand the difference between working directory, staging area, and repository

## 🆘 Troubleshooting

### Common Issues:

1. **Permission denied**: Make sure you're running terminal/command prompt as administrator (Windows) or using `sudo` (macOS/Linux)

2. **Command not found**: Ensure Git was added to your PATH during installation

3. **Git not configured**: Double-check your `git config` commands

4. **Repository not initialized**: Make sure you're in the correct directory when running `git init`

## 📚 Resources

- [Git Official Documentation](https://git-scm.com/doc)
- [Workshop: Git Installation](../workshops/workshop-01-git-installation.md)
- [Tutorial: Git Introduction](../sections/section-01/tutorial.md)

## 📝 Notes

- This homework builds the foundation for all future Git work in the course
- Keep this repository as you'll use it in future homework assignments
- Document any issues you encountered and how you resolved them