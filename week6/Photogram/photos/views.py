from django.views.generic import CreateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Image, Photogram


class PhotoListView(ListView):
    template_name = 'photo_list.html'
    model = Photogram


class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model = Photogram


class PhotoCreateView(CreateView):
    template_name = "photo_add.html"
    model = Photogram
    fields = '__all__'


class PhotoUpdateView(UpdateView):
    template_name = "photo_edit.html"
    model = Photogram
    fields = '__all__'


class PhotoDeleteView(DeleteView):
    model = Photogram
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photogram_list')


class ImageListView(ListView):
    template_name = 'image_list.html'
    model = Image


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'image_delete.html'
    success_url = reverse_lazy('image_list')


class ImageCreateView(LoginRequiredMixin, CreateView):
    template_name = "image_add.html"
    model = Image
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instance.chapter_id = 1
    #     return super().form_valid(form)


# class ImageDetailView(DetailView):
#     template_name = 'image_detail.html'
#     model = Image


# class ImageUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = "image_edit.html"
#     model = Image
#     fields = '__all__'
