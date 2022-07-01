from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Person


def get_author(user):
    return Person.objects.get_or_create(user=user)[0]


class PersonHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/message/'
        return f'/person/{get_author(self.request.user).pk}'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('home')


class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/add.html'


class PersonListView(ListView):
    template_name = 'person/list.html'
    model = Person
    context_object_name = 'persons'


class PersonDetailView(DetailView):
    template_name = 'person/detail.html'
    model = Person
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(dict(messages=kwargs.get('person').messages))
        return kwargs


class PersonCreateView(LoginRequiredMixin, CreateView):
    template_name = "person/add.html"
    model = Person
    fields = '__all__'


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "person/edit.html"
    model = Person
    fields = '__all__'


class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'person/delete.html'
    success_url = reverse_lazy('person_list')
