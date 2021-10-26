from django.contrib.auth import get_user_model
from author.models import Author
from django.test import TestCase
from django.urls import reverse

from .models import Author


class AuthorDataTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_add_author(self):
        self.assertEqual(len(Author.objects.all()), 0)
        Author.objects.create(title='Tale of 2 Cities', author='Chuck Dickens')
        Author.objects.create(title='Iliad', author='Homer')
        self.assertEqual(len(Author.objects.all()), 2)

    def test_author_title(self):
        Author.objects.create(title='Iliad', author='Homer')
        b = Author.objects.get(pk=1)
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author, 'Homer')
        self.assertEqual(b.description, 'None')

    def test_author_edit(self):
        Author.objects.create(title='Iliad', author='Homer')
        b = Author.objects.get(pk=1)
        b.author = 'Mark Seaman'
        b.description = 'No description'
        b.save()
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author, 'Mark Seaman')
        self.assertEqual(b.description, 'No description')

    def test_author_delete(self):
        Author.objects.create(title='Iliad', author='Homer')
        b = Author.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Author.objects.all()), 0)

    def test_string_representation(self):
        author = Author.objects.create(title='Iliad', author='Homer')
        self.assertEqual(
            str(author), '1 - Iliad by Homer')


class AuthorViewsTest(TestCase):

    def login(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        user = get_user_model().objects.create_user(**args)
        response = self.client.login(username='TEST_DUDE', password='secret')
        self.assertEqual(response, True)

    def setUp(self):
        self.author = Author.objects.create(title='Iliad', author='Homer')

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('author_list'))

    def test_author_list_view(self):
        self.assertEqual(reverse('author_list'), '/author/')
        response = self.client.get('/author/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_author_detail_view(self):
        self.assertEqual(reverse('author_detail', args='1'), '/author/1')
        self.assertEqual(reverse('author_detail', args='2'), '/author/2')
        response = self.client.get(reverse('author_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_author_add_view(self):

        # Add without Login
        author = dict(title='Star Wars', author='Darth Vadar', description='None')
        response = self.client.post(reverse('author_add'), author)
        self.assertEqual(response.url, '/accounts/login/?next=/author/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('author_add'), author)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/author/2')

        # List the authors
        response = self.client.get('/author/')
        self.assertContains(response, '<tr>', count=3)

    def test_author_edit_view(self):

        # Edit without Login
        self.assertEqual(reverse('author_edit', args='1'), '/author/1/')
        response = self.client.get('/author/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/author/1/')

        # Login to edit
        self.login()
        author = dict(title='Oddessy', author='Homer', description='None')
        response = self.client.post('/author/1/', author)

        # Check the redirect
        self.assertEqual(response.url, '/author/1')
        response = self.client.get(response.url)
        self.assertContains(response, 'Homer')

        # Check the author object
        author = Author.objects.get(pk=1)
        self.assertEqual(author.author, 'Homer')
        self.assertEqual(author.title, 'Oddessy')

    def test_author_delete_view(self):
        self.login()
        self.assertEqual(reverse('author_delete', args='1'), '/author/1/delete')
        response = self.client.get('/author/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/author/1/delete')
        self.assertEqual(len(Author.objects.all()), 0)
