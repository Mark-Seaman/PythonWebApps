
from django.urls import path

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
]
