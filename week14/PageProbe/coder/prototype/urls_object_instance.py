
from django.urls import path

from .views_object_instance import ClassNameDeleteView, ClassNameDetailView, ClassNameListView, ClassNameCreateView, ClassNameUpdateView


urlpatterns = [

    # ClassName
    path('',                       ClassNameListView.as_view(),    name='object_instance_list'),
    path('<int:pk>',               ClassNameDetailView.as_view(),  name='object_instance_detail'),
    path('add',                    ClassNameCreateView.as_view(),  name='object_instance_add'),
    path('<int:pk>/',              ClassNameUpdateView.as_view(),  name='object_instance_edit'),
    path('<int:pk>/delete',        ClassNameDeleteView.as_view(),  name='object_instance_delete'),

]
