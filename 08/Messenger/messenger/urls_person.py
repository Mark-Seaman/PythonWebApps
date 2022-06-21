
from django.urls import path

from .views_person import PersonDeleteView, PersonDetailView, PersonListView, PersonCreateView, PersonUpdateView


urlpatterns = [

    # Person
    path('',                       PersonListView.as_view(),    name='person_list'),
    path('<int:pk>',               PersonDetailView.as_view(),  name='person_detail'),
    path('add',                    PersonCreateView.as_view(),  name='person_add'),
    path('<int:pk>/',              PersonUpdateView.as_view(),  name='person_edit'),
    path('<int:pk>/delete',        PersonDeleteView.as_view(),  name='person_delete'),

]
