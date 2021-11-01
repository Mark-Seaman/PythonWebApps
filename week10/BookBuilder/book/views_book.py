from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Book, Chapter
from .book import xget_author


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
        return dict(object=book, chapters=Chapter.objects.filter(book=book))


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "book_add.html"
    model = Book
    fields = ['title', 'author', 'description', 'doc_path']

    # def form_valid(self, form):
    #     # form.instance.author = xget_author('Mark Seaman')
    #     return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "book_edit.html"
    model = Book
    fields = ['title', 'author', 'description', 'doc_path']


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')
