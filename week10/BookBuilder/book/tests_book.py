from django.contrib.auth import get_user_model
from book.models import Book
from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookDataTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_add_book(self):
        self.assertEqual(len(Book.objects.all()), 0)
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

    def login(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        user = get_user_model().objects.create_user(**args)
        response = self.client.login(username='TEST_DUDE', password='secret')
        self.assertEqual(response, True)

    def setUp(self):
        self.book1 = dict(title='Iliad', author='Homer', description='description')
        self.book2 = dict(title='Star Wars', author='Darth Vadar', description='None')

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('book_list'))

    def test_book_list_view(self):
        self.assertEqual(reverse('book_list'), '/book/')
        Book.objects.create(**self.book1)
        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_book_detail_view(self):
        Book.objects.create(**self.book1)
        self.assertEqual(reverse('book_detail', args='1'), '/book/1')
        self.assertEqual(reverse('book_detail', args='2'), '/book/2')
        response = self.client.get(reverse('book_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_book_add_view(self):
        Book.objects.create(**self.book1)

        # Add without Login
        response = self.client.post(reverse('book_add'), self.book1)
        self.assertEqual(response.url, '/accounts/login/?next=/book/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('book_add'), self.book2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/book/2')

        # List the books
        response = self.client.get('/book/')
        self.assertContains(response, '<tr>', count=3)

    def test_book_edit_view(self):
        Book.objects.create(**self.book1)

        # Edit without Login
        self.assertEqual(reverse('book_edit', args='1'), '/book/1/')
        response = self.client.get('/book/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/book/1/')

        # Login to edit
        self.login()
        response = self.client.post('/book/1/', self.book2)

        # Check the redirect
        self.assertEqual(response.url, '/book/1')
        response = self.client.get(response.url)
        self.assertContains(response, 'Darth Vadar')

        # Check the book object
        book = Book.objects.get(pk=1)
        self.assertEqual(book.author, 'Darth Vadar')
        self.assertEqual(book.title, 'Star Wars')

    def test_book_delete_view(self):
        Book.objects.create(**self.book1)

        self.login()
        self.assertEqual(reverse('book_delete', args='1'), '/book/1/delete')
        response = self.client.get('/book/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/book/1/delete')
        self.assertEqual(len(Book.objects.all()), 0)
