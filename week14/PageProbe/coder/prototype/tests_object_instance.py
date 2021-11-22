from django.test import TestCase
from django.urls import reverse

from object_instance.object_instance import create_bacs200, create_bacs350

from .models import Author, ClassObject, Lesson
from coder.coder import create_test_user


class ClassObjectDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.object_instance1 = dict(name='Dickens', title='Tale of 2 Cities', author=self.author1,
                            description='None', doc_path='Documents')
        self.object_instance2 = dict(name='Homer', title='Iliad', author=self.author2,
                            description='None', doc_path='Documents')

    def test_add_object_instance(self):
        self.assertEqual(len(ClassObject.objects.all()), 0)
        ClassObject.create(**self.object_instance1)
        ClassObject.create(**self.object_instance2)
        x = ClassObject.objects.get(pk=2)
        self.assertEqual(str(x), '2 - Homer by 2 - Homer')
        self.assertEqual(x.author.name, 'Homer')
        self.assertEqual(x.title, 'Iliad')
        self.assertEqual(len(ClassObject.objects.all()), 2)

    def test_object_instance_edit(self):
        ClassObject.create(**self.object_instance1)
        b = ClassObject.objects.get(pk=1)
        b.author = self.author2
        b.title = 'Iliad'
        b.description = 'No description'
        b.save()
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author.name, 'Homer')
        self.assertEqual(b.description, 'No description')

    def test_object_instance_delete(self):
        ClassObject.objects.create(**self.object_instance1)
        b = ClassObject.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(ClassObject.objects.all()), 0)


class ClassObjectViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.object_instance1 = dict(name='BACS 200',
                            title='UNC BACS 200',
                            subtitle='Subtitle UNC BACS 200',
                            author=self.author1,
                            description='description',
                            doc_path='Documents/object_instance/bacs200',
                            num_projects=14,
                            num_lessons=42)
        self.object_instance2 = dict(name='BACS 350',
                            title='UNC BACS 350',
                            subtitle='Subtitle UNC BACS 350',
                            author=self.author1,
                            description='None',
                            doc_path='Documents/object_instance/bacs350',
                            num_projects=14,
                            num_lessons=42)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('object_instance_list'))

    def test_object_instance_list_view(self):
        self.assertEqual(reverse('object_instance_list'), '/object_instance/')
        ClassObject.objects.create(**self.object_instance1)
        ClassObject.objects.create(**self.object_instance2)
        response = self.client.get('/object_instance/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'object_instance_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_object_instance_detail_view(self):
        ClassObject.objects.create(**self.object_instance1)
        self.assertEqual(reverse('object_instance_detail', args='1'), '/object_instance/1')
        self.assertEqual(reverse('object_instance_detail', args='2'), '/object_instance/2')
        response = self.client.get(reverse('object_instance_detail', args='1'))
        self.assertContains(response, 'BACS 200')

    def test_object_instance_add_view(self):

        # Add without Login
        response = self.client.post(reverse('object_instance_add'), self.object_instance1)
        self.assertEqual(response.url, '/accounts/login/?next=/object_instance/add')
        self.assertEqual(len(ClassObject.objects.all()), 0)

        # Login to add
        self.login()
        response = self.client.post(reverse('object_instance_add'), self.object_instance1)
        response = self.client.post(reverse('object_instance_add'), self.object_instance2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/object_instance/2')
        response = self.client.get('/object_instance/')
        self.assertEqual(len(ClassObject.objects.all()), 2)
        response = self.client.get(reverse('object_instance_detail', args='2'))
        self.assertContains(response, 'BACS 350')

    def test_object_instance_edit_view(self):

        # Edit without Login
        ClassObject.objects.create(**self.object_instance1)
        self.assertEqual(reverse('object_instance_edit', args='1'), '/object_instance/1/')
        response = self.client.get('/object_instance/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/object_instance/1/')

        # Login to edit
        self.login()
        response = self.client.post('/object_instance/1/', self.object_instance2)
        self.assertEqual(response.url, '/object_instance/1')
        response = self.client.get(response.url)
        self.assertContains(response, self.object_instance2['title'])
        self.assertContains(response, self.author1.name)

        # Check the object_instance object
        object_instance = ClassObject.objects.get(pk=1)
        self.assertEqual(object_instance.author, self.author1)
        self.assertEqual(object_instance.title, 'UNC BACS 350')

    def test_object_instance_delete_view(self):
        self.login()
        ClassObject.objects.create(**self.object_instance1)
        self.assertEqual(reverse('object_instance_delete', args='1'), '/object_instance/1/delete')
        response = self.client.get('/object_instance/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/object_instance/1/delete')
        self.assertEqual(len(ClassObject.objects.all()), 0)


class ClassObjectFixtureTest(TestCase):
    #     fixtures = ['Documents/Test/data.json']

    #     def test_with_data(self):
    #         self.assertEqual(len(Author.objects.all()), 0)
    #         self.assertEqual(len(ClassObject.objects.all()), 0)
    #         self.assertEqual(len(Lesson.objects.all()), 0)

    def test_import_object_instances(self):
        self.user, self.user_args = create_test_user()
        create_bacs200()
        create_bacs350()
        object_instance = ClassObject.objects.get(pk=1)
        self.assertEqual((object_instance.name, object_instance.author.name), ('bacs200', 'Mark Seaman'))
        self.assertEqual(len(ClassObject.objects.all()), 2)
    #     # print(Author.objects.all())
    #     # print(object_instance.objects.all())
    #     # print(Chapter.objects.all())
    #     self.assertEqual(len(Author.objects.all()), 3)
    #     self.assertEqual(len(Lesson.objects.all()), 70)
