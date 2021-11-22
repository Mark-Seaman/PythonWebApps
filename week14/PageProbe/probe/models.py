from django.db import models
from django.urls.base import reverse_lazy


class Probe(models.Model):

    name = models.CharField(max_length=100)
    page = models.URLField()
    text = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.page}'

    def get_absolute_url(self):
        return reverse_lazy('lesson_list')
