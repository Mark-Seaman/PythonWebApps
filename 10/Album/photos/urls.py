
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from .views_user import UserAddView, UserHomeView, UserUpdateView
from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorUpdateView


urlpatterns = [

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),

    # User
    path('',                              RedirectView.as_view(url='author/home')),
    path('author/home',                   UserHomeView.as_view(),  name='author_home'),
    path('author/add',                    UserAddView.as_view(),   name='user_add'),
    path('accounts/<int:pk>/',            UserUpdateView.as_view(),  name='user_edit'),

    # Author
    path('author/',                       AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',               AuthorDetailView.as_view(),  name='author_detail'),
    path('author/<int:pk>/',              AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',        AuthorDeleteView.as_view(),  name='author_delete'),

]
