# Run redis or another brocker
redis-server

# Celery
celery -A stts_site worker --loglevel=info

# a-a-and...
py manage.py runserver
