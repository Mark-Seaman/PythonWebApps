from django.urls import include, path

from .views_accounts import UserHomeView, UserAddView, UserUpdateView
from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorUpdateView
from .views_book import BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView
from .views_chapter import ChapterDeleteView, ChapterDetailView, ChapterCreateView, ChapterUpdateView


urlpatterns = [

    # User Accounts
    path('',                            UserHomeView.as_view(),     name='home'),
    path('accounts/',                   include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',          UserUpdateView.as_view(),   name='account_edit'),
    path('accounts/signup/',            UserAddView.as_view(),      name='signup'),

    # Author
    path('author/',                     AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',             AuthorDetailView.as_view(),  name='author_detail'),
    path('author/<int:pk>/',            AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',      AuthorDeleteView.as_view(),  name='author_delete'),

    # Book
    path('book/',                       BookListView.as_view(),     name='book_list'),
    path('book/<int:pk>',               BookDetailView.as_view(),   name='book_detail'),
    path('book/add',                    BookCreateView.as_view(),   name='book_add'),
    path('book/<int:pk>/',              BookUpdateView.as_view(),   name='book_edit'),
    path('book/<int:pk>/delete',        BookDeleteView.as_view(),   name='book_delete'),

    # path('chapter/<int:book>/',         ChapterListView.as_view(),    name='chapter_list'),
    path('chapter/<int:pk>',            ChapterDetailView.as_view(),  name='chapter_detail'),
    path('chapter/<int:book>/add',      ChapterCreateView.as_view(),  name='chapter_add'),
    path('chapter/<int:pk>/',           ChapterUpdateView.as_view(),  name='chapter_edit'),
    path('chapter/<int:pk>/delete',     ChapterDeleteView.as_view(),  name='chapter_delete'),

]
