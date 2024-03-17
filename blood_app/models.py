from django.db import models
from accounts.models import User,UserInfo
# Create your models here.


class BloodEventModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name="user")
    userInfo=models.OneToOneField(UserInfo,on_delete=models.CASCADE, related_name="user_info")
    title=models.CharField(max_length=255)
    blood_group=models.CharField(max_length=25)
    description=models.TextField()

    def __str__(self):
        return self.title

