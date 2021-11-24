from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import DataFactory


class DataFactoryView(RedirectView):
    url = reverse_lazy('factory_list')


class DataFactoryListView(ListView):
    template_name = 'factory_list.html'
    model = DataFactory


class DataFactoryDetailView(DetailView):
    template_name = 'factory_detail.html'
    model = DataFactory

    def get_context_data(self, **kwargs):
        kwargs = self.super().get_context_data(**kwargs)
        # kwargs.update(dict(dependent=Dependent.obects.filter(factory=kwargs.get('object'))))
        return kwargs


class DataFactoryCreateView(LoginRequiredMixin, CreateView):
    template_name = "factory_add.html"
    model = DataFactory
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class DataFactoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "factory_edit.html"
    model = DataFactory
    fields = '__all__'


class DataFactoryDeleteView(LoginRequiredMixin, DeleteView):
    model = DataFactory
    template_name = 'factory_delete.html'
    success_url = reverse_lazy('factory_list')
