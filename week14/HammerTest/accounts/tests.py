from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


def create_test_user():
    args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
    user = get_user_model().objects.filter(username='TEST_DUDE')
    if user:
        user = user[0]
    else:
        user = get_user_model().objects.create_user(**args)
    return user, args


class TestAccountsData(TestCase):

    def test_accounts(self):
        self.user, self.user_args = create_test_user()
        self.assertEqual(self.user.email, 'me@here.com')
        self.assertEqual(len(User.objects.all()), 1)

    def test_string(self):
        self.user, self.user_args = create_test_user()
        self.assertEqual(str(self.user), 'TEST_DUDE')


class TestAccountsViews(TestCase):

    def test_home_view(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme.html')

    def test_login_view(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/accounts/login/')

        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme.html')

    def test_logout_view(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('test_list'))

    def test_signup_view(self):
        response = self.client.get('/accounts/signup')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, reverse('signup'))

        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theme.html')
