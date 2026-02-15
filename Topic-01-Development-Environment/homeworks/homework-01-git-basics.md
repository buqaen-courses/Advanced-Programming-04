# Homework 1 — Practical Introduction to Git and Local Version Control

*(Warm-up exercise — no submission required)*

**Estimated duration:** 90–120 minutes
**Level:** Absolute beginner
**Purpose:** To gain hands-on understanding of how Git tracks, stores, and manages file changes locally.

---

## 1. Overall Objective

In this exercise, you will learn — through direct practice — how to:

* Understand what Git is and why it is used
* Put a project under version control
* Track changes made to files
* Create and store project versions (commits)
* View project history
* Safely experiment and revert changes

This exercise is designed purely for familiarization and practical understanding of Git fundamentals.

---

## 2. What Does Git Actually Do?

In software development, files change constantly.
Without version control:

* You cannot easily track what changed
* Returning to previous versions is difficult
* Collaboration becomes complicated

Git solves these problems.

Git records **snapshots of your entire project** at specific moments in time.
Each snapshot represents an official version of the project that can be revisited later.

As a result:

* Changes are traceable
* Previous versions are preserved
* Safe experimentation becomes possible

---

## 3. Installing and Preparing Git

### Step 1 — Install Git

Visit:

[https://git-scm.com/downloads](https://git-scm.com/downloads)

Download and install the version for your operating system.
If unsure about installation options, accept the default settings.

---

### Step 2 — Verify Installation

Open a terminal or command prompt and run:

```bash
git --version
```

If a version number appears, Git is installed successfully.

---

## 4. Configure Your Identity

Git records who makes each change.
You must configure your name and email once.

```bash
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```

These settings apply to all your projects.

To verify:

```bash
git config --global --list
```

---

## 5. Create Your First Git Project

### Step 1 — Create a Project Folder

```bash
mkdir my-first-git-project
cd my-first-git-project
```

---

### Step 2 — Initialize Git

```bash
git init
```

This activates Git in the current directory and creates a hidden `.git` folder.

This folder contains:

* Project history
* Configuration
* Branch information
* Internal Git data

Deleting this folder removes all Git history.

---

## 6. Create a File and Check Project Status

Create a file:

```bash
echo "Hello Git" > README.md
```

Check project status:

```bash
git status
```

Git reports that a new file exists but is not yet tracked.

This means:

**Git sees the file but is not managing it yet.**

---

## 7. Add Changes to the Staging Area

Git records changes in two steps:

1. Select changes
2. Permanently record them

Step one:

```bash
git add README.md
```

Git is now ready to record this file.

---

## 8. Create Your First Commit

Step two:

```bash
git commit -m "Initial project version"
```

A permanent version of the project is now stored.

Each commit includes:

* File states
* Timestamp
* Author
* Message

---

## 9. View Project History

```bash
git log
```

Or a shorter version:

```bash
git log --oneline
```

Each entry represents one project version.

---

## 10. Modify a File and Create a New Version

Edit the file:

```bash
echo "Version 2" >> README.md
```

View changes:

```bash
git diff
```

Save the new version:

```bash
git add README.md
git commit -m "Update README"
```

Your project now has multiple versions.

---

## 11. Git’s Three-Area Structure

This is a fundamental concept.

Git has three main areas:

### 1. Working Directory

Where you edit files.

### 2. Staging Area

Where selected changes are prepared for commit.

### 3. Repository

Where committed versions are permanently stored.

Workflow:

Edit → Stage → Commit

---

## 12. Experiment and Revert Changes

Make a temporary change:

```bash
echo "temporary change" >> README.md
```

Revert it:

```bash
git restore README.md
```

The file returns to the last committed version.

This is one of Git’s most important capabilities.

---

## 13. View Complete Version History

```bash
git log --oneline
```

You can observe the project’s evolution over time.

---

## 14. Conceptual Summary

In this exercise you:

* Installed Git
* Created a repository
* Created and modified files
* Saved versions
* Viewed history
* Reverted experimental changes

You now understand the basic idea of version control.

---

## 15. Git Commands Used in This Exercise

| Command                          | Purpose               | Simple Explanation             |
| -------------------------------- | --------------------- | ------------------------------ |
| `git --version`                  | Check installation    | Displays installed Git version |
| `git config --global user.name`  | Set username          | Identifies the author          |
| `git config --global user.email` | Set email             | Records author email           |
| `git config --global --list`     | View settings         | Shows current configuration    |
| `git init`                       | Initialize repository | Activates Git in a folder      |
| `git status`                     | Check status          | Shows file tracking state      |
| `git add <file>`                 | Stage file            | Select changes for commit      |
| `git add .`                      | Stage all changes     | Add everything                 |
| `git commit -m "message"`        | Save version          | Record permanent snapshot      |
| `git log`                        | View history          | Full commit history            |
| `git log --oneline`              | Short history         | Compact history view           |
| `git diff`                       | Show changes          | Compare with last commit       |
| `git restore <file>`             | Undo changes          | Revert file to last commit     |

---

## 16. Final Note

This exercise is intended solely for familiarization.
Its purpose is to help you understand how Git:

* Tracks changes
* Stores versions
* Enables safe rollback

These fundamentals form the foundation for advanced Git concepts such as branching, merging, and collaboration.

