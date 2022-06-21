from django.test import TestCase
from django.urls import reverse

from .models import Message
from .test_util import create_test_user


class MessageDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.Message1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.Message2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Message.objects.all()), 0)
        Message.objects.create(**self.Message1)
        x = Message.objects.get(pk=1)
        self.assertEqual(x.title, self.Message1['title'])
        self.assertEqual(len(Message.objects.all()), 1)

    def test_test_edit(self):
        Message.objects.create(**self.Message1)
        x = Message.objects.get(pk=1)
        x.title = self.Message2['title']
        x.body = self.Message2['body']
        x.save()
        self.assertEqual(x.title, self.Message2['title'])
        self.assertEqual(x.body, self.Message2['body'])
        self.assertEqual(len(Message.objects.all()), 1)

    def test_test_delete(self):
        Message.objects.create(**self.Message1)
        b = Message.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Message.objects.all()), 0)


class MessageViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.Message1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.Message2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('Message_list'))

    def test_Message_list_view(self):
        self.assertEqual(reverse('Message_list'), '/Message/')
        Message.objects.create(**self.Message1)
        Message.objects.create(**self.Message2)
        response = self.client.get('/Message/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Message_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_Message_detail_view(self):
        Message.objects.create(**self.Message1)
        self.assertEqual(reverse('Message_detail', args='1'), '/Message/1')
        self.assertEqual(reverse('Message_detail', args='2'), '/Message/2')
        response = self.client.get(reverse('Message_detail', args='1'))
        self.assertContains(response, 'body')

    def test_Message_add_view(self):

        # Add without Login
        response = self.client.post(reverse('Message_add'), self.Message1)
        response = self.client.post(reverse('Message_add'), self.Message2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/Message/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('Message_add'), self.Message1)
        response = self.client.post(reverse('Message_add'), self.Message2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Message.objects.all()), 2)

    def test_Message_edit_view(self):

        # Edit without Login
        response = Message.objects.create(**self.Message1)
        response = self.client.post(reverse('Message_edit', args='1'), self.Message2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/Message/1/')

        # Login to edit
        self.login()
        response = self.client.post('/Message/1/', self.Message2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        Message = Message.objects.get(pk=1)
        self.assertEqual(Message.title, self.Message2['title'])
        self.assertEqual(Message.body, self.Message2['body'])

    def test_Message_delete_view(self):
        self.login()
        Message.objects.create(**self.Message1)
        self.assertEqual(reverse('Message_delete', args='1'), '/Message/1/delete')
        response = self.client.post('/Message/1/delete')
        self.assertEqual(len(Message.objects.all()), 0)
