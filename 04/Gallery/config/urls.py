from django.views.generic import RedirectView
from django.urls import path

from doc.views import DocumentView
from photos.views import PhotoDetailView, PhotoListView


urlpatterns = [

    # Home
    path('', RedirectView.as_view(url='photo/')),

    # Document
    path('doc/', DocumentView.as_view(), name='document'),
    path('doc/<str:doc>', DocumentView.as_view()),

    # Photos
    path('photo/', PhotoListView.as_view()),
    path('photo/<int:id>', PhotoDetailView.as_view()),
]
