from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Message, Person


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class MessageDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = Person.objects.create(user=self.user, bio='single tester')
        self.message1 = dict(author=self.person, title='Doc Title 1', text='Doc Text 1')
        self.message2 = dict(author=self.person, title='Doc Title 2', text='Doc Text 2')

    def test_add(self):
        self.assertEqual(len(Message.objects.all()), 0)
        Message.objects.create(**self.message1)
        x = Message.objects.get(pk=1)
        self.assertEqual(x.title, self.message1['title'])
        self.assertEqual(len(Message.objects.all()), 1)

    def test_edit(self):
        Message.objects.create(**self.message1)
        x = Message.objects.get(pk=1)
        x.title = self.message2['title']
        x.text = self.message2['text']
        x.save()
        self.assertEqual(x.title, self.message2['title'])
        self.assertEqual(x.text, self.message2['text'])
        self.assertEqual(len(Message.objects.all()), 1)

    def test_delete(self):
        Message.objects.create(**self.message1)
        b = Message.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Message.objects.all()), 0)


class MessageViewsTest(TestCase):

    def login(self):
        username = self.user.username
        password = user_args()['password']
        response = self.client.login(username=username, password=password)
        self.assertEqual(response, True)

    def setUp(self):
        self.user = test_user()
        self.person = Person.objects.create(user=self.user, bio='single tester')
        self.message1 = dict(author=self.person, recipient=self.person,  title='Doc Title 1', text='Doc Text 1')
        self.message2 = dict(author=self.person, recipient=self.person, title='Doc Title 2', text='Doc Text 2')
        self.m1 = dict(recipient=self.person, title='Doc Title 1', text='Doc Text 1')
        self.m2 = dict(recipient=self.person, title='Doc Title 2', text='Doc Text 2')

    def test_message_list_view(self):
        self.assertEqual(reverse('message_list'), '/message/')
        Message.objects.create(**self.message1)
        Message.objects.create(**self.message2)
        response = self.client.get('/message/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'message/list.html')
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
        response = self.client.post(reverse('message_add'), self.m1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/message/add')

        # Login to add Person record
        self.login()
        response = self.client.get('/')
        response = self.client.post(reverse('message_add'), self.m1)
        response = self.client.post(reverse('message_add'), self.m2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Message.objects.all()), 2)

    def test_message_edit_view(self):

        # Edit without Login
        response = Message.objects.create(**self.message1)
        response = self.client.post(reverse('message_edit', args='1'), self.m2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/message/1/')

        # Login to add Person record
        self.login()
        response = self.client.get('/')
        response = self.client.post('/message/1/', self.m2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        message = Message.objects.get(pk=1)
        self.assertEqual(message.title, self.message2['title'])
        self.assertEqual(message.text, self.message2['text'])

    def test_message_delete_view(self):
        self.login()
        Message.objects.create(**self.message1)
        self.assertEqual(reverse('message_delete', args='1'), '/message/1/delete')
        response = self.client.post('/message/1/delete')
        self.assertEqual(len(Message.objects.all()), 0)
