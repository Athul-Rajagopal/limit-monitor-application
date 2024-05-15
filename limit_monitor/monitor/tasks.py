# tasks.py
from celery import shared_task
from .models import Limit

@shared_task
def check_limits():
    limits = Limit.objects.all()
    for limit in limits:
        if limit.is_met():
            limit.status = 'Completed'
            limit.save()
