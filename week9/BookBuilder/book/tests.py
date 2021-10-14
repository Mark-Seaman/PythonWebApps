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
        self.assertEqual(b.description, 'None')

    def test_book_edit(self):
        Book.objects.create(title='Iliad', author='Homer')
        b = Book.objects.get(pk=1)
        b.author = 'Mark Seaman'
        b.description = 'No description'
        b.save()
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author, 'Mark Seaman')
        self.assertEqual(b.description, 'No description')

    def test_book_delete(self):
        Book.objects.create(title='Iliad', author='Homer')
        b = Book.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Book.objects.all()), 0)

    def test_string_representation(self):
        book = Book.objects.create(title='Iliad', author='Homer')
        self.assertEqual(
            str(book), '1 - Iliad by Homer')


class BookViewsTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(title='Iliad', author='Homer')

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_get_absolute_url(self):
        self.assertEqual(self.book.get_absolute_url(), '/book/1')

    def test_book_list_view(self):
        self.assertEqual(reverse('book_list'), '/book/')
        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<td>', count=4)

    def test_book_detail_view(self):
        self.assertEqual(reverse('book_detail', args='2'), '/book/2')
        response = self.client.get('/book/1')
        self.assertEqual(response.status_code, 200)

    def test_book_add_view(self):
        self.assertEqual(reverse('book_add'), '/book/add')
        response = self.client.get('/book/add')
        self.assertEqual(response.status_code, 200)
        content = dict(title='Life at Home', author='Darth Vadar')
        response = self.client.post('/book/add', content)
        response = self.client.get('/book/')
        self.assertContains(response, '<td>', count=8)

    def test_book_edit_view(self):
        self.assertEqual(reverse('book_edit', args='2'), '/book/2/')
        response = self.client.get('/book/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Homer')
        contents = dict(title='Life at Home', author='Darth Vadar')
        response = self.client.post('/book/1/', contents)
        book = Book.objects.get(pk=1)
        self.assertEqual(book.author, 'Darth Vadar')

    def test_book_delete_view(self):
        self.assertEqual(reverse('book_delete', args='2'), '/book/2/delete')
        response = self.client.get('/book/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/book/1/delete')
        self.assertEqual(len(Book.objects.all()), 0)
