# Django Blog

A simple Django blog application demonstrating basic project setup and HTTP response handling.

## Setup Instructions

### 1. Environment Setup

- Create project folder and open in IDE
- Create GitHub repository and connect to workspace
- Set up virtual environment with Python 3.12:
  - Use Command Palette → Python: Create environment → Venv → Python 3.12
  - Add `.venv` to `.gitignore`
  - Restart terminal

### 2. Install Django

```bash
pip3 install django~=4.2.1
pip3 freeze > requirements.txt
```

### 3. Create Project & App

```bash
# Create Django project
django-admin startproject config .

# Create blog app
python3 manage.py startapp blog
```

### 4. Configure Application

**Add app to `config/settings.py`:**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

**Create view in `blog/views.py`:**

```python
from django.http import HttpResponse

def blog(request):
    return HttpResponse("Hello, blog!")
```

**Configure URL in `config/urls.py`:**

```python
from django.contrib import admin
from django.urls import path
from blog.views import blog

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('admin/', admin.site.urls),
]
```

### 5. Troubleshooting

- **psycopg2 Installation Issue**: If you encounter a `Getting requirements to build wheel` error when installing `psycopg2`, use the pre-compiled binary package instead:
  ```bash
  pip3 install psycopg2-binary
  ```
  This avoids the need to compile from source. For more details, see the [official documentation](https://www.psycopg.org/docs/install.html).

### 6. Run Server

```bash
python3 manage.py runserver
```

Visit `http://localhost:8000/blog/` to see "Hello, blog!" displayed.

## URLs Configuration

The `config/urls.py` file maps URL patterns to views:

```python
urlpatterns = [
    path('blog/', blog, name='blog'),    # /blog/ → blog view
    path('admin/', admin.site.urls),     # /admin/ → Django admin
]
```

- **URL Pattern**: `'blog/'` matches requests to `/blog/`
- **View Function**: `blog` handles the request and returns a response
- **Name**: `'blog'` allows reverse URL lookup with `{% url 'blog' %}` or `reverse('blog')`

## Running the Server

Start the Django development server:

```bash
python3 manage.py runserver
```

The server will run on `http://localhost:8000/` by default.

**Available URLs:**

- `http://localhost:8000/blog/` - Displays "Hello, blog!"
- `http://localhost:8000/admin/` - Django admin interface

**To stop the server:** Press `Ctrl+C` in the terminal

## Key Concepts

- **Virtual Environment**: Isolated Python environment for project dependencies
- **Django Project**: Container for all apps and configuration (`config/`)
- **Django App**: Modular component with specific functionality (`blog/`)
- **URL Patterns**: Maps URLs to view functions with reusable names
- **HttpResponse**: Returns text/HTML content to the browser

## Project Structure

```
django-blog/
├── .venv/              # Virtual environment (gitignored)
├── .gitignore          # Git ignore rules
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── db.sqlite3          # SQLite database
├── blog/               # Blog application
│   ├── views.py        # View functions
│   ├── models.py       # Database models
│   └── ...
└── config/             # Project configuration
    ├── settings.py     # Django settings
    ├── urls.py         # URL routing
    └── ...
```
