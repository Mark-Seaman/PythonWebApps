
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from news.views_author import UserUpdateView, AuthorAddView

urlpatterns = [

    # Admin
    # path('admin/', admin.site.urls),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/', UserUpdateView.as_view(),  name='account_edit'),
    path('accounts/signup/', AuthorAddView.as_view(), name='signup'),

    # News
    path('', RedirectView.as_view(url='author/home')),
    path('article/', include('news.urls_article')),
    path('author/', include('news.urls_author')),

]
