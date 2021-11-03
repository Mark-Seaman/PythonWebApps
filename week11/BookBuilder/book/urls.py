
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorCreateView, AuthorUpdateView
from .views_book import BookView, BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView
from .views_chapter import ChapterDeleteView, ChapterDetailView, ChapterListView, ChapterCreateView, ChapterUpdateView
from .views_note import NoteView, NoteDeleteView, NoteDetailView, NoteListView, NoteCreateView, NoteUpdateView


urlpatterns = [

    path('',                            BookView.as_view(),        name='home'),

    # Author
    path('author/',                     AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',             AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add',                  AuthorCreateView.as_view(),  name='author_add'),
    path('author/<int:pk>/',            AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',      AuthorDeleteView.as_view(),  name='author_delete'),

    # Book
    path('book/',                       BookListView.as_view(),    name='book_list'),
    path('book/<int:pk>',               BookDetailView.as_view(),  name='book_detail'),
    path('book/add',                    BookCreateView.as_view(),  name='book_add'),
    path('book/<int:pk>/',              BookUpdateView.as_view(),  name='book_edit'),
    path('book/<int:pk>/delete',        BookDeleteView.as_view(),  name='book_delete'),

    # Chapter
    path('chapter/',                    ChapterListView.as_view(),    name='chapter_list'),
    path('chapter/<int:pk>',            ChapterDetailView.as_view(),  name='chapter_detail'),
    path('chapter/add',                 ChapterCreateView.as_view(),  name='chapter_add'),
    path('chapter/<int:pk>/',           ChapterUpdateView.as_view(),  name='chapter_edit'),
    path('chapter/<int:pk>/delete',     ChapterDeleteView.as_view(),  name='chapter_delete'),

    # Note
    path('note/',                       NoteListView.as_view(),    name='note_list'),
    path('note/<int:pk>',               NoteDetailView.as_view(),  name='note_detail'),
    path('note/add',                    NoteCreateView.as_view(),  name='note_add'),
    path('note/<int:pk>/',              NoteUpdateView.as_view(),  name='note_edit'),
    path('note/<int:pk>/delete',        NoteDeleteView.as_view(),  name='note_delete'),

]
