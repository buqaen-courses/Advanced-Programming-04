# Homework 2 — Working with Forks and Submitting Your Course Assignments

**Section:** 2 — Repository Basics
**Estimated Time:** 90–120 minutes
**Difficulty:** Intermediate
**Prerequisite:** Homework 1 (Git Fundamentals)

---

## 📋 Overview

In this homework, you will **not create a new repository from scratch**.
Instead, you will work with the **main course repository**.

Your goal is to:

1. Fork the official course repository on GitHub
2. Clone your fork locally
3. Add your assignments inside the predefined `homeworks` directory
4. Push your work to your forked repository
5. Submit the link to your repository in the course LMS

This structure will be used for **all future homework submissions**.

---

## 🎯 Learning Objectives

By completing this homework, you will learn how to:

* Fork an existing repository
* Work inside a structured project maintained by others
* Organize assignments in predefined directories
* Push changes to your personal fork
* Submit your work via repository link
* Embed images and write Markdown documentation

---

## 📁 Understanding the Repository Structure

The main course repository already contains a folder named:

```
homeworks/
```

Inside it, each topic has its own directory:

```
homeworks/
    topic1/
    topic2/
    topic3/
```

From now on:

✔ Every assignment must be placed in the correct topic folder
✔ Each homework gets its own subfolder
✔ Your work must remain organized and readable

---

## 🧭 Part 1 — Fork and Clone the Course Repository

### Step 1 — Fork the Repository

1. Open the official course repository in your browser
2. Click **Fork**
3. A copy of the repository will be created in your account

This copy is fully yours — you can modify it freely.

---

### Step 2 — Clone Your Fork Locally

```bash
git clone https://github.com/yourusername/course-repository-name.git
cd course-repository-name
```

You now have a local working copy.

---

## 🧭 Part 2 — Create Homework 1 Inside Topic 1

Navigate to:

```
homeworks/topic1/
```

---

### Step 1 — Create Your Homework Folder

```bash
mkdir homework1
cd homework1
```

---

### Step 2 — Create an Images Folder

```bash
mkdir images
```

---

### Step 3 — Add an Image

Place any image inside the folder.
Example:

```
images/image1.png
```

---

### Step 4 — Create a README File

```bash
touch README.md
```

---

### Step 5 — Display the Image in Markdown

Edit `README.md` and insert:

```markdown
# Homework 1

This is my first homework submission.

## Image Example

![Example Image](images/image1.png)
```

---

### Step 6 — Commit and Push

```bash
git add .
git commit -m "Add homework1 for topic1 with image and README"
git push origin main
```

Your first structured homework is now submitted.

---

## 🧭 Part 3 — Complete Homework 2 Inside Topic 1

Now create a second assignment folder.

Return to:

```
homeworks/topic1/
```

---

### Step 1 — Create Homework 2 Folder

```bash
mkdir homework2
cd homework2
```

---

### Step 2 — Create the Following Structure

```
homework2/
    README.md
    notes.md
    experiment.txt
    images/
```

Create them:

```bash
mkdir images
touch README.md
touch notes.md
touch experiment.txt
```

---

### Step 3 — Write Content

#### README.md

Explain:

* What this homework demonstrates
* What Git commands you used
* What you learned

---

#### notes.md

Write short explanations of:

* Working directory
* Staging area
* Commit
* Repository history

---

#### experiment.txt

Perform a simple Git experiment:

1. Write a sentence
2. Commit it
3. Modify it
4. Commit again

Example content:

```
Version 1: Initial idea
Version 2: Improved idea
```

---

### Step 4 — Add an Image

Place a second image in:

```
images/
```

Display it in `README.md`.

---

### Step 5 — Commit Log Section

In `README.md`, include:

```bash
git log --oneline
```

Copy the output and paste it into the file.

This shows your version history.

---

### Step 6 — Commit and Push

```bash
git add .
git commit -m "Add homework2 for topic1 with documentation and experiment"
git push
```

---

## 🧭 Part 4 — Submit Your Repository

After pushing all changes:

1. Open your fork in the browser
2. Copy the repository URL
3. Submit the link in the course LMS

That link is your submission.

---

## 📌 Important Rules

* Do NOT modify other students’ folders
* Do NOT change the main structure
* Use meaningful commit messages
* Keep files organized and readable

---

## ✅ Completion Checklist

You are done when:

✔ Repository forked
✔ Fork cloned locally
✔ `homeworks/topic1/homework1` created
✔ Image embedded in Markdown
✔ `homework2` created with documentation
✔ Git experiment recorded
✔ Changes pushed to fork
✔ Repository link submitted

---

## 📊 Git Commands Used in This Homework

| Command             | Purpose                     |
| ------------------- | --------------------------- |
| `git clone`         | Download repository locally |
| `git add`           | Stage changes               |
| `git commit`        | Save a version              |
| `git push`          | Upload changes              |
| `git log --oneline` | View history                |
| `mkdir`             | Create folder               |
| `touch`             | Create file                 |

---

## 🎓 Outcome

After completing this homework, you will understand how real course assignments are managed using:

* Forked repositories
* Structured directories
* Version tracking
* Remote submission

This workflow mirrors professional collaborative development.


