
# 📦 Task: Install and Use `uv` – A Fast Python Package Manager

## 🎯 Objective:
Your task is to install `uv` from scratch on your system, understand what it does, and use it to create a virtual environment, initialize a project, and install some packages.

---

## 📌 What is `uv`?
`uv` is a fast and modern Python package manager, designed as a drop-in replacement for `pip`, `pip-tools`, and `virtualenv`. It allows you to manage virtual environments and install packages quickly and easily.

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
```

**Verify the installation:**
```bash
uv --version
```

---

### 3️⃣ Project Setup and Initialization:

1. **Create a new project folder:**
```bash
mkdir uv-practice
cd uv-practice
```

2. **Create a virtual environment inside your project:**
```bash
uv venv
```

3. **Activate the virtual environment:**

**On Windows:**
```bash
.venv\Scriptsctivate
```

4. **Initialize the project using `uv init`:**
```bash
uv init .
```
This will create a `uv.toml` configuration file in your project directory to manage your dependencies.

---

### 4️⃣ Running Your Python Project:

Once your environment is active and project initialized, you can run your Python files using:

```bash
uv run main.py
```

**Note:**  
- Make sure you have a `main.py` file inside your project folder.
- `uv run` automatically uses your virtual environment and runs the given Python script without needing to manually activate the environment again.

---

## ✅ Summary:

- Installed `uv`
- Created and activated a virtual environment
- Initialized the project with `uv init`
- Ran a Python script using `uv run`

---

🎉 Congratulations — you’re now ready to use `uv` for fast, modern Python project management!
