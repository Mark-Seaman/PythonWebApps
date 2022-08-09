
from django.urls import path

from .views_blog import BlogDeleteView, BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView


urlpatterns = [

    # Blog
    path('',                       BlogListView.as_view(),    name='blog_list'),
    path('<int:pk>',               BlogDetailView.as_view(),  name='blog_detail'),
    path('add',                    BlogCreateView.as_view(),  name='blog_add'),
    path('<int:pk>/',              BlogUpdateView.as_view(),  name='blog_edit'),
    path('<int:pk>/delete',        BlogDeleteView.as_view(),  name='blog_delete'),

]
