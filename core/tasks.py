from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from celery import shared_task

User = get_user_model()


@shared_task(bind=True)
def test_func(self):
    return "*******CELERY DONE*******"


@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    for user in users:
        send_mail(
            subject="Checkout new movies",
            message="New movies",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=True
        )
    return "EMAILS WERE SENT BY CELERY"
