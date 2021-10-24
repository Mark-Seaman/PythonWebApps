
from django.contrib import admin
from django.urls import path

from accounts.views import AccountDeleteView, AccountDetailView, AccountListView, AccountCreateView, AccountUpdateView, SignUpView

urlpatterns = [

    # Account Views
    path('',                   AccountListView.as_view(),    name='account_list'),
    path('<int:pk>',           AccountDetailView.as_view(),  name='account_detail'),
    path('add',                AccountCreateView.as_view(),  name='account_add'),
    path('<int:pk>/',          AccountUpdateView.as_view(),  name='account_edit'),
    path('<int:pk>/delete',    AccountDeleteView.as_view(),  name='account_delete'),

    # Sign Up
    path('signup/', SignUpView.as_view(), name='signup'),
]
