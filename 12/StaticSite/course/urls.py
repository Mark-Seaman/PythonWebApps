from django.views.generic import RedirectView
from django.urls import path

from .views import LessonDetailView


urlpatterns = [

    # Lesson
    path('', RedirectView.as_view(url='1')),
    path('<int:pk>', LessonDetailView.as_view(),  name='lesson_detail'),

]
