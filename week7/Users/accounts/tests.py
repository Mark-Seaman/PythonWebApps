from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def create_test_user():
    return get_user_model().objects.create_user(
        username='TEST_DUDE', email='me@here.com', password='secret',
        first_name='Testy', last_name='Sensei')


class TestCase(TestCase):

    def test_accounts(self):
        user = create_test_user()
        self.assertEqual(user.email, 'me@here.com')
        self.assertEqual(len(User.objects.all()), 1)
