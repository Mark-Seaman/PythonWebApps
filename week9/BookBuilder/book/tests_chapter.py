from django.contrib.auth import get_user_model
from chapter.models import Chapter
from django.test import TestCase
from django.urls import reverse

from .models import Chapter


class ChapterDataTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_add_chapter(self):
        self.assertEqual(len(Chapter.objects.all()), 0)
        Chapter.objects.create(title='Tale of 2 Cities', author='Chuck Dickens')
        Chapter.objects.create(title='Iliad', author='Homer')
        self.assertEqual(len(Chapter.objects.all()), 2)

    def test_chapter_title(self):
        Chapter.objects.create(title='Iliad', author='Homer')
        b = Chapter.objects.get(pk=1)
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author, 'Homer')
        self.assertEqual(b.description, 'None')

    def test_chapter_edit(self):
        Chapter.objects.create(title='Iliad', author='Homer')
        b = Chapter.objects.get(pk=1)
        b.author = 'Mark Seaman'
        b.description = 'No description'
        b.save()
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author, 'Mark Seaman')
        self.assertEqual(b.description, 'No description')

    def test_chapter_delete(self):
        Chapter.objects.create(title='Iliad', author='Homer')
        b = Chapter.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Chapter.objects.all()), 0)

    def test_string_representation(self):
        chapter = Chapter.objects.create(title='Iliad', author='Homer')
        self.assertEqual(
            str(chapter), '1 - Iliad by Homer')


class ChapterViewsTest(TestCase):

    def login(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        user = get_user_model().objects.create_user(**args)
        response = self.client.login(username='TEST_DUDE', password='secret')
        self.assertEqual(response, True)

    def setUp(self):
        self.chapter = Chapter.objects.create(title='Iliad', author='Homer')

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('chapter_list'))

    def test_chapter_list_view(self):
        self.assertEqual(reverse('chapter_list'), '/chapter/')
        response = self.client.get('/chapter/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chapter_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_chapter_detail_view(self):
        self.assertEqual(reverse('chapter_detail', args='1'), '/chapter/1')
        self.assertEqual(reverse('chapter_detail', args='2'), '/chapter/2')
        response = self.client.get(reverse('chapter_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_chapter_add_view(self):

        # Add without Login
        chapter = dict(title='Star Wars', author='Darth Vadar', description='None')
        response = self.client.post(reverse('chapter_add'), chapter)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('chapter_add'), chapter)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/chapter/2')

        # List the chapters
        response = self.client.get('/chapter/')
        self.assertContains(response, '<tr>', count=3)

    def test_chapter_edit_view(self):

        # Edit without Login
        self.assertEqual(reverse('chapter_edit', args='1'), '/chapter/1/')
        response = self.client.get('/chapter/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/1/')

        # Login to edit
        self.login()
        chapter = dict(title='Oddessy', author='Homer', description='None')
        response = self.client.post('/chapter/1/', chapter)

        # Check the redirect
        self.assertEqual(response.url, '/chapter/1')
        response = self.client.get(response.url)
        self.assertContains(response, 'Homer')

        # Check the chapter object
        chapter = Chapter.objects.get(pk=1)
        self.assertEqual(chapter.author, 'Homer')
        self.assertEqual(chapter.title, 'Oddessy')

    def test_chapter_delete_view(self):
        self.login()
        self.assertEqual(reverse('chapter_delete', args='1'), '/chapter/1/delete')
        response = self.client.get('/chapter/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/chapter/1/delete')
        self.assertEqual(len(Chapter.objects.all()), 0)
