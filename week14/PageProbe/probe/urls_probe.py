
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.urls import path

from .views_probe import ClassNameView, ClassNameDeleteView, ClassNameDetailView, ClassNameListView, ClassNameCreateView, ClassNameUpdateView


urlpatterns = [

    # Probe
    path('probe/',                       ClassNameListView.as_view(),    name='probe_list'),
    path('probe/<int:pk>',               ClassNameDetailView.as_view(),  name='probe_detail'),
    path('probe/add',                    ClassNameCreateView.as_view(),  name='probe_add'),
    path('probe/<int:pk>/',              ClassNameUpdateView.as_view(),  name='probe_edit'),
    path('probe/<int:pk>/delete',        ClassNameDeleteView.as_view(),  name='probe_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
