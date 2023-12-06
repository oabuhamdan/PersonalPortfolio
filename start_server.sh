#!/bin/bash
python manage.py makemigrations;
python manage.py migrate --noinput;
python manage.py loaddata fixtures/*;
python manage.py collectstatic --no-input;
python manage.py createsuperuser --noinput;
gunicorn mysite.wsgi:application -b 0.0.0.0:8000 --log-file /app/static/gunicorn_error.log;
