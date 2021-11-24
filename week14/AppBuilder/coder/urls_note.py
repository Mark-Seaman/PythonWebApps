
from django.urls import path

from .views_note import NoteDeleteView, NoteDetailView, NoteListView, NoteCreateView, NoteUpdateView


urlpatterns = [

    # Note
    path('',                       NoteListView.as_view(),    name='note_list'),
    path('<int:pk>',               NoteDetailView.as_view(),  name='note_detail'),
    path('add',                    NoteCreateView.as_view(),  name='note_add'),
    path('<int:pk>/',              NoteUpdateView.as_view(),  name='note_edit'),
    path('<int:pk>/delete',        NoteDeleteView.as_view(),  name='note_delete'),

]
