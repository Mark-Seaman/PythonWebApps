from django.urls.conf import include
from django.contrib import admin
from django.urls import path

from coder.views_factory import DataFactoryView


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # Data Factory
    path('', DataFactoryView.as_view()),
    path('factory/', include('coder.urls_factory')),

    # Hammer Test
    path('test/', include('hammer.urls_probe')),

]
