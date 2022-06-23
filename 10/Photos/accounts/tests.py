from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class UserDataTest(TestCase):

    def setUp(self):
        user = test_user()
        self.user1 = dict(username='TESTER 1', email='test1@test.us', password='secret 1')
        self.user2 = dict(username='TESTER 2', email='test2@test.us', password='secret 2')

    def test_user_add(self):
        self.assertEqual(len(User.objects.all()), 1)
        User.objects.create(**self.user1)
        User.objects.create(**self.user2)

        x = User.objects.get(pk=3)
        self.assertEqual(x.username, self.user2['username'])
        self.assertEqual(len(User.objects.all()), 3)

    def test_user_edit(self):
        User.objects.create(**self.user1)
        User.objects.create(**self.user2)

        x = User.objects.get(pk=2)
        x.first_name = self.user2['username']
        x.save()

        self.assertEqual(x.username, self.user1['username'])
        self.assertEqual(x.first_name, self.user2['username'])
        self.assertEqual(len(User.objects.all()), 3)
