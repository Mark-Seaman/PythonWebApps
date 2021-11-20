from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from markdown import markdown

from .models import Lesson
from .course import get_lesson


class LessonView(RedirectView):
    url = '/lesson/'


class LessonListView(ListView):
    template_name = 'lesson_list.html'
    model = Lesson

    def get_queryset(self):
        return super().get_queryset()


class LessonDetailView(DetailView):
    template_name = 'lesson_detail.html'
    model = Lesson

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        lesson = kwargs['object']
        lesson = get_lesson(lesson.course, lesson.order)
        return {'object': lesson}


class LessonCreateView(LoginRequiredMixin, CreateView):
    template_name = "lesson_add.html"
    model = Lesson
    fields = '__all__'

    def form_valid(self, form):
        form.instance.course_id = 1
        return super().form_valid(form)


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "lesson_edit.html"
    model = Lesson
    fields = '__all__'


class LessonDeleteView(LoginRequiredMixin, DeleteView):
    model = Lesson
    template_name = 'lesson_delete.html'
    success_url = reverse_lazy('lesson_list')
