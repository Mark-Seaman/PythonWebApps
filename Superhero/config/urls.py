from django.views.generic import RedirectView
from django.urls import path
from hero.views import HeroView, HeroListView

urlpatterns =  [
    path('', RedirectView.as_view(url='heroes/')),
    path('heroes/', HeroListView.as_view()),
    path('heroes/<int:id>', HeroView.as_view()),
]