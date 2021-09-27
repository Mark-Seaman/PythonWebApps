
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path

<<<<<<< HEAD
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
=======
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

>>>>>>> 8d974573ad4e9519dc36325f4186732bed818555
]
