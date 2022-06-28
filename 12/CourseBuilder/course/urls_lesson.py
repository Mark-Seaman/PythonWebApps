
from django.urls import path

from .views_lesson import LessonDeleteView, LessonDetailView, LessonListView, LessonCreateView, LessonUpdateView


urlpatterns = [

    # Lesson
    path('lesson/',                       LessonListView.as_view(),    name='lesson_list'),
    path('lesson/<int:pk>',               LessonDetailView.as_view(),  name='lesson_detail'),
    path('lesson/add',                    LessonCreateView.as_view(),  name='lesson_add'),
    path('lesson/<int:pk>/',              LessonUpdateView.as_view(),  name='lesson_edit'),
    path('lesson/<int:pk>/delete',        LessonDeleteView.as_view(),  name='lesson_delete'),

]
