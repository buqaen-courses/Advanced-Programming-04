# Homework 3: Git Branching Mastery - Parallel Development Workflows

**Section**: 3 - Understanding Git States (Advanced)
**Estimated Time**: 120-150 minutes
**Difficulty**: Advanced
**Prerequisites**: Homework 1 & 3 (Git Fundamentals, Repository Operations & State Management)

---

## 📋 Assignment Overview

In this homework, you'll become a branching expert by mastering Git's parallel development workflows. You'll create feature branches, implement complex changes across multiple branches, resolve merge conflicts, manage branch lifecycles, and work with remote branches. This comprehensive branching experience will prepare you for collaborative development environments where multiple developers work simultaneously on different features.

**Learning Objectives:**
- Master Git branching concepts and parallel development workflows
- Create, switch, and manage branches effectively using modern Git commands
- Implement features on separate branches without affecting main code
- Perform merges including conflict resolution strategies
- Manage branch lifecycles (create, rename, delete branches)
- Work with remote branches and collaborative workflows
- Understand branching best practices and common patterns

**Note:** This homework uses modern Git commands (`git switch`, `git switch -c`) introduced in Git 2.23. For backward compatibility, older commands (`git checkout`, `git checkout -b`) are noted in comments where relevant.

---

## 🎯 Requirements

### Part 1: Branching Fundamentals Repository Setup (15 points)

#### Task 1.1: Create Project Repository
**Objective**: Set up a structured repository for practicing branching workflows

**Requirements:**
- Create a new local Git repository for branching practice
- Initialize with a well-structured project layout
- Create initial commits establishing a stable main branch foundation

**Project Setup:**
```bash
# Create new directory for branching practice
mkdir git-branching-mastery
cd git-branching-mastery

# Initialize repository
git init

# Create project structure
mkdir src tests docs scripts
echo "# Git Branching Mastery Project" > README.md
echo "# Project Documentation" > docs/README.md
echo "print('Hello from main branch')" > src/app.py
echo "# Basic test suite" > tests/test_app.py

# Stage and commit initial files
git add .
git commit -m "Initial project setup with basic structure"
```

**Deliverables:**
- Repository initialized and committed
- Project structure created with src/, tests/, docs/, scripts/ directories
- Initial commit on main branch

#### Task 1.2: Explore Branch Commands
**Objective**: Understand branch listing and status commands

**Requirements:**
- Practice all branch listing variations
- Understand branch status indicators
- Document current repository state

**Commands to Practice:**
```bash
# List local branches
git branch

# List branches with detailed information
git branch -v

# Show current branch and status
git status

# Show branch relationship graph (after creating more branches)
git log --oneline --graph --all
```

**Deliverables:**
- Screenshot or documentation of branch listing outputs
- Understanding of branch status indicators (* for current branch)

---

### Part 2: Feature Branch Development (25 points)

#### Task 2.1: Authentication Feature Implementation
**Objective**: Develop a complete authentication feature on a dedicated branch

**Requirements:**
- Create and switch to `feature/auth` branch
- Implement authentication module with multiple components
- Create comprehensive commits with meaningful messages
- Test functionality independently

**Implementation Steps:**
```bash
# Create and switch to feature branch
git switch -c feature/auth

# Implement authentication components
echo "# Authentication Module" > src/auth.py
echo "def login(username, password):
    # Basic authentication logic
    return True" >> src/auth.py

echo "# User model" > src/user.py
echo "class User:
    def __init__(self, username):
        self.username = username" >> src/user.py

# Create authentication tests
echo "# Authentication tests" > tests/test_auth.py
echo "def test_login():
    assert True  # Placeholder test" >> tests/test_auth.py

# Commit feature components
git add src/auth.py
git commit -m "Add basic authentication module"

git add src/user.py tests/test_auth.py
git commit -m "Add user model and authentication tests"
```

**Deliverables:**
- `feature/auth` branch with authentication implementation
- Multiple focused commits demonstrating feature development
- Authentication module, user model, and tests implemented

#### Task 2.2: UI Enhancement Feature
**Objective**: Develop UI improvements on a separate feature branch

**Requirements:**
- Create `feature/ui-improvements` branch from main
- Implement styling and UI components
- Create documentation for UI changes
- Maintain separation from authentication work

**Implementation Steps:**
```bash
# Switch back to main and create UI branch
git switch main
git switch -c feature/ui-improvements

# Implement UI components
mkdir -p src/ui templates/static
echo "# UI Components" > src/ui/components.py
echo "class Button:
    def __init__(self, text):
        self.text = text" >> src/ui/components.py

echo "# Main stylesheet" > templates/static/style.css
echo "body { font-family: Arial, sans-serif; }
.button { padding: 10px; background: #007bff; color: white; }" >> templates/static/style.css

# Update documentation
echo "## UI Improvements
- Added reusable UI components
- Implemented consistent styling
- Enhanced user experience" >> docs/README.md

# Commit UI changes
git add .
git commit -m "Add UI components and styling improvements"
```

