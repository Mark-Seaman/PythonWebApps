
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorCreateView, AuthorHomeView, AuthorUpdateView, UserUpdateView


urlpatterns = [

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',          UserUpdateView.as_view(),  name='user_edit'),

    # Author
    path('',                              RedirectView.as_view(url='author/home')),
    path('author/home',                   AuthorHomeView.as_view(),    name='author_home'),

    path('author/',                       AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',               AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add',                    AuthorCreateView.as_view(),  name='author_add'),
    path('author/<int:pk>/',              AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',        AuthorDeleteView.as_view(),  name='author_delete'),

]
