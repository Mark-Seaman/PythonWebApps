from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
# from django.conf import settings

# from accounts.models import UserAccount

# User = settings.AUTH_USER_MODEL


class Author(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse_lazy('author_list')


class Article (models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('article_list')
