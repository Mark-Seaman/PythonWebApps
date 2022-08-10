from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class BookDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.book1 = dict(user=self.user)
    #     Book.objects.create(**self.book1)

    # def test_add(self):
    #     self.assertEqual(len(Book.objects.all()), 0)
    #     Book.objects.create(**self.book1)
    #     x = Book.objects.get(pk=1)
    #     self.assertEqual(x.title, self.book1['title'])
    #     self.assertEqual(len(Book.objects.all()), 1)
    #
    # def test_edit(self):
    #     Book.objects.create(**self.book1)
    #     x = Book.objects.get(pk=1)
    #     x.title = self.book2['title']
    #     x.body = self.book2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.book2['title'])
    #     self.assertEqual(x.body, self.book2['body'])
    #     self.assertEqual(len(Book.objects.all()), 1)
    #
    # def test_delete(self):
    #     Book.objects.create(**self.book1)
    #     b = Book.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(Book.objects.all()), 0)


class BookViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.book1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.book2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('book_list'))

    # def test_book_list_view(self):
    #     self.assertEqual(reverse('book_list'), '/book/')
    #     Book.objects.create(**self.book1)
    #     Book.objects.create(**self.book2)
    #     response = self.client.get('/book/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'book_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_book_detail_view(self):
    #     Book.objects.create(**self.book1)
    #     self.assertEqual(reverse('book_detail', args='1'), '/book/1')
    #     self.assertEqual(reverse('book_detail', args='2'), '/book/2')
    #     response = self.client.get(reverse('book_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_book_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('book_add'), self.book1)
    #     response = self.client.post(reverse('book_add'), self.book2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/book/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('book_add'), self.book1)
    #     response = self.client.post(reverse('book_add'), self.book2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(Book.objects.all()), 2)
    #
    # def test_book_edit_view(self):
    #
    #     # Edit without Login
    #     response = Book.objects.create(**self.book1)
    #     response = self.client.post(reverse('book_edit', args='1'), self.book2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/book/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/book/1/', self.book2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     book = Book.objects.get(pk=1)
    #     self.assertEqual(book.title, self.book2['title'])
    #     self.assertEqual(book.body, self.book2['body'])
    #
    # def test_book_delete_view(self):
    #     self.login()
    #     Book.objects.create(**self.book1)
    #     self.assertEqual(reverse('book_delete', args='1'), '/book/1/delete')
    #     response = self.client.post('/book/1/delete')
    #     self.assertEqual(len(Book.objects.all()), 0)
