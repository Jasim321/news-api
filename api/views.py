from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes

from rest_framework.permissions import IsAuthenticated

class NewsArticleList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    @api_view(('GET',))
    def newsList(request):
        """
        Return a list of all Articles.
        """
        article = Articles.objects.all()
        serializer = NewsListSerializer(article, many=True)
        return Response(serializer.data)
    
    @api_view(('GET',))
    def newsDetail(request, pk):
        """
        Return a list of all Articles.
        """
        article = Articles.objects.get(id=pk)
        serializer = NewsListSerializer(article, many=False)
        return Response(serializer.data)

class AuthorsList(APIView):
    """
        Return a list of Authors
    """
    permission_classes = [IsAuthenticated]

    @api_view(('GET',))
    def authorsList(request):
        users = Author.objects.all()
        serializer = AuthorsListSerializer(users, many=True)
        return Response(serializer.data)
    
    @api_view(('GET',))
    def authorsDetail(request, pk):
        user = Author.objects.get(id=pk)
        serializer = AuthorsListSerializer(user, many=False)
        return Response(serializer.data)

class CategoryList(APIView):
    """
        Return a list of Categories
    """
    permission_classes = [IsAuthenticated]

    @api_view(('GET',))
    def categoryList(request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)                    
    
    @api_view(('GET',)) 
    def categoryDetail(request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategoryListSerializer(category, many=False)
        return Response(serializer.data)
