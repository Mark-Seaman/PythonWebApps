from pathlib import Path
from django.views.generic import TemplateView
from markdown import markdown

from .models import Note


class NoteListView(TemplateView):
    template_name = 'notes.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Note.objects.all()
        }


class NoteDetailView(TemplateView):
    template_name = 'note.html'

    def get_context_data(self, **kwargs):
        return {
            'note': Note.objects.get(pk=kwargs['pk'])
        }


class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('doc', 'README.md')
        markdown_text = open(f'{document}').read()
        return dict(title=document, body=markdown(markdown_text))
