from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    password2=serializers.CharField(max_length=68,min_length=6,write_only=True)

    class Meta:
        model=User
        fields=['email','first_name','last_name','password','password2']

    def validate(self, attrs):
        password=attrs['password']
        password2=attrs['password2']

        if password!=password2:
            raise ValidationError(_('Password do not match'))
        return attrs


    def create(self,validated_data):
        email=validated_data['email']
        first_name=validated_data.get('first_name')
        last_name=validated_data.get('last_name')
        password=validated_data.get('password')
        user=User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        return user