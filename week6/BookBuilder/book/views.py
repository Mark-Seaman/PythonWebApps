from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Book


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book


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
