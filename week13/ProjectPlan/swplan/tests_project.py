from django.test import TestCase
from django.urls import reverse

from .models import Project
from .test_util import create_test_user


class ProjectDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.project1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.project2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Project.objects.all()), 0)
        Project.objects.create(**self.project1)
        x = Project.objects.get(pk=1)
        self.assertEqual(x.title, self.project1['title'])
        self.assertEqual(len(Project.objects.all()), 1)

    def test_test_edit(self):
        Project.objects.create(**self.project1)
        x = Project.objects.get(pk=1)
        x.title = self.project2['title']
        x.body = self.project2['body']
        x.save()
        self.assertEqual(x.title, self.project2['title'])
        self.assertEqual(x.body, self.project2['body'])
        self.assertEqual(len(Project.objects.all()), 1)

    def test_test_delete(self):
        Project.objects.create(**self.project1)
        b = Project.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Project.objects.all()), 0)


class ProjectViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.project1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.project2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('project_list'))

    def test_project_list_view(self):
        self.assertEqual(reverse('project_list'), '/project/')
        Project.objects.create(**self.project1)
        Project.objects.create(**self.project2)
        response = self.client.get('/project/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_project_detail_view(self):
        Project.objects.create(**self.project1)
        self.assertEqual(reverse('project_detail', args='1'), '/project/1')
        self.assertEqual(reverse('project_detail', args='2'), '/project/2')
        response = self.client.get(reverse('project_detail', args='1'))
        self.assertContains(response, 'body')

    def test_project_add_view(self):

        # Add without Login
        response = self.client.post(reverse('project_add'), self.project1)
        response = self.client.post(reverse('project_add'), self.project2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/project/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('project_add'), self.project1)
        response = self.client.post(reverse('project_add'), self.project2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Project.objects.all()), 2)

    def test_project_edit_view(self):

        # Edit without Login
        response = Project.objects.create(**self.project1)
        response = self.client.post(reverse('project_edit', args='1'), self.project2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/project/1/')

        # Login to edit
        self.login()
        response = self.client.post('/project/1/', self.project2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        project = Project.objects.get(pk=1)
        self.assertEqual(project.title, self.project2['title'])
        self.assertEqual(project.body, self.project2['body'])

    def test_project_delete_view(self):
        self.login()
        Project.objects.create(**self.project1)
        self.assertEqual(reverse('project_delete', args='1'), '/project/1/delete')
        response = self.client.post('/project/1/delete')
        self.assertEqual(len(Project.objects.all()), 0)
