# Workshop 3: Git States and File Lifecycle

## Duration: 75-90 minutes

## Objective
By the end of this workshop, you will master Git's three main areas (working directory, staging area, repository) and understand how files move through different states during the development process.

## Prerequisites
- Git installed and configured ([Workshop 1](workshop-01-basic-setup.md))
- Basic repository operations ([Workshop 2](workshop-02-first-repo.md))
- Understanding of Git concepts ([Tutorial 3](../tutorials/03-repository-basics.md))

## Materials Needed
- Computer with Git installed
- Terminal/command prompt
- Text editor
- Sample project files

---

## Part 1: Understanding Git's Three Areas

### Step 1: Git Areas Overview

**Discussion Points:**
Git operates with three main areas where your files can exist:

1. **Working Directory**: Your local file system where you edit files
2. **Staging Area (Index)**: Preparation area for the next commit
3. **Repository**: Where committed snapshots are permanently stored

**Visual Concept:**
```
Working Directory ── git add ──► Staging Area ── git commit ──► Repository
       ▲                           │                           │
       │                           │                           │
       └──── git restore ──────────┘                           │
           (discard changes)                                   │
                                                               │
                                               ┌───────────────┘
                                               │
                                               ▼
Repository ◄── git reset ─── Staging Area ◄── git reset ─── Working Directory
   HEAD                           HEAD                    (modified files)
```

### Step 2: Create Practice Repository

**Instructions:**
```bash
mkdir git-states-practice
cd git-states-practice
git init
echo "# Git States Practice" > README.md
git add README.md
git commit -m "Initial commit"
```

---

## Part 2: Exploring File States

### Step 3: Untracked Files

**What you'll do:** Experience the untracked state.

**Instructions:**
```bash
# Create new files
echo "print('Hello, World!')" > hello.py
echo "function greet() { return 'Hi!'; }" > hello.js

# Check status
git status
```

**Expected Output:**
```
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.js
        hello.py

nothing added to commit but untracked files present (use "git add" to track)
```

**Key Points:**
- Untracked files exist in working directory but Git doesn't know about them
- They won't be included in commits unless staged
- Use `.gitignore` to permanently ignore certain files

### Step 4: Staging Files

**Instructions:**
```bash
# Stage one file
git add hello.py

# Check status
git status
```

**Expected Output:**
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.js
```

**Discussion:**
- `hello.py` is now in staging area (ready for commit)
- `hello.js` remains untracked
- You can stage files selectively

### Step 5: Mixed States - Modified Files

**Instructions:**
```bash
# Modify the staged file
echo "print('Hello, Git World!')" >> hello.py

# Check status
git status
```

**Expected Output:**
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   hello.py
```

**Key Insight:**
- Same file can have staged AND unstaged changes!
- This shows Git's granular control over file states

---

## Part 3: State Transitions

### Step 6: Working Directory → Staging Area

**Instructions:**
```bash
# Stage the modified file again
git add hello.py

# Check status
git status
```

**Expected Output:**
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py
```

### Step 7: Staging Area → Repository

**Instructions:**
```bash
# Commit staged changes
git commit -m "Add hello.py with greeting function"

# Check status
git status
git log --oneline
```

**Expected Output:**
```
On branch main
nothing to commit, working tree clean

abc1234 Add hello.py with greeting function
xyz7890 Initial commit
```

### Step 8: Repository → Modified (Working Directory)

**Instructions:**
```bash
# Modify existing file
echo "# Updated greeting" >> hello.py
echo "print('Welcome to Git!')" >> hello.py

git status
```

**Expected Output:**
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   hello.py
```

---

## Part 4: Advanced State Management

### Step 9: Selective Staging with git add -p

**Instructions:**
```bash
# Create multiple changes in one file
echo "" >> hello.py
echo "# New feature comment" >> hello.py
echo "def farewell():" >> hello.py
echo "    return 'Goodbye!'" >> hello.py

# Try interactive staging
git add -p hello.py
```

**Interactive Prompts:**
- `y` - yes, stage this hunk
- `n` - no, don't stage this hunk
- `s` - split the hunk into smaller pieces
- `q` - quit, don't stage anything else

### Step 10: Unstaging Changes

