from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('author_detail', args=[str(self.id)])

    @property
    def books(self):
        return Book.objects.filter(author=self)

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @staticmethod
    def get_me(user):
        author = Author.objects.get_or_create(user=user)[0]
        if author.name == ' ':
            author.user.first_name = 'Unknown'
            author.user.last_name = 'User'
            author.user.save()
        return author


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('book_detail', args=[str(self.id)])

    # @property
    # def dependents(self):
    #     return Dependents.objects.filter(parent=self)

    # @property
    # def name(self):
    #     return self.user.first_name + ' ' + self.user.last_name


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('chapter_detail', args=[str(self.id)])

    # @property
    # def dependents(self):
    #     return Dependents.objects.filter(parent=self)
