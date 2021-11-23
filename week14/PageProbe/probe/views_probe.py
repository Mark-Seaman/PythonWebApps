from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Probe


class ProbeView(RedirectView):
    url = reverse_lazy('probe_list')


class ProbeListView(ListView):
    template_name = 'probe_list.html'
    model = Probe


class ProbeDetailView(DetailView):
    template_name = 'probe_detail.html'
    model = Probe

    def get_context_data(self, **kwargs):
        probe = Probe.objects.get(pk=self.kwargs['pk'])
        return dict(object=probe, lessons=Lesson.objects.filter(probe=probe))


class ProbeCreateView(LoginRequiredMixin, CreateView):
    template_name = "probe_add.html"
    model = Probe
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class ProbeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "probe_edit.html"
    model = Probe
    fields = '__all__'


class ProbeDeleteView(LoginRequiredMixin, DeleteView):
    model = Probe
    template_name = 'probe_delete.html'
    success_url = reverse_lazy('probe_list')
