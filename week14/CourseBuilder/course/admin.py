from django.contrib import admin
from .models import Author, Course, Chapter, Image

admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Author)
admin.site.register(Image)
