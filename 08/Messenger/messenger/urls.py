from messenger.views_accounts import UserUpdateView, UserAddView, UserHomeView
from django.contrib import admin
from django.urls import include, path

from .views_message import MessageDeleteView, MessageDetailView, MessageListView, MessageCreateView, MessageUpdateView
from .views_person import PersonDeleteView, PersonDetailView, PersonListView, PersonUpdateView

urlpatterns = [

    # User Accounts
    path('',                        UserHomeView.as_view(),     name='home'),
    path('accounts/',               include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',      UserUpdateView.as_view(),   name='account_edit'),
    path('accounts/signup/',        UserAddView.as_view(),      name='signup'),
    path('admin/',                  admin.site.urls),

    # Person
    path('person/',                       PersonListView.as_view(),    name='person_list'),
    path('person/<int:pk>',               PersonDetailView.as_view(),  name='person_detail'),
    # path('add',                         PersonCreateView.as_view(),  name='person_add'),
    path('person/<int:pk>/',              PersonUpdateView.as_view(),  name='person_edit'),
    path('person/<int:pk>/delete',        PersonDeleteView.as_view(),  name='person_delete'),

    # Message
    path('message/',                       MessageListView.as_view(),    name='message_list'),
    path('message/<int:pk>',               MessageDetailView.as_view(),  name='message_detail'),
    path('message/add',                    MessageCreateView.as_view(),  name='message_add'),
    path('message/<int:pk>/',              MessageUpdateView.as_view(),  name='message_edit'),
    path('message/<int:pk>/delete',        MessageDeleteView.as_view(),  name='message_delete'),


]
