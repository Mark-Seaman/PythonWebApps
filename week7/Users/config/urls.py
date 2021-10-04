from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
]
