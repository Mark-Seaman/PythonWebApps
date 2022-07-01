from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Milestone


class MilestoneView(RedirectView):
    url = reverse_lazy('milestone_list')


class MilestoneListView(ListView):
    template_name = 'milestone/list.html'
    model = Milestone
    context_object_name = 'milestones'


class MilestoneDetailView(DetailView):
    template_name = 'milestone/detail.html'
    model = Milestone
    context_object_name = 'milestone'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        milestone = kwargs.get('milestone')
        kwargs['tasks'] = milestone.tasks
        return kwargs


class MilestoneCreateView(CreateView):
    template_name = "milestone/add.html"
    model = Milestone
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instance.author = Person.get_me(self.request.user)
    #     return super().form_valid(form)


class MilestoneUpdateView(UpdateView):
    template_name = "milestone/edit.html"
    model = Milestone
    fields = '__all__'


class MilestoneDeleteView(DeleteView):
    model = Milestone
    template_name = 'milestone/delete.html'
    success_url = reverse_lazy('milestone_list')
