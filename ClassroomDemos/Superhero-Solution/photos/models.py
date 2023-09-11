from django.db import models
from django.urls import reverse_lazy


def get_upload(instance, filename):
    return f'images/{filename}'


class Photo (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)

    def __str__(self):
        return f'{self.pk} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('photo_detail', args=[str(self.id)])
