from django.urls.conf import include, include
from django.urls import path

from .views_author import AuthorAddView, AuthorDeleteView, AuthorDetailView, AuthorHomeView, AuthorListView, AuthorCreateView, AuthorUpdateView, UserUpdateView
from .views_book import BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView
from .views_chapter import ChapterDeleteView, ChapterDetailView, ChapterListView, ChapterCreateView, ChapterUpdateView


urlpatterns = [

    # Accounts
    path('accounts/',                   include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',          UserUpdateView.as_view(),  name='account_edit'),
    path('accounts/signup/',            AuthorAddView.as_view(), name='signup'),

    # News
    path('',                            AuthorHomeView.as_view()),

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
    path('chapter/<int:book>/',         ChapterListView.as_view(),    name='chapter_list'),
    path('chapter/<int:pk>',            ChapterDetailView.as_view(),  name='chapter_detail'),
    path('chapter/<int:book>/add',      ChapterCreateView.as_view(),  name='chapter_add'),
    path('chapter/<int:pk>/',           ChapterUpdateView.as_view(),  name='chapter_edit'),
    path('chapter/<int:pk>/delete',     ChapterDeleteView.as_view(),  name='chapter_delete'),

]
