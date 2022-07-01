from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Lesson


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class LessonDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.lesson1 = dict(user=self.user)
    #     Lesson.objects.create(**self.lesson1)

    # def test_add_test(self):
    #     self.assertEqual(len(Lesson.objects.all()), 0)
    #     Lesson.objects.create(**self.lesson1)
    #     x = Lesson.objects.get(pk=1)
    #     self.assertEqual(x.title, self.lesson1['title'])
    #     self.assertEqual(len(Lesson.objects.all()), 1)
    #
    # def test_test_edit(self):
    #     Lesson.objects.create(**self.lesson1)
    #     x = Lesson.objects.get(pk=1)
    #     x.title = self.lesson2['title']
    #     x.body = self.lesson2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.lesson2['title'])
    #     self.assertEqual(x.body, self.lesson2['body'])
    #     self.assertEqual(len(Lesson.objects.all()), 1)
    #
    # def test_test_delete(self):
    #     Lesson.objects.create(**self.lesson1)
    #     b = Lesson.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(Lesson.objects.all()), 0)


class LessonViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.lesson1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.lesson2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('lesson_list'))

    # def test_lesson_list_view(self):
    #     self.assertEqual(reverse('lesson_list'), '/lesson/')
    #     Lesson.objects.create(**self.lesson1)
    #     Lesson.objects.create(**self.lesson2)
    #     response = self.client.get('/lesson/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'lesson_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_lesson_detail_view(self):
    #     Lesson.objects.create(**self.lesson1)
    #     self.assertEqual(reverse('lesson_detail', args='1'), '/lesson/1')
    #     self.assertEqual(reverse('lesson_detail', args='2'), '/lesson/2')
    #     response = self.client.get(reverse('lesson_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_lesson_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('lesson_add'), self.lesson1)
    #     response = self.client.post(reverse('lesson_add'), self.lesson2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/lesson/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('lesson_add'), self.lesson1)
    #     response = self.client.post(reverse('lesson_add'), self.lesson2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(Lesson.objects.all()), 2)
    #
    # def test_lesson_edit_view(self):
    #
    #     # Edit without Login
    #     response = Lesson.objects.create(**self.lesson1)
    #     response = self.client.post(reverse('lesson_edit', args='1'), self.lesson2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/lesson/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/lesson/1/', self.lesson2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     lesson = Lesson.objects.get(pk=1)
    #     self.assertEqual(lesson.title, self.lesson2['title'])
    #     self.assertEqual(lesson.body, self.lesson2['body'])
    #
    # def test_lesson_delete_view(self):
    #     self.login()
    #     Lesson.objects.create(**self.lesson1)
    #     self.assertEqual(reverse('lesson_delete', args='1'), '/lesson/1/delete')
    #     response = self.client.post('/lesson/1/delete')
    #     self.assertEqual(len(Lesson.objects.all()), 0)
