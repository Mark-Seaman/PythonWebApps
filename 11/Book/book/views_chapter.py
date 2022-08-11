from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Chapter


class ChapterView(RedirectView):
    url = reverse_lazy('chapter_list')


# class ChapterListView(ListView):
#     template_name = 'chapter/list.html'
#     model = Chapter
#     context_object_name = 'chapters'

#     def get_queryset(self):
#         return super().get_queryset()


class ChapterDetailView(DetailView):
    template_name = 'chapter/detail.html'
    model = Chapter
    context_object_name = 'chapter'


class ChapterCreateView(LoginRequiredMixin, CreateView):
    template_name = "chapter/add.html"
    model = Chapter
    fields = '__all__'

    def form_valid(self, form):
        form.instance.book_id = self.kwargs.get('book')
        return super().form_valid(form)


class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "chapter/edit.html"
    model = Chapter
    fields = '__all__'


class ChapterDeleteView(LoginRequiredMixin, DeleteView):
    model = Chapter
    template_name = 'chapter/delete.html'
    # success_url = reverse_lazy('book_detail')

    def get_success_url(self):
        chapter = Chapter.objects.get(pk=self.kwargs.get('pk'))
        return f'/book/{chapter.book.pk}'
