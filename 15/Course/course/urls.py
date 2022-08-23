
from django.urls import include, path

from .views_student import StudentDeleteView, StudentDetailView, StudentListView, UserAddView, StudentView, StudentUpdateView, UserUpdateView


urlpatterns = [
    # Accounts
    path('accounts/',                      include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',             UserUpdateView.as_view(),    name='user_edit'),
    path('accounts/add',                    UserAddView.as_view(),       name='user_add'),

    # Student
    path('',                               StudentView.as_view(),        name='student_view'),
    path('student/',                       StudentListView.as_view(),    name='student_list'),
    path('student/<int:pk>',               StudentDetailView.as_view(),  name='student_detail'),
    path('student/<int:pk>/',              StudentUpdateView.as_view(),  name='student_edit'),
    path('student/<int:pk>/delete',        StudentDeleteView.as_view(),  name='student_delete'),

]
