from book.models import Book
from django.test import TestCase
from django.urls import reverse

from .models import Chapter


class ChapterDataTest(TestCase):

    def create_chapter(self, title):
        return Chapter.objects.create(book=self.book, title=title, order=1,
                                      markdown="# Best of Times", document='tale.md')

    def setUp(self):
        self.book = Book.objects.create(title='Tale of 2 Cities', author='Chuck Dickens')
        self.create_chapter('Best of Times')

    def test_add_chapter(self):
        self.assertEqual(len(Chapter.objects.all()), 1)
        chapter = self.create_chapter('Worst of Times')
        chapter.order = 2
        chapter.markdown = "# Worst of Times"
        chapter.document = 'tale2.md'
        chapter.save()
        self.assertEqual(len(Chapter.objects.all()), 2)


class ChapterViewsTest(TestCase):

    # def login(self):
    #     args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
    #     user = get_user_model().objects.create_user(**args)
    #     response = self.client.login(username='TEST_DUDE', password='secret')
    #     self.assertEqual(response, True)

    def setUp(self):
        self.book = Chapter.objects.create(title='Iliad', author='Homer')
