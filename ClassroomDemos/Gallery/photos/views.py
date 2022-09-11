from pathlib import Path
from django.views.generic import TemplateView


class PhotoView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        name = kwargs['name']
        image = f'/static/images/{name}'
        return {'photo': image}


class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        photos = Path('static/images').iterdir()
        photos = [f for f in photos]
        return dict(photos=photos)
