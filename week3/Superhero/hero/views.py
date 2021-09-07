from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'body': 'My name is Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }


class IronManView(TemplateView):
    template_name = "iron_man.html"


class BlackWidow(TemplateView):
    template_name = 'black_widow.html'
