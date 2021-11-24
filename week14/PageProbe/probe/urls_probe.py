from django.urls import path

from .views_probe import (ProbeClearView, ProbeCreateView, ProbeDeleteView,
                          ProbeDetailView, ProbeLaunchView, ProbeListView,
                          ProbeUpdateView)

urlpatterns = [

    # ClassObject
    path('',                       ProbeListView.as_view(),    name='probe_list'),
    path('<int:pk>',               ProbeDetailView.as_view(),  name='probe_detail'),
    path('add',                    ProbeCreateView.as_view(),  name='probe_add'),
    path('<int:pk>/',              ProbeUpdateView.as_view(),  name='probe_edit'),
    path('<int:pk>/delete',        ProbeDeleteView.as_view(),  name='probe_delete'),
    path('<int:pk>/clear',         ProbeClearView.as_view(),   name='probe_clear'),
    path('test',                   ProbeLaunchView.as_view(),  name='probe_launch'),

]
