from django.contrib import admin
from django.urls import path
from photos.views import PhotoView

urlpatterns = [
    path('', PhotoView.as_view()),
]
