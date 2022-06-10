from django.db import models
from django.urls.base import reverse_lazy


class Probe(models.Model):

    name = models.CharField(max_length=100)
    page = models.URLField()
    text = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.page}'

    def get_absolute_url(self):
        return reverse_lazy('probe_list')

    @staticmethod
    def create(**kwargs):
        c = Probe.objects.get_or_create(name=kwargs.get('name'))[0]
        c.page = kwargs.get('page')
        c.text = kwargs.get('text')
        c.save()
        return c


class Result(models.Model):

    probe = models.ForeignKey(Probe, on_delete=models.CASCADE, editable=False)
    date = models.DateTimeField(auto_now=True)
    output = models.TextField(default='Not yet run')
    passed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.probe.name} - {self.date} - {self.passed}'

    def get_absolute_url(self):
        return reverse_lazy('probe_list')

    @staticmethod
    def create(**kwargs):
        c = Result.objects.create(probe=kwargs.get('probe'))
        c.output = kwargs.get('output')
        c.passed = kwargs.get('passed')
        c.save()
        return c
