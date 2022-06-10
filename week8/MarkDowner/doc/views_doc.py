from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Document


class DocumentView(RedirectView):
    url = reverse_lazy('doc_list')


class DocumentListView(ListView):
    template_name = 'doc_list.html'
    model = Document


class DocumentDetailView(DetailView):
    template_name = 'doc_detail.html'
    model = Document

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     kwargs.update(dict(dependent=Dependent.obects.filter(doc=kwargs.get('object'))))
    #     return kwargs


class DocumentCreateView(LoginRequiredMixin, CreateView):
    template_name = "doc_add.html"
    model = Document
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "doc_edit.html"
    model = Document
    fields = '__all__'


class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    template_name = 'doc_delete.html'
    success_url = reverse_lazy('doc_list')
