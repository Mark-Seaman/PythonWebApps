
from django.urls import path

from .views_message import MessageDeleteView, MessageDetailView, MessageListView, MessageCreateView, MessageUpdateView


urlpatterns = [

    # Message
    path('',                       MessageListView.as_view(),    name='message_list'),
    path('<int:pk>',               MessageDetailView.as_view(),  name='message_detail'),
    path('add',                    MessageCreateView.as_view(),  name='message_add'),
    path('<int:pk>/',              MessageUpdateView.as_view(),  name='message_edit'),
    path('<int:pk>/delete',        MessageDeleteView.as_view(),  name='message_delete'),

]
