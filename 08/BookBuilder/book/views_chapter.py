from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Chapter


class ChapterView(RedirectView):
    url = reverse_lazy('chapter_list')


class ChapterListView(ListView):
    template_name = 'chapter_list.html'
    model = Chapter
    context_object_name = 'chapters'


class ChapterDetailView(DetailView):
    template_name = 'chapter_detail.html'
    model = Chapter
    context_object_name = 'chapter'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     chapter = kwargs.get('chapter')
    #     kwargs.update(dict(dependent=chapter.dependents))
    #     return kwargs


class ChapterCreateView(LoginRequiredMixin, CreateView):
    template_name = "chapter_add.html"
    model = Chapter
    fields = '__all__'

    def form_valid(self, form):
        # form.instance.owner = Owner.objects.get(user=self.request.user)
        return super().form_valid(form)


class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "chapter_edit.html"
    model = Chapter
    fields = '__all__'


class ChapterDeleteView(LoginRequiredMixin, DeleteView):
    model = Chapter
    template_name = 'chapter_delete.html'
    success_url = reverse_lazy('chapter_list')
