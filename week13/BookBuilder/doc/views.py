from django.views.generic import RedirectView, TemplateView
from markdown import markdown
from os import listdir


class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('doc', 'Index')
        markdown_text = open(f'Documents/Notes/{document}.md').read()
        return dict(doc=markdown(markdown_text), file=document)


def scan_document_files():
    for d in ["Documents/Poems", "Documents/Leverage"]:
        print(f'Scanning files in {d}')
        for f in listdir(d):
            print(f'{d}/{f}')
            open(f'{d}/{f}').read()
