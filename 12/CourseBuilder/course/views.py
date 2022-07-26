from re import L
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from pathlib import Path
from markdown import markdown

from .models import Lesson


def get_document(lesson):
    doc = Path(lesson.document).read_text()
    return markdown(doc)


class LessonDetailView(DetailView):
    template_name = 'lesson/detail.html'
    model = Lesson
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        lesson = kwargs.get('lesson')
        kwargs['body'] = get_document(lesson)
        kwargs['lessons'] = Lesson.objects.all()
        return kwargs
