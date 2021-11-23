
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.urls import path

from .views_object_instance import ClassNameView, ClassNameDeleteView, ClassNameDetailView, ClassNameListView, ClassNameCreateView, ClassNameUpdateView


urlpatterns = [

    # ClassObject
    path('object_instance/',                       ClassNameListView.as_view(),    name='object_instance_list'),
    path('object_instance/<int:pk>',               ClassNameDetailView.as_view(),  name='object_instance_detail'),
    path('object_instance/add',                    ClassNameCreateView.as_view(),  name='object_instance_add'),
    path('object_instance/<int:pk>/',              ClassNameUpdateView.as_view(),  name='object_instance_edit'),
    path('object_instance/<int:pk>/delete',        ClassNameDeleteView.as_view(),  name='object_instance_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
