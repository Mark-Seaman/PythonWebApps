from django.urls import path
from photos.views import PhotoView, PhotoListView

urlpatterns = [
    path('<str:name>', PhotoView.as_view()),
    path('', PhotoListView.as_view()),
]
