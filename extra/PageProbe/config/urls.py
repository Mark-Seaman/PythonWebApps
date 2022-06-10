from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include

from probe.views_probe import ProbeView


urlpatterns = [

    path('', ProbeView.as_view()),
    path('probe/', include('probe.urls_probe')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
