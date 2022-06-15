from django.views.generic import TemplateView
from markdown import markdown


class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('doc', 'Index')
        return document_data(document)


def document_card(document):
    if not document.endswith('.md'):
        document += '.md'
    markdown_text = open(f'Documents/{document}').read()
    link = dict(href='Index', text='Doc Index')
    return dict(body=markdown(markdown_text), file=document, color='bg-primary text-light p-5', width='', link=link)


def document_data(document):
    return dict(documents=[document_card(document)])
