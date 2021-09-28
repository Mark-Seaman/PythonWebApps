from django.test import TestCase
from .models import Book


class BookTest(TestCase):

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
