from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from django.views.generic import TemplateView

from accounts.views import HomeView, SignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomeView.as_view(), name='home'),
]
