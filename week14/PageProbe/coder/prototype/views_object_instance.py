from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import ClassObject, Lesson
from .object_instance import get_author


class BookView(RedirectView):
    url = reverse_lazy('object_instance_list')


class BookListView(ListView):
    template_name = 'object_instance_list.html'
    model = ClassObject


class BookDetailView(DetailView):
    template_name = 'object_instance_detail.html'
    model = ClassObject

    def get_context_data(self, **kwargs):
        object_instance = ClassObject.objects.get(pk=self.kwargs['pk'])
        return dict(object=object_instance, lessons=Lesson.objects.filter(object_instance=object_instance))


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "object_instance_add.html"
    model = ClassObject
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "object_instance_edit.html"
    model = ClassObject
    fields = '__all__'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = ClassObject
    template_name = 'object_instance_delete.html'
    success_url = reverse_lazy('object_instance_list')
