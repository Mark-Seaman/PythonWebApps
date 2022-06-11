from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# from .models import UserAccount


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class AccountView(RedirectView):
    url = '/accounts/'


class AccountListView(ListView):
    template_name = 'account_list.html'
    model = User


class AccountDetailView(DetailView):
    template_name = 'account_detail.html'
    model = User


class AccountCreateView(LoginRequiredMixin, CreateView):
    template_name = "account_add.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('account_list')


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('account_list')


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'account_delete.html'
    success_url = reverse_lazy('account_list')
