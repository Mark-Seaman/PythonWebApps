from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm


from .models import Author, Book, Chapter


def get_author(user):
    return Author.objects.get_or_create(user=user)[0]


class AuthorHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/book/'
        return f'/author/{get_author(self.request.user).pk}'


class AuthorAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('author_home')


class AuthorView(RedirectView):
    url = '/author/'


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author

    def get_context_data(self, **kwargs):
        author = Author.objects.get(pk=self.kwargs['pk'])
        return dict(object=author, books=Book.objects.filter(author=author))


class AuthorCreateView(LoginRequiredMixin, CreateView):
    template_name = "author_add.html"
    model = Author
    fields = ['name']
    success_url = reverse_lazy('author_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "author_edit.html"
    model = Author
    fields = ['name']
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('author_list')
