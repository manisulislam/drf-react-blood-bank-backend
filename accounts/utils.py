import random
from django.core.mail import EmailMessage
from .models import User,OneTimePassword
from django.conf import settings
def generate_otp():
    otp=""
    for i in range(6):
        otp+=str(random.randint(1,9))
    return otp

def send_code_to_user(email):
    Subject="One time password for email verification"
    otp_code=generate_otp()
    user=User.objects.get(email=email)
    email_body=f"Hi {user.first_name}, Thanks for signing up.Please verify your email given otp code {otp_code} "
    from_email=settings.EMAIL_HOST
    OneTimePassword.objects.create(user=user,otp=otp_code)
    send_email=EmailMessage(subject=Subject,body=email_body,from_email=from_email,to=[email])
    send_email.send()

def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST,
        to=[data['to_email']]
    )
    email.send()