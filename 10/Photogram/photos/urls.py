
from django.urls import path

<<<<<<< HEAD
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

=======
from .views import ImageCreateView, ImageDeleteView, ImageListView, PhotoDeleteView, PhotoDetailView, PhotoListView, PhotoCreateView, \
    PhotoUpdateView
from django.contrib import admin

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Photogram
    path('',                   PhotoListView.as_view(),    name='photo_list'),
    path('<int:pk>',           PhotoDetailView.as_view(),  name='photo_detail'),
    path('add',                PhotoCreateView.as_view(),  name='photo_add'),
    path('<int:pk>/',          PhotoUpdateView.as_view(),  name='photo_edit'),
    path('<int:pk>/delete',    PhotoDeleteView.as_view(),  name='photo_delete'),

    # Image
    path('image/',                      ImageListView.as_view(),    name='image_list'),
    path('image/add',                   ImageCreateView.as_view(),  name='image_add'),
    path('image/<int:pk>/delete',       ImageDeleteView.as_view(),  name='image_delete'),
>>>>>>> ba095
]
