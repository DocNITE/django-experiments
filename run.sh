# Clear old processes
killall redis-server
killall celery

# Run redis or another brocker
redis-server

# Celery
celery -A stts_site worker --loglevel=info

# a-a-and...
py manage.py runserver
