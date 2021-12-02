from django.test import TestCase
from django.urls import reverse

from .models import Document
from .models import Document
from coder.coder import create_test_user


class DocumentDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.document1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.document2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Document.objects.all()), 0)
        Document.objects.create(**self.document1)
        x = Document.objects.get(pk=1)
        self.assertEqual(x.title, self.document1['title'])
        self.assertEqual(len(Document.objects.all()), 1)

    def test_test_edit(self):
        Document.objects.create(**self.document1)
        x = Document.objects.get(pk=1)
        x.title = self.document2['title']
        x.body = self.document2['body']
        x.save()
        self.assertEqual(x.title, self.document2['title'])
        self.assertEqual(x.body, self.document2['body'])
        self.assertEqual(len(Document.objects.all()), 1)

    def test_test_delete(self):
        Document.objects.create(**self.document1)
        b = Document.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Document.objects.all()), 0)


class DocumentViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.document1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.document2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('document_list'))

    def test_document_list_view(self):
        self.assertEqual(reverse('document_list'), '/document/')
        Document.objects.create(**self.document1)
        Document.objects.create(**self.document2)
        response = self.client.get('/document/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'document_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_document_detail_view(self):
        Document.objects.create(**self.document1)
        self.assertEqual(reverse('document_detail', args='1'), '/document/1')
        self.assertEqual(reverse('document_detail', args='2'), '/document/2')
        response = self.client.get(reverse('document_detail', args='1'))
        self.assertContains(response, 'body')

    def test_document_add_view(self):

        # Add without Login
        response = self.client.post(reverse('document_add'), self.document1)
        response = self.client.post(reverse('document_add'), self.document2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/document/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('document_add'), self.document1)
        response = self.client.post(reverse('document_add'), self.document2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Document.objects.all()), 2)

    def test_document_edit_view(self):

        # Edit without Login
        response = Document.objects.create(**self.document1)
        response = self.client.post(reverse('document_edit', args='1'), self.document2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/document/1/')

        # Login to edit
        self.login()
        response = self.client.post('/document/1/', self.document2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        document = Document.objects.get(pk=1)
        self.assertEqual(document.title, self.document2['title'])
        self.assertEqual(document.body, self.document2['body'])

    def test_document_delete_view(self):
        self.login()
        Document.objects.create(**self.document1)
        self.assertEqual(reverse('document_delete', args='1'), '/document/1/delete')
        response = self.client.post('/document/1/delete')
        self.assertEqual(len(Document.objects.all()), 0)
