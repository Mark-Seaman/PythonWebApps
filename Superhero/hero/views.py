from pathlib import Path
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class HeroView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        name = kwargs['name']
        image = f'\static\images\{name}'
        return {'photo': image}

class HeroListView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        photos = Path('static/images').iterdir()
        photos = [f for f in photos]
        return dict(photos=photos)
