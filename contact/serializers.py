from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields=['full_name','email','message']