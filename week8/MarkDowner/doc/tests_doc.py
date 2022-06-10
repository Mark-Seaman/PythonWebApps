from django.test import TestCase
from django.urls import reverse

from .models import Document
from workshop.coder import create_test_user


class DocumentDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.doc1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.doc2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Document.objects.all()), 0)
        Document.objects.create(**self.doc1)
        x = Document.objects.get(pk=1)
        self.assertEqual(x.title, self.doc1['title'])
        self.assertEqual(len(Document.objects.all()), 1)

    def test_test_edit(self):
        Document.objects.create(**self.doc1)
        x = Document.objects.get(pk=1)
        x.title = self.doc2['title']
        x.body = self.doc2['body']
        x.save()
        self.assertEqual(x.title, self.doc2['title'])
        self.assertEqual(x.body, self.doc2['body'])
        self.assertEqual(len(Document.objects.all()), 1)

    def test_test_delete(self):
        Document.objects.create(**self.doc1)
        b = Document.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Document.objects.all()), 0)


class DocumentViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.doc1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.doc2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('doc_list'))

    def test_doc_list_view(self):
        self.assertEqual(reverse('doc_list'), '/doc/')
        Document.objects.create(**self.doc1)
        Document.objects.create(**self.doc2)
        response = self.client.get('/doc/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doc_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_doc_detail_view(self):
        Document.objects.create(**self.doc1)
        self.assertEqual(reverse('doc_detail', args='1'), '/doc/1')
        self.assertEqual(reverse('doc_detail', args='2'), '/doc/2')
        response = self.client.get(reverse('doc_detail', args='1'))
        self.assertContains(response, 'body')

    def test_doc_add_view(self):

        # Add without Login
        response = self.client.post(reverse('doc_add'), self.doc1)
        response = self.client.post(reverse('doc_add'), self.doc2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/doc/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('doc_add'), self.doc1)
        response = self.client.post(reverse('doc_add'), self.doc2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Document.objects.all()), 2)

    def test_doc_edit_view(self):

        # Edit without Login
        response = Document.objects.create(**self.doc1)
        response = self.client.post(reverse('doc_edit', args='1'), self.doc2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/doc/1/')

        # Login to edit
        self.login()
        response = self.client.post('/doc/1/', self.doc2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        doc = Document.objects.get(pk=1)
        self.assertEqual(doc.title, self.doc2['title'])
        self.assertEqual(doc.body, self.doc2['body'])

    def test_doc_delete_view(self):
        self.login()
        Document.objects.create(**self.doc1)
        self.assertEqual(reverse('doc_delete', args='1'), '/doc/1/delete')
        response = self.client.post('/doc/1/delete')
        self.assertEqual(len(Document.objects.all()), 0)
