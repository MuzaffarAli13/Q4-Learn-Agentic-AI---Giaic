# Task: Install and Use `uv` – A Fast Python Package Manager

## Objective:
Your task is to install `uv` from scratch on your system, understand what it does, and use it to create a virtual environment and install some packages.

---

## 📌 What is `uv`?
`uv` is a fast and modern Python package manager, designed as a drop-in replacement for `pip`, `pip-tools`, and `virtualenv`.

---

## 📖 Task Steps:

### 1️⃣ Research:
- **What is `uv`?**  
  `uv` is a Python package manager that combines package management and virtual environment management into one fast tool, acting as a replacement for tools like `pip`, `pip-tools`, and `virtualenv`.

- **3 Key Features of `uv` (in your own words):**
  1. Extremely fast installation of Python packages.
  2. Manages virtual environments without needing external tools.
  3. Compatible as a drop-in replacement for pip and virtualenv commands.

---

### 2️⃣ Installation:

**On Windows (using PowerShell with Administrator privileges):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
