from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book, Chapter


class ChapterDataTest(TestCase):

    def setUp(self):
        self.book_title = 'Iliad'
        self.chapter1 = dict(book=self.book_title, title='Achilles', order='1', document='1.md')
        self.chapter2 = dict(book=self.book_title, title='Agamememnon', order='2', document='2.md')

    def test_add_chapter(self):
        self.assertEqual(len(Chapter.objects.all()), 0)
        Chapter.objects.create(**self.chapter1)
        Chapter.objects.create(**self.chapter2)
        self.assertEqual(len(Chapter.objects.all()), 2)

    def test_chapter_list(self):
        Chapter.objects.create(**self.chapter1)
        Chapter.objects.create(**self.chapter2)
        b = Chapter.objects.filter(book=self.book_title).order_by('order')
        self.assertEqual(b[0].title, 'Achilles')
        self.assertEqual(b[1].title, 'Agamememnon')
        self.assertEqual(b[1].document, '2.md')

    def test_chapter_edit(self):
        Chapter.objects.create(**self.chapter1)
        b = Chapter.objects.get(pk=1)
        b.title = 'Agamememnon'
        b.order = 2
        b.document = '2.md'
        b.save()
        self.assertEqual(b.title, 'Agamememnon')
        self.assertEqual(b.order, 2)
        self.assertEqual(b.document, '2.md')

    def test_chapter_delete(self):
        Chapter.objects.create(**self.chapter1)
        b = Chapter.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Chapter.objects.all()), 0)


class ChapterViewsTest(TestCase):

    def login(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        user = get_user_model().objects.create_user(**args)
        response = self.client.login(username='TEST_DUDE', password='secret')
        self.assertEqual(response, True)

    def setUp(self):
        self.book_title = 'Iliad'
        self.chapter1 = dict(book=self.book_title, title='Achilles', order='1', document='1.md')
        self.chapter2 = dict(book=self.book_title, title='Agamememnon', order='2', document='2.md')

    def test_home(self):
        response = self.client.get('/chapter')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, reverse('chapter_list'))

    def test_chapter_list_view(self):
        Chapter.objects.create(**self.chapter1)
        self.assertEqual(reverse('chapter_list'), '/chapter/')
        response = self.client.get('/chapter/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chapter_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_chapter_detail_view(self):
        self.assertEqual(reverse('chapter_detail', args='1'), '/chapter/1')
        self.assertEqual(reverse('chapter_detail', args='2'), '/chapter/2')
        Chapter.objects.create(**self.chapter1)
        response = self.client.get(reverse('chapter_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_chapter_add_view(self):

        # Add without Login
        chapter = dict(book=self.book_title, title='Agamememnon', order='2', document='2.md')
        response = self.client.post(reverse('chapter_add'), chapter)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('chapter_add'), self.chapter1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/chapter/')

        # List the chapters
        response = self.client.get('/chapter/')
        self.assertContains(response, '<tr>', count=2)

    def test_chapter_edit_view(self):

        # Edit without Login
        self.assertEqual(reverse('chapter_edit', args='1'), '/chapter/1/')
        response = self.client.get('/chapter/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/1/')

        # Login to edit
        self.login()
        Chapter.objects.create(**self.chapter1)
        response = self.client.get('/chapter/1')
        # self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Achilles')

        # Check after edit
        response = self.client.post('/chapter/1/', self.chapter2)
        response = self.client.get('/chapter/1')
        self.assertContains(response, 'Agamememnon')
        self.assertContains(response, '2.md')

    def test_chapter_delete_view(self):
        self.login()
        Chapter.objects.create(**self.chapter1)
        self.assertEqual(reverse('chapter_delete', args='1'), '/chapter/1/delete')
        response = self.client.get('/chapter/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/chapter/1/delete')
        self.assertEqual(len(Chapter.objects.all()), 0)
