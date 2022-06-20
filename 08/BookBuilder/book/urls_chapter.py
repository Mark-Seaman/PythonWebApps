
from django.urls import path

from .views_chapter import ChapterDeleteView, ChapterDetailView, ChapterListView, ChapterCreateView, ChapterUpdateView


urlpatterns = [

    # Chapter
    path('',                       ChapterListView.as_view(),    name='chapter_list'),
    path('<int:pk>',               ChapterDetailView.as_view(),  name='chapter_detail'),
    path('add',                    ChapterCreateView.as_view(),  name='chapter_add'),
    path('<int:pk>/',              ChapterUpdateView.as_view(),  name='chapter_edit'),
    path('<int:pk>/delete',        ChapterDeleteView.as_view(),  name='chapter_delete'),

]
