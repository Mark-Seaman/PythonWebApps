
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from .views_author import UserUpdateView, AuthorAddView
from .views_author import AuthorDetailView, AuthorHomeView, AuthorListView, AuthorUpdateView, AuthorDeleteView
from .views_article import ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView

urlpatterns = [

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',          UserUpdateView.as_view(),  name='user_edit'),

    # Author
    path('',                           RedirectView.as_view(url='author/home')),
    path('author/',                    AuthorListView.as_view(),    name='author_list'),
    path('author/home',                AuthorHomeView.as_view(),    name='author_home'),
    path('author/<int:pk>',            AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add/',                AuthorAddView.as_view(),     name='author_add'),
    path('author/<int:pk>/',           AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',     AuthorDeleteView.as_view(),  name='author_delete'),

    # Article
    path('article/',                  ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',          ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',               ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/',         ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete',   ArticleDeleteView.as_view(),  name='article_delete'),

]
