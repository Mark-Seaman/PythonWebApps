from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='message/')),

    # Blog
    path('person', include('messenger.urls_person')),
    path('message', include('messenger.urls_message')),

]
