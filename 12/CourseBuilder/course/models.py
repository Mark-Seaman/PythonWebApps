from django.db import models
from django.urls.base import reverse_lazy


class Lesson(models.Model):
    title = models.CharField(max_length=200, default='No title')

    @property
    def document(self):
        return f'Documents/{int(self.pk):02}.md'

    @property
    def url(self):
        return f'/lesson/{self.pk}'

    @staticmethod
    def lessons(course):
        return Lesson.objects.all())

    def __str__(self):
        return f'{self.pk} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('lesson_list')
