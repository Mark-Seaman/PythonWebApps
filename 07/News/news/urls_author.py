
from django.urls import path

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorCreateView, AuthorUpdateView


urlpatterns = [

    # Author
    path('',                       AuthorListView.as_view(),    name='author_list'),
    path('<int:pk>',               AuthorDetailView.as_view(),  name='author_detail'),
    path('add',                    AuthorCreateView.as_view(),  name='author_add'),
    path('<int:pk>/',              AuthorUpdateView.as_view(),  name='author_edit'),
    path('<int:pk>/delete',        AuthorDeleteView.as_view(),  name='author_delete'),

]
