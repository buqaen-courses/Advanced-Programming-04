# Homework 1: Git Basics & Repository Management

## Learning Objectives
By completing this homework, you will be able to:
- Create and manage local Git repositories
- Understand Git's working directory, staging area, and repository states
- Use basic Git commands (init, add, commit, status, log)
- Create organized project structures with multiple folders
- Manage files and folders through Git's lifecycle

## Prerequisites
- Git installed on your system
- Basic understanding of command line operations
- Text editor for creating files

## Instructions

### Part 1: Project Setup and Git Initialization

1. **Create a new folder for your homework project:**
   ```bash
   # Create a folder named after your student ID
   mkdir your-student-id-git-basics
   cd your-student-id-git-basics
   ```

2. **Initialize a Git repository:**
   ```bash
   git init
   ```

3. **Check the repository status:**
   ```bash
   git status
   ```
   You should see that you're on the `main` branch and have an empty repository.

### Part 2: Create Project Structure

Create the following folder structure with files:

```
your-student-id-git-basics/
├── README.md (main project README)
├── hw1/
│   ├── hello.py
│   ├── calculator.py
│   └── README.md
└── hw2/
    ├── data_processor.py
    ├── file_manager.py
    └── README.md
```

### Part 3: Create Main Project README

Create a `README.md` file in the root directory with the following content:

```markdown
# Student Git Basics Project

**Student Information:**
- Student ID: [Your Student ID]
- Name: [Your Full Name]
- Family: [Your Family Name]

## Table of Contents

### Homework 1: Basic Programming
- Location: `hw1/`
- Files: Basic Python programs
- Description: Simple Python scripts demonstrating basic programming concepts

### Homework 2: Data Processing
- Location: `hw2/`
- Files: Data manipulation programs
- Description: Python scripts for processing and managing data files

## Project Structure
```
your-student-id-git-basics/
├── README.md           # This file - project overview
├── hw1/               # Homework 1 files
│   ├── hello.py       # Basic greeting program
│   ├── calculator.py  # Simple calculator
│   └── README.md      # HW1 documentation
└── hw2/               # Homework 2 files
    ├── data_processor.py    # Data processing utilities
    ├── file_manager.py      # File management tools
    └── README.md            # HW2 documentation
```

## Git Workflow Used
This project demonstrates basic Git operations:
- Repository initialization
- Sequential file additions and commits
- Organized project structure
- Documentation for each component
```

### Part 4: Create Homework 1 Files

1. **Create the hw1 folder:**
   ```bash
   mkdir hw1
   ```

2. **Create hw1/hello.py:**
   ```python
   # Homework 1: Basic Python Program
   # Student ID: [Your Student ID]

   print("Hello, World!")
   print("This is a simple Python program for Git basics homework.")
   ```

3. **Create hw1/calculator.py:**
   ```python
   # Simple Calculator Program
   # Student ID: [Your Student ID]

   print("=== Simple Calculator ===")
   print("2 + 3 =", 2 + 3)
   print("10 - 4 =", 10 - 4)
   print("5 * 6 =", 5 * 6)
   ```

4. **Create hw1/README.md:**
   ```markdown
   # Homework 1: Basic Python Programming

   ## Description
   This homework contains simple Python programs for practicing Git operations.

   ## Files
   - `hello.py`: A basic "Hello World" program
   - `calculator.py`: Simple arithmetic calculations

   ## Learning Outcomes
   - Understanding Python file structure
   - Basic print statements
   - Simple arithmetic operations

   ## Usage
   Run each program using Python:
   ```bash
   python hello.py
   python calculator.py
   ```
   ```

### Part 5: Git Operations for Homework 1

1. **Add and commit the main README:**
   ```bash
   git add README.md
   git commit -m "Add main project README with student info and table of contents"
   ```

2. **Create and add hw1 folder:**
   ```bash
   git add hw1/
   git commit -m "Add homework 1 folder with basic Python programs"
   ```

3. **Check the commit history:**
   ```bash
   git log --oneline
   ```
   You should see two commits.

### Part 6: Create Homework 2 Files

1. **Create the hw2 folder:**
   ```bash
   mkdir hw2
   ```

2. **Create hw2/data_processor.py:**
   ```python
   # Data Processor Program
   # Student ID: [Your Student ID]

   print("=== Data Processor ===")

   # Simple data processing
   numbers = [1, 2, 3, 4, 5]
   total = sum(numbers)
   average = total / len(numbers)

   print(f"Numbers: {numbers}")
   print(f"Total: {total}")
   print(f"Average: {average}")
   ```

3. **Create hw2/file_manager.py:**
   ```python
   # File Manager Program
   # Student ID: [Your Student ID]

   print("=== File Manager ===")
   print("This program demonstrates basic file operations.")
   print("Current directory contains Python files for Git homework.")
   ```

4. **Create hw2/README.md:**
   ```markdown
   # Homework 2: Data Processing and File Management

   ## Description
   This homework contains simple Python programs for practicing Git operations.

   ## Files
   - `data_processor.py`: Basic data calculations
   - `file_manager.py`: Simple file management demonstration

   ## Learning Outcomes
   - Understanding Python file organization
   - Basic data manipulation
   - Simple print statements

   ## Usage
   Run each program using Python:
   ```bash
   python data_processor.py
   python file_manager.py
   ```
   ```

### Part 7: Final Git Operations

1. **Add and commit homework 2:**
   ```bash
   git add hw2/
   git commit -m "Add homework 2 folder with data processing programs"
   ```

2. **Update the main README with final project information:**
   Edit the main README.md to add a section about the Git workflow used. Then commit this change:
   ```bash
   git add README.md
   git commit -m "Update main README with complete project documentation"
   ```

3. **Check final repository status:**
   ```bash
   git status
   git log --oneline
   ```

## Expected Repository History

After completing all steps, your `git log --oneline` should show something like:
```
3e4f5a6 Update main README with complete project documentation
2b8c9d1 Add homework 2 folder with data processing programs
1a7b2c3 Add homework 1 folder with basic Python programs
9f8e7d6 Add main project README with student info and table of contents
```

## Submission Requirements

1. **Repository Structure**: Ensure your folder structure matches the specification
2. **Git History**: Demonstrate sequential commits as shown above
3. **File Content**: All Python files should be functional and well-documented
4. **README Files**: All README files should contain appropriate content
5. **Student Information**: Update all files with your actual student information

## Assessment Criteria

- [ ] Correct folder structure created
- [ ] Git repository properly initialized
- [ ] Sequential commits demonstrate Git workflow understanding
- [ ] Python files are syntactically correct and functional
- [ ] README files contain appropriate documentation
- [ ] Student information properly included
- [ ] Git history shows logical progression of work

## Troubleshooting

### Common Issues:
1. **"fatal: not a git repository"**: Make sure you're in the correct directory and have run `git init`
2. **"nothing to commit"**: Check `git status` to see what files need to be added
3. **Python syntax errors**: Test your Python files before committing

### Useful Commands:
```bash
# Check current status
git status

# See commit history
git log --oneline

# See what changed in each commit
git show <commit-hash>

# Unstage files if needed
git reset HEAD <file>
```