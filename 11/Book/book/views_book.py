from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Author, Book


class BookListView(ListView):
    template_name = 'book/list.html'
    model = Book
    context_object_name = 'books'


class BookDetailView(DetailView):
    template_name = 'book/detail.html'
    model = Book
    context_object_name = 'book'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     book = kwargs.get('book')
    #     kwargs['dependents'] = book.dependents
    #     return kwargs


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "book/add.html"
    model = Book
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = Author.get_me(self.request.user)
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "book/edit.html"
    model = Book
    fields = '__all__'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = reverse_lazy('book_list')
