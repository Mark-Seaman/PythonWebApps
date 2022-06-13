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

    @property
    def projects(self):
        return Project.objects.filter(developer=self)

    def get_absolute_url(self):
        return reverse_lazy('developer_list')


class Project(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

    @property
    def milestones(self):
        return Milestone.objects.filter(project=self)

    def get_absolute_url(self):
        return reverse_lazy('project_detail', args=[str(self.id)])


class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    notes = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

    @property
    def tasks(self):
        return Task.objects.filter(milestone=self)

    def get_absolute_url(self):
        return reverse_lazy('milestone_detail', args=[str(self.id)])


class Task(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('task_detail', args=[str(self.id)])

    # @property
    # def dependents(self):
    #     return Dependents.objects.filter(parent=self)
