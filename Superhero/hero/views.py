from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Hero

class HeroListView(ListView):
    template_name = "hero/list.html"
    model = Hero

class HeroDetailView(DetailView):
    template_name = "hero/detail.html"
    model = Hero

class HeroCreateView(CreateView):
    template_name = "hero/add.html"
    model = Hero
    fields = "__all__"

class HeroUpdateView(UpdateView):
    template_name = "hero/edit.html"
    model = Hero
    fields = "__all__"

class HeroDeleteView(DeleteView):
    template_name = "hero/delete.html"
    model = Hero
    success_url = reverse_lazy('hero_list')