**Deliverables:**
- `feature/ui-improvements` branch with UI enhancements
- UI components, styling, and documentation
- Clean separation from authentication feature

---

### Part 3: Merge Operations and Conflict Resolution (30 points)

#### Task 3.1: Fast-Forward Merge Practice
**Objective**: Practice clean merges without conflicts

**Requirements:**
- Merge UI improvements into main branch
- Demonstrate fast-forward merge behavior
- Verify merged changes are properly integrated

**Merge Process:**
```bash
# Switch to main and merge UI branch
git switch main
git merge feature/ui-improvements

# Verify merge results
git log --oneline -5
ls -la src/ui/
```

**Deliverables:**
- Successful fast-forward merge
- UI improvements integrated into main branch
- Documentation of merge process and results

#### Task 3.2: Merge Conflict Creation and Resolution
**Objective**: Create and resolve merge conflicts between feature branches

**Requirements:**
- Create conflicting changes on both main and auth branches
- Perform merge that creates conflicts
- Resolve conflicts using appropriate strategies
- Document conflict resolution process

**Conflict Scenario Setup:**
```bash
# Make changes on main that will conflict
git switch main
echo "# Configuration file" > config.py
echo "DEBUG = True" >> config.py
echo "SECRET_KEY = 'main-branch-key'" >> config.py
git add config.py
git commit -m "Add configuration file with main settings"

# Make conflicting changes on auth branch
git switch feature/auth
echo "# Configuration file" > config.py
echo "DEBUG = False" >> config.py
echo "SECRET_KEY = 'auth-branch-key'" >> config.py
git add config.py
git commit -m "Add configuration file with auth settings"

# Attempt merge to create conflict
git switch main
git merge feature/auth
```

**Conflict Resolution:**
```bash
# Check conflict status
git status

# View conflict markers
cat config.py

# Resolve conflicts (choose appropriate values)
echo "# Configuration file" > config.py
echo "DEBUG = True  # Production setting" >> config.py
echo "SECRET_KEY = 'merged-key-from-both-branches'" >> config.py

# Complete merge
git add config.py
git commit -m "Resolve merge conflict: combine config settings from main and auth branches"
```

**Deliverables:**
- Documented merge conflict scenario
- Step-by-step conflict resolution process
- Successfully resolved and committed merge
- Explanation of resolution strategy used

#### Task 3.3: Three-Way Merge Practice
**Objective**: Practice complex merge scenarios with divergent branches

**Requirements:**
- Create additional commits on both branches after initial conflict
- Perform three-way merge requiring manual resolution
- Demonstrate understanding of merge commit creation

**Advanced Merge Scenario:**
```bash
# Add more commits to both branches
git switch main
echo "# Advanced config" >> config.py
git commit -am "Add advanced configuration options"

git switch feature/auth
echo "# Auth-specific config" >> config.py
git commit -am "Add authentication-specific configuration"

# Perform three-way merge
git switch main
git merge feature/auth --no-ff  # Force merge commit
```

**Deliverables:**
- Three-way merge completed successfully
- Merge commit created with appropriate message
- Documentation of merge strategy and reasoning

---

### Part 4: Branch Management and Cleanup (15 points)

#### Task 4.1: Branch Organization
**Objective**: Organize and manage repository branches effectively

**Requirements:**
- List all branches with detailed information
- Rename branches following naming conventions
- Delete merged branches safely
- Maintain clean branch structure

**Branch Management:**
```bash
# View all branches with details
git branch -v
git branch --merged
git branch --no-merged

# Rename branches
git branch -m feature/auth feature/authentication
git branch -m feature/ui-improvements feature/ui-enhancements

# Safe deletion of merged branches
git branch -d feature/ui-enhancements

# Force delete if necessary (document why)
# git branch -D feature/authentication
```

**Deliverables:**
- Organized branch structure
- Properly named branches following conventions
- Cleaned up merged branches
- Documentation of branch management decisions

#### Task 4.2: Branch History Analysis
**Objective**: Analyze branch relationships and commit history

**Requirements:**
- Create visual representation of branch structure
- Analyze commit relationships across branches
- Document branching strategy effectiveness

**History Analysis:**
```bash
# View complete branch graph
git log --oneline --graph --all --decorate

# Show branch-specific history
git log --oneline feature/authentication
git log --oneline main --not feature/authentication

# Analyze merge commits
git log --merges --oneline
```

