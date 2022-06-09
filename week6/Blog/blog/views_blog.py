from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Article, Blog


class BlogView(RedirectView):
    url = reverse_lazy('blog_list')


class BlogListView(ListView):
    template_name = 'blog_list.html'
    model = Blog


class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = Blog

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(dict(articles=Article.objects.filter(blog=kwargs.get('object'))))
        return kwargs


class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = "blog_add.html"
    model = Blog
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "blog_edit.html"
    model = Blog
    fields = '__all__'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')
