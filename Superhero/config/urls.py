from django.contrib import admin
from django.urls import path
from hero.views import HeroView, HeroListView

urlpatterns =  [
    path('admin/', admin.site.urls),
    path('', HeroListView.as_view()),
    path('<int:pk>', HeroView.as_view()),
]