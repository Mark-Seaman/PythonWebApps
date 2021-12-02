from django.db import models
from django.urls.base import reverse_lazy


class Document(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('document_list')
