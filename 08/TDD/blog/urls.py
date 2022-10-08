from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # Article
    path("article/", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("article/add", ArticleCreateView.as_view(), name="article_add"),
    path("article/<int:pk>/", ArticleUpdateView.as_view(), name="article_edit"),
    path("article/<int:pk>/delete", ArticleDeleteView.as_view(), name="article_delete"),
]
