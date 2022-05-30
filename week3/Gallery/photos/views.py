from django.views.generic import TemplateView


class PhotosView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=[1, 2, 3])
