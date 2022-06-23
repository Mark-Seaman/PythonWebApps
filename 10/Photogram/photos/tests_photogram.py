from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Photogram


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class PhotogramDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.photogram1 = dict(author=self.person, title="Title 1", image="/static/images/img1.jpg")
        self.photogram1 = dict(author=self.person, title="Title 1", image="/static/images/img1.jpg")

    #     Photogram.objects.create(**self.photogram1)

    # def test_add_test(self):
    #     self.assertEqual(len(Photogram.objects.all()), 0)
    #     Photogram.objects.create(**self.photogram1)
    #     x = Photogram.objects.get(pk=1)
    #     self.assertEqual(x.title, self.photogram1['title'])
    #     self.assertEqual(len(Photogram.objects.all()), 1)
    #
    # def test_test_edit(self):
    #     Photogram.objects.create(**self.photogram1)
    #     x = Photogram.objects.get(pk=1)
    #     x.title = self.photogram2['title']
    #     x.body = self.photogram2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.photogram2['title'])
    #     self.assertEqual(x.body, self.photogram2['body'])
    #     self.assertEqual(len(Photogram.objects.all()), 1)
    #
    # def test_test_delete(self):
    #     Photogram.objects.create(**self.photogram1)
    #     b = Photogram.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(Photogram.objects.all()), 0)


class PhotogramViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.photogram1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.photogram2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('photogram_list'))

    # def test_photogram_list_view(self):
    #     self.assertEqual(reverse('photogram_list'), '/photogram/')
    #     Photogram.objects.create(**self.photogram1)
    #     Photogram.objects.create(**self.photogram2)
    #     response = self.client.get('/photogram/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'photogram_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_photogram_detail_view(self):
    #     Photogram.objects.create(**self.photogram1)
    #     self.assertEqual(reverse('photogram_detail', args='1'), '/photogram/1')
    #     self.assertEqual(reverse('photogram_detail', args='2'), '/photogram/2')
    #     response = self.client.get(reverse('photogram_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_photogram_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('photogram_add'), self.photogram1)
    #     response = self.client.post(reverse('photogram_add'), self.photogram2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/photogram/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('photogram_add'), self.photogram1)
    #     response = self.client.post(reverse('photogram_add'), self.photogram2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(Photogram.objects.all()), 2)
    #
    # def test_photogram_edit_view(self):
    #
    #     # Edit without Login
    #     response = Photogram.objects.create(**self.photogram1)
    #     response = self.client.post(reverse('photogram_edit', args='1'), self.photogram2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/photogram/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/photogram/1/', self.photogram2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     photogram = Photogram.objects.get(pk=1)
    #     self.assertEqual(photogram.title, self.photogram2['title'])
    #     self.assertEqual(photogram.body, self.photogram2['body'])
    #
    # def test_photogram_delete_view(self):
    #     self.login()
    #     Photogram.objects.create(**self.photogram1)
    #     self.assertEqual(reverse('photogram_delete', args='1'), '/photogram/1/delete')
    #     response = self.client.post('/photogram/1/delete')
    #     self.assertEqual(len(Photogram.objects.all()), 0)
