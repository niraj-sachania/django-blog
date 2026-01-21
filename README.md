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

- **Admin Theme/Styling Not Loading**: If the Django admin panel appears without CSS styling, you have three options:

  **Option 1 (Development):** Set `DEBUG = True` in `config/settings.py`

  **Option 2 (Production):** Collect static files:

  ```bash
  python3 manage.py collectstatic
  ```

  Ensure `STATIC_ROOT` and `STATIC_URL` are properly configured in your settings.

  **Option 3 (Heroku):** Remove the `DISABLE_COLLECTSTATIC` config variable:

  ```bash
  heroku config:unset DISABLE_COLLECTSTATIC
  ```

  Then redeploy your app. Heroku will automatically run collectstatic during deployment.

### 6. Load Sample Data (Optional)

To populate the database with sample blog posts:

1. Create a fixtures directory:

   ```bash
   mkdir -p blog/fixtures
   ```

2. Add your fixture data in `blog/fixtures/posts.json` (JSON format with model data)

3. Load the fixture data:
   ```bash
   python3 ./manage.py loaddata posts
   ```

**To create a JSON dump of existing data:**

```bash
# Dump all data from a specific model
python3 ./manage.py dumpdata blog.Post > blog/fixtures/posts.json

# Dump with indentation for readability
python3 ./manage.py dumpdata blog.Post --indent 2 > blog/fixtures/posts.json

# Dump all data from the blog app
python3 ./manage.py dumpdata blog --indent 2 > blog/fixtures/blog_data.json
```

This is useful for testing, development purposes, and backing up data.

### 7. Run Server

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

## Terminal Commands Reference

All terminal commands used in this project, in chronological order:

### Environment Setup

```bash
# Activate virtual environment
source /Users/nss/Documents/dev/2025/django-blog/.venv/bin/activate
```

### Django Installation

```bash
# Install Django
pip3 install django~=4.2.1

# Save dependencies (use --local to exclude global packages)
pip3 freeze > requirements.txt
pip3 freeze --local > requirements.txt
```

### Project Creation

```bash
# Create Django project (config directory)
django-admin startproject config .

# Create blog app
python3 manage.py startapp blog
```

### Database Setup

```bash
# Install PostgreSQL adapter
pip3 install psycopg2-binary

# Install database URL parser
pip3 install dj-database-url

# Update requirements
pip3 freeze > requirements.txt

# Make migrations (create migration files)
python3 manage.py makemigrations

# Apply migrations (update database schema)
python3 manage.py migrate

# Create superuser for admin access
python3 manage.py createsuperuser

# Load fixture data (if you have a posts.json file)
python3 ./manage.py loaddata posts
```

### Additional Package Installations

```bash
# Install Django Allauth (for authentication)
pip3 install django-allauth

# Install Django Summernote (for rich text editor)
pip3 install django-summernote

# Update requirements
pip3 freeze --local > requirements.txt
```

**Required configurations:**

**Django Allauth:**

- Add `'django.contrib.sites'`, `'allauth'`, `'allauth.account'`, `'allauth.socialaccount'` to `INSTALLED_APPS`
- Add `'allauth.account.middleware.AccountMiddleware'` to `MIDDLEWARE`
- Set `SITE_ID = 1`
- Configure `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL`
- Add `path("accounts/", include("allauth.urls"))` to `urls.py`
- Run migrations: `python3 manage.py migrate`

**Django Summernote:**

- Add `'django_summernote'` to `INSTALLED_APPS`
- Add `path('summernote/', include('django_summernote.urls'))` to `urls.py`
- Run migrations: `python3 manage.py migrate`
- Use in admin: `from django_summernote.admin import SummernoteModelAdmin`

**dj-database-url:**

- Import in settings: `import dj_database_url`
- Parse DATABASE_URL: `DATABASES = {'default': dj_database_url.parse(os.getenv("DATABASE_URL"))}`

**Gunicorn:**

- Create `Procfile`: `web: gunicorn config.wsgi`
- No additional Django configuration needed

**psycopg2-binary:**

- No configuration needed (PostgreSQL adapter for Python)

### Deployment Setup

```bash
# Install Gunicorn web server
pip3 install gunicorn

# Update requirements
pip3 freeze > requirements.txt

# Log in to Heroku
heroku login

# Create Heroku app
heroku create <app-name>

# Add PostgreSQL database
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DATABASE_URL="your-database-url"

# Deploy to Heroku
git push heroku main

# Run migrations on Heroku
heroku run python manage.py migrate

# Collect static files (for production)
python3 manage.py collectstatic

# Create superuser on Heroku
heroku run python manage.py createsuperuser

# Open deployed app
heroku open

# View logs
heroku logs --tail
```

### Development Server

```bash
# Run local development server
python3 manage.py runserver

# Stop server: Ctrl+C
```

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
