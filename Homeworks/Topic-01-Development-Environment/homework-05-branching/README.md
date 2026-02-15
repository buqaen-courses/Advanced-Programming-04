# Homework 05: Branching Fundamentals

## 📋 Overview

This homework focuses on mastering Git branching concepts and workflows. You'll learn how to create, manage, and merge branches, resolve merge conflicts, and follow professional branching strategies.

## 🎯 Learning Objectives

By completing this homework, you will be able to:

- Create and manage Git branches effectively
- Switch between branches and understand branch isolation
- Merge branches using different strategies
- Resolve merge conflicts confidently
- Follow professional branching workflows
- Use branches for safe experimentation and collaboration

## 📝 Assignment Tasks

### Part 1: Branch Creation and Management

1. **Set up a branching practice repository**:
   ```bash
   mkdir branching-practice
   cd branching-practice
   git init

   # Create initial content
   echo "# Branching Practice Project" > README.md
   echo "print('Main application')" > app.py
   mkdir features docs

   git add .
   git commit -m "Initial project setup"
   ```

2. **Create and explore branches**:
   ```bash
   # View current branches
   git branch

   # Create new branches
   git branch feature/user-auth
   git branch bugfix/login-error
   git branch experiment/new-ui

   # View all branches
   git branch -v
   ```

3. **Switch between branches**:
   ```bash
   git checkout feature/user-auth
   git status

   git checkout bugfix/login-error
   git checkout experiment/new-ui

   # Return to main
   git checkout main
   ```

### Part 2: Working on Feature Branches

1. **Develop on feature branch**:
   ```bash
   git checkout feature/user-auth

   # Create authentication files
   echo "# User Authentication Module" > features/auth.py
   echo "def login(username, password):" >> features/auth.py
   echo "    # TODO: Implement login logic" >> features/auth.py
   echo "    return True" >> features/auth.py

   echo "# Authentication Tests" > features/test_auth.py
   echo "def test_login():" >> features/test_auth.py
   echo "    assert login('user', 'pass') == True" >> features/test_auth.py

   git add features/
   git commit -m "Add basic user authentication feature"
   ```

2. **Make multiple commits on feature branch**:
   ```bash
   # Enhance authentication
   echo "def register(username, password):" >> features/auth.py
   echo "    # TODO: Implement registration" >> features/auth.py
   echo "    return True" >> features/auth.py

   git add features/auth.py
   git commit -m "Add user registration function"

   # Update tests
   echo "def test_register():" >> features/test_auth.py
   echo "    assert register('newuser', 'pass') == True" >> features/test_auth.py

   git add features/test_auth.py
   git commit -m "Add registration tests"
   ```

### Part 3: Branch Merging

1. **Merge completed feature**:
   ```bash
   # Switch to main
   git checkout main

   # Merge feature branch
   git merge feature/user-auth

   # Check result
   git log --oneline --graph
   git branch  # Feature branch still exists
   ```

2. **Clean up merged branch**:
   ```bash
   git branch -d feature/user-auth
   git branch  # Feature branch is gone
   ```

### Part 4: Merge Conflicts

1. **Create conflicting changes**:
   ```bash
   # Start new feature branch
   git checkout -b feature/ui-improvements

   # Modify README on feature branch
   echo "" >> README.md
   echo "## Features" >> README.md
   echo "- User authentication system" >> README.md
   echo "- Modern UI design" >> README.md

   git add README.md
   git commit -m "Update README with new features"
   ```

2. **Create conflict on main branch**:
   ```bash
   git checkout main

   # Modify README differently
   echo "" >> README.md
   echo "## Project Features" >> README.md
   echo "- User login and registration" >> README.md
   echo "- Responsive web interface" >> README.md

   git add README.md
   git commit -m "Update README with project features"
   ```

3. **Attempt merge and resolve conflict**:
   ```bash
   git merge feature/ui-improvements
   # This will show a merge conflict

   # Check status
   git status

   # View conflicting file
   cat README.md

   # Edit file to resolve conflict
   # Remove conflict markers and combine content
   echo "# Branching Practice Project" > README.md
   echo "" >> README.md
   echo "## Project Features" >> README.md
   echo "- User login and registration" >> README.md
   echo "- User authentication system" >> README.md
   echo "- Responsive web interface" >> README.md
   echo "- Modern UI design" >> README.md

   git add README.md
   git commit -m "Merge UI improvements with resolved conflicts"
   ```

### Part 5: Advanced Branching Scenarios

