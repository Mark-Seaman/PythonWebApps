from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Superhero


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class SuperheroDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.hero1 = dict(name='NAME 1', identity="ID 1")
        self.hero2 = dict(name='NAME 2', identity="ID 2")
        # Superhero.objects.create(**self.hero1)

    def test_add(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        Superhero.objects.create(**self.hero1)
        x = Superhero.objects.get(pk=1)
        self.assertEqual(x.name, self.hero1['name'])
        self.assertEqual(len(Superhero.objects.all()), 1)

    def test_edit(self):
        Superhero.objects.create(**self.hero1)
        x = Superhero.objects.get(pk=1)
        x.name = self.hero2['name']
        x.identity = self.hero2['identity']
        x.save()
        self.assertEqual(x.name, self.hero2['name'])
        self.assertEqual(x.identity, self.hero2['identity'])
        self.assertEqual(len(Superhero.objects.all()), 1)

    def test_delete(self):
        Superhero.objects.create(**self.hero1)
        b = Superhero.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Superhero.objects.all()), 0)


class SuperheroViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user = test_user()
        self.hero1 = dict(name='NAME 1', identity="ID 1")
        self.hero2 = dict(name='NAME 2', identity="ID 2")

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/list.html')

    def test_hero_list_view(self):
        self.assertEqual(reverse('hero_list'), '/')
        Superhero.objects.create(**self.hero1)
        Superhero.objects.create(**self.hero2)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_hero_detail_view(self):
        Superhero.objects.create(**self.hero1)
        self.assertEqual(reverse('hero_detail', args='1'), '/1')
        self.assertEqual(reverse('hero_detail', args='2'), '/2')
        response = self.client.get(reverse('hero_detail', args='1'))
        self.assertContains(response, 'name')

# Debug these tests !

    # def test_hero_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('hero_add'), self.hero1)
    #     response = self.client.post(reverse('hero_add'), self.hero2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/hero/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('hero_add'), self.hero1)
    #     response = self.client.post(reverse('hero_add'), self.hero2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(Superhero.objects.all()), 2)
    #
    # def test_hero_edit_view(self):
    #
    #     # Edit without Login
    #     response = Superhero.objects.create(**self.hero1)
    #     response = self.client.post(reverse('hero_edit', args='1'), self.hero2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/hero/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/hero/1/', self.hero2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     hero = Superhero.objects.get(pk=1)
    #     self.assertEqual(hero.title, self.hero2['title'])
    #     self.assertEqual(hero.body, self.hero2['body'])
    #
    # def test_hero_delete_view(self):
    #     self.login()
    #     Superhero.objects.create(**self.hero1)
    #     self.assertEqual(reverse('hero_delete', args='1'), '/hero/1/delete')
    #     response = self.client.post('/hero/1/delete')
    #     self.assertEqual(len(Superhero.objects.all()), 0)
