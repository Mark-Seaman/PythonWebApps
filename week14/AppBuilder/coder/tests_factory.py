from django.test import TestCase
from django.urls import reverse

from .models import DataFactory
from coder.coder import create_test_user


class DataFactoryDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.factory1 = dict(class_name='Book', object_name='book', module_name='book')
        self.factory2 = dict(class_name='Course', object_name='course', module_name='course')

    def test_factory_add(self):
        self.assertEqual(len(DataFactory.objects.all()), 0)
        DataFactory.create(**self.factory1)
        DataFactory.create(**self.factory2)
        x = DataFactory.objects.get(pk=1)
        self.assertEqual(x.module_name, self.factory1['module_name'])
        self.assertEqual(len(DataFactory.objects.all()), 2)

    def test_factory_edit(self):
        DataFactory.create(**self.factory1)
        x = DataFactory.objects.get(pk=1)
        x.module_name = self.factory2['module_name']
        x.save()
        self.assertEqual(x.module_name, self.factory2['module_name'])

    def test_factory_delete(self):
        DataFactory.objects.create(**self.factory1)
        b = DataFactory.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(DataFactory.objects.all()), 0)


class DataFactoryViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.factory1 = dict(class_name='Book', object_name='book', module_name='book')
        self.factory2 = dict(class_name='Course', object_name='course', module_name='course')

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('factory_list'))

    def test_factory_list_view(self):
        self.assertEqual(reverse('factory_list'), '/factory/')
        DataFactory.objects.create(**self.factory1)
        DataFactory.objects.create(**self.factory2)
        response = self.client.get('/factory/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'factory_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_factory_detail_view(self):
        DataFactory.objects.create(**self.factory1)
        self.assertEqual(reverse('factory_detail', args='1'), '/factory/1')
        self.assertEqual(reverse('factory_detail', args='2'), '/factory/2')
        response = self.client.get(reverse('factory_detail', args='1'))
        self.assertContains(response, 'Book')

    def test_factory_add_view(self):

        # Add without Login
        response = self.client.post(reverse('factory_add'), self.factory1)
        self.assertEqual(response.url, '/accounts/login/?next=/factory/add')
        self.assertEqual(len(DataFactory.objects.all()), 0)

        # Login to add
        self.login()
        response = self.client.post(reverse('factory_add'), self.factory1)
        response = self.client.post(reverse('factory_add'), self.factory2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/factory/')
        response = self.client.get('/factory/')
        self.assertEqual(len(DataFactory.objects.all()), 2)
        response = self.client.get(reverse('factory_detail', args='2'))
        self.assertContains(response, 'Course')

    def test_factory_edit_view(self):

        # Edit without Login
        DataFactory.objects.create(**self.factory1)
        self.assertEqual(reverse('factory_edit', args='1'), '/factory/1/')
        response = self.client.get('/factory/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/factory/1/')

        # Login to edit
        self.login()
        response = self.client.post('/factory/1/', self.factory2)
        self.assertEqual(response.url, '/factory/')
        f = DataFactory.objects.get(pk=1)
        self.assertEqual(f.class_name, self.factory2['class_name'])

    def test_factory_delete_view(self):
        self.login()
        DataFactory.objects.create(**self.factory1)
        self.assertEqual(reverse('factory_delete', args='1'), '/factory/1/delete')
        response = self.client.get('/factory/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/factory/1/delete')
        self.assertEqual(len(DataFactory.objects.all()), 0)
