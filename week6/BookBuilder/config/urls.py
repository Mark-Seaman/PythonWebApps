"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from book.views import BookView, BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Book Views
    path('', BookView.as_view()),
    path('book/',                   BookListView.as_view(),    name='book_list'),
    path('book/<int:pk>',           BookDetailView.as_view(),  name='book_detail'),
    path('book/add',                BookCreateView.as_view(),  name='book_add'),
    path('book/<int:pk>/',          BookUpdateView.as_view(),  name='book_edit'),
    path('book/<int:pk>/delete',    BookDeleteView.as_view(),  name='book_delete'),

]
