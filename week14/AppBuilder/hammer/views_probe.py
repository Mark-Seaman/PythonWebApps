from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Test
from .probe import execute_probe, result_list


class TestView(RedirectView):
    url = reverse_lazy('test_list')


class TestRunView(RedirectView):

    def get_redirect_url(self, **kwargs):
        pk = self.kwargs.get('pk')
        probe = Test.objects.filter(pk=pk)
        execute_probe(probe)
        return reverse('test_detail', args=[pk])


class TestListView(ListView):
    template_name = 'test_list.html'
    model = Test


class TestDetailView(DetailView):
    template_name = 'test_detail.html'
    model = Test

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        probe = kwargs['object']
        execute_probe(probe)
        kwargs['results'] = result_list(probe)
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
