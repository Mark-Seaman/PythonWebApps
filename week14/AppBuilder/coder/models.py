from django.db import models
from django.urls.base import reverse_lazy


class DataFactory(models.Model):

    class_name = models.CharField(max_length=20)
    object_name = models.CharField(max_length=20)
    module_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.class_name}'

    def get_absolute_url(self):
        return reverse_lazy('factory_list')

    @staticmethod
    def create(**kwargs):
        class_name = kwargs.get('class_name')
        object_name = kwargs.get('object_name')
        module_name = kwargs.get('module_name')
        x = DataFactory.objects.get_or_create(class_name=class_name,
                                              object_name=object_name,
                                              module_name=module_name)[0]
        return x
