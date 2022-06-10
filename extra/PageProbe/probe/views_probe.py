from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  RedirectView, UpdateView)
from requests import get

from .models import Probe
from .probe import clear_probe_history, execute_probe, launch_all_probes, result_list


class ProbeView(RedirectView):
    url = reverse_lazy('probe_list')


class ProbeListView(ListView):
    template_name = 'probe_list.html'
    model = Probe


class ProbeDetailView(DetailView):
    template_name = 'probe_detail.html'
    model = Probe

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        probe = kwargs['object']
        execute_probe(probe)
        kwargs['results'] = result_list(probe)
        return kwargs


class ProbeLaunchView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        launch_all_probes()
        return reverse('probe_list')


class ProbeClearView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        probe_pk = self.kwargs.get('pk')
        clear_probe_history(probe_pk)
        return reverse('probe_detail', args=[probe_pk])


class ProbeCreateView(CreateView):
    template_name = "probe_add.html"
    model = Probe
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class ProbeUpdateView(UpdateView):
    template_name = "probe_edit.html"
    model = Probe
    fields = '__all__'


class ProbeDeleteView(DeleteView):
    model = Probe
    template_name = 'probe_delete.html'
    success_url = reverse_lazy('probe_list')
