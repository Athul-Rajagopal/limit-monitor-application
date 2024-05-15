from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

app = Celery('limit_monitor')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'check-limits-every-midnight': {
        'task': 'monitor.tasks.check_limits',
        'schedule': crontab(hour=0, minute=0),
    },
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
