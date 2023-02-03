from .models import *
from rest_framework import serializers

class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
    

class AuthorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
