from django.test import TestCase
from django.urls import reverse

from .models import Milestone
from .test_util import create_test_user


class MilestoneDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.milestone1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.milestone2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Milestone.objects.all()), 0)
        Milestone.objects.create(**self.milestone1)
        x = Milestone.objects.get(pk=1)
        self.assertEqual(x.title, self.milestone1['title'])
        self.assertEqual(len(Milestone.objects.all()), 1)

    def test_test_edit(self):
        Milestone.objects.create(**self.milestone1)
        x = Milestone.objects.get(pk=1)
        x.title = self.milestone2['title']
        x.body = self.milestone2['body']
        x.save()
        self.assertEqual(x.title, self.milestone2['title'])
        self.assertEqual(x.body, self.milestone2['body'])
        self.assertEqual(len(Milestone.objects.all()), 1)

    def test_test_delete(self):
        Milestone.objects.create(**self.milestone1)
        b = Milestone.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Milestone.objects.all()), 0)


class MilestoneViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.milestone1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.milestone2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('milestone_list'))

    def test_milestone_list_view(self):
        self.assertEqual(reverse('milestone_list'), '/milestone/')
        Milestone.objects.create(**self.milestone1)
        Milestone.objects.create(**self.milestone2)
        response = self.client.get('/milestone/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'milestone_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_milestone_detail_view(self):
        Milestone.objects.create(**self.milestone1)
        self.assertEqual(reverse('milestone_detail', args='1'), '/milestone/1')
        self.assertEqual(reverse('milestone_detail', args='2'), '/milestone/2')
        response = self.client.get(reverse('milestone_detail', args='1'))
        self.assertContains(response, 'body')

    def test_milestone_add_view(self):

        # Add without Login
        response = self.client.post(reverse('milestone_add'), self.milestone1)
        response = self.client.post(reverse('milestone_add'), self.milestone2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/milestone/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('milestone_add'), self.milestone1)
        response = self.client.post(reverse('milestone_add'), self.milestone2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Milestone.objects.all()), 2)

    def test_milestone_edit_view(self):

        # Edit without Login
        response = Milestone.objects.create(**self.milestone1)
        response = self.client.post(reverse('milestone_edit', args='1'), self.milestone2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/milestone/1/')

        # Login to edit
        self.login()
        response = self.client.post('/milestone/1/', self.milestone2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        milestone = Milestone.objects.get(pk=1)
        self.assertEqual(milestone.title, self.milestone2['title'])
        self.assertEqual(milestone.body, self.milestone2['body'])

    def test_milestone_delete_view(self):
        self.login()
        Milestone.objects.create(**self.milestone1)
        self.assertEqual(reverse('milestone_delete', args='1'), '/milestone/1/delete')
        response = self.client.post('/milestone/1/delete')
        self.assertEqual(len(Milestone.objects.all()), 0)
