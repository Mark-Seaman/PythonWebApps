
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls.conf import include, include
from django.urls import path

from .views_object_instance import ClassNameDeleteView, ClassNameDetailView, ClassNameListView, ClassNameCreateView, ClassNameUpdateView


urlpatterns = [

    # ClassObject
    path('',                       ClassNameListView.as_view(),    name='object_instance_list'),
    path('<int:pk>',               ClassNameDetailView.as_view(),  name='object_instance_detail'),
    path('add',                    ClassNameCreateView.as_view(),  name='object_instance_add'),
    path('<int:pk>/',              ClassNameUpdateView.as_view(),  name='object_instance_edit'),
    path('<int:pk>/delete',        ClassNameDeleteView.as_view(),  name='object_instance_delete'),

]
