from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Milestone, Project


class MilestoneView(RedirectView):
    url = reverse_lazy('milestone_list')


class MilestoneListView(ListView):
    template_name = 'milestone_list.html'
    model = Milestone
    context_object_name = 'milestones'

    def get_queryset(self):
        p = self.kwargs.get('project')
        return Milestone.objects.filter(project=p)


class MilestoneDetailView(DetailView):
    template_name = 'milestone_detail.html'
    model = Milestone
    context_object_name = 'milestone'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     kwargs.update(dict(dependent=Dependent.obects.filter(milestone=kwargs.get('object'))))
    #     return kwargs


class MilestoneCreateView(LoginRequiredMixin, CreateView):
    template_name = "milestone_add.html"
    model = Milestone
    fields = '__all__'

    def form_valid(self, form):
        form.instance.project = Project.objects.get(pk=self.kwargs.get('project'))
        return super().form_valid(form)


class MilestoneUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "milestone_edit.html"
    model = Milestone
    fields = '__all__'


class MilestoneDeleteView(LoginRequiredMixin, DeleteView):
    model = Milestone
    template_name = 'milestone_delete.html'
    # success_url = '/'
