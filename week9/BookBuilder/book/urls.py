
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path

from book.views import BookView, BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView

urlpatterns = [

    path('',                   BookListView.as_view(),    name='book_list'),
    path('<int:pk>',           BookDetailView.as_view(),  name='book_detail'),
    path('add',                BookCreateView.as_view(),  name='book_add'),
    path('<int:pk>/',          BookUpdateView.as_view(),  name='book_edit'),
    path('<int:pk>/delete',    BookDeleteView.as_view(),  name='book_delete'),

]
