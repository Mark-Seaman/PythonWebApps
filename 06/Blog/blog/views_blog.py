from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Blog


class BlogView(RedirectView):
    url = reverse_lazy('blog_list')


class BlogListView(ListView):
    template_name = 'blog/list.html'
    model = Blog
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Blog
    context_object_name = 'blog'


class BlogCreateView(CreateView):
    template_name = "blog/add.html"
    model = Blog
    fields = '__all__'


class BlogUpdateView(UpdateView):
    template_name = "blog/edit.html"
    model = Blog
    fields = '__all__'


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog_list')
