
from django.urls import path

from .views_student import StudentDeleteView, StudentDetailView, StudentListView, StudentCreateView, StudentUpdateView


urlpatterns = [

    # Student
    path('student/',                       StudentListView.as_view(),    name='student_list'),
    path('student/<int:pk>',               StudentDetailView.as_view(),  name='student_detail'),
    path('student/add',                    StudentCreateView.as_view(),  name='student_add'),
    path('student/<int:pk>/',              StudentUpdateView.as_view(),  name='student_edit'),
    path('student/<int:pk>/delete',        StudentDeleteView.as_view(),  name='student_delete'),

]
