
from django.contrib import admin
from django.urls import path

from book.views import BookView, BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Book Views
    path('', BookView.as_view()),
    path('book/',                   BookListView.as_view(),    name='book_list'),
    path('book/<int:pk>',           BookDetailView.as_view(),  name='book_detail'),
    path('book/add',                BookCreateView.as_view(),  name='book_add'),
    path('book/<int:pk>/',          BookUpdateView.as_view(),  name='book_edit'),
    path('book/<int:pk>/delete',    BookDeleteView.as_view(),  name='book_delete'),

]
