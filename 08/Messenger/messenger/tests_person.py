from django.test import TestCase
from django.urls import reverse

from .models import Person
from .test_util import create_test_user


class PersonDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.person1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.person2 = dict(title='Doc Title 2', body='Doc Body 2')

    def test_add_test(self):
        self.assertEqual(len(Person.objects.all()), 0)
        Person.objects.create(**self.person1)
        x = Person.objects.get(pk=1)
        self.assertEqual(x.title, self.person1['title'])
        self.assertEqual(len(Person.objects.all()), 1)

    def test_test_edit(self):
        Person.objects.create(**self.person1)
        x = Person.objects.get(pk=1)
        x.title = self.person2['title']
        x.body = self.person2['body']
        x.save()
        self.assertEqual(x.title, self.person2['title'])
        self.assertEqual(x.body, self.person2['body'])
        self.assertEqual(len(Person.objects.all()), 1)

    def test_test_delete(self):
        Person.objects.create(**self.person1)
        b = Person.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Person.objects.all()), 0)


class PersonViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.person1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.person2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('person_list'))

    def test_person_list_view(self):
        self.assertEqual(reverse('person_list'), '/person/')
        Person.objects.create(**self.person1)
        Person.objects.create(**self.person2)
        response = self.client.get('/person/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_person_detail_view(self):
        Person.objects.create(**self.person1)
        self.assertEqual(reverse('person_detail', args='1'), '/person/1')
        self.assertEqual(reverse('person_detail', args='2'), '/person/2')
        response = self.client.get(reverse('person_detail', args='1'))
        self.assertContains(response, 'body')

    def test_person_add_view(self):

        # Add without Login
        response = self.client.post(reverse('person_add'), self.person1)
        response = self.client.post(reverse('person_add'), self.person2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/person/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('person_add'), self.person1)
        response = self.client.post(reverse('person_add'), self.person2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(len(Person.objects.all()), 2)

    def test_person_edit_view(self):

        # Edit without Login
        response = Person.objects.create(**self.person1)
        response = self.client.post(reverse('person_edit', args='1'), self.person2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/person/1/')

        # Login to edit
        self.login()
        response = self.client.post('/person/1/', self.person2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        person = Person.objects.get(pk=1)
        self.assertEqual(person.title, self.person2['title'])
        self.assertEqual(person.body, self.person2['body'])

    def test_person_delete_view(self):
        self.login()
        Person.objects.create(**self.person1)
        self.assertEqual(reverse('person_delete', args='1'), '/person/1/delete')
        response = self.client.post('/person/1/delete')
        self.assertEqual(len(Person.objects.all()), 0)
