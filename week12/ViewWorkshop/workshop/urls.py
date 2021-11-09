# from .views import CarouselView, DocumentView, HomeView, SuperView
from django.urls import path

from .views import AccordionView, CardView, DocumentView, HtmlView, TableView, TabsView


urlpatterns = [

    # Templates
    path('', HtmlView.as_view(template_name='home.html'), name='home'),
    path('theme.html', HtmlView.as_view(template_name='theme.html'), name='theme'),

    # Document
    path('doc/', DocumentView.as_view(), name='document'),
    path('doc/<str:doc>', DocumentView.as_view()),

    # Cards
    path('card',  CardView.as_view(), name='card'),

    # Table
    path('table',  TableView.as_view(), name='table'),

    # Tabs and Accordion
    path('tabs',  TabsView.as_view(), name='tabs'),
    path('accordion',  AccordionView.as_view(), name='accordion'),


    #     path('carousel',  CarouselView.as_view(), name='carousel'),


    #     path('super',  SuperView.as_view(), name='super'),

]
