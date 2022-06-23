
from django.urls import path

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorHomeView, AuthorListView, AuthorUpdateView
from .views_photogram import PhotogramDeleteView, PhotogramDetailView, PhotogramListView, PhotogramCreateView, PhotogramUpdateView


urlpatterns = [

    # Default
    path('',                              AuthorHomeView.as_view(), name='author_home'),

    # Author
    path('author/',                       AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',               AuthorDetailView.as_view(),  name='author_detail'),
    # path('author/add',                  AuthorCreateView.as_view(),  name='author_add'),
    path('author/<int:pk>/',              AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',        AuthorDeleteView.as_view(),  name='author_delete'),

    # Photogram
    path('photogram/',                       PhotogramListView.as_view(),    name='photogram_list'),
    path('photogram/<int:pk>',               PhotogramDetailView.as_view(),  name='photogram_detail'),
    path('photogram/add',                    PhotogramCreateView.as_view(),  name='photogram_add'),
    path('photogram/<int:pk>/',              PhotogramUpdateView.as_view(),  name='photogram_edit'),
    path('photogram/<int:pk>/delete',        PhotogramDeleteView.as_view(),  name='photogram_delete'),

]
