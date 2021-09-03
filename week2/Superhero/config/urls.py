from django.urls import path
from hero.views import HulkView, BlackWidow, IronManView

urlpatterns = [
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidow.as_view()),
]
