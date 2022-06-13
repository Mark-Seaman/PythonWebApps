
from django.urls import path

from .views_developer import AccountUpdateView, DeveloperDeleteView, DeveloperDetailView, DeveloperListView, DeveloperUpdateView, DeveloperSignUpView


urlpatterns = [

    # Account Views
    path('account/<int:pk>/',      AccountUpdateView.as_view(),  name='account_edit'),
    path('signup/',                DeveloperSignUpView.as_view(), name='signup'),

    # Developer
    path('',                       DeveloperListView.as_view(),    name='developer_list'),
    path('<int:pk>',               DeveloperDetailView.as_view(),  name='developer_detail'),
    # path('add',                    DeveloperCreateView.as_view(),  name='developer_add'),
    path('<int:pk>/',              DeveloperUpdateView.as_view(),  name='developer_edit'),
    path('<int:pk>/delete',        DeveloperDeleteView.as_view(),  name='developer_delete'),

]
