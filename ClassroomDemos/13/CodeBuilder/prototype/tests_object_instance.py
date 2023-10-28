from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import ClassName


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class ClassNameDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.object_instance1 = dict(user=self.user)
    #     ClassName.objects.create(**self.object_instance1)

    # def test_add(self):
    #     self.assertEqual(len(ClassName.objects.all()), 0)
    #     ClassName.objects.create(**self.object_instance1)
    #     x = ClassName.objects.get(pk=1)
    #     self.assertEqual(x.title, self.object_instance1['title'])
    #     self.assertEqual(len(ClassName.objects.all()), 1)
    #
    # def test_edit(self):
    #     ClassName.objects.create(**self.object_instance1)
    #     x = ClassName.objects.get(pk=1)
    #     x.title = self.object_instance2['title']
    #     x.body = self.object_instance2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.object_instance2['title'])
    #     self.assertEqual(x.body, self.object_instance2['body'])
    #     self.assertEqual(len(ClassName.objects.all()), 1)
    #
    # def test_delete(self):
    #     ClassName.objects.create(**self.object_instance1)
    #     b = ClassName.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(ClassName.objects.all()), 0)


class ClassNameViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.object_instance1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.object_instance2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('object_instance_list'))

    # def test_object_instance_list_view(self):
    #     self.assertEqual(reverse('object_instance_list'), '/object_instance/')
    #     ClassName.objects.create(**self.object_instance1)
    #     ClassName.objects.create(**self.object_instance2)
    #     response = self.client.get('/object_instance/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'object_instance_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_object_instance_detail_view(self):
    #     ClassName.objects.create(**self.object_instance1)
    #     self.assertEqual(reverse('object_instance_detail', args='1'), '/object_instance/1')
    #     self.assertEqual(reverse('object_instance_detail', args='2'), '/object_instance/2')
    #     response = self.client.get(reverse('object_instance_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_object_instance_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('object_instance_add'), self.object_instance1)
    #     response = self.client.post(reverse('object_instance_add'), self.object_instance2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/object_instance/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('object_instance_add'), self.object_instance1)
    #     response = self.client.post(reverse('object_instance_add'), self.object_instance2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(ClassName.objects.all()), 2)
    #
    # def test_object_instance_edit_view(self):
    #
    #     # Edit without Login
    #     response = ClassName.objects.create(**self.object_instance1)
    #     response = self.client.post(reverse('object_instance_edit', args='1'), self.object_instance2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/object_instance/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/object_instance/1/', self.object_instance2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     object_instance = ClassName.objects.get(pk=1)
    #     self.assertEqual(object_instance.title, self.object_instance2['title'])
    #     self.assertEqual(object_instance.body, self.object_instance2['body'])
    #
    # def test_object_instance_delete_view(self):
    #     self.login()
    #     ClassName.objects.create(**self.object_instance1)
    #     self.assertEqual(reverse('object_instance_delete', args='1'), '/object_instance/1/delete')
    #     response = self.client.post('/object_instance/1/delete')
    #     self.assertEqual(len(ClassName.objects.all()), 0)
