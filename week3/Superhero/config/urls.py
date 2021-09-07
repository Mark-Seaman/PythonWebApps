from django.urls import path
from hero.views import BlackWidow, HulkView, IndexView, IronManView

urlpatterns = [
    path('', IndexView.as_view()),
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidow.as_view()),
]
