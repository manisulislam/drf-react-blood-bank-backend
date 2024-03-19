from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import BloodEventSerializers,DonorSerializers
from rest_framework.permissions import IsAuthenticated
from .models import BloodEventModel,DonorModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BloodEventView(ListCreateAPIView):
    serializer_class=BloodEventSerializers
    permissions_classes=[IsAuthenticated]
    model=BloodEventModel
class DonorListView(APIView):
    serializer_class=DonorSerializers
    def get(self, request):
        donors=DonorModel.objects.all()
        serializer=self.serializer_class(donors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
