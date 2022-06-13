
from django.urls import path

from .views_task import TaskDeleteView, TaskDetailView, TaskListView, TaskCreateView, TaskUpdateView


urlpatterns = [

    # Task
    path('',                       TaskListView.as_view(),    name='task_list'),
    path('<int:pk>',               TaskDetailView.as_view(),  name='task_detail'),
    path('add',                    TaskCreateView.as_view(),  name='task_add'),
    path('<int:pk>/',              TaskUpdateView.as_view(),  name='task_edit'),
    path('<int:pk>/delete',        TaskDeleteView.as_view(),  name='task_delete'),

]
