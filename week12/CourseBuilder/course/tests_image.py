from django.test import TestCase
from django.urls import reverse

from .models import Author, Image, Lesson
from coder.coder import create_test_user


class ImageDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.image1 = dict(title='Tale of 2 Cities', author=self.author1, description='None', doc_path='Documents')
        self.image2 = dict(title='Iliad', author=self.author2, description='None', doc_path='Documents')

#     def test_add_image(self):
#         self.assertEqual(len(Image.objects.all()), 0)
#         Image.objects.create(**self.image1)
#         Image.objects.create(**self.image2)
#         x = Image.objects.get(pk=2)
#         self.assertEqual(str(x), '2 - Iliad by 2 - Homer')
#         self.assertEqual(x.author.name, 'Homer')
#         self.assertEqual(x.title, 'Iliad')
#         self.assertEqual(len(Image.objects.all()), 2)

#     def test_image_edit(self):
#         Image.objects.create(**self.image1)
#         b = Image.objects.get(pk=1)
#         b.author = self.author2
#         b.title = 'Iliad'
#         b.description = 'No description'
#         b.save()
#         self.assertEqual(b.title, 'Iliad')
#         self.assertEqual(b.author.name, 'Homer')
#         self.assertEqual(b.description, 'No description')

#     def test_image_delete(self):
#         Image.objects.create(**self.image1)
#         b = Image.objects.get(pk=1)
#         b.delete()
#         self.assertEqual(len(Image.objects.all()), 0)

#     def test_import_images(self):
#         import_all_images()
#         # print(Author.objects.all())
#         # print(Image.objects.all())
#         # print(Chapter.objects.all())
#         self.assertEqual(len(Author.objects.all()), 3)
#         self.assertEqual(len(Image.objects.all()), 2)
#         self.assertEqual(len(Chapter.objects.all()), 70)


# class ImageViewsTest(TestCase):

#     def login(self):
#         response = self.client.login(username=self.user.username,  password=self.user_args['password'])
#         self.assertEqual(response, True)

#     def setUp(self):
#         self.user, self.user_args = create_test_user()
#         self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
#         self.author2 = Author.objects.create(user=self.user, name='Homer')
#         self.image1 = dict(title='Iliad',   author=self.author1, description='description', doc_path='Documents')
#         self.image2 = dict(title='Odyssey', author=self.author1, description='None', doc_path='Documents')

#     def test_home(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, reverse('image_list'))

#     def test_image_list_view(self):
#         self.assertEqual(reverse('image_list'), '/image/')
#         Image.objects.create(**self.image1)
#         Image.objects.create(**self.image2)
#         response = self.client.get('/image/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'image_list.html')
#         self.assertTemplateUsed(response, 'theme.html')
#         self.assertContains(response, '<tr>', count=3)

#     def test_image_detail_view(self):
#         Image.objects.create(**self.image1)
#         self.assertEqual(reverse('image_detail', args='1'), '/image/1')
#         self.assertEqual(reverse('image_detail', args='2'), '/image/2')
#         response = self.client.get(reverse('image_detail', args='1'))
#         self.assertEqual(response.status_code, 200)

#     def test_image_add_view(self):

#         # Add without Login
#         response = self.client.post(reverse('image_add'), self.image1)
#         self.assertEqual(response.url, '/accounts/login/?next=/image/add')
#         self.assertEqual(len(Image.objects.all()), 0)

#         # Login to add
#         self.login()
#         response = self.client.post(reverse('image_add'), self.image1)
#         response = self.client.post(reverse('image_add'), self.image2)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/image/2')
#         response = self.client.get('/image/')
#         self.assertEqual(len(Image.objects.all()), 2)

#     def test_image_edit_view(self):

#         # Edit without Login
#         Image.objects.create(**self.image1)
#         self.assertEqual(reverse('image_edit', args='1'), '/image/1/')
#         response = self.client.get('/image/1/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/accounts/login/?next=/image/1/')

#         # Login to edit
#         self.login()
#         response = self.client.post('/image/1/', self.image2)
#         self.assertEqual(response.url, '/image/1')
#         response = self.client.get(response.url)
#         self.assertContains(response, self.image2['title'])
#         self.assertContains(response, self.author1.name)

#         # Check the image object
#         image = Image.objects.get(pk=1)
#         self.assertEqual(image.author, self.author1)
#         self.assertEqual(image.title, 'Odyssey')

#     def test_image_delete_view(self):
#         self.login()
#         Image.objects.create(**self.image1)
#         self.assertEqual(reverse('image_delete', args='1'), '/image/1/delete')
#         response = self.client.get('/image/1/delete')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post('/image/1/delete')
#         self.assertEqual(len(Image.objects.all()), 0)
