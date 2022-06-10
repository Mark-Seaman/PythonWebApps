from django.contrib.auth import get_user_model
from book.models import Author
from django.test import TestCase
from django.urls import reverse

from .models import Author
from book.book import create_test_user


class AuthorDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = dict(user=self.user, name='Chuck Dickens')
        self.author2 = dict(user=self.user, name='Homer')

    def test_add_author(self):
        self.assertEqual(len(Author.objects.all()), 0)
        Author.objects.create(**self.author1)
        Author.objects.create(**self.author2)
        self.assertEqual(len(Author.objects.all()), 2)

        b = Author.objects.get(pk=2)
        self.assertEqual(b.name, 'Homer')
        self.assertEqual(b.user.username, 'TEST_DUDE')

    def test_author_edit(self):
        Author.objects.create(**self.author1)
        Author.objects.create(**self.author2)
        b = Author.objects.get(pk=1)
        b.name = 'Mark Seaman'
        b.save()
        b = Author.objects.get(pk=1)
        self.assertEqual(b.name, 'Mark Seaman')

    def test_author_delete(self):
        Author.objects.create(**self.author1)
        Author.objects.create(**self.author2)
        b = Author.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Author.objects.all()), 1)


class AuthorViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = dict(user=self.user, name='Chuck Dickens')
        self.author2 = dict(user=self.user, name='Homer')

    def test_author_list_view(self):
        Author.objects.create(**self.author1)
        Author.objects.create(**self.author2)
        self.assertEqual(reverse('author_list'), '/author/')
        response = self.client.get('/author/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_author_detail_view(self):
        Author.objects.create(**self.author1)
        self.assertEqual(reverse('author_detail', args='1'), '/author/1')
        response = self.client.get(reverse('author_detail', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_detail.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, 'Dickens')

    def test_author_add_view(self):

        # Add without Login
        response = self.client.post(reverse('author_add'), self.author1)
        self.assertEqual(response.url, '/accounts/login/?next=/author/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('author_add'), self.author1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/author/')

        # List the authors
        response = self.client.get('/author/')
        self.assertContains(response, '<tr>', count=2)

    def test_author_edit_view(self):

        # Edit without Login
        self.assertEqual(reverse('author_edit', args='1'), '/author/1/')
        response = self.client.get('/author/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/author/1/')

        # Login to edit
        self.login()
        response = self.client.post(reverse('author_add'), self.author1)
        response = self.client.post('/author/1/', self.author2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertContains(response, 'Homer')

    def test_author_delete_view(self):
        Author.objects.create(**self.author1)
        Author.objects.create(**self.author2)
        self.login()
        self.assertEqual(reverse('author_delete', args='1'), '/author/1/delete')
        response = self.client.get('/author/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/author/1/delete')
        self.assertEqual(len(Author.objects.all()), 1)
