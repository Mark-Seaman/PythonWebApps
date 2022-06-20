from django.contrib.auth import get_user_model
from os.path import exists
from markdown import markdown

from book.models import Author, Book, Chapter


def create_book(**kwargs):
    title = kwargs.get('title')
    author = kwargs.get('author')
    book = Book.objects.get_or_create(title=title, author=author)[0]
    book.doc_path = kwargs.get('doc_path')
    book.description = kwargs.get('description')
    book.save()
    return book


def create_author(name):
    user = get_user_model().objects.get(pk=1)
    return Author.objects.get_or_create(name=name, user=user)[0]


def get_author(name):
    return Author.objects.get(name=name)


def get_book(title):
    return Book.objects.get(title=title)


def get_chapter(book, order):
    c = Chapter.objects.get(book=book, order=order)
    c.markdown = open(f'{book.doc_path}/{c.document}').read()
    c.html = markdown(c.markdown)
    c.save()
    return c
