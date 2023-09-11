from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Student


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class StudentDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.student1 = dict(user=self.user)
    #     Student.objects.create(**self.student1)

    # def test_add(self):
    #     self.assertEqual(len(Student.objects.all()), 0)
    #     Student.objects.create(**self.student1)
    #     x = Student.objects.get(pk=1)
    #     self.assertEqual(x.title, self.student1['title'])
    #     self.assertEqual(len(Student.objects.all()), 1)
    #
    # def test_edit(self):
    #     Student.objects.create(**self.student1)
    #     x = Student.objects.get(pk=1)
    #     x.title = self.student2['title']
    #     x.body = self.student2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.student2['title'])
    #     self.assertEqual(x.body, self.student2['body'])
    #     self.assertEqual(len(Student.objects.all()), 1)
    #
    # def test_delete(self):
    #     Student.objects.create(**self.student1)
    #     b = Student.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(Student.objects.all()), 0)


class StudentViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.student1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.student2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('student_list'))

    # def test_student_list_view(self):
    #     self.assertEqual(reverse('student_list'), '/student/')
    #     Student.objects.create(**self.student1)
    #     Student.objects.create(**self.student2)
    #     response = self.client.get('/student/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'student_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_student_detail_view(self):
    #     Student.objects.create(**self.student1)
    #     self.assertEqual(reverse('student_detail', args='1'), '/student/1')
    #     self.assertEqual(reverse('student_detail', args='2'), '/student/2')
    #     response = self.client.get(reverse('student_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_student_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('student_add'), self.student1)
    #     response = self.client.post(reverse('student_add'), self.student2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/student/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('student_add'), self.student1)
    #     response = self.client.post(reverse('student_add'), self.student2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(Student.objects.all()), 2)
    #
    # def test_student_edit_view(self):
    #
    #     # Edit without Login
    #     response = Student.objects.create(**self.student1)
    #     response = self.client.post(reverse('student_edit', args='1'), self.student2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/student/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/student/1/', self.student2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     student = Student.objects.get(pk=1)
    #     self.assertEqual(student.title, self.student2['title'])
    #     self.assertEqual(student.body, self.student2['body'])
    #
    # def test_student_delete_view(self):
    #     self.login()
    #     Student.objects.create(**self.student1)
    #     self.assertEqual(reverse('student_delete', args='1'), '/student/1/delete')
    #     response = self.client.post('/student/1/delete')
    #     self.assertEqual(len(Student.objects.all()), 0)
