from django.db import models
from django.urls.base import reverse_lazy


class Milestone(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    notes = models.TextField()

    def __str__(self):
        return f'Milestone {self.order} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('milestone_detail', args=[str(self.id)])

    @property
    def tasks(self):
        return Task.objects.filter(milestone=self)


class Task(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    notes = models.TextField()

    def __str__(self):
        return f'{self.milestone} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('task_detail', args=[str(self.id)])
