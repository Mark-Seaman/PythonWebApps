from django.test import TestCase
from django.urls import reverse

from .models import Chapter
from .test_util import create_test_user


class ChapterDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.chapter1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.chapter2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Chapter.objects.all()), 0)
        Chapter.objects.create(**self.chapter1)
        x = Chapter.objects.get(pk=1)
        self.assertEqual(x.title, self.chapter1['title'])
        self.assertEqual(len(Chapter.objects.all()), 1)

    def test_test_edit(self):
        Chapter.objects.create(**self.chapter1)
        x = Chapter.objects.get(pk=1)
        x.title = self.chapter2['title']
        x.body = self.chapter2['body']
        x.save()
        self.assertEqual(x.title, self.chapter2['title'])
        self.assertEqual(x.body, self.chapter2['body'])
        self.assertEqual(len(Chapter.objects.all()), 1)

    def test_test_delete(self):
        Chapter.objects.create(**self.chapter1)
        b = Chapter.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Chapter.objects.all()), 0)


class ChapterViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.chapter1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.chapter2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('chapter_list'))

    def test_chapter_list_view(self):
        self.assertEqual(reverse('chapter_list'), '/chapter/')
        Chapter.objects.create(**self.chapter1)
        Chapter.objects.create(**self.chapter2)
        response = self.client.get('/chapter/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chapter_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_chapter_detail_view(self):
        Chapter.objects.create(**self.chapter1)
        self.assertEqual(reverse('chapter_detail', args='1'), '/chapter/1')
        self.assertEqual(reverse('chapter_detail', args='2'), '/chapter/2')
        response = self.client.get(reverse('chapter_detail', args='1'))
        self.assertContains(response, 'body')

    def test_chapter_add_view(self):

        # Add without Login
        response = self.client.post(reverse('chapter_add'), self.chapter1)
        response = self.client.post(reverse('chapter_add'), self.chapter2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('chapter_add'), self.chapter1)
        response = self.client.post(reverse('chapter_add'), self.chapter2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Chapter.objects.all()), 2)

    def test_chapter_edit_view(self):

        # Edit without Login
        response = Chapter.objects.create(**self.chapter1)
        response = self.client.post(reverse('chapter_edit', args='1'), self.chapter2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/1/')

        # Login to edit
        self.login()
        response = self.client.post('/chapter/1/', self.chapter2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        chapter = Chapter.objects.get(pk=1)
        self.assertEqual(chapter.title, self.chapter2['title'])
        self.assertEqual(chapter.body, self.chapter2['body'])

    def test_chapter_delete_view(self):
        self.login()
        Chapter.objects.create(**self.chapter1)
        self.assertEqual(reverse('chapter_delete', args='1'), '/chapter/1/delete')
        response = self.client.post('/chapter/1/delete')
        self.assertEqual(len(Chapter.objects.all()), 0)
