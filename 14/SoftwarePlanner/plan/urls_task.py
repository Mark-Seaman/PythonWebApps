
from django.urls import path

from .views_task import TaskDeleteView, TaskDetailView, TaskListView, TaskCreateView, TaskUpdateView


urlpatterns = [

    # Task
    path('task/',                       TaskListView.as_view(),    name='task_list'),
    path('task/<int:pk>',               TaskDetailView.as_view(),  name='task_detail'),
    path('task/add',                    TaskCreateView.as_view(),  name='task_add'),
    path('task/<int:pk>/',              TaskUpdateView.as_view(),  name='task_edit'),
    path('task/<int:pk>/delete',        TaskDeleteView.as_view(),  name='task_delete'),

]
