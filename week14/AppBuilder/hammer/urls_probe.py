
from django.urls import path

from .views_probe import (TestCreateView, TestDeleteView, TestDetailView,
                          TestListView, TestRunView, TestUpdateView)

urlpatterns = [

    # Test
    path('',                       TestListView.as_view(),    name='test_list'),
    path('<int:pk>',               TestDetailView.as_view(),  name='test_detail'),
    path('add',                    TestCreateView.as_view(),  name='test_add'),
    path('<int:pk>/',              TestUpdateView.as_view(),  name='test_edit'),
    path('<int:pk>/delete',        TestDeleteView.as_view(),  name='test_delete'),
    path('<int:pk>/run',           TestRunView.as_view(),  name='test_run'),

]
