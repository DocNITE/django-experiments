import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stts_site.settings')

app = Celery('stts_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Im not sure, but for now we should auto-reg the tasks.py's async funcs
app.autodiscover_tasks(['suggest'])