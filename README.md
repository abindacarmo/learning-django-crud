# Learning Django CRUD

A simple CRUD application built with Django as part of learning Python web development.

## 🛠️ Tech Stack
- Python 3.x
- Django 4.x
- SQLite (default database)

## ✨ Features
- Create — add new student data
- Read — display student list & detail
- Update — edit existing student data
- Delete — remove student data

## 🚀 Getting Started

### 1. Clone the repository
git clone https://github.com/abindacarmo/learning-django-crud.git
cd learning-django-crud

### 2. Create a virtual environment
python -m venv env
- source env/bin/activate  # Linux/Mac
- env\Scripts\activate     # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run migrations
python manage.py migrate

### 5. Start the development server
python manage.py runserver

Open in browser: http://127.0.0.1:8000

## 📁 Project Structure
```
PRATIKA_DJANGO/
├── manage.py
├── README.md
├── .gitignore
├── db.sqlite3
├── App/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
├── practice_django/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── static/
│   ├── css/
│   └── js/
└── template/
    ├── base.html
    ├── home.html
    ├── konaba.html
    └── lista_estudante.html

```

## 🎯 Learning Goals
This project was built to understand the basics of Django, including:
- MVT (Model-View-Template) pattern
- Django ORM
- URL routing
- Form handling
- Static files management

## 📝 License
This project is open source and available under the MIT License.
