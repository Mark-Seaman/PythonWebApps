
from django.urls import path

from .views_object_instance import ClassNameDeleteView, ClassNameDetailView, ClassNameListView, ClassNameCreateView, ClassNameUpdateView


urlpatterns = [

    # ClassName
    path('object_instance/',                       ClassNameListView.as_view(),    name='object_instance_list'),
    path('object_instance/<int:pk>',               ClassNameDetailView.as_view(),  name='object_instance_detail'),
    path('object_instance/add',                    ClassNameCreateView.as_view(),  name='object_instance_add'),
    path('object_instance/<int:pk>/',              ClassNameUpdateView.as_view(),  name='object_instance_edit'),
    path('object_instance/<int:pk>/delete',        ClassNameDeleteView.as_view(),  name='object_instance_delete'),

]
