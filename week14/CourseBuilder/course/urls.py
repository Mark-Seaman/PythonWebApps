
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.urls import path

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorCreateView, AuthorUpdateView
from .views_course import BookView, BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView
from .views_chapter import ChapterDeleteView, ChapterDetailView, ChapterListView, ChapterCreateView, ChapterUpdateView
from .views_image import ImageDeleteView, ImageListView, ImageCreateView


urlpatterns = [

    path('',                            BookView.as_view(),        name='home'),

    # Author
    path('author/',                     AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',             AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add',                  AuthorCreateView.as_view(),  name='author_add'),
    path('author/<int:pk>/',            AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',      AuthorDeleteView.as_view(),  name='author_delete'),

    # Course
    path('course/',                       BookListView.as_view(),    name='course_list'),
    path('course/<int:pk>',               BookDetailView.as_view(),  name='course_detail'),
    path('course/add',                    BookCreateView.as_view(),  name='course_add'),
    path('course/<int:pk>/',              BookUpdateView.as_view(),  name='course_edit'),
    path('course/<int:pk>/delete',        BookDeleteView.as_view(),  name='course_delete'),

    # Chapter
    path('chapter/',                    ChapterListView.as_view(),    name='chapter_list'),
    path('chapter/<int:pk>',            ChapterDetailView.as_view(),  name='chapter_detail'),
    path('chapter/add',                 ChapterCreateView.as_view(),  name='chapter_add'),
    path('chapter/<int:pk>/',           ChapterUpdateView.as_view(),  name='chapter_edit'),
    path('chapter/<int:pk>/delete',     ChapterDeleteView.as_view(),  name='chapter_delete'),

    # Image
    path('image/',                      ImageListView.as_view(),    name='image_list'),
    path('image/add',                   ImageCreateView.as_view(),  name='image_add'),
    path('image/<int:pk>/delete',       ImageDeleteView.as_view(),  name='image_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
