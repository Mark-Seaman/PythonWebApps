
from django.urls import path

from .views_article import ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView
from .views_blog import BlogDeleteView, BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView


urlpatterns = [

    # Article
    path('article/',                       ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',               ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',                    ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/',              ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete',        ArticleDeleteView.as_view(),  name='article_delete'),

    # Blog
    path('blog/',                       BlogListView.as_view(),    name='blog_list'),
    path('blog/<int:pk>',               BlogDetailView.as_view(),  name='blog_detail'),
    path('blog/add',                    BlogCreateView.as_view(),  name='blog_add'),
    path('blog/<int:pk>/',              BlogUpdateView.as_view(),  name='blog_edit'),
    path('blog/<int:pk>/delete',        BlogDeleteView.as_view(),  name='blog_delete'),

]
