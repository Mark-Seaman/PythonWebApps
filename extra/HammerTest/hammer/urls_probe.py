
from django.urls import path

from .views_probe import (TestApproveView, TestCreateView, TestDeleteView, TestDetailView,
                          TestListView, TestResetView, TestRunView, TestUpdateView)

urlpatterns = [

    # Test
    path('',                       TestListView.as_view(),      name='test_list'),
    path('<int:pk>',               TestDetailView.as_view(),    name='test_detail'),
    path('add',                    TestCreateView.as_view(),    name='test_add'),
    path('<int:pk>/',              TestUpdateView.as_view(),    name='test_edit'),
    path('<int:pk>/delete',        TestDeleteView.as_view(),    name='test_delete'),

    # Results
    path('<int:pk>/run',           TestRunView.as_view(),       name='test_run'),
    path('<int:pk>/approve',       TestApproveView.as_view(),   name='test_approve'),
    path('<int:pk>/reset',         TestResetView.as_view(),   name='test_reset'),

]
