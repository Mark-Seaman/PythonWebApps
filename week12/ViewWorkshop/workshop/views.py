from django.views.generic import RedirectView, TemplateView
from os import listdir
from markdown import markdown
from django.views.generic import TemplateView


class HtmlView(TemplateView):
    template_name = 'home.html'


class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('doc', 'Index')
        markdown_text = open(f'Documents/{document}.md').read()
        return dict(doc=markdown(markdown_text), file=document)
