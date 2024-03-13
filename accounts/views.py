from django.shortcuts import render
from .serializers import UserRegisterSerializer,LogInSerializer,PasswordResetRequestSerializer,SetNewPasswordSerializer,LogOutUserSerializer,UserInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .utils import send_code_to_user
from .models import OneTimePassword,User
from rest_framework.permissions import IsAuthenticated
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# Create your views here.

class UserRegisterView(GenericAPIView):
    serializer_class=UserRegisterSerializer

    def post(self,request):
        user=request.data
        serializer=self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data=serializer.data
            #send an email
            send_code_to_user(user['email'])
            return Response({
                'data':user_data,
                'message': "Thanks for signing up a otp code sent to verify your email"

            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class VerifyUserEmail(GenericAPIView):
    def post(self, request):
        otp_code=request.data.get('otp_code')
        try:
            otp_code_object=OneTimePassword.objects.get(otp=otp_code)
            user=otp_code_object.user
            if not user.is_verified:
                user.is_verified=True
                user.save()
                return Response({'message':'successfully verified email'},status=status.HTTP_200_OK)
            return Response({'message':f'{user.first_name} is already verified'},status=status.HTTP_204_NO_CONTENT)
           
        except OneTimePassword.DoesNotExist:
            return Response({
                'message':'otp code not provided'
            },status=status.HTTP_404_NOT_FOUND)
    
class LoginUserView(GenericAPIView):
    serializer_class=LogInSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class TestAuthenticationView(GenericAPIView):
     permission_classes = [IsAuthenticated]

     def get(self, request):
        data={
            'msg':'it is working'
        }
        return Response(data, status=status.HTTP_200_OK)
        
class PasswordResetRequestView(GenericAPIView):
    serializer_class=PasswordResetRequestSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response({
            'message':'a link has to be sent to your email to reset password'
        },status=status.HTTP_200_OK)


class PasswordResetConfirmView(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            user_id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'massage':'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({
                'success':True,
                'message':'Password reset confirm',
                'uidb64':uidb64,
                'token':token
            },status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError:
            return Response({'massage':'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

class SetNewPasswordView(GenericAPIView):

    serializer_class=SetNewPasswordSerializer

    def patch(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message':'password reset successfully'}, status=status.HTTP_200_OK)

class LogOutUserView(GenericAPIView):

    serializer_class=LogOutUserSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

class UserInfoView(GenericAPIView):
    serializer_class=UserInfoSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_204_NO_CONTENT)
