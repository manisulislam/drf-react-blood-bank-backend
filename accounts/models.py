from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_laze as _
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True,max_length=55,verbose_name=_('Emial Address'))
    first_name=models.CharField(max_length=100,verbose_name=_('First Name'))
    last_name=models.CharField(max_length=100,verbose_name=_('Last Name'))
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    date_joinded=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    def __str__(self):
        return self.email
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def tokens(self):
        pass