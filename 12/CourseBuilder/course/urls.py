from django.views.generic import RedirectView
from django.urls import path

from .views import LessonDetailView


urlpatterns = [

    # Lesson
    path('', RedirectView.as_view(url='lesson/1')),
    path('lesson/<int:pk>', LessonDetailView.as_view(),  name='lesson_detail'),

]
