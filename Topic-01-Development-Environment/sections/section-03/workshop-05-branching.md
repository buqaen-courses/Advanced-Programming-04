# Workshop 5: Branching Basics

## Duration: 60-75 minutes

## Objective
By the end of this workshop, you will understand Git branching, create and manage branches, and merge changes safely.

## Prerequisites
- Git installed and configured ([Workshop 1](workshop-01-basic-setup.md))
- Basic repository operations ([Workshop 2](workshop-02-first-repo.md))
- File operations ([Workshop 4](workshop-04-file-operations.md))
- Understanding of Git states ([Tutorial 3](../tutorials/03-git-states.md))

## Materials Needed
- Computer with Git installed
- Terminal/command prompt
- Text editor
- GitHub account (optional, for remote operations)

---

## Part 1: Understanding Branches

### Step 1: What is a Branch?

**Discussion Points:**
- A branch is a parallel version of your repository
- Main branch (usually `main` or `master`) is the default
- Branches allow safe experimentation
- Each branch has its own commit history
- Branches can be merged back together

**Visual Concept:**
```
main: A ── B ── C ── D
                   │
feature:           └─ E ── F
```

### Step 2: Create Test Repository

**Instructions:**
```bash
mkdir git-branching-practice
cd git-branching-practice
git init
echo "# Branching Practice" > README.md
git add README.md
git commit -m "Initial commit"
```

---

## Part 2: Creating and Switching Branches

### Step 3: View Current Branches

**What you'll do:** Check existing branches in your repository.

**Instructions:**
```bash
git branch
```

**Expected Result:**
```
* main
```

(The asterisk shows your current branch)

### Step 4: Create a New Branch

**Instructions:**
```bash
git branch feature-login
```

**Expected Result:**
- No output (branch created)
- Run `git branch` again to see both branches

### Step 5: Switch to New Branch

**Instructions:**
```bash
git checkout feature-login
# or (newer syntax):
git switch feature-login
```

**Expected Result:**
```bash
Switched to branch 'feature-login'
```

### Step 6: Verify Branch Switch

**Instructions:**
```bash
git branch
git status
```

**Expected Result:**
```
  main
* feature-login
```

---

## Part 3: Working on Branches

### Step 7: Make Changes on Feature Branch

**Instructions:**
```bash
echo "Login functionality" > login.js
echo "User authentication module" >> login.js
git add login.js
git commit -m "Add basic login functionality"
```

### Step 8: Switch Back to Main

**Instructions:**
```bash
git checkout main
# or: git switch main
```

**Expected Result:**
- Notice that `login.js` is gone! (because it only exists on the feature branch)

### Step 9: Create Another Feature Branch

**Instructions:**
```bash
git checkout -b feature-ui
# This creates AND switches to the new branch
```

### Step 10: Make UI Changes

**Instructions:**
```bash
mkdir styles
echo "body { font-family: Arial; }" > styles/main.css
git add styles/
git commit -m "Add basic styling"
```

---

## Part 4: Merging Branches

### Step 11: Merge Feature Branch into Main

**Instructions:**
```bash
git checkout main
git merge feature-ui
```

**Expected Result:**
```
Updating 0f8a2d3..4c9e1f5
Fast-forward
 styles/main.css | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 styles/main.css
```

### Step 12: Check Repository State

**Instructions:**
```bash
git log --oneline --graph --all
ls -la
```

**Expected Result:**
- Both branches visible in graph
- `styles/` directory present

### Step 13: Merge Feature Branch with Conflicts

**Instructions:**
```bash
# Create a conflict scenario
echo "Version A" > conflict.txt
git add conflict.txt
git commit -m "Add conflict.txt with version A"

git checkout feature-login
echo "Version B" > conflict.txt
git add conflict.txt
git commit -m "Add conflict.txt with version B"

# Now merge and create conflict
git checkout main
git merge feature-login
```

**Expected Result:**
```
Auto-merging conflict.txt
CONFLICT (add/add): Merge conflict in conflict.txt
Automatic merge failed; fix conflicts and then commit the result.
```

