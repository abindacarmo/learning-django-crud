# 🐍 Django Command Reference
> From Environment Setup to App Creation

---

## 1. Setting Up Virtual Environment

Before starting a Django project, create a **virtual environment** to isolate your project's dependencies from the global Python installation.

| Command | Description |
|---|---|
| `python -m venv env` | Create a virtual environment named `env` |
| `python -m venv venv` | Create a virtual environment named `venv` (common alternative) |
| `source env/bin/activate` | Activate virtual environment **(Linux / macOS)** |
| `env\Scripts\activate` | Activate virtual environment **(Windows CMD)** |
| `.\env\Scripts\Activate.ps1` | Activate virtual environment **(Windows PowerShell)** |
| `deactivate` | Deactivate the current virtual environment |

> 📝 **Note:** Always activate your virtual environment before running any Django commands.

---

## 2. Installing Django

After activating the virtual environment, install Django using `pip`.

| Command | Description |
|---|---|
| `pip install django` | Install the latest version of Django |
| `pip install django==4.2` | Install a specific version of Django |
| `pip install -r requirements.txt` | Install all dependencies from requirements file |
| `pip freeze > requirements.txt` | Export installed packages to `requirements.txt` |
| `pip show django` | Show installed Django version and info |
| `pip list` | List all installed packages in the environment |

---

## 3. Creating a Django Project

A Django **project** is the top-level container for your entire web application, including settings, URLs, and configurations.

| Command | Description |
|---|---|
| `django-admin startproject myproject` | Create a new Django project named `myproject` |
| `django-admin startproject myproject .` | Create project in the current directory (no subdirectory) |
| `cd myproject` | Navigate into the project directory |

> 📝 **Note:** The dot (`.`) at the end avoids creating a nested project folder — useful when you already created a directory.

### Project Structure
```
myproject/
├── manage.py               ← Command-line utility for project management
└── myproject/
    ├── __init__.py         ← Marks directory as a Python package
    ├── settings.py         ← All project configuration (DB, apps, etc.)
    ├── urls.py             ← URL routing — maps URLs to views
    ├── wsgi.py             ← WSGI entry point for deployment
    └── asgi.py             ← ASGI entry point for async/WebSocket support
```

---

## 4. Running the Development Server

| Command | Description |
|---|---|
| `python manage.py runserver` | Start dev server at `http://127.0.0.1:8000/` |
| `python manage.py runserver 8080` | Run server on a custom port (e.g. 8080) |
| `python manage.py runserver 0.0.0.0:8000` | Allow access from other devices on the network |
| `Ctrl + C` | Stop the running development server |

---

## 5. Creating a Django App

A Django **app** is a modular component within a project that handles a specific functionality (e.g., blog, users, products). One project can have multiple apps.

| Command | Description |
|---|---|
| `python manage.py startapp myapp` | Create a new app named `myapp` |
| `python manage.py startapp blog` | Example: create an app named `blog` |
| `python manage.py startapp users` | Example: create an app named `users` |

> 📝 **Note:** After creating an app, register it in `settings.py` under `INSTALLED_APPS`:
> ```python
> INSTALLED_APPS = [
>     ...
>     'myapp',  # add your app here
> ]
> ```

### App Structure
```
myapp/
├── migrations/     ← Stores database migration files
├── __init__.py
├── admin.py        ← Register models to display in Django Admin
├── apps.py         ← App configuration class
├── models.py       ← Define your database models (tables & fields)
├── tests.py        ← Write automated tests for the app
└── views.py        ← Business logic — handles requests and returns responses
```

> 📝 **Note:** `urls.py` and `forms.py` are **not generated automatically** — you need to create them manually.

---

## 6. Database & Migrations

Migrations are Django's way of propagating changes you make to your **models** into the database schema.

| Command | Description |
|---|---|
| `python manage.py makemigrations` | Detect model changes and create migration files |
| `python manage.py makemigrations myapp` | Create migrations for a specific app only |
| `python manage.py migrate` | Apply all pending migrations to the database |
| `python manage.py migrate myapp` | Apply migrations for a specific app only |
| `python manage.py showmigrations` | List all migrations and their status |
| `python manage.py sqlmigrate myapp 0001` | Show the SQL for a specific migration |

---

## 7. Admin Panel & Superuser

Django comes with a powerful built-in admin interface. Create a superuser to access it.

| Command | Description |
|---|---|
| `python manage.py createsuperuser` | Create an admin/superuser account (interactive) |
| `python manage.py changepassword username` | Change the password for a specific user |

> 📝 **Note:** Access the admin panel at `http://127.0.0.1:8000/admin/` after creating a superuser.

---

## 8. Other Useful Commands

| Command | Description |
|---|---|
| `python manage.py shell` | Open an interactive Python shell with Django context |
| `python manage.py dbshell` | Open a database shell (SQLite, PostgreSQL, etc.) |
| `python manage.py check` | Check the project for any errors or issues |
| `python manage.py collectstatic` | Collect all static files into `STATIC_ROOT` |
| `python manage.py test` | Run all tests in the project |
| `python manage.py test myapp` | Run tests for a specific app |
| `python manage.py flush` | Clear all data from the database (reset tables) |
| `python manage.py loaddata fixture.json` | Load data from a fixture file into the database |
| `python manage.py dumpdata myapp > file.json` | Export app data to a JSON fixture file |
| `python manage.py help` | Show all available management commands |

---

## ⚡ Quick Start Workflow Summary

Here is the complete sequence from zero to a running Django project with an app:

```bash
# Step 1 — Create virtual environment
python -m venv env

# Step 2 — Activate it (Linux/macOS)
source env/bin/activate
# or on Windows:
# env\Scripts\activate

# Step 3 — Install Django
pip install django

# Step 4 — Create Django project
django-admin startproject myproject .

# Step 5 — Create an app
python manage.py startapp myapp

# Step 6 — Register app in settings.py
# Add 'myapp' to INSTALLED_APPS manually

# Step 7 — Create migration files
python manage.py makemigrations

# Step 8 — Apply migrations to database
python manage.py migrate

# Step 9 — Create admin account
python manage.py createsuperuser

# Step 10 — Start development server
python manage.py runserver
```

---

*Happy coding! 🚀*