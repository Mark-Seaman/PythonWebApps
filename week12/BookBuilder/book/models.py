from django.db import models
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User


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


# --------------------
# Author
#
# user - login credentials for author
# name - name of author

class Author(models.Model):
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk} - {self.name}'


# --------------------
# Book
#
# title - title of the book
# author - name of author
# description - summary of the book

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    description = models.TextField(default='None')
    doc_path = models.CharField(max_length=200, default='Documents')

    def __str__(self):
        return f'{self.pk} - {self.title} by {self.author}'

    def get_absolute_url(self):
        return reverse_lazy('book_detail', args=[str(self.id)])


# --------------------
# Chapter
#
# book - points to book object
# order - chapter order
# title - title text of chapter
# markdown - markdown text
# html - HTML text from markdown
# document - path to markdown file

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, editable=False)
    order = models.IntegerField()
    title = models.CharField(max_length=200)
    markdown = models.TextField()
    html = models.TextField()
    document = models.CharField(max_length=200)

    def export_record(self):
        return [self.order, self.title, self.document]

    @staticmethod
    def import_record(book, values):
        c = Chapter.objects.get_or_create(book=book, order=values[0])[0]
        c.title = values[1]
        c.document = values[2]
        c.save()

    def __str__(self):
        return f'{self.book.title} - {self.order} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('chapter_list')


# --------------------
# Note
#
# chapter - points to chapter object
# author - creator of note
# title - title text of chapter
# text - markdown text

class Note(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.chapter.order} {self.chapter.book.title}'

    def get_absolute_url(self):
        return reverse_lazy('note_list')
