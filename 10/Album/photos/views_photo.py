from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, TemplateView, UpdateView

from .models import Author, Photo


class PhotoView(RedirectView):
    url = reverse_lazy('photo_list')


class PhotoListView(ListView):
    template_name = 'photo/list.html'
    model = Photo
    context_object_name = 'photos'


class PhotoCarouselView(TemplateView):
    template_name = 'photo/carousel.html'

    def get_context_data(self, **kwargs):
        photos = Author.get_me(self.request.user).photos
        carousel = carousel_data(photos)
        return dict(title='Carousel View', carousel=carousel)


def carousel_data(photos):
    return [
        dict(image_url=f"/media/{photos[0].image}", label="One", active="active"),
        dict(image_url=f"/media/{photos[1].image}", label="Two"),
        dict(image_url=f"/media/{photos[2].image}", label="Three"),
        dict(image_url="https://source.unsplash.com/random/1200x800?ocean", label="Ocean"),
        dict(image_url="https://source.unsplash.com/random/1200x800?flower", label="Flower"),
    ]


class PhotoDetailView(DetailView):
    template_name = 'photo/detail.html'
    model = Photo
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = "photo/add.html"
    model = Photo
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = Author.get_me(self.request.user)
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "photo/edit.html"
    model = Photo
    fields = '__all__'


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/delete.html'
    success_url = reverse_lazy('photo_list')
