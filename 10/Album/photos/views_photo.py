from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Photo


class PhotoView(RedirectView):
    url = reverse_lazy('photo_list')


class PhotoListView(ListView):
    template_name = 'photo_list.html'
    model = Photo
    context_object_name = 'photos'


class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model = Photo
    context_object_name = 'photo'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     photo = kwargs.get('photo')
    #     kwargs.update(dict(dependent=photo.dependents))
    #     return kwargs


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = "photo_add.html"
    model = Photo
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instance.author = Person.get_me(self.request.user)
    #     return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "photo_edit.html"
    model = Photo
    fields = '__all__'


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photo_list')

