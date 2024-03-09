from django.shortcuts import render
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .utils import send_code_to_user
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