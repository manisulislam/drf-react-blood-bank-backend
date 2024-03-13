from django.contrib import admin
from .models import User, UserInfo

# Register your models here.

admin.site.register(User)
admin.site.register(UserInfo)