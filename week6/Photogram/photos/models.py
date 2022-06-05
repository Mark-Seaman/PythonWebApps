from django.db import models
from django.urls import reverse_lazy


def get_upload(filename):
    return f'images/{filename}'


class Photogram(models.Model):

    image = models.ImageField(null=True, blank=True, upload_to=get_upload)
    headline = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.headline}'

    def get_absolute_url(self):
        return reverse_lazy('photo_list')

# --------------------
# Image
#
# chapter - points to chapter object
# image - URL of saved image
# title - title text of chapter


def get_upload(instance, filename):
    return f'images/{instance.folder}/{filename}'


class Image(models.Model):
    folder = models.CharField(max_length=100, default='book')
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('image_list')
