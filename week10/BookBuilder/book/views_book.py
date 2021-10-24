from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.views.generic.base import TemplateView

from .models import Book, Chapter


class BookView(RedirectView):
    url = '/book/'


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        book = Book.objects.get(pk=self.kwargs['pk'])
        return dict(object=book, chapters=Chapter.objects.filter(book=book.title))


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "book_add.html"
    model = Book
    fields = ['title', 'author', 'description']


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "book_edit.html"
    model = Book
    fields = ['title', 'author', 'description']


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')
