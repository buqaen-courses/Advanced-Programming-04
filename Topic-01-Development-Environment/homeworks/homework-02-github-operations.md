# Homework 2: GitHub Operations & Repository Management

## Learning Objectives
By completing this homework, you will be able to:
- Create and manage GitHub repositories
- Use Personal Access Tokens for authentication
- Clone repositories using PAT authentication
- Perform Git restore operations for files and commits
- Understand remote repository operations

## Prerequisites
- GitHub account with Personal Access Token (see Tutorial 4)
- Git installed and configured
- Basic Git knowledge from Homework 1
- Understanding of GitHub Personal Access Tokens

## Instructions

### Part 1: GitHub Repository Setup

1. **Create a new GitHub repository:**
   - Go to GitHub.com and sign in
   - Click the "+" icon → "New repository"
   - Repository name: `advanced-programming-hw2-[your-student-id]`
   - Description: "Homework 2: GitHub Operations and Restore Commands"
   - Set to **Public** (for easier access during learning)
   - **Do NOT initialize** with README, .gitignore, or license
   - Click "Create repository"

2. **Note your repository URL:**
   After creation, GitHub will show you the repository URL. It should look like:
   ```
   https://github.com/YOUR_USERNAME/advanced-programming-hw2-YOUR_STUDENT_ID.git
   ```

### Part 2: Local Repository Setup and Initial Commit

1. **Create a local project folder:**
   ```bash
   # Create folder for this homework
   mkdir github-operations-hw2
   cd github-operations-hw2
   ```

2. **Initialize Git repository:**
   ```bash
   git init
   ```

3. **Create initial project structure:**
   ```
   github-operations-hw2/
   ├── README.md
   ├── src/
   │   ├── main.py
   │   ├── utils.py
   │   └── config.py
   ├── tests/
   │   ├── test_main.py
   │   └── test_utils.py
   └── docs/
       ├── user-guide.md
       └── api-reference.md
   ```

4. **Create the initial files:**

   **README.md:**
   ```markdown
   # GitHub Operations Homework 2

   **Student Information:**
   - Student ID: [Your Student ID]
   - Name: [Your Full Name]
   - Family: [Your Family Name]

   ## Project Description
   This project demonstrates GitHub operations including repository creation,
   Personal Access Token authentication, and Git restore operations.

   ## Repository Structure
   - `src/`: Main source code
   - `tests/`: Unit tests
   - `docs/`: Documentation files

   ## GitHub Repository
   This project will be pushed to GitHub using Personal Access Token authentication.
   ```

   **src/main.py:**
   ```python
   # Main application file
   # Student ID: [Your Student ID]

   print("=== GitHub Operations Homework ===")
   print("Welcome to GitHub Operations Homework 2!")
   print("Student ID: YOUR_STUDENT_ID")
   print("Course: Advanced Programming")
   ```

   **src/utils.py:**
   ```python
   # Utility functions
   # Student ID: [Your Student ID]

   print("=== Utility Functions ===")
   print("This file contains utility functions for the homework.")
   print("Simple calculations: 10 + 5 =", 10 + 5)
   ```

   **src/config.py:**
   ```python
   # Configuration settings
   # Student ID: [Your Student ID]

   print("=== Configuration Settings ===")
   print("App Name: GitHub Operations Demo")
   print("Version: 1.0.0")
   print("Author: YOUR_NAME")
   ```

5. **Initial commit:**
   ```bash
   git add .
   git commit -m "Initial commit: Project structure and basic files"
   ```

### Part 3: Connect to GitHub Repository

1. **Add GitHub remote using Personal Access Token:**
   ```bash
   # Replace YOUR_USERNAME, YOUR_PAT, and YOUR_STUDENT_ID with actual values
   git remote add origin https://YOUR_USERNAME:YOUR_PAT@github.com/YOUR_USERNAME/advanced-programming-hw2-YOUR_STUDENT_ID.git
   ```

2. **Push to GitHub:**
   ```bash
   git push -u origin main
   ```

3. **Verify on GitHub:**
   - Go to your repository on GitHub
   - Confirm all files are uploaded
   - Check the commit history

### Part 4: Create Documentation Files

   **docs/user-guide.md:**
   ```markdown
   # User Guide

   ## Getting Started

   This project demonstrates GitHub operations and repository management.

   ## Installation

   1. Clone the repository:
   ```bash
   git clone https://YOUR_USERNAME:YOUR_PAT@github.com/YOUR_USERNAME/advanced-programming-hw2-YOUR_STUDENT_ID.git
   ```

   2. Navigate to the project directory:
   ```bash
   cd advanced-programming-hw2-YOUR_STUDENT_ID
   ```

   3. Run the main application:
   ```bash
   python src/main.py
   ```

   ## Usage

   ### Configuration
   Edit `src/config.py` to modify application settings.

   ## Features

   - Student information display
   - Simple utility functions
   - Configuration management
   ```

   **docs/api-reference.md:**
   ```markdown
   # API Reference

   ## Files

   ### main.py
   Main application file that displays welcome messages and student information.

   ### utils.py
   Contains utility functions and simple calculations.

   ### config.py
   Configuration file with application settings.
   ```

3. **Commit the new files:**
   ```bash
   git add .
   git commit -m "Add documentation files"
   git push origin main
   ```

### Part 5: Git Restore Operations

#### 5.1 Restore a Single File

1. **Modify a file (simulate accidental changes):**
   ```bash
   # Make changes to src/utils.py
   echo "# This is an accidental change" >> src/utils.py
   ```

2. **Check the status:**
   ```bash
   git status
   ```
   You should see `src/utils.py` as modified.

3. **Restore the file to its last committed state:**
   ```bash
   git restore src/utils.py
   ```

