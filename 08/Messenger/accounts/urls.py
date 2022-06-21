from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from messenger.views_accounts import UserUpdateView, UserAddView, UserHomeView


urlpatterns = [

    # Default
    path('', UserHomeView.as_view(), name='home'),

    # Admin
    path('admin/', admin.site.urls),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/', UserUpdateView.as_view(),  name='account_edit'),
    path('accounts/signup/', UserAddView.as_view(), name='signup'),

]
