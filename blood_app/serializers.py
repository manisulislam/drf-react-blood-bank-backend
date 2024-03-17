from rest_framework import serializers
from .models import BloodEventModel

class BloodEventSerializers(serializers.ModelSerializer):
    class Meta:
        model=BloodEventModel
        fields=['title','blood_group','description']

