from django.urls import path

from .views import DocumentView, HtmlView

urlpatterns = [

    # Templates
    path('', HtmlView.as_view(template_name='home.html'), name='home'),
    path('theme.html', HtmlView.as_view(template_name='theme.html'), name='theme'),

    # Document
    path('doc/', DocumentView.as_view(), name='document'),
    path('doc/<str:doc>', DocumentView.as_view()),
]
