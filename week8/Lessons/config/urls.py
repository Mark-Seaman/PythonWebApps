from django.urls import path
from django.views.generic import TemplateView


class PageView(TemplateView):
    def get_template_names(self):
        return self.kwargs.get('page')


urlpatterns = [
    path('<str:page>', PageView.as_view()),
]
