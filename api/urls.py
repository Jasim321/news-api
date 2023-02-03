from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('articles/', NewsArticleList.newsList, name='articles'),
    path('get-article/<str:pk>', NewsArticleList.newsDetail, name='get-article'),
    
    path('authors/', AuthorsList.authorsList, name='authors'),
    path('get-author/<str:pk>', AuthorsList.authorsDetail, name='get-author'),
    
    path('categories/', CategoryList.categoryList, name='categories'),
    path('get-category/<str:pk>', CategoryList.categoryDetail, name='get-category'),
    
]
