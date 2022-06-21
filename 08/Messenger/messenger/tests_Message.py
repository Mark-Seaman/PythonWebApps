from django.test import TestCase
from django.urls import reverse

from .models import Message
from .test_util import create_test_user


class MessageDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.message1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.message2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Message.objects.all()), 0)
        Message.objects.create(**self.message1)
        x = Message.objects.get(pk=1)
        self.assertEqual(x.title, self.message1['title'])
        self.assertEqual(len(Message.objects.all()), 1)

    def test_test_edit(self):
        Message.objects.create(**self.message1)
        x = Message.objects.get(pk=1)
        x.title = self.message2['title']
        x.body = self.message2['body']
        x.save()
        self.assertEqual(x.title, self.message2['title'])
        self.assertEqual(x.body, self.message2['body'])
        self.assertEqual(len(Message.objects.all()), 1)

    def test_test_delete(self):
        Message.objects.create(**self.message1)
        b = Message.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Message.objects.all()), 0)


class MessageViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.message1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.message2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('message_list'))

    def test_message_list_view(self):
        self.assertEqual(reverse('message_list'), '/message/')
        Message.objects.create(**self.message1)
        Message.objects.create(**self.message2)
        response = self.client.get('/message/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'message_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_message_detail_view(self):
        Message.objects.create(**self.message1)
        self.assertEqual(reverse('message_detail', args='1'), '/message/1')
        self.assertEqual(reverse('message_detail', args='2'), '/message/2')
        response = self.client.get(reverse('message_detail', args='1'))
        self.assertContains(response, 'body')

    def test_message_add_view(self):

        # Add without Login
        response = self.client.post(reverse('message_add'), self.message1)
        response = self.client.post(reverse('message_add'), self.message2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/message/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('message_add'), self.message1)
        response = self.client.post(reverse('message_add'), self.message2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Message.objects.all()), 2)

    def test_message_edit_view(self):

        # Edit without Login
        response = Message.objects.create(**self.message1)
        response = self.client.post(reverse('message_edit', args='1'), self.message2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/message/1/')

        # Login to edit
        self.login()
        response = self.client.post('/message/1/', self.message2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        message = Message.objects.get(pk=1)
        self.assertEqual(message.title, self.message2['title'])
        self.assertEqual(message.body, self.message2['body'])

    def test_message_delete_view(self):
        self.login()
        Message.objects.create(**self.message1)
        self.assertEqual(reverse('message_delete', args='1'), '/message/1/delete')
        response = self.client.post('/message/1/delete')
        self.assertEqual(len(Message.objects.all()), 0)
