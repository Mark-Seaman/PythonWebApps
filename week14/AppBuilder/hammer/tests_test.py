from django.test import TestCase
from django.urls import reverse

from .models import Author, Test
from coder.coder import create_test_user


class TestDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.test1 = dict(name='Dickens', title='Tale of 2 Cities', author=self.author1,
                                     description='None', doc_path='Documents')
        self.test2 = dict(name='Homer', title='Iliad', author=self.author2,
                                     description='None', doc_path='Documents')

    def test_add_test(self):
        self.assertEqual(len(Test.objects.all()), 0)
        Test.create(**self.test1)
        Test.create(**self.test2)
        x = Test.objects.get(pk=2)
        self.assertEqual(str(x), '2 - Homer by 2 - Homer')
        self.assertEqual(x.author.name, 'Homer')
        self.assertEqual(x.title, 'Iliad')
        self.assertEqual(len(Test.objects.all()), 2)

#     def test_test_edit(self):
#         Test.create(**self.test1)
#         b = Test.objects.get(pk=1)
#         b.author = self.author2
#         b.title = 'Iliad'
#         b.description = 'No description'
#         b.save()
#         self.assertEqual(b.title, 'Iliad')
#         self.assertEqual(b.author.name, 'Homer')
#         self.assertEqual(b.description, 'No description')

#     def test_test_delete(self):
#         Test.objects.create(**self.test1)
#         b = Test.objects.get(pk=1)
#         b.delete()
#         self.assertEqual(len(Test.objects.all()), 0)


# class TestViewsTest(TestCase):

#     def login(self):
#         response = self.client.login(username=self.user.username,  password=self.user_args['password'])
#         self.assertEqual(response, True)

#     def setUp(self):
#         self.user, self.user_args = create_test_user()
#         self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
#         self.author2 = Author.objects.create(user=self.user, name='Homer')
#         self.test1 = dict(name='BACS 200',
#                                      title='UNC BACS 200',
#                                      subtitle='Subtitle UNC BACS 200',
#                                      author=self.author1,
#                                      description='description',
#                                      doc_path='Documents/test/bacs200',
#                                      num_projects=14,
#                                      num_lessons=42)
#         self.test2 = dict(name='BACS 350',
#                                      title='UNC BACS 350',
#                                      subtitle='Subtitle UNC BACS 350',
#                                      author=self.author1,
#                                      description='None',
#                                      doc_path='Documents/test/bacs350',
#                                      num_projects=14,
#                                      num_lessons=42)

#     def test_home(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, reverse('test_list'))

#     def test_test_list_view(self):
#         self.assertEqual(reverse('test_list'), '/test/')
#         Test.objects.create(**self.test1)
#         Test.objects.create(**self.test2)
#         response = self.client.get('/test/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'test_list.html')
#         self.assertTemplateUsed(response, 'theme.html')
#         self.assertContains(response, '<tr>', count=3)

#     def test_test_detail_view(self):
#         Test.objects.create(**self.test1)
#         self.assertEqual(reverse('test_detail', args='1'), '/test/1')
#         self.assertEqual(reverse('test_detail', args='2'), '/test/2')
#         response = self.client.get(reverse('test_detail', args='1'))
#         self.assertContains(response, 'BACS 200')

#     def test_test_add_view(self):

#         # Add without Login
#         response = self.client.post(reverse('test_add'), self.test1)
#         self.assertEqual(response.url, '/accounts/login/?next=/test/add')
#         self.assertEqual(len(Test.objects.all()), 0)

#         # Login to add
#         self.login()
#         response = self.client.post(reverse('test_add'), self.test1)
#         response = self.client.post(reverse('test_add'), self.test2)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/test/2')
#         response = self.client.get('/test/')
#         self.assertEqual(len(Test.objects.all()), 2)
#         response = self.client.get(reverse('test_detail', args='2'))
#         self.assertContains(response, 'BACS 350')

#     def test_test_edit_view(self):

#         # Edit without Login
#         Test.objects.create(**self.test1)
#         self.assertEqual(reverse('test_edit', args='1'), '/test/1/')
#         response = self.client.get('/test/1/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/accounts/login/?next=/test/1/')

#         # Login to edit
#         self.login()
#         response = self.client.post('/test/1/', self.test2)
#         self.assertEqual(response.url, '/test/1')
#         response = self.client.get(response.url)
#         self.assertContains(response, self.test2['title'])
#         self.assertContains(response, self.author1.name)

#         # Check the test object
#         test = Test.objects.get(pk=1)
#         self.assertEqual(test.author, self.author1)
#         self.assertEqual(test.title, 'UNC BACS 350')

#     def test_test_delete_view(self):
#         self.login()
#         Test.objects.create(**self.test1)
#         self.assertEqual(reverse('test_delete', args='1'), '/test/1/delete')
#         response = self.client.get('/test/1/delete')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post('/test/1/delete')
#         self.assertEqual(len(Test.objects.all()), 0)
