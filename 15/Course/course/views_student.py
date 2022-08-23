from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Student


class StudentView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return reverse_lazy('student_list')
        return f'/student/{Student.get_me(self.request.user).pk}'


class StudentListView(ListView):
    template_name = 'student/list.html'
    model = Student
    context_object_name = 'students'


class StudentDetailView(DetailView):
    template_name = 'student/detail.html'
    model = Student
    context_object_name = 'student'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     student = kwargs.get('student')
    #     kwargs['dependents'] = student.dependents
    #     return kwargs


class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = "student/add.html"
    model = Student
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instance.book = 1
    #     form.instance.author = Person.get_me(self.request.user)
    #     return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "student/edit.html"
    model = Student
    fields = '__all__'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student/delete.html'
    success_url = reverse_lazy('student_list')


class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('student_view')
