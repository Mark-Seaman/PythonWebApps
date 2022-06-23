<<<<<<< HEAD
from django.contrib.auth.models import User
from django.db import models
from django.urls.base import reverse_lazy


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    notes = models.TextField()
=======
from django.db import models
from django.urls import reverse_lazy


def get_upload(instance, filename):
    if instance.folder:
        return f'images/{instance.folder}/{filename}'
    return f'images/{filename}'


class Image(models.Model):
    folder = models.CharField(max_length=100, default='')
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)
    title = models.CharField(max_length=200)
>>>>>>> ba095

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse_lazy('author_detail', args=[str(self.id)])

    @property
    def photos(self):
        return Photogram.objects.filter(author=self)

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @staticmethod
    def get_me(user):
        return Author.objects.get_or_create(user=user)[0]


class Photogram(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('photogram_detail', args=[str(self.id)])
=======
        return reverse_lazy('image_list')


class Photogram(models.Model):

    photo = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    headline = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.headline}'

    def get_absolute_url(self):
        return reverse_lazy('photo_list')
>>>>>>> ba095
