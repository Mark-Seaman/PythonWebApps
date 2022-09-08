from django.urls import path
from hero.views import HomeView, HulkView, IronManView, BlackWidowView

urlpatterns =  [
    path('', HomeView.as_view()),
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidowView.as_view()),
]