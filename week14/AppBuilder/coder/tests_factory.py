from django.test import TestCase
from django.urls import reverse

from .models import Author, DataFactory
from coder.coder import create_test_user


class DataFactoryDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.factory1 = dict(name='Dickens', title='Tale of 2 Cities', author=self.author1,
                                     description='None', doc_path='Documents')
        self.factory2 = dict(name='Homer', title='Iliad', author=self.author2,
                                     description='None', doc_path='Documents')

    def test_add_factory(self):
        self.assertEqual(len(DataFactory.objects.all()), 0)
        DataFactory.create(**self.factory1)
        DataFactory.create(**self.factory2)
        x = DataFactory.objects.get(pk=2)
        self.assertEqual(str(x), '2 - Homer by 2 - Homer')
        self.assertEqual(x.author.name, 'Homer')
        self.assertEqual(x.title, 'Iliad')
        self.assertEqual(len(DataFactory.objects.all()), 2)

#     def test_factory_edit(self):
#         DataFactory.create(**self.factory1)
#         b = DataFactory.objects.get(pk=1)
#         b.author = self.author2
#         b.title = 'Iliad'
#         b.description = 'No description'
#         b.save()
#         self.assertEqual(b.title, 'Iliad')
#         self.assertEqual(b.author.name, 'Homer')
#         self.assertEqual(b.description, 'No description')

#     def test_factory_delete(self):
#         DataFactory.objects.create(**self.factory1)
#         b = DataFactory.objects.get(pk=1)
#         b.delete()
#         self.assertEqual(len(DataFactory.objects.all()), 0)


# class DataFactoryViewsTest(TestCase):

#     def login(self):
#         response = self.client.login(username=self.user.username,  password=self.user_args['password'])
#         self.assertEqual(response, True)

#     def setUp(self):
#         self.user, self.user_args = create_test_user()
#         self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
#         self.author2 = Author.objects.create(user=self.user, name='Homer')
#         self.factory1 = dict(name='BACS 200',
#                                      title='UNC BACS 200',
#                                      subtitle='Subtitle UNC BACS 200',
#                                      author=self.author1,
#                                      description='description',
#                                      doc_path='Documents/factory/bacs200',
#                                      num_projects=14,
#                                      num_lessons=42)
#         self.factory2 = dict(name='BACS 350',
#                                      title='UNC BACS 350',
#                                      subtitle='Subtitle UNC BACS 350',
#                                      author=self.author1,
#                                      description='None',
#                                      doc_path='Documents/factory/bacs350',
#                                      num_projects=14,
#                                      num_lessons=42)

#     def test_home(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, reverse('factory_list'))

#     def test_factory_list_view(self):
#         self.assertEqual(reverse('factory_list'), '/factory/')
#         DataFactory.objects.create(**self.factory1)
#         DataFactory.objects.create(**self.factory2)
#         response = self.client.get('/factory/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'factory_list.html')
#         self.assertTemplateUsed(response, 'theme.html')
#         self.assertContains(response, '<tr>', count=3)

#     def test_factory_detail_view(self):
#         DataFactory.objects.create(**self.factory1)
#         self.assertEqual(reverse('factory_detail', args='1'), '/factory/1')
#         self.assertEqual(reverse('factory_detail', args='2'), '/factory/2')
#         response = self.client.get(reverse('factory_detail', args='1'))
#         self.assertContains(response, 'BACS 200')

#     def test_factory_add_view(self):

#         # Add without Login
#         response = self.client.post(reverse('factory_add'), self.factory1)
#         self.assertEqual(response.url, '/accounts/login/?next=/factory/add')
#         self.assertEqual(len(DataFactory.objects.all()), 0)

#         # Login to add
#         self.login()
#         response = self.client.post(reverse('factory_add'), self.factory1)
#         response = self.client.post(reverse('factory_add'), self.factory2)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/factory/2')
#         response = self.client.get('/factory/')
#         self.assertEqual(len(DataFactory.objects.all()), 2)
#         response = self.client.get(reverse('factory_detail', args='2'))
#         self.assertContains(response, 'BACS 350')

#     def test_factory_edit_view(self):

#         # Edit without Login
#         DataFactory.objects.create(**self.factory1)
#         self.assertEqual(reverse('factory_edit', args='1'), '/factory/1/')
#         response = self.client.get('/factory/1/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/accounts/login/?next=/factory/1/')

#         # Login to edit
#         self.login()
#         response = self.client.post('/factory/1/', self.factory2)
#         self.assertEqual(response.url, '/factory/1')
#         response = self.client.get(response.url)
#         self.assertContains(response, self.factory2['title'])
#         self.assertContains(response, self.author1.name)

#         # Check the factory object
#         factory = DataFactory.objects.get(pk=1)
#         self.assertEqual(factory.author, self.author1)
#         self.assertEqual(factory.title, 'UNC BACS 350')

#     def test_factory_delete_view(self):
#         self.login()
#         DataFactory.objects.create(**self.factory1)
#         self.assertEqual(reverse('factory_delete', args='1'), '/factory/1/delete')
#         response = self.client.get('/factory/1/delete')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post('/factory/1/delete')
#         self.assertEqual(len(DataFactory.objects.all()), 0)
