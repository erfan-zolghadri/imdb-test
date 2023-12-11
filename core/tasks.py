from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string

from celery import shared_task

from .models import Movie

User = get_user_model()


@shared_task(bind=True)
def send_mail_func(self):
    movie_queryset = Movie.objects.all().order_by("-created_at")[:5]
    users = User.objects.all()
    email_subject = "Checkout new movies"
    email_body = render_to_string(
        template_name="email.html", context={"movie_queryset": movie_queryset}
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    for user in users:
        send_mail(
            subject=email_subject,
            message=email_body,
            from_email=from_email,
            recipient_list=[user.email],
            fail_silently=True,
        )
    return "EMAILS WERE SENT"
