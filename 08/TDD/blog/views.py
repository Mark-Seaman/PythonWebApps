from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Article


class ArticleListView(ListView):
    template_name = "article/list.html"
    model = Article
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    template_name = "article/detail.html"
    model = Article
    context_object_name = "article"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/add.html"
    model = Article
    fields = "__all__"


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article/edit.html"
    model = Article
    fields = "__all__"


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "article/delete.html"
    success_url = reverse_lazy("article_list")
