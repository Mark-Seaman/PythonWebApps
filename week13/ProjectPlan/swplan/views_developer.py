from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, ListView, RedirectView, UpdateView
from markdown import markdown

from .models import Developer, Project


def check_developers():
    for user in User.objects.all():
        if not Developer.objects.filter(user=user):
            Developer.objects.create(user=user)


def list_projects(developer):
    check_developers()
    return dict(projects=developer.projects)
    # return dict(projects=Project.objects.filter(developer=developer))


class DeveloperSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('developer_list')


class DeveloperView(RedirectView):
    url = reverse_lazy('developer_list')


class DeveloperListView(ListView):
    template_name = 'developer_list.html'
    model = Developer
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        check_developers()
        kwargs = super().get_context_data(**kwargs)
        return kwargs


class DeveloperDetailView(DetailView):
    template_name = 'developer_detail.html'
    model = Developer

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(list_projects(kwargs.get('object')))
        return kwargs


# class DeveloperCreateView(LoginRequiredMixin, CreateView):
#     template_name = "developer_add.html"
#     model = Developer
#     fields = '__all__'

#     def form_valid(self, form):
#         form.instance.author_id = 1
#         return super().form_valid(form)


class DeveloperUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "developer_edit.html"
    model = Developer
    fields = '__all__'


class DeveloperDeleteView(LoginRequiredMixin, DeleteView):
    model = Developer
    template_name = 'developer_delete.html'
    success_url = reverse_lazy('developer_list')
