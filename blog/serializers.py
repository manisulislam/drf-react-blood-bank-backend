from rest_framework import serializers
from .models import BlogModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel
        fields=['title','description']