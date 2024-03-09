from django.shortcuts import render
from .serializers import UserRegisterSerializer,LogInSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .utils import send_code_to_user
from .models import OneTimePassword
from rest_framework.permissions import IsAuthenticated
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
        