4. **Verify the file is restored:**
   ```bash
   git status
   git diff src/utils.py
   ```

#### 5.2 Restore Multiple Files

1. **Modify multiple files:**
   ```bash
   # Modify several files
   echo "# Accidental change 1" >> src/main.py
   echo "# Accidental change 2" >> README.md
   echo "# Accidental change 3" >> src/config.py
   ```

2. **Check status:**
   ```bash
   git status
   ```

3. **Restore all modified files:**
   ```bash
   git restore .
   ```

4. **Verify all files are restored:**
   ```bash
   git status
   ```

#### 5.3 Restore a Specific Commit (Whole Repository)

1. **Make some changes and commit them:**
   ```bash
   # Modify a file
   echo "# Temporary change for restore demo" >> src/utils.py

   # Commit the change
   git add src/utils.py
   git commit -m "Temporary commit for restore demonstration"
   ```

2. **Check the commit history:**
   ```bash
   git log --oneline
   ```
   Note the commit hash of the "Temporary commit" (let's call it `abc1234`).

3. **Make more changes:**
   ```bash
   # Make additional changes
   echo "# More changes" >> src/main.py
   echo "# Even more changes" >> README.md
   ```

4. **Restore the entire repository to a previous commit:**
   ```bash
   # Replace abc1234 with the actual commit hash
   git reset --hard abc1234
   ```

5. **Verify the restore:**
   ```bash
   git status
   git log --oneline
   ```

6. **Note:** This operation removes all uncommitted changes and resets to the specified commit.

### Part 6: Advanced Restore Operations

#### 6.1 Restore Staged Files

1. **Stage some changes:**
   ```bash
   # Modify and stage files
   echo "# Staged change" >> src/config.py
   git add src/config.py
   ```

2. **Check status:**
   ```bash
   git status
   ```

3. **Unstage the file (restore from staging area):**
   ```bash
   git restore --staged src/config.py
   ```

4. **Verify:**
   ```bash
   git status
   ```

#### 6.2 Soft Reset vs Hard Reset

1. **Create a new commit:**
   ```bash
   echo "# Demo commit" >> docs/user-guide.md
   git add docs/user-guide.md
   git commit -m "Demo commit for reset comparison"
   ```

2. **Make more changes:**
   ```bash
   echo "# More changes for reset demo" >> docs/api-reference.md
   ```

3. **Demonstrate soft reset (keeps changes):**
   ```bash
   git reset --soft HEAD~1
   git status
   ```
   Notice the changes are still there but unstaged.

4. **Demonstrate mixed reset (default):**
   ```bash
   git add docs/api-reference.md
   git commit -m "Another demo commit"
   git reset HEAD~1
   git status
   ```

5. **Demonstrate hard reset:**
   ```bash
   git add docs/api-reference.md
   git commit -m "Final demo commit"
   git reset --hard HEAD~1
   git status
   ```

### Part 7: Final Repository Management

1. **Create a comprehensive update:**
   Add a section to the main README about Git restore operations and update all files with your actual student information.

2. **Final commit and push:**
   ```bash
   git add .
   git commit -m "Complete homework 2 with restore operations demonstration"
   git push origin main
   ```

3. **Verify final repository:**
   - Check GitHub repository
   - Ensure all files are present
   - Review commit history

## Expected Repository Structure

```
advanced-programming-hw2-YOUR_STUDENT_ID/
├── README.md                    # Main project documentation
├── src/                        # Source code
│   ├── main.py                 # Main application
│   ├── utils.py                # Utility functions
│   └── config.py               # Configuration
└── docs/                       # Documentation
    ├── user-guide.md          # User guide
    └── api-reference.md       # API documentation
```

## Git Commands Used in This Homework

| Command | Purpose |
|---------|---------|
| `git init` | Initialize repository |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit staged changes |
| `git remote add origin URL` | Add remote repository |
| `git push -u origin main` | Push to GitHub |
| `git restore <file>` | Restore file to last commit |
| `git restore .` | Restore all files |
| `git reset --hard <commit>` | Reset repository to specific commit |
| `git restore --staged <file>` | Unstage a file |
| `git reset --soft HEAD~1` | Soft reset (keep changes) |
| `git status` | Check repository status |
| `git log --oneline` | View commit history |

## Assessment Criteria

- [ ] GitHub repository created successfully
- [ ] Personal Access Token authentication working
- [ ] Repository cloned using PAT in URL format
- [ ] File restore operations demonstrated
- [ ] Commit restore operations demonstrated
- [ ] Proper commit messages used
- [ ] Student information included in all files
- [ ] Repository structure matches specification
- [ ] Documentation files created and committed

## Troubleshooting

### Authentication Issues:
1. **"Authentication failed"**: Verify your PAT is correct and has proper scopes
2. **"Repository not found"**: Check repository name and username in URL
3. **PAT expired**: Generate a new token if expired

### Restore Operation Issues:
1. **"fatal: ambiguous argument"**: Use full commit hash instead of short hash
2. **Changes not restored**: Ensure you're using the correct restore command
3. **Hard reset warning**: Hard reset permanently removes changes - use carefully

### Useful Commands for Debugging:
```bash
# Check remote configuration
git remote -v

# Check current branch
git branch

# See detailed commit information
git show <commit-hash>

# Check what would be restored
git diff <file>
```

## Security Notes

- **Never commit your PAT to version control**
- **Use PATs with minimal required scopes**
- **Regenerate tokens periodically**
- **Store tokens securely (password manager)**

## Next Steps

After completing this homework, you should be comfortable with:
- Creating and managing GitHub repositories
- Using Personal Access Tokens for authentication
- Performing various Git restore operations
- Understanding the difference between different reset types
- Managing remote repositories effectively