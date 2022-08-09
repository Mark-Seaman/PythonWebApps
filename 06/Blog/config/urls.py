from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    # Admin
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    # Blog
    path('', include('blog.urls')),

]
