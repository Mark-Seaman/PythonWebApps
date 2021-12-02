
from django.urls import path

from .views_document import DocumentDeleteView, DocumentDetailView, DocumentListView, DocumentCreateView, DocumentUpdateView


urlpatterns = [

    # Document
    path('',                       DocumentListView.as_view(),    name='document_list'),
    path('<int:pk>',               DocumentDetailView.as_view(),  name='document_detail'),
    path('add',                    DocumentCreateView.as_view(),  name='document_add'),
    path('<int:pk>/',              DocumentUpdateView.as_view(),  name='document_edit'),
    path('<int:pk>/delete',        DocumentDeleteView.as_view(),  name='document_delete'),

]
