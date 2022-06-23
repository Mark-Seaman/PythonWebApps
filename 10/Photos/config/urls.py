from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [

    # Photogram
    path('', include('photos.urls')),
    path('', include('accounts.urls')),

]
