from pathlib import Path
from django.views.generic import TemplateView
from markdown import markdown


class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('doc', 'Index.md')
        markdown_text = open(f'{document}').read()
        return dict(title=document, body=markdown(markdown_text))
