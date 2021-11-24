
from django.urls import path

from .views_factory import DataFactoryDeleteView, DataFactoryDetailView, DataFactoryListView, DataFactoryCreateView, DataFactoryUpdateView


urlpatterns = [

    # DataFactory
    path('',                       DataFactoryListView.as_view(),    name='factory_list'),
    path('<int:pk>',               DataFactoryDetailView.as_view(),  name='factory_detail'),
    path('add',                    DataFactoryCreateView.as_view(),  name='factory_add'),
    path('<int:pk>/',              DataFactoryUpdateView.as_view(),  name='factory_edit'),
    path('<int:pk>/delete',        DataFactoryDeleteView.as_view(),  name='factory_delete'),

]
