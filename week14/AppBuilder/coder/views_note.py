from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Note


class NoteView(RedirectView):
    url = reverse_lazy('note_list')


class NoteListView(ListView):
    template_name = 'note_list.html'
    model = Note


class NoteDetailView(DetailView):
    template_name = 'note_detail.html'
    model = Note

    def get_context_data(self, **kwargs):
        kwargs = self.super().get_context_data(**kwargs)
        # kwargs.update(dict(dependent=Dependent.obects.filter(note=kwargs.get('object'))))
        return kwargs


class NoteCreateView(LoginRequiredMixin, CreateView):
    template_name = "note_add.html"
    model = Note
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "note_edit.html"
    model = Note
    fields = '__all__'


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('note_list')
