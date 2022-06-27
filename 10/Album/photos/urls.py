
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorAddView, AuthorHomeView, AuthorUpdateView, UserUpdateView


urlpatterns = [

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),

    # User
    path('',                              RedirectView.as_view(url='author/home')),
    path('author/home',                   AuthorHomeView.as_view(),  name='author_home'),
    path('author/add',                    AuthorAddView.as_view(),   name='user_add'),
    path('accounts/<int:pk>/',            UserUpdateView.as_view(),  name='user_edit'),

    # Author
    path('author/',                       AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',               AuthorDetailView.as_view(),  name='author_detail'),
    path('author/<int:pk>/',              AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',        AuthorDeleteView.as_view(),  name='author_delete'),

]
