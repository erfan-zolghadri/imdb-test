from django.contrib.auth import get_user_model

from celery import shared_task

User = get_user_model()


@shared_task(bind=True)
def send_mail_func(self):
    return "EMAIL WAS SENT"