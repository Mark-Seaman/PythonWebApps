from django.test import TestCase
from django.urls import reverse

from probe.probe import create_bacs200, create_bacs350

from .models import Author, Probe, Lesson
from coder.coder import create_test_user


class ProbeDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.probe1 = dict(name='Dickens', title='Tale of 2 Cities', author=self.author1,
                                     description='None', doc_path='Documents')
        self.probe2 = dict(name='Homer', title='Iliad', author=self.author2,
                                     description='None', doc_path='Documents')

    def test_add_probe(self):
        self.assertEqual(len(Probe.objects.all()), 0)
        Probe.create(**self.probe1)
        Probe.create(**self.probe2)
        x = Probe.objects.get(pk=2)
        self.assertEqual(str(x), '2 - Homer by 2 - Homer')
        self.assertEqual(x.author.name, 'Homer')
        self.assertEqual(x.title, 'Iliad')
        self.assertEqual(len(Probe.objects.all()), 2)

    def test_probe_edit(self):
        Probe.create(**self.probe1)
        b = Probe.objects.get(pk=1)
        b.author = self.author2
        b.title = 'Iliad'
        b.description = 'No description'
        b.save()
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author.name, 'Homer')
        self.assertEqual(b.description, 'No description')

    def test_probe_delete(self):
        Probe.objects.create(**self.probe1)
        b = Probe.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Probe.objects.all()), 0)


class ProbeViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.probe1 = dict(name='BACS 200',
                                     title='UNC BACS 200',
                                     subtitle='Subtitle UNC BACS 200',
                                     author=self.author1,
                                     description='description',
                                     doc_path='Documents/probe/bacs200',
                                     num_projects=14,
                                     num_lessons=42)
        self.probe2 = dict(name='BACS 350',
                                     title='UNC BACS 350',
                                     subtitle='Subtitle UNC BACS 350',
                                     author=self.author1,
                                     description='None',
                                     doc_path='Documents/probe/bacs350',
                                     num_projects=14,
                                     num_lessons=42)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('probe_list'))

    def test_probe_list_view(self):
        self.assertEqual(reverse('probe_list'), '/probe/')
        Probe.objects.create(**self.probe1)
        Probe.objects.create(**self.probe2)
        response = self.client.get('/probe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'probe_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_probe_detail_view(self):
        Probe.objects.create(**self.probe1)
        self.assertEqual(reverse('probe_detail', args='1'), '/probe/1')
        self.assertEqual(reverse('probe_detail', args='2'), '/probe/2')
        response = self.client.get(reverse('probe_detail', args='1'))
        self.assertContains(response, 'BACS 200')

    def test_probe_add_view(self):

        # Add without Login
        response = self.client.post(reverse('probe_add'), self.probe1)
        self.assertEqual(response.url, '/accounts/login/?next=/probe/add')
        self.assertEqual(len(Probe.objects.all()), 0)

        # Login to add
        self.login()
        response = self.client.post(reverse('probe_add'), self.probe1)
        response = self.client.post(reverse('probe_add'), self.probe2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/probe/2')
        response = self.client.get('/probe/')
        self.assertEqual(len(Probe.objects.all()), 2)
        response = self.client.get(reverse('probe_detail', args='2'))
        self.assertContains(response, 'BACS 350')

    def test_probe_edit_view(self):

        # Edit without Login
        Probe.objects.create(**self.probe1)
        self.assertEqual(reverse('probe_edit', args='1'), '/probe/1/')
        response = self.client.get('/probe/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/probe/1/')

        # Login to edit
        self.login()
        response = self.client.post('/probe/1/', self.probe2)
        self.assertEqual(response.url, '/probe/1')
        response = self.client.get(response.url)
        self.assertContains(response, self.probe2['title'])
        self.assertContains(response, self.author1.name)

        # Check the probe object
        probe = Probe.objects.get(pk=1)
        self.assertEqual(probe.author, self.author1)
        self.assertEqual(probe.title, 'UNC BACS 350')

    def test_probe_delete_view(self):
        self.login()
        Probe.objects.create(**self.probe1)
        self.assertEqual(reverse('probe_delete', args='1'), '/probe/1/delete')
        response = self.client.get('/probe/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/probe/1/delete')
        self.assertEqual(len(Probe.objects.all()), 0)
