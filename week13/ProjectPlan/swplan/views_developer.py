from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Developer


class DeveloperView(RedirectView):
    url = reverse_lazy('developer_list')


class DeveloperListView(ListView):
    template_name = 'developer_list.html'
    model = Developer


class DeveloperDetailView(DetailView):
    template_name = 'developer_detail.html'
    model = Developer

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     kwargs.update(dict(dependent=Dependent.obects.filter(developer=kwargs.get('object'))))
    #     return kwargs


class DeveloperCreateView(LoginRequiredMixin, CreateView):
    template_name = "developer_add.html"
    model = Developer
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class DeveloperUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "developer_edit.html"
    model = Developer
    fields = '__all__'


class DeveloperDeleteView(LoginRequiredMixin, DeleteView):
    model = Developer
    template_name = 'developer_delete.html'
    success_url = reverse_lazy('developer_list')
