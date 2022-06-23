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

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('image_list')


class Photogram(models.Model):

    photo = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    headline = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.headline}'

    def get_absolute_url(self):
        return reverse_lazy('photo_list')
