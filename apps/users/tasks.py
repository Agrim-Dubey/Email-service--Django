
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3})
def send_verification_email(self, email, token):
    link = f"http://localhost:8000/verify/?token={token}"

    send_mail(
        subject="Verify your account",
        message=f"Click to verify: {link}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
