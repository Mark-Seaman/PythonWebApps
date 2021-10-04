from book.models import Book
from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookCRUDTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_num_book(self):
        self.assertEqual(len(Book.objects.all()), 0)

    def test_add_book(self):
        Book.objects.create(title='Tale of 2 Cities', author='Chuck Dickens')
        Book.objects.create(title='Iliad', author='Homer')
        self.assertEqual(len(Book.objects.all()), 2)

    def test_book_title(self):
        Book.objects.create(title='Iliad', author='Homer')
        b = Book.objects.get(pk=1)
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author, 'Homer')

    def test_book_edit(self):
        Book.objects.create(title='Iliad', author='Homer')
        b = Book.objects.get(pk=1)
        b.author = 'Mark Seaman'
        b.save()
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author, 'Mark Seaman')

    def test_book_edit(self):
        Book.objects.create(title='Iliad', author='Homer')
        b = Book.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Book.objects.all()), 0)

    def test_string_representation(self):
        book = Book.objects.create(title='Iliad', author='Homer')
        self.assertEqual(
            str(book), '1 - Iliad by Homer')


class BookViewsTest(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_get_absolute_url(self):
        book = Book.objects.create(title='Iliad', author='Homer')
        self.assertEqual(book.get_absolute_url(), '/book/1')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_view(self):
        response = self.client.get('/book/')
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertTemplateUsed(response, 'book_theme.html')
