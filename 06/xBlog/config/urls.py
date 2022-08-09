from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # Home
    path('', RedirectView.as_view(url='blog/')),

    # Blog
    path('blog/', include('blog.urls_blog')),
    path('article/', include('blog.urls_article')),

]
