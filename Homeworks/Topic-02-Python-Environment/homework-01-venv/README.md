# Homework 01: Virtual Environment Fundamentals

## 📋 Overview

This homework focuses on understanding and creating Python virtual environments for project isolation and dependency management.

## 🎯 Learning Objectives

By completing this homework, you will be able to:

- Understand the purpose of virtual environments
- Create and activate virtual environments
- Install packages in isolated environments
- Deactivate and manage multiple environments
- Troubleshoot common virtual environment issues

## 📝 Assignment Tasks

### Part 1: Understanding Virtual Environments

1. **Research virtual environments**:
   - Why are virtual environments important?
   - What problems do they solve?
   - How do they differ from system-wide installations?

2. **Check your Python installation**:
   ```bash
   python --version
   python -m venv --help
   ```

### Part 2: Creating Virtual Environments

1. **Create your first virtual environment**:
   ```bash
   python -m venv myproject_env
   ```

2. **Explore the created environment**:
   ```bash
   ls -la myproject_env/  # Linux/macOS
   dir myproject_env/     # Windows
   ```

3. **Activate the environment**:
   ```bash
   # Windows
   myproject_env\Scripts\activate

   # Linux/macOS
   source myproject_env/bin/activate
   ```

4. **Verify activation**:
   ```bash
   which python  # Should show virtual environment path
   pip list      # Should show basic packages
   ```

### Part 3: Working with Packages

1. **Install packages in the virtual environment**:
   ```bash
   pip install requests
   pip install flask
   ```

2. **Check installed packages**:
   ```bash
   pip list
   pip freeze > requirements.txt
   ```

3. **Deactivate the environment**:
   ```bash
   deactivate
   ```

4. **Verify deactivation**:
   ```bash
   which python  # Should show system Python
   ```

### Part 4: Multiple Environments

1. **Create a second environment** for a different project
2. **Install different packages** in each environment
3. **Switch between environments** and verify isolation

## 📁 Submission Requirements

Create the following files in this folder:

```
homework-01-venv/
├── README.md                    # This file (update with your work)
├── venv-explanation.md          # Your research on virtual environments
├── environment-creation.txt     # Commands for creating and activating venv
├── package-installation.txt     # Commands for installing packages
├── environment-comparison.txt   # Comparison of different environments
├── requirements.txt             # Generated from one of your environments
└── screenshots/                 # Optional: screenshots of terminal output
```

## ✅ Verification Checklist

- [ ] Understand the purpose of virtual environments
- [ ] Successfully created and activated a virtual environment
- [ ] Installed packages in the virtual environment
- [ ] Verified environment isolation
- [ ] Can switch between different environments
- [ ] Generated requirements.txt file

## 📚 Resources

- [Tutorial: Virtual Environments](../sections/section-01/tutorial.md)
- [Workshop: Environment Setup](../sections/section-01/workshop.md)