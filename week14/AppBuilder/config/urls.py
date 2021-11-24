from django.urls.conf import include
from django.contrib import admin
from django.urls import path


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # Data Factory
    path('factory/', include('coder.urls_factory')),

    # Hammer Test
    path('test/', include('hammer.urls_test')),

]