### Step 14: Resolve Merge Conflict

**Instructions:**
```bash
git status
cat conflict.txt
```

**Expected Result:**
```
<<<<<<< HEAD
Version A
=======
Version B
>>>>>>> feature-login
```

**Resolve the conflict:**
```bash
# Edit conflict.txt to resolve
echo "Version A and B combined" > conflict.txt

# Mark as resolved
git add conflict.txt
git commit -m "Resolve merge conflict between main and feature-login"
```

---

## Part 5: Branch Management

### Step 15: View All Branches

**Instructions:**
```bash
git branch -a  # Show all branches
git branch -v  # Show branches with last commit
```

### Step 16: Rename Branch

**Instructions:**
```bash
git branch -m main master  # Rename current branch
# or rename another branch:
git branch -m old-name new-name
```

### Step 17: Delete Branches

**Instructions:**
```bash
git branch -d feature-ui  # Safe delete (only if merged)
```

**Expected Result:**
- Branch deleted successfully

```bash
git branch -D feature-login  # Force delete (even if not merged)
```

---

## Part 6: Remote Branch Operations

### Step 18: Push Branch to Remote

**Instructions:**
```bash
# Assuming you have a remote named 'origin'
git checkout -b feature-remote
echo "Remote feature" > remote.txt
git add remote.txt
git commit -m "Add remote feature"

git push -u origin feature-remote
```

### Step 19: Pull Remote Branches

**Instructions:**
```bash
# See all remote branches
git branch -r

# Checkout remote branch
git checkout origin/feature-remote
# or create local branch tracking remote
git checkout -b local-feature origin/feature-remote
```

### Step 20: Delete Remote Branch

**Instructions:**
```bash
git push origin --delete feature-remote
```

---

## Part 7: Branching Best Practices

### Discussion Points:
- **Feature branches**: Create branches for new features
- **Bug fix branches**: Isolate bug fixes
- **Release branches**: Prepare releases
- **Hotfix branches**: Emergency fixes for production

### Naming Conventions:
```bash
# Good branch names
feature/user-authentication
bugfix/login-validation
release/v2.1.0
hotfix/security-patch

# Avoid
new-feature
fix
temp
```

### Branch Lifespan:
- Create branches for specific purposes
- Delete branches after merging
- Keep main branch clean and deployable

---

## Practice Exercises

### Exercise 1: Basic Branching Workflow
1. Create a new branch called `exercise-1`
2. Add a new file with some content
3. Commit the changes
4. Switch back to main and merge the branch
5. Delete the merged branch

### Exercise 2: Conflict Resolution
1. Create two branches from main
2. Make different changes to the same file in each branch
3. Merge one branch (should conflict)
4. Resolve the conflict and complete the merge

### Exercise 3: Branch Management
1. Create 3 feature branches
2. Make different commits in each
3. Merge them one by one into main
4. Clean up merged branches

## Summary

Key concepts covered:
- **Creating branches**: `git branch`, `git checkout -b`
- **Switching branches**: `git checkout`, `git switch`
- **Merging**: `git merge`
- **Conflict resolution**: Manual editing + `git add` + `git commit`
- **Branch management**: Listing, deleting, renaming branches
- **Remote branches**: Pushing, pulling, tracking

Remember:
- Branches are lightweight and cheap to create
- Always check `git status` and `git branch` to know your location
- Resolve conflicts carefully - they affect both files and history
- Keep main branch stable and deployable

Next, you'll learn about [advanced branching strategies](../tutorials/05-branching-strategies.md).

## Additional Resources

- [Git Branching Documentation](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [Interactive Branching Tutorial](https://learngitbranching.js.org/)
- [Branching Best Practices](https://www.git-tower.com/learn/git/ebook/en/command-line/branching-merging/branches/)

## Quiz

1. What command creates and switches to a new branch?
2. How do you merge a feature branch into main?
3. What does a merge conflict look like?
4. How do you delete a merged branch safely?
5. Why should you use feature branches?