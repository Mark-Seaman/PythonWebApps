from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from .models import Image, Chapter


class ImageListView(ListView):
    template_name = 'image_list.html'
    model = Image


# class ImageDetailView(DetailView):
#     template_name = 'image_detail.html'
#     model = Image


class ImageCreateView(LoginRequiredMixin, CreateView):
    template_name = "image_add.html"
    model = Image
    fields = ['image', 'title']

    # def form_valid(self, form):
    #     form.instance.chapter_id = 1
    #     return super().form_valid(form)


# class ImageUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = "image_edit.html"
#     model = Image
#     fields = '__all__'


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'image_delete.html'
    success_url = reverse_lazy('image_list')
