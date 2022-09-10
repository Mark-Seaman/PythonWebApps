from django.views.generic import TemplateView


class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'id': 'Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }


class IronManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'IronMan',
            'id': 'Tony Stark',
            'image': '/static/images/iron_man.jpg'
        }
