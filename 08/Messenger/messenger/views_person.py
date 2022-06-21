from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Person


class PersonView(RedirectView):
    url = reverse_lazy('person_list')


class PersonListView(ListView):
    template_name = 'person_list.html'
    model = Person
    context_object_name = 'persons'


class PersonDetailView(DetailView):
    template_name = 'person_detail.html'
    model = Person
    context_object_name = 'person'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     person = kwargs.get('person')
    #     kwargs.update(dict(dependent=person.dependents))
    #     return kwargs


class PersonCreateView(LoginRequiredMixin, CreateView):
    template_name = "person_add.html"
    model = Person
    fields = '__all__'

    def form_valid(self, form):
        # form.instance.owner = Owner.objects.get(user=self.request.user)
        return super().form_valid(form)


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "person_edit.html"
    model = Person
    fields = '__all__'


class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'person_delete.html'
    success_url = reverse_lazy('person_list')
