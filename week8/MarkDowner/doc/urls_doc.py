
from django.urls import path

from .views_doc import DocumentDeleteView, DocumentDetailView, DocumentListView, DocumentCreateView, DocumentUpdateView


urlpatterns = [

    # Document
    path('',                       DocumentListView.as_view(),    name='doc_list'),
    path('<int:pk>',               DocumentDetailView.as_view(),  name='doc_detail'),
    path('add',                    DocumentCreateView.as_view(),  name='doc_add'),
    path('<int:pk>/',              DocumentUpdateView.as_view(),  name='doc_edit'),
    path('<int:pk>/delete',        DocumentDeleteView.as_view(),  name='doc_delete'),

]
