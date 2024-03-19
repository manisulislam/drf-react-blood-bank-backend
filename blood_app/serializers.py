from rest_framework import serializers
from .models import BloodEventModel,DonorModel

class BloodEventSerializers(serializers.ModelSerializer):
    class Meta:
        model=BloodEventModel
        fields=['title','blood_group','description']

class DonorSerializers(serializers.ModelSerializer):
    class Meta:
        model=DonorModel
        fields=['name','blood_group','location','phone_number']

