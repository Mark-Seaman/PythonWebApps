from django.views.generic import TemplateView
from markdown import markdown

from .models import Superhero


class HeroListView(TemplateView):
    template_name = 'superheros.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Superhero.objects.all()
        }


class HeroDetailView(TemplateView):
    template_name = 'superhero.html'

    def get_context_data(self, **kwargs):
        return {
            'superhero': Superhero.objects.get(pk=kwargs['pk'])
        }
