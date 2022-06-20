from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Book


class BookView(RedirectView):
    url = reverse_lazy('book_list')


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book
    context_object_name = 'books'


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book
    context_object_name = 'book'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     book = kwargs.get('book')
    #     kwargs.update(dict(dependent=book.dependents))
    #     return kwargs


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "book_add.html"
    model = Book
    fields = '__all__'

    def form_valid(self, form):
        # form.instance.owner = Owner.objects.get(user=self.request.user)
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "book_edit.html"
    model = Book
    fields = '__all__'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')
