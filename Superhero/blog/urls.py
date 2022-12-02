from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    #Article
    path("article/", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
]