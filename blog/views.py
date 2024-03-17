from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import BlogSerializer
from .models import BlogModel

# Create your views here.

class BlogView(ListAPIView):
    serializer_class=BlogSerializer
    model=BlogModel