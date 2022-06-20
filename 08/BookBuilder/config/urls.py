from django.urls import include, path
from django.views.generic import RedirectView

from book.views_author import AccountUpdateView, SignUpView

urlpatterns = [

    # Admin
    # path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='book/')),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),    # Login
    # path('accounts/', include('accounts.urls')),
    path('account/<int:pk>/',  AccountUpdateView.as_view(),  name='account_edit'),
    path('signup/', SignUpView.as_view(), name='signup'),    # Sign Up

    # Blog
    path('author/', include('book.urls_author')),
    path('book/', include('book.urls_book')),
    path('chapter/', include('book.urls_chapter')),

]
