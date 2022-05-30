from django.urls import path
from photos.views import PhotoDetailView, PhotoListView

urlpatterns = [
    path('', PhotoListView.as_view()),
    path('<int:id>', PhotoDetailView.as_view()),
]
