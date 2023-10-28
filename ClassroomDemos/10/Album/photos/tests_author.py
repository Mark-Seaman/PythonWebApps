from django.contrib.auth.models import User
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
        self.author = dict(user=self.user, bio='single tester')

    def test_add_test(self):
        self.assertEqual(len(Author.objects.all()), 0)
        Author.objects.create(**self.author)
        x = Author.objects.get(pk=1)
        self.assertEqual(x.user.username, self.author['user'].username)
        self.assertEqual(x.bio, self.author['bio'])
        self.assertEqual(len(Author.objects.all()), 1)

    def test_user_edit(self):
        user = User.objects.get(pk=1)
        user.first_name = 'First'
        user.last_name = 'Last'
        user.email = 'user@a.us'
        user.save()
        user = User.objects.get(pk=1)
        self.assertEqual(user.email, 'user@a.us')

    def test_edit(self):
        Author.objects.create(**self.author)
        x = Author.objects.get(pk=1)
        x.bio = 'new tester'
        x.save()
        self.assertEqual(x.user.username, self.author['user'].username)
        self.assertEqual(x.bio, 'new tester')
        self.assertEqual(len(Author.objects.all()), 1)

    def test_delete(self):
        Author.objects.create(**self.author)
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
        self.author = dict(user=self.user, bio='single tester')
        self.author2 = dict(user=self.user, bio='new tester')

    def test_author_list_view(self):
        self.assertEqual(reverse('author_list'), '/author/')
        Author.objects.create(**self.author)
        response = self.client.get('/author/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_author_detail_view(self):
        Author.objects.create(**self.author)
        self.assertEqual(reverse('author_detail', args='1'), '/author/1')
        response = self.client.get(reverse('author_detail', args='1'))
        self.assertContains(response, 'body')

    def test_author_add_view(self):
        # Login to create Author
        self.login()
        response = self.client.get('/author/home')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/author/1')
        self.assertEqual(len(Author.objects.all()), 1)

    def test_author_home(self):
        # Annonymous should show Articles
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'author/home')
        response = self.client.get('/author/home')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/author/')
        self.assertEqual(len(Author.objects.all()), 0)

    def test_user_edit_view(self):
        # Edit without Login
        user_args = dict(first_name='First', last_name='Last', email='user@a.us', username='TESTER', password='secret')
        response = self.client.post(reverse('user_edit', args='1'), user_args)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/user/1/')
        self.assertEqual(User.objects.get(pk=1).email, 'test@test.us')

        # Login to edit
        self.login()
        response = self.client.post('/accounts/1/', user_args)
        self.assertEqual(User.objects.get(pk=1).email, 'test@test.us')

    def test_author_edit_view(self):
        # Edit without Login
        response = Author.objects.create(**self.author)
        response = self.client.post(reverse('author_edit', args='1'), self.author)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/author/1/')

        # Login to edit
        self.login()
        response = self.client.post('/author/1/', self.author2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        author = Author.objects.get(pk=1)
        self.assertEqual(author.bio, self.author2['bio'])

    def test_author_delete_view(self):
        self.login()
        Author.objects.create(**self.author)
        self.assertEqual(reverse('author_delete', args='1'), '/author/1/delete')
        response = self.client.post('/author/1/delete')
        self.assertEqual(len(Author.objects.all()), 0)