**Instructions:**
```bash
# Unstage all changes
git reset

# Check status
git status
```

**Expected Output:**
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   hello.py
```

### Step 11: Discarding Working Directory Changes

**Instructions:**
```bash
# Discard all working directory changes
git restore hello.py

# Check status and file content
git status
cat hello.py
```

**Expected Output:**
- File reverts to last committed version
- No changes shown in status

---

## Part 5: Complex State Scenarios

### Step 12: Files in Multiple States Simultaneously

**Instructions:**
```bash
# Modify file
echo "# Feature A" >> hello.py
git add hello.py

# Modify again (creates staged + unstaged changes)
echo "# Feature B" >> hello.py

git status
```

**Expected Output:**
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   hello.py
```

### Step 13: Using git diff to Compare States

**Instructions:**
```bash
# Working directory vs staging area
git diff

# Staging area vs last commit
git diff --staged

# Working directory vs last commit
git diff HEAD
```

**Discussion:**
- `git diff`: Shows unstaged changes
- `git diff --staged`: Shows staged changes
- `git diff HEAD`: Shows all changes (staged + unstaged)

### Step 14: Committing Only Staged Changes

**Instructions:**
```bash
# Commit only staged changes
git commit -m "Add feature A"

# Check what remains
git status
git diff
```

**Expected Output:**
- Only Feature B changes remain (unstaged)

---

## Part 6: State Troubleshooting

### Step 15: Accidentally Staged Wrong File

**Scenario:** You staged a file you didn't want to commit.

**Instructions:**
```bash
# Create a file you don't want to commit
echo "Secret password: 12345" > sensitive.txt
git add sensitive.txt

git status
```

**Recovery:**
```bash
# Unstage the file
git reset HEAD sensitive.txt

# File is back to untracked/modified state
git status

# Remove the file completely
rm sensitive.txt
```

### Step 16: Lost Changes Recovery

**Scenario:** You discarded changes you wanted to keep.

**Instructions:**
```bash
# Make changes and commit
echo "Important work" >> hello.py
git add hello.py
git commit -m "Important changes"

# Accidentally discard changes (don't do this!)
echo "More work" >> hello.py
git restore hello.py  # Oops!

# Changes are gone!
cat hello.py
```

**Recovery:**
```bash
# Use reflog to find the commit
git reflog

# Find the commit hash, then restore
git restore --source=<commit-hash> hello.py
```

---

## Part 7: Advanced State Commands

### Step 17: git reset Variations

**Instructions:**
```bash
# Make some changes and commits first
echo "Change 1" >> hello.py
git add hello.py
git commit -m "Change 1"

echo "Change 2" >> hello.py
git add hello.py
git commit -m "Change 2"

echo "Change 3" >> hello.py
git add hello.py
git commit -m "Change 3"

git log --oneline
```

**Reset Types:**
```bash
# Soft reset (keeps changes staged)
git reset --soft HEAD~1
git status  # Changes are staged

# Mixed reset (keeps changes unstaged) - default
git reset HEAD~1
git status  # Changes are unstaged

# Hard reset (destroys changes) - DANGER!
git reset --hard HEAD~1  # DON'T DO THIS WITH REAL WORK
```

### Step 18: git rm vs git rm --cached

**Instructions:**
```bash
# Create and track a file
echo "Temporary file" > temp.txt
git add temp.txt
git commit -m "Add temp file"

# Remove from working directory AND staging area
git rm temp.txt
git status  # Shows deleted file staged

# Restore it
git restore temp.txt

# Remove from staging area ONLY (keep in working directory)
git rm --cached temp.txt
git status  # File is untracked again
```

---

## Part 8: State Visualization

### Step 19: Complete State Workflow

**Instructions:**
Let's create a comprehensive example showing all states:

```bash
# Start clean
git status

# 1. Create untracked file
echo "New project file" > project.txt
git status  # Shows untracked

# 2. Stage the file
git add project.txt
git status  # Shows staged

# 3. Modify staged file (creates mixed state)
echo "Additional content" >> project.txt
git status  # Shows staged + unstaged changes
git diff     # Shows unstaged changes
git diff --staged  # Shows staged changes

# 4. Stage all changes
git add project.txt
git status  # Shows fully staged

# 5. Commit
git commit -m "Add project file with complete content"
git status  # Clean

# 6. Modify committed file
echo "Post-commit changes" >> project.txt
git status  # Shows modified
```

