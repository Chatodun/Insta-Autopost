import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autopost_instagram.settings')
app = Celery('autopost-instagram')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
