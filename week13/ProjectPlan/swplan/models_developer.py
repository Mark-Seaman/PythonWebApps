from django.db import models
from django.urls.base import reverse_lazy


class Developer(models.Model):
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('developer_detail', args=[str(self.id)])

    # @property
    # def dependents(self):
    #     return Dependents.objects.filter(parent=self)

