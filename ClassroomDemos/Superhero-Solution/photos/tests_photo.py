from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Author, Photo


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class PhotoDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.photo1 = dict(title='title 1', image="photo1.png")
        self.photo2 = dict(title='title 2', image="photo2.png")
        # Photo.objects.create(**self.photo1)

    def test_add_test(self):
        self.assertEqual(len(Photo.objects.all()), 0)
        Photo.objects.create(**self.photo1)
        x = Photo.objects.get(pk=1)
        self.assertEqual(x.title, self.photo1['title'])
        self.assertEqual(len(Photo.objects.all()), 1)

#     def test_test_edit(self):
#         Photo.objects.create(**self.photo1)
#         x = Photo.objects.get(pk=1)
#         x.title = self.photo2['title']
#         x.image = self.photo2['image']
#         x.save()
#         self.assertEqual(x.title, self.photo2['title'])
#         self.assertEqual(x.image, self.photo2['image'])
#         self.assertEqual(len(Photo.objects.all()), 1)

#     def test_test_delete(self):
#         Photo.objects.create(**self.photo1)
#         b = Photo.objects.get(pk=1)
#         b.delete()
#         self.assertEqual(len(Photo.objects.all()), 0)


# class PhotoViewsTest(TestCase):

#     def login(self):
#         username = self.user.username
#         password = user_args()['password']
#         response = self.client.login(username=username, password=password)
#         self.assertEqual(response, True)

#     def setUp(self):
#         self.user = test_user()
#         self.author = Author.objects.create(user=self.user, bio='single tester')
#         self.photo1 = dict(author=self.author, title='title 1', image="photo1.png")
#         self.photo2 = dict(author=self.author, title='title 2', image="photo2.png")

#     def test_photo_list_view(self):
#         self.assertEqual(reverse('photo_list'), '/photo/')
#         Photo.objects.create(**self.photo1)
#         Photo.objects.create(**self.photo2)
#         response = self.client.get('/photo/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'photo/list.html')
#         self.assertTemplateUsed(response, 'theme.html')
#         self.assertContains(response, '<tr>', count=3)

#     def test_photo_detail_view(self):
#         Photo.objects.create(**self.photo1)
#         self.assertEqual(reverse('photo_detail', args='1'), '/photo/1')
#         self.assertEqual(reverse('photo_detail', args='2'), '/photo/2')
#         response = self.client.get(reverse('photo_detail', args='1'))
#         self.assertContains(response, 'body')

#     def test_photo_add_view(self):

#         # Add without Login
#         response = self.client.post(reverse('photo_add'), self.photo1)
#         response = self.client.post(reverse('photo_add'), self.photo2)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/accounts/login/?next=/photo/add')

#         # Login to add
#         self.login()
#         response = self.client.post(reverse('photo_add'), self.photo1)
#         response = self.client.post(reverse('photo_add'), self.photo2)
#         self.assertEqual(response.status_code, 302)
#         response = self.client.get(response.url)
#         self.assertEqual(len(Photo.objects.all()), 2)

#     def test_photo_edit_view(self):
#         photo2 = dict(title='title 2', image="photo2.png")

#         # Edit without Login
#         response = Photo.objects.create(**self.photo1)
#         response = self.client.post(reverse('photo_edit', args='1'), photo2)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/accounts/login/?next=/photo/1/')

#         # Login to edit
#         self.login()
#         response = self.client.post('/photo/1/', photo2)
#         self.assertEqual(response.status_code, 302)
#         response = self.client.get(response.url)
#         photo = Photo.objects.get(pk=1)
#         self.assertEqual(photo.title, self.photo2['title'])

#     def test_photo_delete_view(self):
#         self.login()
#         Photo.objects.create(**self.photo1)
#         self.assertEqual(reverse('photo_delete', args='1'), '/photo/1/delete')
#         response = self.client.post('/photo/1/delete')
#         self.assertEqual(len(Photo.objects.all()), 0)
