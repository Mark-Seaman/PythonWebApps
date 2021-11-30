from django.urls.conf import include
from django.contrib import admin
from django.urls import path

from hammer.views_probe import TestView


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # Hammer Test
    path('', TestView.as_view()),
    path('test/', include('hammer.urls_probe')),

]
