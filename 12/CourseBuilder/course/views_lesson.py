from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Lesson


class LessonView(RedirectView):
    url = reverse_lazy('lesson_list')


class LessonListView(ListView):
    template_name = 'lesson_list.html'
    model = Lesson
    context_object_name = 'lessons'


class LessonDetailView(DetailView):
    template_name = 'lesson_detail.html'
    model = Lesson
    context_object_name = 'lesson'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     lesson = kwargs.get('lesson')
    #     kwargs.update(dict(dependent=lesson.dependents))
    #     return kwargs


class LessonCreateView(LoginRequiredMixin, CreateView):
    template_name = "lesson_add.html"
    model = Lesson
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instance.author = Person.get_me(self.request.user)
    #     return super().form_valid(form)


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "lesson_edit.html"
    model = Lesson
    fields = '__all__'


class LessonDeleteView(LoginRequiredMixin, DeleteView):
    model = Lesson
    template_name = 'lesson_delete.html'
    success_url = reverse_lazy('lesson_list')

