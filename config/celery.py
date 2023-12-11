from __future__ import absolute_import, unicode_literals
import os

from django.conf import settings

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("imdb")

app.conf.update(timezone="Asia/Tehran", enable_utc=True)
app.config_from_object(settings, namespace="CELERY")

# Celery Beat
app.conf.beat_schedule = {
    "send-email-every-day": {
        "task": "core.tasks.send_mail_func",
        "schedule": crontab(hour=18, minute=0),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
