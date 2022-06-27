
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from .views_user import UserAddView, UserHomeView, UserUpdateView
from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorUpdateView
from .views_photo import PhotoCarouselView, PhotoDeleteView, PhotoDetailView, PhotoListView, PhotoCreateView, PhotoUpdateView


urlpatterns = [

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),

    # User
    path('',                            RedirectView.as_view(url='user/home')),
    path('user/home',                   UserHomeView.as_view(),     name='user_home'),
    path('user/add',                    UserAddView.as_view(),      name='user_add'),
    path('user/<int:pk>/',              UserUpdateView.as_view(),   name='user_edit'),

    # Author
    path('author/',                     AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',             AuthorDetailView.as_view(),  name='author_detail'),
    path('author/<int:pk>/',            AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',      AuthorDeleteView.as_view(),  name='author_delete'),

    # Photo
    path('photo/carousel',              PhotoCarouselView.as_view()),
    path('photo/',                      PhotoListView.as_view(),    name='photo_list'),
    path('photo/<int:pk>',              PhotoDetailView.as_view(),  name='photo_detail'),
    path('photo/add',                   PhotoCreateView.as_view(),  name='photo_add'),
    path('photo/<int:pk>/',             PhotoUpdateView.as_view(),  name='photo_edit'),
    path('photo/<int:pk>/delete',       PhotoDeleteView.as_view(),  name='photo_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
