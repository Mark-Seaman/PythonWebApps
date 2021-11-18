from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.views.generic.base import TemplateView

from .models import Author, Course, Chapter


class AuthorView(RedirectView):
    url = '/author/'


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author

    def get_context_data(self, **kwargs):
        author = Author.objects.get(pk=self.kwargs['pk'])
        return dict(object=author, books=Course.objects.filter(author=author))


class AuthorCreateView(LoginRequiredMixin, CreateView):
    template_name = "author_add.html"
    model = Author
    fields = ['name']
    success_url = reverse_lazy('author_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "author_edit.html"
    model = Author
    fields = ['name', 'photo']
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('author_list')
