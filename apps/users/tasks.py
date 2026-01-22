from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3})
def send_verification_email(self, student_mail, student_name):
    subject = "Welcome to Our Platform"
    
    plain_message = f"""
    Hello {student_name},
    
    Your registration is successful!
    
    Thank you for joining us.
    
    Regards,
    Team
    """
    
    html_message = f"""
    <html>
    <body style="font-family: Arial, sans-serif;">
        <h2>Hello {student_name}! 👋</h2>
        <p>Your registration is <strong>successful!</strong></p>
        <p>Thank you for joining us.</p>
        <p><strong>Regards,</strong><br>Team</p>
    </body>
    </html>
    """
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[student_mail],
        html_message=html_message,
        fail_silently=False,
    )