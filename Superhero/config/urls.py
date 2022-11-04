from django.contrib import admin
from django.urls import path, include

from hero.views_accounts import UserUpdateView, UserAddView

urlpatterns = [

    # Blog
    path('', include('blog.urls')),

    # Hero
    path('', include('hero.urls')),

    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/', UserUpdateView.as_view(), name='account_edit'),
    path('accounts/signup/', UserAddView.as_view(), name='signup'),

    # Admin views for users
    # path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]
