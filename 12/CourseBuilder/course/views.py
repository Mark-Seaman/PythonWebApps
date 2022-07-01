from re import L
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from pathlib import Path
from markdown import markdown

from .models import Lesson


def get_lesson(i, path):
    lesson = Lesson.objects.get_or_create(pk=i+1)[0]
    lesson.title = get_title(path)
    lesson.save()


def get_title(doc):
    if not doc.exists():
        return f'Document not found, {doc}'
    return doc.read_text().split('\n')[0][10:]


def get_document(lesson):
    doc = Path(lesson.document).read_text()
    return markdown(doc)


def update_lessons():
    for i, doc in enumerate(sorted(Path('Documents/').iterdir())):
        get_lesson(i, doc)


# class LessonListView(ListView):
#     template_name = 'lesson/list.html'
#     model = Lesson
#     context_object_name = 'lessons'

#     def get_context_data(self, **kwargs):
#         update_lessons()
#         kwargs = super().get_context_data(**kwargs)
#         return kwargs


class LessonDetailView(DetailView):
    template_name = 'lesson/detail.html'
    model = Lesson
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        update_lessons()
        kwargs = super().get_context_data(**kwargs)
        lesson = kwargs.get('lesson')
        kwargs['body'] = get_document(lesson)
        kwargs['lessons'] = Lesson.objects.all()
        return kwargs
