from django.urls import path
from photos.views import PhotosView

urlpatterns = [
    path('', PhotosView.as_view()),
]
