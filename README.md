# 9kloud — Online Courses (Django)

A Django-powered online courses site with authentication, searchable courses, enroll/unenroll, My Courses, and a unified base layout.

## Features
- Authentication: signup/login/logout, password reset (console email in dev)
- Courses: list with search, detail page with lessons, enroll/unenroll
- My Courses: see enrolled courses
- Teachers: dynamic from `Instructor` model
- Unified layout: `templates/base.html` with navbar auth links, search, messages, and footer

## Local Development
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell
pip install -r requirements.txt  # if present, else: pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit:
- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Courses: http://127.0.0.1:8000/courses/

## Password Reset (Dev)
Emails are printed to the console by default. Trigger at `/accounts/password_reset/` and use the link from the server output.

## Production Settings
Set environment variables and run with `DJANGO_SETTINGS_MODULE=ninekloud.settings_prod`.

Important env vars:
- `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`
- Database: `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- Email: `EMAIL_BACKEND`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS`, `DEFAULT_FROM_EMAIL`

Static files:
```bash
python manage.py collectstatic --noinput
```

## Deploying
Use Gunicorn/Uvicorn behind Nginx or a PaaS (Render/Railway). Example run:
```bash
export DJANGO_SETTINGS_MODULE=ninekloud.settings_prod
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn ninekloud.wsgi:application --bind 0.0.0.0:8000
```

## License
MIT