1. **Work with multiple active branches**:
   ```bash
   # Create bug fix branch
   git checkout -b bugfix/critical-security

   # Fix the bug
   echo "# Security fix applied" > security.patch
   git add security.patch
   git commit -m "Fix critical security vulnerability"

   # Create documentation branch
   git checkout main
   git checkout -b docs/api-reference

   echo "# API Documentation" > docs/api.md
   echo "## Authentication Endpoints" >> docs/api.md
   git add docs/
   git commit -m "Add API documentation"
   ```

2. **Merge multiple branches**:
   ```bash
   # Merge security fix
   git checkout main
   git merge bugfix/critical-security
   git branch -d bugfix/critical-security

   # Merge documentation
   git merge docs/api-reference
   git branch -d docs/api-reference
   ```

### Part 6: Branch History and Visualization

1. **Explore branch history**:
   ```bash
   git log --oneline --graph --all
   git log --oneline --graph --decorate
   ```

2. **Compare branches**:
   ```bash
   git diff main..feature/ui-improvements
   git diff --name-only main..feature/ui-improvements
   ```

3. **Branch statistics**:
   ```bash
   git shortlog -sn  # Commits per author
   git log --oneline | wc -l  # Total commits
   ```

### Part 7: Professional Branching Workflow

1. **Follow Git Flow principles**:
   ```bash
   # Create feature branch from main
   git checkout main
   git pull  # Ensure up to date
   git checkout -b feature/new-dashboard

   # Work on feature
   echo "# Dashboard Component" > features/dashboard.py
   git add features/dashboard.py
   git commit -m "feat: add dashboard component"

   # Regular commits
   echo "def render_dashboard():" >> features/dashboard.py
   git commit -am "feat: implement dashboard rendering"

   # Push feature branch
   git push -u origin feature/new-dashboard
   ```

2. **Simulate code review process**:
   ```bash
   # Create pull request (simulate by merging)
   git checkout main
   git merge feature/new-dashboard
   git branch -d feature/new-dashboard
   ```

## 📊 Deliverables

### Repository Structure
Your final repository should demonstrate branching:
```
branching-practice/
├── .git/
├── README.md (showing merged features)
├── app.py
├── features/
│   ├── auth.py
│   ├── test_auth.py
│   └── dashboard.py
├── docs/
│   └── api.md
└── security.patch
```

### Git History
Your repository should show:
- Multiple branches created and merged
- Conflict resolution commits
- Feature development workflow
- Clean branch management

### Branch Visualization
```bash
git log --oneline --graph --all --decorate
```
Should show a branching tree with merges.

## ✅ Verification Checklist

- [ ] Repository with multiple branches created
- [ ] Feature branches with multiple commits
- [ ] Successful branch merging (fast-forward and merge commits)
- [ ] Merge conflict created and resolved
- [ ] Branches properly cleaned up after merging
- [ ] Branch history visualized and understood
- [ ] Professional branching workflow followed
- [ ] Remote branch operations (if applicable)

## 🆘 Troubleshooting Guide

### "error: cannot delete branch"
```bash
# Branch not merged
git branch -D branch-name  # Force delete

# Or merge first
git merge branch-name
git branch -d branch-name
```

### "You have unmerged paths" (merge conflict)
```bash
# Check conflicted files
git status

# Edit files to resolve conflicts
# Remove <<<<<<<, =======, >>>>>>> markers

git add <resolved-files>
git commit -m "Resolve merge conflicts"
```

### "Not currently on any branch" (detached HEAD)
```bash
# Create new branch from current state
git checkout -b temp-branch

# Or return to main
git checkout main
```

### Lost commits after merge
```bash
git reflog  # Find lost commits
git checkout <commit-hash>
git checkout -b recovery-branch
```

## 📚 Additional Resources

- [Git Branching Official Documentation](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [Interactive Branching Tutorial](https://learngitbranching.js.org/)
- [Git Flow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

## 🎯 Success Criteria

Your homework demonstrates mastery when:
- You can create and manage multiple branches effectively
- You understand branch isolation and parallel development
- You can resolve merge conflicts confidently
- Your repository shows a clear branching history
- You follow professional branching practices
- You can explain the benefits of branching workflows

**Branching Skills Mastered:**
- Branch creation, switching, and deletion
- Feature branch workflow
- Merge strategies and conflict resolution
- Branch visualization and history analysis
- Professional collaboration patterns

**Estimated completion time: 100-130 minutes**