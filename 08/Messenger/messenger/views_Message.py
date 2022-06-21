from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Message


class MessageView(RedirectView):
    url = reverse_lazy('Message_list')


class MessageListView(ListView):
    template_name = 'Message_list.html'
    model = Message
    context_object_name = 'Messages'


class MessageDetailView(DetailView):
    template_name = 'Message_detail.html'
    model = Message
    context_object_name = 'Message'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     Message = kwargs.get('Message')
    #     kwargs.update(dict(dependent=Message.dependents))
    #     return kwargs


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = "Message_add.html"
    model = Message
    fields = '__all__'

    def form_valid(self, form):
        # form.instance.owner = Owner.objects.get(user=self.request.user)
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "Message_edit.html"
    model = Message
    fields = '__all__'


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'Message_delete.html'
    success_url = reverse_lazy('Message_list')
