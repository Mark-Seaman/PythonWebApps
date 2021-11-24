from django.urls.conf import include
from django.contrib import admin
from django.urls import path


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # Book
    path('', include('coder.urls_factory')),

]
