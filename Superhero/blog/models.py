from django.db import models
from django.urls import reverse_lazy


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("article_list")

