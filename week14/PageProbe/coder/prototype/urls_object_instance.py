
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.urls import path

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorCreateView, AuthorUpdateView
from .views_object_instance import BookView, BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView
from .views_lesson import LessonDeleteView, LessonDetailView, LessonListView, LessonCreateView, LessonUpdateView
from .views_image import ImageDeleteView, ImageListView, ImageCreateView


urlpatterns = [

    path('',                            BookView.as_view(),        name='home'),

    # Author
    path('author/',                     AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',             AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add',                  AuthorCreateView.as_view(),  name='author_add'),
    path('author/<int:pk>/',            AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',      AuthorDeleteView.as_view(),  name='author_delete'),

    # ClassObject
    path('object_instance/',                       BookListView.as_view(),    name='object_instance_list'),
    path('object_instance/<int:pk>',               BookDetailView.as_view(),  name='object_instance_detail'),
    path('object_instance/add',                    BookCreateView.as_view(),  name='object_instance_add'),
    path('object_instance/<int:pk>/',              BookUpdateView.as_view(),  name='object_instance_edit'),
    path('object_instance/<int:pk>/delete',        BookDeleteView.as_view(),  name='object_instance_delete'),

    # Lesson
    path('lesson/',                    LessonListView.as_view(),    name='lesson_list'),
    path('lesson/<int:pk>',            LessonDetailView.as_view(),  name='lesson_detail'),
    path('lesson/add',                 LessonCreateView.as_view(),  name='lesson_add'),
    path('lesson/<int:pk>/',           LessonUpdateView.as_view(),  name='lesson_edit'),
    path('lesson/<int:pk>/delete',     LessonDeleteView.as_view(),  name='lesson_delete'),

    # Image
    path('image/',                      ImageListView.as_view(),    name='image_list'),
    path('image/add',                   ImageCreateView.as_view(),  name='image_add'),
    path('image/<int:pk>/delete',       ImageDeleteView.as_view(),  name='image_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
