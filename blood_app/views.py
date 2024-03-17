from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import BloodEventSerializers
from rest_framework.permissions import IsAuthenticated
from .models import BloodEventModel
# Create your views here.

class BloodEventView(ListCreateAPIView):
    serializer_class=BloodEventSerializers
    permissions_classes=[IsAuthenticated]
    model=BloodEventModel