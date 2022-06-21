from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Person


def get_person(user):
    return Person.objects.get_or_create(user=user)[0]


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('person_home')


class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PersonHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/message/'
        return f'/person/{get_person(self.request.user).pk}'


class PersonListView(ListView):
    template_name = 'person_list.html'
    model = Person
    context_object_name = 'persons'


class PersonDetailView(DetailView):
    template_name = 'person_detail.html'
    model = Person
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(dict(messages=kwargs.get('object').messages))
        return kwargs


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "person_edit.html"
    model = Person
    fields = '__all__'


class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'person_delete.html'
    success_url = reverse_lazy('person_list')
