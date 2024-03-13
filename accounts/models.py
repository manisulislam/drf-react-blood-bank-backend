from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True,max_length=55,verbose_name=_('Email Address'))
    first_name=models.CharField(max_length=100,verbose_name=_('First Name'))
    last_name=models.CharField(max_length=100,verbose_name=_('Last Name'))
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    objects=UserManager()

    def __str__(self):
        return self.email
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
class OneTimePassword(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    otp=models.CharField(max_length=6)


    def __str__(self):
        return f"{self.user.first_name} passcode"


class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.CharField(max_length=4)
    address=models.CharField(max_length=255)
    last_donation_date=models.DateTimeField()
    isDonate=models.BooleanField(default=False)
    blood_group=models.CharField(max_length=30)


    def __str__(self):
        return self.user.first_name