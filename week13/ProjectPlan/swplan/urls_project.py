
from django.urls import path

from .views_project import ProjectDeleteView, ProjectDetailView, ProjectListView, ProjectCreateView, ProjectUpdateView


urlpatterns = [

    # Project
    path('',                       ProjectListView.as_view(),    name='project_list'),
    path('<int:pk>',               ProjectDetailView.as_view(),  name='project_detail'),
    path('add',                    ProjectCreateView.as_view(),  name='project_add'),
    path('<int:pk>/',              ProjectUpdateView.as_view(),  name='project_edit'),
    path('<int:pk>/delete',        ProjectDeleteView.as_view(),  name='project_delete'),

]
