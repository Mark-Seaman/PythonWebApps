
from django.urls import path
from django.views.generic import RedirectView

from .views_milestone import MilestoneDeleteView, MilestoneDetailView, MilestoneListView, MilestoneCreateView, MilestoneUpdateView
from .views_task import TaskDeleteView, TaskDetailView, TaskListView, TaskCreateView, TaskUpdateView


urlpatterns = [

    # Task
    path('task/',                       TaskListView.as_view(),    name='task_list'),
    path('task/<int:pk>',               TaskDetailView.as_view(),  name='task_detail'),
    path('task/<int:milestone>/add',    TaskCreateView.as_view(),  name='task_add'),
    path('task/<int:pk>/',              TaskUpdateView.as_view(),  name='task_edit'),
    path('task/<int:pk>/delete',        TaskDeleteView.as_view(),  name='task_delete'),

    # Milestone
    path('', RedirectView.as_view(url='milestone/')),
    path('milestone/',                       MilestoneListView.as_view(),    name='milestone_list'),
    path('milestone/<int:pk>',               MilestoneDetailView.as_view(),  name='milestone_detail'),
    path('milestone/add',                    MilestoneCreateView.as_view(),  name='milestone_add'),
    path('milestone/<int:pk>/',              MilestoneUpdateView.as_view(),  name='milestone_edit'),
    path('milestone/<int:pk>/delete',        MilestoneDeleteView.as_view(),  name='milestone_delete'),

]
