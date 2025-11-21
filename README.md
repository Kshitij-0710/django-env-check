📦 django-env-check

A tiny, zero-dependency helper that ensures all required environment variables are present before your Django app starts.

Useful for:

catching missing .env keys early

avoiding silent misconfigurations in production

safer deployments

enforcing required environment setup

Simple, lightweight, and framework-friendly.

🚀 Installation
pip install django-env-check

🧠 Why this package?

Every Django project uses environment variables.
But most developers never validate whether the required ones exist.

This leads to:

missing SECRET_KEY

wrong DATABASE_URL

email failures

API tokens missing

difficult-to-debug production issues

django-env-check solves this with one line of code.

🔧 Usage

Add this at the top of your settings.py:

from env_check import check_env

check_env([
    "SECRET_KEY",
    "DATABASE_URL",
    "EMAIL_HOST_USER",
    "EMAIL_HOST_PASSWORD"
])


If any variable is missing, Django will refuse to start:

[django-env-check] Missing environment variables: SECRET_KEY, DATABASE_URL

🟡 Warning Mode (recommended for development)

In dev mode you may not want hard failures.

check_env(["SECRET_KEY"], warn_only=True)


Output:

WARNING: [django-env-check] Missing environment variables: SECRET_KEY

💡 Tip: Auto-enable warning mode in DEBUG
check_env(["SECRET_KEY", "DATABASE_URL"], warn_only=DEBUG)

✔ Return Value

check_env(...) returns True when:

all variables exist

or warn_only=True (even if missing)

You can use this inside custom logic if needed.

❗ Custom Exception

If not using warning mode, missing variables raise:

env_check.EnvMissingError


You can catch it manually:

from env_check import check_env, EnvMissingError

try:
    check_env(["SECRET_KEY"])
except EnvMissingError as e:
    print("Config error:", str(e))

📁 Folder Structure
env_check/
    checker.py
    __init__.py
pyproject.toml
README.md
LICENSE

🧪 Testing your installation
python -c "from env_check import check_env; check_env(['X'], warn_only=True)"

python -c "from env_check import check_env; check_env(['X'])"


(Second one should raise EnvMissingError.)

📜 License

MIT License.
Feel free to use, modify and contribute.

🤝 Contributing

Pull requests are welcome!
If you’d like to improve features (like returning missing keys or adding default fallbacks), feel free to open an issue.

⭐ Support the project

If this package helps you, give it a star on GitHub ❤️
Your support encourages new features & improvements.