
from django.urls import path

from .views_doc import DocumentView


urlpatterns = [

    # Document
    path('', DocumentView.as_view(), name='document'),
    path('<str:doc>', DocumentView.as_view()),

]
