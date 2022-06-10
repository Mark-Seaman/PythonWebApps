from django.contrib import admin
from .models import Author, Book, Chapter, Image

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Author)
admin.site.register(Image)
