from django.db import models
from django.urls import reverse_lazy


class Blog(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='Abe Lincoln')
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('blog_list')


class Article (models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('article_list')
