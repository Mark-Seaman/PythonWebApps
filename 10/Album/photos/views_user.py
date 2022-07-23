from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Author


# User Account Views

class UserHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/author/'
        author = Author.get_me(self.request.user)
        if author.name == ' ':
            author.user.first_name = 'Unknown'
            author.user.last_name = 'User'
            author.user.email = 'me@here.com'
            author.user.save()
        return f'/author/{author.pk}'


class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/add.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('author_home')
