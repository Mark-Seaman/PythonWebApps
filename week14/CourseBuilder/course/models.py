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
    folder = models.CharField(max_length=100, default='course')
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
# Course
#
# name - identity of course

class Course(models.Model):
    name = models.CharField(max_length=20, default='XXX')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False, default=1)
    description = models.TextField(default='No Description is Set')
    doc_path = models.CharField(max_length=200, default='Documents')
    num_projects = models.IntegerField(default=14)
    num_lessons = models.IntegerField(default=42)

    def __str__(self):
        return f'{self.pk} - {self.name} by {self.author}'

    def get_absolute_url(self):
        return reverse_lazy('course_detail', args=[str(self.id)])

    @staticmethod
    def create(**kwargs):
        c = Course.objects.get_or_create(name=kwargs.get('name'))[0]
        c.title = kwargs.get('title')
        c.subtitle = kwargs.get('subtitle')
        c.author = kwargs.get('author', 1)
        c.doc_path = kwargs.get('doc_path')
        c.description = kwargs.get('description')
        c.num_projects = kwargs.get('num_projects', 14)
        c.num_lessons = kwargs.get('num_lessons', 42)
        c.save()
        return c


# --------------------
# Lesson
#
# course - points to course object
# order - chapter order
# title - title text of chapter
# markdown - markdown text
# html - HTML text from markdown
# document - path to markdown file


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, editable=False)
    order = models.IntegerField()
    title = models.CharField(max_length=200)
    markdown = models.TextField()
    html = models.TextField()
    document = models.CharField(max_length=200)

    def export_record(self):
        return [self.order, self.title, self.document]

    @staticmethod
    def import_record(course, values):
        Lesson.create(course, values[0], values[1], values[2])

    @staticmethod
    def create(course, order, title, document):
        c = Lesson.objects.get_or_create(course=course, order=order)[0]
        c.title = title
        c.document = document
        c.save()
        return c

    def __str__(self):
        return f'{self.course.title} - {self.order} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('lesson_list')


# --------------------
# Note
#
# chapter - points to chapter object
# author - creator of note
# title - title text of chapter
# text - markdown text

class Note(models.Model):
    chapter = models.ForeignKey(Lesson, on_delete=models.CASCADE, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.chapter.order} {self.chapter.course.title}'

    def get_absolute_url(self):
        return reverse_lazy('note_list')
