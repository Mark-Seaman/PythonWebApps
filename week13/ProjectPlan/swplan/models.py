from django.contrib.auth.models import User
from django.db import models
from django.urls.base import reverse_lazy


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.user.username}'

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_absolute_url(self):
        return reverse_lazy('developer_list')


class Project(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('project_list')


class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    notes = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('milestone_list')
