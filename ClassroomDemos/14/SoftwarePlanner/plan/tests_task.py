from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Task


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class TaskDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.task1 = dict(user=self.user)
    #     Task.objects.create(**self.task1)

    # def test_add_test(self):
    #     self.assertEqual(len(Task.objects.all()), 0)
    #     Task.objects.create(**self.task1)
    #     x = Task.objects.get(pk=1)
    #     self.assertEqual(x.title, self.task1['title'])
    #     self.assertEqual(len(Task.objects.all()), 1)
    #
    # def test_test_edit(self):
    #     Task.objects.create(**self.task1)
    #     x = Task.objects.get(pk=1)
    #     x.title = self.task2['title']
    #     x.body = self.task2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.task2['title'])
    #     self.assertEqual(x.body, self.task2['body'])
    #     self.assertEqual(len(Task.objects.all()), 1)
    #
    # def test_test_delete(self):
    #     Task.objects.create(**self.task1)
    #     b = Task.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(Task.objects.all()), 0)


class TaskViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.task1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.task2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('task_list'))

    # def test_task_list_view(self):
    #     self.assertEqual(reverse('task_list'), '/task/')
    #     Task.objects.create(**self.task1)
    #     Task.objects.create(**self.task2)
    #     response = self.client.get('/task/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'task_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_task_detail_view(self):
    #     Task.objects.create(**self.task1)
    #     self.assertEqual(reverse('task_detail', args='1'), '/task/1')
    #     self.assertEqual(reverse('task_detail', args='2'), '/task/2')
    #     response = self.client.get(reverse('task_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_task_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('task_add'), self.task1)
    #     response = self.client.post(reverse('task_add'), self.task2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/task/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('task_add'), self.task1)
    #     response = self.client.post(reverse('task_add'), self.task2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(Task.objects.all()), 2)
    #
    # def test_task_edit_view(self):
    #
    #     # Edit without Login
    #     response = Task.objects.create(**self.task1)
    #     response = self.client.post(reverse('task_edit', args='1'), self.task2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/task/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/task/1/', self.task2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     task = Task.objects.get(pk=1)
    #     self.assertEqual(task.title, self.task2['title'])
    #     self.assertEqual(task.body, self.task2['body'])
    #
    # def test_task_delete_view(self):
    #     self.login()
    #     Task.objects.create(**self.task1)
    #     self.assertEqual(reverse('task_delete', args='1'), '/task/1/delete')
    #     response = self.client.post('/task/1/delete')
    #     self.assertEqual(len(Task.objects.all()), 0)
