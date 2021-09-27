
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path

from book.views import BookAddView, BookEditView, BookListView, BookDetailView


urlpatterns = [
    # Admin Views
    path('admin/', admin.site.urls),

    # Book
    path('',      RedirectView.as_view(),   name='home',  url='/book/'),
    path('book/',          BookListView.as_view(),     name='book_list'),
    path('book/<int:pk>',  BookDetailView.as_view(),   name='book_detail'),
    path('book/add',       BookAddView.as_view(),      name='book_add'),
    path('book/<int:pk>/', BookEditView.as_view(),     name='book_edit'),
]
