from django.test import TestCase
from django.urls import reverse

from .models import Article
from .test_util import create_test_user


class ArticleDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.article1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.article2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Article.objects.all()), 0)
        Article.objects.create(**self.article1)
        x = Article.objects.get(pk=1)
        self.assertEqual(x.title, self.article1['title'])
        self.assertEqual(len(Article.objects.all()), 1)

    def test_test_edit(self):
        Article.objects.create(**self.article1)
        x = Article.objects.get(pk=1)
        x.title = self.article2['title']
        x.body = self.article2['body']
        x.save()
        self.assertEqual(x.title, self.article2['title'])
        self.assertEqual(x.body, self.article2['body'])
        self.assertEqual(len(Article.objects.all()), 1)

    def test_test_delete(self):
        Article.objects.create(**self.article1)
        b = Article.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Article.objects.all()), 0)


class ArticleViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.article1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.article2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('article_list'))

    def test_article_list_view(self):
        self.assertEqual(reverse('article_list'), '/article/')
        Article.objects.create(**self.article1)
        Article.objects.create(**self.article2)
        response = self.client.get('/article/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_article_detail_view(self):
        Article.objects.create(**self.article1)
        self.assertEqual(reverse('article_detail', args='1'), '/article/1')
        self.assertEqual(reverse('article_detail', args='2'), '/article/2')
        response = self.client.get(reverse('article_detail', args='1'))
        self.assertContains(response, 'body')

    def test_article_add_view(self):

        # Add without Login
        response = self.client.post(reverse('article_add'), self.article1)
        response = self.client.post(reverse('article_add'), self.article2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/article/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('article_add'), self.article1)
        response = self.client.post(reverse('article_add'), self.article2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Article.objects.all()), 2)

    def test_article_edit_view(self):

        # Edit without Login
        response = Article.objects.create(**self.article1)
        response = self.client.post(reverse('article_edit', args='1'), self.article2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/article/1/')

        # Login to edit
        self.login()
        response = self.client.post('/article/1/', self.article2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        article = Article.objects.get(pk=1)
        self.assertEqual(article.title, self.article2['title'])
        self.assertEqual(article.body, self.article2['body'])

    def test_article_delete_view(self):
        self.login()
        Article.objects.create(**self.article1)
        self.assertEqual(reverse('article_delete', args='1'), '/article/1/delete')
        response = self.client.post('/article/1/delete')
        self.assertEqual(len(Article.objects.all()), 0)
