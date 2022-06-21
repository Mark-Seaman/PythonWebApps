from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Message, Person


class MessageView(RedirectView):
    url = reverse_lazy('message_list')


class MessageListView(ListView):
    template_name = 'message_list.html'
    model = Message
    context_object_name = 'messages'


class MessageDetailView(DetailView):
    template_name = 'message_detail.html'
    model = Message
    context_object_name = 'message'


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = "message_add.html"
    model = Message
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = Person.get_me(self.request.user)
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "message_edit.html"
    model = Message
    fields = '__all__'


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('home')
