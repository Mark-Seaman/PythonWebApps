from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Person


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class PersonDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')

    def test_add_test(self):
        self.assertEqual(len(Person.objects.all()), 0)
        Person.objects.create(**self.person)
        x = Person.objects.get(pk=1)
        self.assertEqual(x.user.username, self.person['user'].username)
        self.assertEqual(x.bio, self.person['bio'])
        self.assertEqual(len(Person.objects.all()), 1)

    def test_test_edit(self):
        Person.objects.create(**self.person)
        x = Person.objects.get(pk=1)
        x.bio = 'new tester'
        x.save()
        self.assertEqual(x.user.username, self.person['user'].username)
        self.assertEqual(x.bio, 'new tester')
        self.assertEqual(len(Person.objects.all()), 1)

    def test_test_delete(self):
        Person.objects.create(**self.person)
        b = Person.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Person.objects.all()), 0)


class PersonViewsTest(TestCase):

    def login(self):
        username = self.user.username
        password = user_args()['password']
        response = self.client.login(username=username, password=password)
        self.assertEqual(response, True)

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.person2 = dict(user=self.user, bio='new tester')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('person_list'))

    def test_person_list_view(self):
        self.assertEqual(reverse('person_list'), '/person/')
        Person.objects.create(**self.person)
        response = self.client.get('/person/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_person_detail_view(self):
        Person.objects.create(**self.person)
        self.assertEqual(reverse('person_detail', args='1'), '/person/1')
        response = self.client.get(reverse('person_detail', args='1'))
        self.assertContains(response, 'body')

    # def test_person_add_view(self):

    #     # Add without Login
    #     response = self.client.post(reverse('person_add'), self.person)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/person/add')

#         # Login to add
#         self.login()
#         response = self.client.post(reverse('person_add'), self.person1)
#         response = self.client.post(reverse('person_add'), self.person2)
#         self.assertEqual(response.status_code, 302)
#         response = self.client.get(response.url)
#         self.assertEqual(len(Person.objects.all()), 2)

    def test_person_edit_view(self):

        # Edit without Login
        response = Person.objects.create(**self.person)
        response = self.client.post(reverse('person_edit', args='1'), self.person)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/person/1/')

        # Login to edit
        self.login()
        response = self.client.post('/person/1/', self.person2)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        person = Person.objects.get(pk=1)
        self.assertEqual(person.bio, self.person2['bio'])

    def test_person_delete_view(self):
        self.login()
        Person.objects.create(**self.person)
        self.assertEqual(reverse('person_delete', args='1'), '/person/1/delete')
        response = self.client.post('/person/1/delete')
        self.assertEqual(len(Person.objects.all()), 0)