---

## Part 9: Best Practices Demonstration

### Step 20: Clean Commit Workflow

**Instructions:**
```bash
# Good practice: Check status before committing
git status

# Good practice: Review changes before staging
git diff

# Good practice: Stage logically related changes
git add -p  # Interactive staging

# Good practice: Write meaningful commit messages
git commit -m "feat: add user authentication module

- Add login function
- Add password validation
- Update user model"

# Good practice: Keep main branch clean
git log --oneline
```

---

## Part 10: State Management Commands Summary

### Essential Commands:

```bash
git status              # Check current state
git add <file>          # Working Directory → Staging Area
git commit -m "msg"     # Staging Area → Repository
git diff                # Compare Working Directory vs Staging Area
git diff --staged       # Compare Staging Area vs Repository
git diff HEAD           # Compare Working Directory vs Repository
git checkout -- <file>  # Repository → Working Directory (discard changes)
git reset HEAD <file>   # Staging Area → Working Directory (unstaging)
git reset --hard HEAD   # Repository → Working Directory + Staging Area
```

### Advanced Commands:

```bash
git add -p              # Interactive staging
git rm --cached <file>  # Remove from staging (keep in working directory)
git reset --soft HEAD~1 # Uncommit but keep staged
git reset --mixed HEAD~1# Uncommit and unstage (default)
git reset --hard HEAD~1 # Uncommit and discard changes (dangerous)
```

---

## Practice Exercises

### Exercise 1: State Exploration
1. Create 3 new files in different states (untracked, staged, modified)
2. Use `git status` to observe each state
3. Move files between states using appropriate commands
4. Document the commands used for each transition

### Exercise 2: Selective Staging
1. Modify a file in 3 different places
2. Use `git add -p` to stage only 2 of the 3 changes
3. Commit the staged changes
4. Verify what was committed vs what remains

### Exercise 3: State Recovery
1. Make changes to a file and stage them
2. Use different `git reset` commands to see their effects
3. Practice discarding changes safely
4. Use `git reflog` to track your actions

### Exercise 4: Complex State Scenario
1. Create a file with multiple changes
2. Stage some changes but not others
3. Modify the already-staged parts
4. Use `git diff` commands to understand what's where
5. Commit only specific parts of the changes

---

## Troubleshooting Guide

### "Nothing added to commit but untracked files present"
**Cause:** You have untracked files that need to be staged
**Solution:** `git add .` or `git add <filename>`

### "Changes not staged for commit"
**Cause:** Modified files need to be staged
**Solution:** `git add <filename>` or `git add .`

### "No changes added to commit"
**Cause:** No staged changes to commit
**Solution:** Stage changes first with `git add`

### "Untracked files would be overwritten by checkout"
**Cause:** Untracked files conflict with checkout target
**Solution:** Remove untracked files or use `git checkout --force`

### Lost changes after reset --hard
**Cause:** Used dangerous command
**Solution:** Check `git reflog` and use `git restore --source=<commit> <file>` to recover

---

## Key Concepts Mastered

✅ **Git's Three Areas:** Working Directory, Staging Area, Repository

✅ **File States:** Untracked, Modified, Staged, Committed

✅ **State Transitions:** Understanding how files move between states

✅ **Selective Staging:** Using `git add -p` for granular control

✅ **State Inspection:** Using `git status` and `git diff` effectively

✅ **State Recovery:** Safe ways to undo changes

✅ **Best Practices:** Clean commits and safe workflows



## Next Steps

Now that you understand Git states, you can:

1. [Learn branching fundamentals](workshop-04-branching.md)
2. [Explore advanced state management](../tutorials/05-advanced-states.md)
3. [Practice with state-focused homework](../homeworks/homework-03-git-states-files.md)

---

## Reflection Questions

1. Why does Git have a staging area? What problem does it solve?
2. What's the difference between `git reset HEAD` and `git restore`?
3. When would you use `git add -p` instead of `git add .`?
4. How can understanding states help you avoid losing work?
5. What's the safest way to undo changes in Git?


