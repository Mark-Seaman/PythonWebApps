from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [

    # Photogram
    path('', RedirectView.as_view(url='author/')),
    path('', include('author.urls')),

]
