from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse_lazy('author_detail', args=[str(self.id)])

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def articles(self):
        return Photo.objects.filter(author=self)

    @staticmethod
    def get_me(user):
        return Author.objects.get_or_create(user=user)[0]


def get_upload(instance, filename):
    # if instance.folder:
    #     return f'images/{instance.folder}/{filename}'
    return f'images/{filename}'


class Photo (models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('photo_detail', args=[str(self.id)])
