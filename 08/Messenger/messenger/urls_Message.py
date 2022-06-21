
from django.urls import path

from .views_Message import MessageDeleteView, MessageDetailView, MessageListView, MessageCreateView, MessageUpdateView


urlpatterns = [

    # Message
    path('',                       MessageListView.as_view(),    name='Message_list'),
    path('<int:pk>',               MessageDetailView.as_view(),  name='Message_detail'),
    path('add',                    MessageCreateView.as_view(),  name='Message_add'),
    path('<int:pk>/',              MessageUpdateView.as_view(),  name='Message_edit'),
    path('<int:pk>/delete',        MessageDeleteView.as_view(),  name='Message_delete'),

]
