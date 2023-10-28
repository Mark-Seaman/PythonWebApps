from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import PhotoCarouselView, PhotoDeleteView, PhotoDetailView, PhotoListView, PhotoCreateView, PhotoUpdateView


urlpatterns = [

    # Photo
    path('photo/',                      PhotoListView.as_view(),    name='photo_list'),
    path('photo/<int:pk>',              PhotoDetailView.as_view(),  name='photo_detail'),
    path('photo/add',                   PhotoCreateView.as_view(),  name='photo_add'),
    path('photo/<int:pk>/',             PhotoUpdateView.as_view(),  name='photo_edit'),
    path('photo/<int:pk>/delete',       PhotoDeleteView.as_view(),  name='photo_delete'),

    # Photo Display
    path('photo/carousel',              PhotoCarouselView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
