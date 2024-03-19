from django.contrib import admin
from .models import BloodEventModel,DonorModel
# Register your models here.
admin.site.register(BloodEventModel)
admin.site.register(DonorModel)