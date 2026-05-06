<div align="center">

# 🛡️ django-env-check

### **Validate your environment variables before Django starts**

[![PyPI version](https://badge.fury.io/py/django-env-check.svg)](https://badge.fury.io/py/django-env-check)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/django-env-check)](https://pepy.tech/project/django-env-check)

**A tiny, zero-dependency helper that ensures all required environment variables are present before your Django app starts.**

[Installation](#-installation) • [Usage](#-usage) • [Features](#-features) • [Contributing](#-contributing)

</div>

---

## 🎯 Why django-env-check?

Every Django project relies on environment variables, but **most developers never validate whether they exist**. This leads to:

- ❌ Missing `SECRET_KEY` or `DATABASE_URL`
- ❌ Silent misconfigurations in production
- ❌ Email failures due to missing credentials
- ❌ API integration issues
- ❌ Hard-to-debug runtime errors

**django-env-check solves this with one line of code.** 

---

## 🚀 Installation

```bash
pip install django-env-check
```

---

## 📖 Usage

### Basic Usage

Add this at the **top of your `settings.py`**:

```python
from env_check import check_env

check_env([
    "SECRET_KEY",
    "DATABASE_URL",
    "EMAIL_HOST_USER",
    "EMAIL_HOST_PASSWORD"
])
```

If any variable is missing, Django **will refuse to start**:

```
[django-env-check] Missing environment variables: SECRET_KEY, DATABASE_URL
```

### 🟡 Warning Mode (Development)

In development, you may want **warnings instead of hard failures**:

```python
check_env(["SECRET_KEY"], warn_only=True)
```

**Output:**
```
⚠️  WARNING: [django-env-check] Missing environment variables: SECRET_KEY
```

### 💡 Auto-enable Warning Mode in DEBUG

```python
from django.conf import settings

check_env(
    ["SECRET_KEY", "DATABASE_URL"],
    warn_only=settings.DEBUG
)
```

---

## ✨ Features

### ✅ Return Value

`check_env(...)` returns `True` when:
- All variables exist **OR**
- `warn_only=True` (even if variables are missing)

Use this in custom logic:

```python
if check_env(["API_KEY"], warn_only=True):
    # Continue with setup
    pass
```

### ❗ Custom Exception Handling

Missing variables raise `EnvMissingError`:

```python
from env_check import check_env, EnvMissingError

try:
    check_env(["SECRET_KEY"])
except EnvMissingError as e:
    print(f"⚠️  Config error: {e}")
```

---

## 🧪 Testing Your Installation

**Test warning mode:**
```bash
python -c "from env_check import check_env; check_env(['X'], warn_only=True)"
```

**Test error mode (should raise `EnvMissingError`):**
```bash
python -c "from env_check import check_env; check_env(['X'])"
```

---

## 📁 Project Structure

```
django-env-check/
├── env_check/
│   ├── __init__.py
│   └── checker.py
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🤝 Contributing

Contributions are **welcome**! 🎉

- 🐛 Found a bug? [Open an issue](https://github.com/YOUR_USERNAME/django-env-check/issues)
- 💡 Have a feature idea? [Submit a pull request](https://github.com/YOUR_USERNAME/django-env-check/pulls)
- 📝 Improve documentation? PRs are appreciated!

---

## 📜 License

**MIT License** – Free to use, modify, and distribute.

---

## ⭐ Support the Project

If **django-env-check** helps you catch bugs early and ship safer code, please:

- ⭐ **Star this repo** on GitHub
- 🐦 **Share it** with your Django community
- 💬 **Leave feedback** or suggestions

Your support encourages new features & improvements!! ❤️

---

<div align="center">

**Made with ❤️ for the Django community**

</div>
