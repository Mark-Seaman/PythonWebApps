<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Author


def create_test_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class AuthorDataTest(TestCase):

    def setUp(self):
        self.user1 = dict(username='TESTER1', email='test1@test.us', password='secret 1')
        self.user2 = dict(username='TESTER2', email='test2@test.us', password='secret 2')
        self.author1 = dict(user=create_test_user(**self.user1), title='test author 1', notes='notes 1')
        self.author2 = dict(user=create_test_user(**self.user2), title='test author 2', notes='notes 2')

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
        x.notes = self.author2['notes']
        x.save()

        self.assertEqual(x.title, self.author2['title'])
        self.assertEqual(x.notes, self.author2['notes'])
        self.assertEqual(len(Author.objects.all()), 1)

    def test_test_delete(self):
        Author.objects.create(**self.author1)
        b = Author.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Author.objects.all()), 0)


class AuthorViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user1['username'],  password=self.user1['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user1 = dict(username='TESTER 1', email='test1@test.us', password='secret 1')
        self.user2 = dict(username='TESTER 2', email='test2@test.us', password='secret 2')
        self.author1 = dict(user=create_test_user(**self.user1), title='test author 1', notes='notes 1')
        self.author2 = dict(user=create_test_user(**self.user2), title='test author 2', notes='notes 2')

    def test_author_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('author_list'))
        Author.objects.create(**self.author1)
        self.login()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/author/1')

    def test_author_list_view(self):
        self.assertEqual(reverse('author_list'), '/author/')
        Author.objects.create(**self.author1)
        Author.objects.create(**self.author2)
        response = self.client.get('/author/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)
    #

    def test_author_detail_view(self):
        Author.objects.create(**self.author1)
        self.assertEqual(reverse('author_detail', args='1'), '/author/1')
        self.assertEqual(reverse('author_detail', args='2'), '/author/2')
        response = self.client.get(reverse('author_detail', args='1'))
        self.assertContains(response, self.author1["title"])

    # def test_author_add_view(self):

    #     # Add without Login
    #     response = self.client.post(reverse('author_add'), self.author1)
    #     response = self.client.post(reverse('author_add'), self.author2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/author/add')
    #     self.assertEqual(len(Author.objects.all()), 0)

    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('author_add'), self.author1)
    #     response = self.client.post(reverse('author_add'), self.author2)
    #     # self.assertEqual(response.status_code, 302)
    #     # response = self.client.get(response.url)
    #     # self.assertEqual(len(Author.objects.all()), 2)

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
        self.assertEqual(author.notes, self.author2['notes'])
    #

    def test_author_delete_view(self):
        Author.objects.create(**self.author1)
        self.login()
        self.assertEqual(reverse('author_delete', args='1'), '/author/1/delete')
        response = self.client.post('/author/1/delete')
        self.assertEqual(len(Author.objects.all()), 0)
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> ba095
