from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from requests import get

from .models import Probe, Result


class ProbeView(RedirectView):
    url = reverse_lazy('probe_list')


# class TestProbeView(RedirectView):

#     def get_redirect_url(self, **kwargs):
#         return super().get_redirect_url(**kwargs)


class ProbeListView(ListView):
    template_name = 'probe_list.html'
    model = Probe


class ProbeDetailView(DetailView):
    template_name = 'probe_detail.html'
    model = Probe

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        probe = kwargs['object']
        response = get(probe.page)
        passed = response.status_code == 200
        Result.create(probe=probe, output=response.text, passed=passed)
        kwargs['results'] = Result.objects.filter(probe=probe)
        return kwargs


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
