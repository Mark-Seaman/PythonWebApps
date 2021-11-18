from django.contrib import admin
from .models import Author, Course, Lesson, Image

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Author)
admin.site.register(Image)
