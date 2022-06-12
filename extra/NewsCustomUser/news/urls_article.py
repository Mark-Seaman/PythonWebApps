
from django.urls import path

from .views_article import ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView


urlpatterns = [

    # Article
    path('',                       ArticleListView.as_view(),    name='article_list'),
    path('<int:pk>',               ArticleDetailView.as_view(),  name='article_detail'),
    path('add',                    ArticleCreateView.as_view(),  name='article_add'),
    path('<int:pk>/',              ArticleUpdateView.as_view(),  name='article_edit'),
    path('<int:pk>/delete',        ArticleDeleteView.as_view(),  name='article_delete'),

]
