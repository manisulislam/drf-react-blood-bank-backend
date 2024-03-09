from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import smart_str, smart_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse




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
    
class LogInSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=255,min_length=6)
    password=serializers.CharField(max_length=65,write_only=True)
    full_name=serializers.CharField(max_length=255,read_only=True)
    access_token=serializers.CharField(max_length=255,read_only=True)
    refresh_token=serializers.CharField(max_length=255,read_only=True)

    class Meta:
        model=User
        fields=['email','password','full_name','access_token','refresh_token']

    def validate(self, attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        request=self.context.get('request')
        user=authenticate(request,email=email, password=password)
        if not user:
            raise AuthenticationFailed('invalid credentials try again')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        user_tokens=user.tokens()


        return {
            'email':user.email,
            'full_name':user.get_full_name,
            'access_token':str(user_tokens.get('access')),
            'refresh_token':str(user_tokens.get('refresh'))

        }

class PasswordResetRequestSerializer(serializers.Serializer):
    email=serializer.EmailField(max_length=255)

    class Meta:
        fields=['email']

    def validate(self, attrs):
        email=attrs.get('email')
        if User.objects.filter(email=email).exist():
            user=User.objects.get(email=email)
            uidb64=urlsafe_base64_encode(smart_bytes(user.id))
            token=PasswordResetTokenGenerator().make_token(user)
            request=self.context.get('request')
            site_domain=get_current_site(request).domain
            relative_link=reverse('password-reset-confirm',kwargs={'uidb64':uidb64,'token':token})
            absolute_link=f"http://{site_domain}{relative_link}"
            email_body=f"hi use the link to reset your password \n {absolute_link}"
            data ={
                'email_body':email_body,
                'email_subject':"Reset Your Password",
                'to_email':user.email
            }
            send_normal_email(data)

        return attrs


class SetNewPasswordSerializer(serializers.Serializer):
    password=serializer.CharField(max_length=68, min_length=6, write_only=True)
    confirm_password=serializer.CharField(max_length=68, min_length=6, write_only=True)
    uidb64=serializer.CharField(write_only=True)
    token=serializer.CharField(write_only=True)

    class Meta:
        fields=['password','confirm_password','uidb64','token']

    def validate(self, attrs):
        try:
            password=attrs.get('password')
            confirm_password=attrs.get('confirm_password')
            uidb64=attrs.get('uidb64')
            token=attrs.get('token')

            user_id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed("link expired")
            if password!=confirm_password:
                raise AuthenticationFailed("password do not match")
            user.set_password(password)
            user.save()

            
        except Exception as e:
            return AuthenticationFailed("link expired")


        

