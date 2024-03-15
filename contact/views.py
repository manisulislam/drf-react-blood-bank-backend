from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import ContactUsSerializer
from rest_framework.permissions import IsAuthenticated
from .models import ContactUs
# Create your views here.

class ContactUsView(ListCreateAPIView):
    serializer_class=ContactUsSerializer
    permission_classes=[IsAuthenticated]
    model=ContactUs