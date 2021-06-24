release: python manage.py makemigrations main --no-input
release: python manage.py migrate main --no-input
web: gunicorn dieteticaolavarria.wsgi --log-file -
