
from django.urls import path

from .views_developer import DeveloperDeleteView, DeveloperDetailView, DeveloperListView, DeveloperCreateView, DeveloperUpdateView


urlpatterns = [

    # Developer
    path('',                       DeveloperListView.as_view(),    name='developer_list'),
    path('<int:pk>',               DeveloperDetailView.as_view(),  name='developer_detail'),
    path('add',                    DeveloperCreateView.as_view(),  name='developer_add'),
    path('<int:pk>/',              DeveloperUpdateView.as_view(),  name='developer_edit'),
    path('<int:pk>/delete',        DeveloperDeleteView.as_view(),  name='developer_delete'),

]
