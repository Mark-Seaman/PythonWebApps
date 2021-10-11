
from django.views.generic import TemplateView
from django.urls import path


class PageView(TemplateView):
    def get_template_names(self):
        return self.kwargs.get('page')


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('<str:page>', PageView.as_view()),
]
