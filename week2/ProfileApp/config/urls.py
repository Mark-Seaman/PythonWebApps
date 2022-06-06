from django.urls import path
from pages.views import ProfileView

urlpatterns = [
    path('', ProfileView.as_view()),
]
