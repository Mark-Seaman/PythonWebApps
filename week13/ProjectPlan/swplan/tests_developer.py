from django.test import TestCase
from django.urls import reverse

from .models import Developer
from .test_util import create_test_user


class DeveloperDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.developer1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.developer2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Developer.objects.all()), 0)
        Developer.objects.create(**self.developer1)
        x = Developer.objects.get(pk=1)
        self.assertEqual(x.title, self.developer1['title'])
        self.assertEqual(len(Developer.objects.all()), 1)

    def test_test_edit(self):
        Developer.objects.create(**self.developer1)
        x = Developer.objects.get(pk=1)
        x.title = self.developer2['title']
        x.body = self.developer2['body']
        x.save()
        self.assertEqual(x.title, self.developer2['title'])
        self.assertEqual(x.body, self.developer2['body'])
        self.assertEqual(len(Developer.objects.all()), 1)

    def test_test_delete(self):
        Developer.objects.create(**self.developer1)
        b = Developer.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Developer.objects.all()), 0)


class DeveloperViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.developer1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.developer2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('developer_list'))

    def test_developer_list_view(self):
        self.assertEqual(reverse('developer_list'), '/developer/')
        Developer.objects.create(**self.developer1)
        Developer.objects.create(**self.developer2)
        response = self.client.get('/developer/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'developer_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_developer_detail_view(self):
        Developer.objects.create(**self.developer1)
        self.assertEqual(reverse('developer_detail', args='1'), '/developer/1')
        self.assertEqual(reverse('developer_detail', args='2'), '/developer/2')
        response = self.client.get(reverse('developer_detail', args='1'))
        self.assertContains(response, 'body')

    def test_developer_add_view(self):

        # Add without Login
        response = self.client.post(reverse('developer_add'), self.developer1)
        response = self.client.post(reverse('developer_add'), self.developer2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/developer/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('developer_add'), self.developer1)
        response = self.client.post(reverse('developer_add'), self.developer2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Developer.objects.all()), 2)

    def test_developer_edit_view(self):

        # Edit without Login
        response = Developer.objects.create(**self.developer1)
        response = self.client.post(reverse('developer_edit', args='1'), self.developer2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/developer/1/')

        # Login to edit
        self.login()
        response = self.client.post('/developer/1/', self.developer2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        developer = Developer.objects.get(pk=1)
        self.assertEqual(developer.title, self.developer2['title'])
        self.assertEqual(developer.body, self.developer2['body'])

    def test_developer_delete_view(self):
        self.login()
        Developer.objects.create(**self.developer1)
        self.assertEqual(reverse('developer_delete', args='1'), '/developer/1/delete')
        response = self.client.post('/developer/1/delete')
        self.assertEqual(len(Developer.objects.all()), 0)
