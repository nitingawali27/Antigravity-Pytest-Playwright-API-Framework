# 📖 Beginner's Guide: Pushing Your Code to GitHub

This guide will help you connect your local project to GitHub and upload your code safely.

---

## 🏗️ Step 1: Initialize Git in Your Local Folder
Before you can use Git, you need to "initialize" it. This creates a hidden `.git` folder that tracks your changes.

**Command:**
```bash
git init
```
**What it does:** It turns your project folder into a Git repository. 

---

## 🔗 Step 2: Link to Your GitHub Repository
Now, tell your local project where the GitHub repository is located.

**Command:**
```bash
git remote add origin https://github.com/nitingawali27/Antigravity-Pytest-Playwright-API-Framework.git
```
**What it does:** It creates a connection named `origin` that points to your GitHub repository.

---

## 📦 Step 3: Add, Commit, and Push Your Code
This is the most common cycle you will follow: **Add → Commit → Push**.

### 1. Add Files
**Command:**
```bash
git add .
```
**What it does:** Stages all your files for the next commit. Thanks to the `.gitignore` file, it will skip all the "junk" files we don't need on GitHub.

### 2. Commit Your Changes
**Command:**
```bash
git commit -m "Initial commit: API Automation Framework"
```
**What it does:** Takes a "snapshot" of your staged files and gives it a descriptive message.

### 3. Push to GitHub
**Command:**
```bash
git branch -M main
git push -u origin main
```
**What it does:** 
- `git branch -M main`: Makes sure your default branch is named `main`.
- `git push -u origin main`: Uploads your code to the `main` branch on GitHub.

---

## 🆘 Step 4: Troubleshooting Common Errors

### 🔑 Authentication Issues (PAT Tokens)
GitHub no longer accepts your regular password for Git commands. You must use a **Personal Access Token (PAT)**.
1. **Generate a PAT** in GitHub: `Settings` → `Developer Settings` → `Personal Access Tokens` → `Tokens (classic)`.
2. When Git asks for your **Password**, paste the **Token** instead.

### 💾 Remote Origin Already Exists
If you get an error saying `remote origin already exists`, it means you already linked it once. You can update it with:
```bash
git remote set-url origin https://github.com/nitingawali27/Antigravity-Pytest-Playwright-API-Framework.git
```

### ❌ Push Rejected (Non-fast-forward)
If you get an error saying your push is rejected, it usually means GitHub has some files (like a `README` or `LICENSE`) that your local project doesn't have.
**The Fix:**
```bash
git pull origin main --rebase
git push origin main
```

---

## ✅ Step 5: How to Verify
1. Go to your GitHub repository URL: [https://github.com/nitingawali27/Antigravity-Pytest-Playwright-API-Framework](https://github.com/nitingawali27/Antigravity-Pytest-Playwright-API-Framework)
2. Refresh the page.
3. You should see your folders (`features`, `tests`, `utils`) and files appearing!

---

> [!TIP]
> **Always check your status!**
> Run `git status` at any time to see which files are tracked, modified, or staged. It's the most helpful command for beginners!
