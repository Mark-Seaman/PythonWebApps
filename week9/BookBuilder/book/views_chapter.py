from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.views.generic.base import TemplateView

from .models import Chapter


class ChapterView(RedirectView):
    url = '/chapter/'


class ChapterListView(ListView):
    template_name = 'chapter_list.html'
    model = Chapter


class ChapterDetailView(DetailView):
    template_name = 'chapter_detail.html'
    model = Chapter


class ChapterCreateView(LoginRequiredMixin, CreateView):
    template_name = "chapter_add.html"
    model = Chapter
    fields = ['title', 'author', 'description']


class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "chapter_edit.html"
    model = Chapter
    fields = ['title', 'author', 'description']


class ChapterDeleteView(LoginRequiredMixin, DeleteView):
    model = Chapter
    template_name = 'chapter_delete.html'
    success_url = reverse_lazy('chapter_list')
