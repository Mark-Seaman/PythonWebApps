from django.test import TestCase
from .models import Book


class BookTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_num_book(self):
        self.assertEqual(len(Book.objects.all()), 0)

    def test_add_book(self):
        Book.objects.create(title='Tale of 2 Cities', author='Chuck Dickens')
        self.assertEqual(len(Book.objects.all()), 1)
