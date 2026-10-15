# Business Management System (Django)

Accounting, inventory, sales, purchases, customers, suppliers, and reports for small businesses (spare parts shop focus).

**Status: Stage 1 of 10** — project skeleton, settings, database configuration, and a status page.

## Requirements
- Python 3.10+ (3.12 recommended)
- Git

## Installation
```bash
python -m venv .venv
# Windows:   .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration
```bash
cp .env.example .env        # Windows: copy .env.example .env
```
Generate a secret key and paste it into `.env` as `DJANGO_SECRET_KEY`:
```bash
python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
```

## Database and first run
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/ (status page), http://127.0.0.1:8000/health/ and http://127.0.0.1:8000/admin/.

## Tests
```bash
python manage.py test
python manage.py check
```

## PostgreSQL (production)
Set `DB_ENGINE=postgres` plus `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` in `.env`, set `DJANGO_DEBUG=False`, then run `migrate`.
Production checklist is expanded in Stage 10.
