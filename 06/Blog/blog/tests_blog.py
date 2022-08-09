from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Blog


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class BlogDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.blog1 = dict(user=self.user)
    #     Blog.objects.create(**self.blog1)

    # def test_add(self):
    #     self.assertEqual(len(Blog.objects.all()), 0)
    #     Blog.objects.create(**self.blog1)
    #     x = Blog.objects.get(pk=1)
    #     self.assertEqual(x.title, self.blog1['title'])
    #     self.assertEqual(len(Blog.objects.all()), 1)
    #
    # def test_edit(self):
    #     Blog.objects.create(**self.blog1)
    #     x = Blog.objects.get(pk=1)
    #     x.title = self.blog2['title']
    #     x.body = self.blog2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.blog2['title'])
    #     self.assertEqual(x.body, self.blog2['body'])
    #     self.assertEqual(len(Blog.objects.all()), 1)
    #
    # def test_delete(self):
    #     Blog.objects.create(**self.blog1)
    #     b = Blog.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(Blog.objects.all()), 0)


class BlogViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.blog1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.blog2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('blog_list'))

    # def test_blog_list_view(self):
    #     self.assertEqual(reverse('blog_list'), '/blog/')
    #     Blog.objects.create(**self.blog1)
    #     Blog.objects.create(**self.blog2)
    #     response = self.client.get('/blog/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_blog_detail_view(self):
    #     Blog.objects.create(**self.blog1)
    #     self.assertEqual(reverse('blog_detail', args='1'), '/blog/1')
    #     self.assertEqual(reverse('blog_detail', args='2'), '/blog/2')
    #     response = self.client.get(reverse('blog_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_blog_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('blog_add'), self.blog1)
    #     response = self.client.post(reverse('blog_add'), self.blog2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/blog/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('blog_add'), self.blog1)
    #     response = self.client.post(reverse('blog_add'), self.blog2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(Blog.objects.all()), 2)
    #
    # def test_blog_edit_view(self):
    #
    #     # Edit without Login
    #     response = Blog.objects.create(**self.blog1)
    #     response = self.client.post(reverse('blog_edit', args='1'), self.blog2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/blog/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/blog/1/', self.blog2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     blog = Blog.objects.get(pk=1)
    #     self.assertEqual(blog.title, self.blog2['title'])
    #     self.assertEqual(blog.body, self.blog2['body'])
    #
    # def test_blog_delete_view(self):
    #     self.login()
    #     Blog.objects.create(**self.blog1)
    #     self.assertEqual(reverse('blog_delete', args='1'), '/blog/1/delete')
    #     response = self.client.post('/blog/1/delete')
    #     self.assertEqual(len(Blog.objects.all()), 0)
