from django.contrib import admin
from django.urls import include, path


urlpatterns = [

    # Accounts
    path('', include('accounts.urls')),

    # Messenger
    path('person/', include('messenger.urls_person')),
    path('message/', include('messenger.urls_message')),

]
