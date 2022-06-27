from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Photo


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class PhotoDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.photo1 = dict(user=self.user)
    #     Photo.objects.create(**self.photo1)

    # def test_add_test(self):
    #     self.assertEqual(len(Photo.objects.all()), 0)
    #     Photo.objects.create(**self.photo1)
    #     x = Photo.objects.get(pk=1)
    #     self.assertEqual(x.title, self.photo1['title'])
    #     self.assertEqual(len(Photo.objects.all()), 1)
    #
    # def test_test_edit(self):
    #     Photo.objects.create(**self.photo1)
    #     x = Photo.objects.get(pk=1)
    #     x.title = self.photo2['title']
    #     x.body = self.photo2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.photo2['title'])
    #     self.assertEqual(x.body, self.photo2['body'])
    #     self.assertEqual(len(Photo.objects.all()), 1)
    #
    # def test_test_delete(self):
    #     Photo.objects.create(**self.photo1)
    #     b = Photo.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(Photo.objects.all()), 0)


class PhotoViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.photo1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.photo2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('photo_list'))

    # def test_photo_list_view(self):
    #     self.assertEqual(reverse('photo_list'), '/photo/')
    #     Photo.objects.create(**self.photo1)
    #     Photo.objects.create(**self.photo2)
    #     response = self.client.get('/photo/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'photo_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_photo_detail_view(self):
    #     Photo.objects.create(**self.photo1)
    #     self.assertEqual(reverse('photo_detail', args='1'), '/photo/1')
    #     self.assertEqual(reverse('photo_detail', args='2'), '/photo/2')
    #     response = self.client.get(reverse('photo_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_photo_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('photo_add'), self.photo1)
    #     response = self.client.post(reverse('photo_add'), self.photo2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/photo/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('photo_add'), self.photo1)
    #     response = self.client.post(reverse('photo_add'), self.photo2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(Photo.objects.all()), 2)
    #
    # def test_photo_edit_view(self):
    #
    #     # Edit without Login
    #     response = Photo.objects.create(**self.photo1)
    #     response = self.client.post(reverse('photo_edit', args='1'), self.photo2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/photo/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/photo/1/', self.photo2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     photo = Photo.objects.get(pk=1)
    #     self.assertEqual(photo.title, self.photo2['title'])
    #     self.assertEqual(photo.body, self.photo2['body'])
    #
    # def test_photo_delete_view(self):
    #     self.login()
    #     Photo.objects.create(**self.photo1)
    #     self.assertEqual(reverse('photo_delete', args='1'), '/photo/1/delete')
    #     response = self.client.post('/photo/1/delete')
    #     self.assertEqual(len(Photo.objects.all()), 0)
