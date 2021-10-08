from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='accounts/'), name='home'),

]
