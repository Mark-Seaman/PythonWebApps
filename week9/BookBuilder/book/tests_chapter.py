from book.models import Book
from django.test import TestCase
from django.urls import reverse

from .models import Book


class ChapterDataTest(TestCase):

    def test_django(self):
        self.assertTrue


class ChapterViewsTest(TestCase):

    # def login(self):
    #     args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
    #     user = get_user_model().objects.create_user(**args)
    #     response = self.client.login(username='TEST_DUDE', password='secret')
    #     self.assertEqual(response, True)

    def setUp(self):
        self.book = Chapter.objects.create(title='Iliad', author='Homer')
