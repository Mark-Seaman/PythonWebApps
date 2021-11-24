from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Test


class TestView(RedirectView):
    url = reverse_lazy('test_list')


class TestListView(ListView):
    template_name = 'test_list.html'
    model = Test


class TestDetailView(DetailView):
    template_name = 'test_detail.html'
    model = Test

    def get_context_data(self, **kwargs):
        kwargs = self.super().get_context_data(**kwargs)
        # kwargs.update(dict(dependent=Dependent.obects.filter(test=kwargs.get('object'))))
        return kwargs


class TestCreateView(LoginRequiredMixin, CreateView):
    template_name = "test_add.html"
    model = Test
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class TestUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "test_edit.html"
    model = Test
    fields = '__all__'


class TestDeleteView(LoginRequiredMixin, DeleteView):
    model = Test
    template_name = 'test_delete.html'
    success_url = reverse_lazy('test_list')
