from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Photogram, Author


class PhotogramListView(ListView):
    template_name = 'photogram_list.html'
    model = Photogram
    context_object_name = 'photograms'


class PhotogramDetailView(DetailView):
    template_name = 'photogram_detail.html'
    model = Photogram
    context_object_name = 'photogram'


class PhotogramCreateView(LoginRequiredMixin, CreateView):
    template_name = "photogram_add.html"
    model = Photogram
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = Author.get_me(self.request.user)
        return super().form_valid(form)


class PhotogramUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "photogram_edit.html"
    model = Photogram
    fields = '__all__'


class PhotogramDeleteView(LoginRequiredMixin, DeleteView):
    model = Photogram
    template_name = 'photogram_delete.html'
    success_url = reverse_lazy('photogram_list')
