from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Author


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class AuthorDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.author1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.author2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Author.objects.all()), 0)
        Author.objects.create(**self.author1)
        x = Author.objects.get(pk=1)
        self.assertEqual(x.title, self.author1['title'])
        self.assertEqual(len(Author.objects.all()), 1)

    def test_test_edit(self):
        Author.objects.create(**self.author1)
        x = Author.objects.get(pk=1)
        x.title = self.author2['title']
        x.body = self.author2['body']
        x.save()
        self.assertEqual(x.title, self.author2['title'])
        self.assertEqual(x.body, self.author2['body'])
        self.assertEqual(len(Author.objects.all()), 1)

    def test_test_delete(self):
        Author.objects.create(**self.author1)
        b = Author.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Author.objects.all()), 0)


class AuthorViewsTest(TestCase):

    def login(self):
        username = self.user.username
        password = user_args()['password']
        response = self.client.login(username=username, password=password)
        self.assertEqual(response, True)

    def setUp(self):
        self.user = test_user()
        self.author1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.author2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('author_list'))

    def test_author_list_view(self):
        self.assertEqual(reverse('author_list'), '/author/')
        Author.objects.create(**self.author1)
        Author.objects.create(**self.author2)
        response = self.client.get('/author/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_author_detail_view(self):
        Author.objects.create(**self.author1)
        self.assertEqual(reverse('author_detail', args='1'), '/author/1')
        self.assertEqual(reverse('author_detail', args='2'), '/author/2')
        response = self.client.get(reverse('author_detail', args='1'))
        self.assertContains(response, 'body')

    def test_author_add_view(self):

        # Add without Login
        response = self.client.post(reverse('author_add'), self.author1)
        response = self.client.post(reverse('author_add'), self.author2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/author/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('author_add'), self.author1)
        response = self.client.post(reverse('author_add'), self.author2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Author.objects.all()), 2)

    def test_author_edit_view(self):

        # Edit without Login
        response = Author.objects.create(**self.author1)
        response = self.client.post(reverse('author_edit', args='1'), self.author2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/author/1/')

        # Login to edit
        self.login()
        response = self.client.post('/author/1/', self.author2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        author = Author.objects.get(pk=1)
        self.assertEqual(author.title, self.author2['title'])
        self.assertEqual(author.body, self.author2['body'])

    def test_author_delete_view(self):
        self.login()
        Author.objects.create(**self.author1)
        self.assertEqual(reverse('author_delete', args='1'), '/author/1/delete')
        response = self.client.post('/author/1/delete')
        self.assertEqual(len(Author.objects.all()), 0)
