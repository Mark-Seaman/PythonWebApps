from django.db import models
from django.urls.base import reverse_lazy


class Test(models.Model):

    name = models.CharField(max_length=20)
    expected = models.TextField()
    source = models.TextField()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse_lazy('test_list')

    @staticmethod
    def create(**kwargs):
        x = Test.objects.get_or_create(name=kwargs.get('name'))[0]
        x.expected = kwargs.get('expected')
        x.source = kwargs.get('source')
        x.save()
