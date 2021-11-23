
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls.conf import include, include
from django.urls import path

from .views_probe import ProbeDeleteView, ProbeDetailView, ProbeListView, ProbeCreateView, ProbeUpdateView


urlpatterns = [

    # ClassObject
    path('',                       ProbeListView.as_view(),    name='probe_list'),
    path('<int:pk>',               ProbeDetailView.as_view(),  name='probe_detail'),
    path('add',                    ProbeCreateView.as_view(),  name='probe_add'),
    path('<int:pk>/',              ProbeUpdateView.as_view(),  name='probe_edit'),
    path('<int:pk>/delete',        ProbeDeleteView.as_view(),  name='probe_delete'),

]
