from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Course, Lesson
from .book import get_author


class BookView(RedirectView):
    url = reverse_lazy('book_list')


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Course


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Course

    def get_context_data(self, **kwargs):
        book = Course.objects.get(pk=self.kwargs['pk'])
        return dict(object=book, chapters=Lesson.objects.filter(book=book))


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "book_add.html"
    model = Course
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "book_edit.html"
    model = Course
    fields = '__all__'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')
