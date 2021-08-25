from django.urls import path
from pages.views import homePageView

urlpatterns = [
    path('', homePageView)
]
