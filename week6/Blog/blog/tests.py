from django.contrib.auth import get_user_model
from django.test import TestCase


def create_test_user():
    args = dict(username='seaman', email='me@here.com', password='secret')
    user = get_user_model().objects.filter(username='seaman')
    if user:
        user = user[0]
    else:
        user = get_user_model().objects.create_user(**args)
    return user, args
