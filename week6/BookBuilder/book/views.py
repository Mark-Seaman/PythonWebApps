from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
=======
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
>>>>>>> 8d974573ad4e9519dc36325f4186732bed818555

from .models import Book


<<<<<<< HEAD
=======
class BookView(RedirectView):
    url = '/book/'


>>>>>>> 8d974573ad4e9519dc36325f4186732bed818555
class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book


<<<<<<< HEAD
class BookAddView(CreateView):
    template_name = "book_edit.html"
    model = Book
    fields = '__all__'


class BookEditView(UpdateView):
    template_name = "book_edit.html"
    model = Book
    fields = '__all__'


# Improvements
# fields = '__all__'
# LoginRequiredMixin,
=======
class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "book_add.html"
    model = Book
    fields = ['title', 'author']


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "book_edit.html"
    model = Book
    fields = ['title', 'author']


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')
>>>>>>> 8d974573ad4e9519dc36325f4186732bed818555
