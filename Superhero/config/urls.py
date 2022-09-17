from django.urls import path
from hero.views import HeroView, HeroListView

urlpatterns =  [
    path('', HeroListView.as_view()),
    path('<str:name>', HeroView.as_view()),
]