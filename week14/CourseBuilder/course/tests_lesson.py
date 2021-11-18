from django.test import TestCase
from django.urls import reverse

from .models import Author, Course, Lesson
from coder.coder import create_test_user


class ChapterDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.book1 = Course.objects.create(title='Tale of 2 Cities', author=self.author1,
                                           description='None', doc_path='Documents')
        self.book2 = Course.objects.create(title='Iliad', author=self.author2,
                                           description='None', doc_path='Documents')

        self.chapter1 = dict(book=self.book2, title='Achilles', order='1', document='1.md')
        self.chapter2 = dict(book=self.book2, title='Agamememnon', order='2', document='2.md')

    def test_add_chapter(self):
        self.assertEqual(len(Lesson.objects.all()), 0)
        Lesson.objects.create(**self.chapter1)
        Lesson.objects.create(**self.chapter2)
        self.assertEqual(len(Lesson.objects.all()), 2)

    def test_chapter_list(self):
        Lesson.objects.create(**self.chapter1)
        Lesson.objects.create(**self.chapter2)
        b = Lesson.objects.filter(book=self.book2).order_by('order')
        self.assertEqual(b[0].title, 'Achilles')
        self.assertEqual(b[1].title, 'Agamememnon')
        self.assertEqual(b[1].document, '2.md')

    def test_chapter_edit(self):
        Lesson.objects.create(**self.chapter1)
        b = Lesson.objects.get(pk=1)
        b.title = 'Agamememnon'
        b.order = 2
        b.document = '2.md'
        b.save()
        self.assertEqual(b.title, 'Agamememnon')
        self.assertEqual(b.order, 2)
        self.assertEqual(b.document, '2.md')

    def test_chapter_delete(self):
        Lesson.objects.create(**self.chapter1)
        b = Lesson.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Lesson.objects.all()), 0)


class ChapterViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author = Author.objects.create(user=self.user, name='Charles Dickens')
        self.book = Course.objects.create(title='Tale of Two Cities', author=self.author,
                                          description='description', doc_path='Documents/Poems')
        self.chapter1 = dict(book=self.book, title='Best of Times',
                             order='1', html='x', markdown='x', document='Coma.md')
        self.chapter2 = dict(book=self.book, title='Worst of Times',
                             order='2', html='x', markdown='x', document='Now.md')

    def test_chapter_list_view(self):
        Lesson.objects.create(**self.chapter1)
        self.assertEqual(reverse('chapter_list'), '/chapter/')
        response = self.client.get('/chapter/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chapter_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_chapter_detail_view(self):
        self.assertEqual(reverse('chapter_detail', args='1'), '/chapter/1')
        self.assertEqual(reverse('chapter_detail', args='2'), '/chapter/2')
        Lesson.objects.create(**self.chapter1)
        response = self.client.get('/chapter/1')
        self.assertEqual(response.status_code, 200)

    def test_chapter_add_view(self):

        # Add without Login
        response = self.client.post(reverse('chapter_add'), self.chapter1)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('chapter_add'), self.chapter1)
        response = self.client.post(reverse('chapter_add'), self.chapter2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/chapter/')
        self.assertEqual(len(Lesson.objects.all()), 2)

        # List the chapters
        response = self.client.get('/chapter/')
        self.assertContains(response, '<tr>', count=3)

    def test_chapter_edit_view(self):

        # Edit without Login
        Lesson.objects.create(**self.chapter1)
        self.assertEqual(reverse('chapter_edit', args='1'), '/chapter/1/')
        response = self.client.get('/chapter/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/1/')

        # Login to edit
        self.login()
        response = self.client.post('/chapter/1/', self.chapter2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/chapter/')

        # Check the book object
        c = Lesson.objects.get(pk=1)
        self.assertEqual(c.title, self.chapter2['title'])
        self.assertNotEqual(c.title, self.chapter1['title'])
        self.assertEqual(c.document, self.chapter2['document'])

    def test_chapter_delete_view(self):
        self.login()
        Lesson.objects.create(**self.chapter1)
        self.assertEqual(reverse('chapter_delete', args='1'), '/chapter/1/delete')
        response = self.client.get('/chapter/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/chapter/1/delete')
        self.assertEqual(len(Lesson.objects.all()), 0)
