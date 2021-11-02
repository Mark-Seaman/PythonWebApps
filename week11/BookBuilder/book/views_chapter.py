from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from markdown import markdown

from .models import Chapter
from .book import get_chapter


class ChapterView(RedirectView):
    url = '/chapter/'


class ChapterListView(ListView):
    template_name = 'chapter_list.html'
    model = Chapter

    def get_queryset(self):
        return super().get_queryset()


class ChapterDetailView(DetailView):
    template_name = 'chapter_detail.html'
    model = Chapter

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        chapter = kwargs['object']
        chapter = get_chapter(chapter.book, chapter.order)
        return {'object': chapter}


class ChapterCreateView(LoginRequiredMixin, CreateView):
    template_name = "chapter_add.html"
    model = Chapter
    fields = '__all__'

    def form_valid(self, form):
        form.instance.book_id = 1
        return super().form_valid(form)


class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "chapter_edit.html"
    model = Chapter
    fields = '__all__'


class ChapterDeleteView(LoginRequiredMixin, DeleteView):
    model = Chapter
    template_name = 'chapter_delete.html'
    success_url = reverse_lazy('chapter_list')
