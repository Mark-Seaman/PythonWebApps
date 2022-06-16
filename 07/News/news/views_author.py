from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from .models import Article, Author


def check_authors():
    for user in User.objects.all():
        if not Author.objects.filter(user=user):
            Author.objects.create(user=user)


def list_articles(author):
    return dict(articles=Article.objects.filter(author=author))


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        check_authors()
        return kwargs


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(list_articles(kwargs.get('object')))
        return kwargs


# class AuthorCreateView(LoginRequiredMixin, CreateView):
#     template_name = "author_add.html"
#     model = Author
#     fields = '__all__'

#     def form_valid(self, form):
#         form.instance.author_id = 1
#         return super().form_valid(form)


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "author_edit.html"
    model = Author
    fields = '__all__'


# class AuthorDeleteView(LoginRequiredMixin, DeleteView):
#     model = Author
#     template_name = 'author_delete.html'
#     success_url = reverse_lazy('author_list')
