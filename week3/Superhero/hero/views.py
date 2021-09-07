from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class HulkView(TemplateView):
    template_name = 'hulk.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page',
            'body': 'Once upon a time ...',
        }


class IronManView(TemplateView):
    template_name = "iron_man.html"


class BlackWidow(TemplateView):
    template_name = 'black_widow.html'