**Deliverables:**
- Visual branch graph diagram
- Analysis of branching strategy effectiveness
- Documentation of commit relationships

---

### Part 5: Remote Branch Operations (15 points)

#### Task 5.1: Remote Repository Setup
**Objective**: Set up remote repository for branch collaboration

**Requirements:**
- Create GitHub repository for the project
- Connect local repository to remote
- Push main branch to establish remote tracking

**Remote Setup:**
```bash
# Create GitHub repository (document URL)
# Add remote origin
git remote add origin https://github.com/YOUR_USERNAME/git-branching-mastery.git

# Push main branch
git push -u origin main
```

**Deliverables:**
- GitHub repository created and connected
- Main branch pushed to remote
- Remote tracking established

#### Task 5.2: Remote Branch Collaboration
**Objective**: Practice collaborative branching workflows

**Requirements:**
- Push feature branches to remote
- Create pull request workflow simulation
- Pull and merge remote changes

**Remote Branch Operations:**
```bash
# Push feature branch to remote
git switch feature/authentication
git push -u origin feature/authentication

# Create another branch for collaboration simulation
git switch main
git switch -c feature/collaboration
echo "# Collaborative feature" > src/collaboration.py
git add src/collaboration.py
git commit -m "Add collaborative feature"
git push -u origin feature/collaboration

# Simulate pulling changes
git switch main
git pull origin main  # If there were remote changes
```

**Deliverables:**
- Multiple branches pushed to remote
- Remote branch tracking established
- Simulated collaborative workflow documented

---

## 📝 Submission Requirements

### Documentation Requirements
Create a comprehensive `BRANCHING_REPORT.md` file documenting:

1. **Repository Structure**
   - Final branch layout and relationships
   - Commit history graph
   - Remote repository URL

2. **Branching Strategy Analysis**
   - Feature branch development process
   - Merge conflict resolution strategies
   - Branch management decisions

3. **Key Learnings**
   - Most important branching concepts mastered
   - Common pitfalls encountered and solutions
   - Best practices identified

4. **Screenshots/Documentation**
   - Branch graphs showing merge relationships
   - Conflict resolution examples
   - Remote branch operations

### Repository State Requirements
- All feature branches either merged or documented for deletion
- Clean main branch with integrated features
- Remote repository with complete branch history
- Comprehensive commit messages throughout

### Grading Criteria
- **Functionality (40%)**: All branching operations work correctly
- **Documentation (30%)**: Clear explanation of processes and decisions
- **Best Practices (20%)**: Proper branching conventions and cleanup
- **Problem Solving (10%)**: Effective conflict resolution and troubleshooting

---

## 🆘 Troubleshooting Guide

### Common Issues and Solutions

**"Branch already exists" error:**
```bash
# Check existing branches
git branch -a

# Delete if needed
git branch -D branch-name
```

**Older Git version compatibility:**
```bash
# If git switch is not available (Git < 2.23), use:
git checkout branch-name          # instead of: git switch branch-name
git checkout -b new-branch        # instead of: git switch -c new-branch

# Update Git if possible:
# On Ubuntu/Debian: sudo apt update && sudo apt install git
# On macOS: brew install git
# On Windows: Download from https://git-scm.com/downloads
```

**Merge conflict resolution stuck:**
```bash
# Abort merge if needed
git merge --abort

# Start fresh with clean branches
```

**Remote branch push issues:**
```bash
# Set upstream properly
git push --set-upstream origin branch-name

# Or use -u flag
git push -u origin branch-name
```

**Lost commits after branch deletion:**
```bash
# Check reflog
git reflog

# Restore if needed
git switch -c recovered-branch <commit-hash>
```

---

## 🎓 Learning Outcomes

By completing this homework, you will demonstrate mastery of:

- ✅ **Modern Git Branching**: Using `git switch` and `git switch -c` for branch operations
- ✅ **Branch Creation & Management**: Creating, switching, and organizing branches
- ✅ **Parallel Development**: Working on multiple features simultaneously
- ✅ **Merge Strategies**: Fast-forward, three-way, and conflict resolution
- ✅ **Branch Lifecycle**: Creation, merging, renaming, and deletion
- ✅ **Remote Collaboration**: Pushing, pulling, and tracking remote branches
- ✅ **Workflow Best Practices**: Clean branching strategies and conventions

---

## 📚 Additional Resources

- [Git Branching Official Documentation](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [Atlassian Git Branching Tutorial](https://www.atlassian.com/git/tutorials/using-branches)
- [GitHub Branching Guide](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)

**Happy branching! 🌳**