from django.test import TestCase
from django.urls import reverse

from .models import Author, Note
from coder.coder import create_test_user


class NoteDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.note1 = dict(name='Dickens', title='Tale of 2 Cities', author=self.author1,
                                     description='None', doc_path='Documents')
        self.note2 = dict(name='Homer', title='Iliad', author=self.author2,
                                     description='None', doc_path='Documents')

    def test_add_note(self):
        self.assertEqual(len(Note.objects.all()), 0)
        Note.create(**self.note1)
        Note.create(**self.note2)
        x = Note.objects.get(pk=2)
        self.assertEqual(str(x), '2 - Homer by 2 - Homer')
        self.assertEqual(x.author.name, 'Homer')
        self.assertEqual(x.title, 'Iliad')
        self.assertEqual(len(Note.objects.all()), 2)

#     def test_note_edit(self):
#         Note.create(**self.note1)
#         b = Note.objects.get(pk=1)
#         b.author = self.author2
#         b.title = 'Iliad'
#         b.description = 'No description'
#         b.save()
#         self.assertEqual(b.title, 'Iliad')
#         self.assertEqual(b.author.name, 'Homer')
#         self.assertEqual(b.description, 'No description')

#     def test_note_delete(self):
#         Note.objects.create(**self.note1)
#         b = Note.objects.get(pk=1)
#         b.delete()
#         self.assertEqual(len(Note.objects.all()), 0)


# class NoteViewsTest(TestCase):

#     def login(self):
#         response = self.client.login(username=self.user.username,  password=self.user_args['password'])
#         self.assertEqual(response, True)

#     def setUp(self):
#         self.user, self.user_args = create_test_user()
#         self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
#         self.author2 = Author.objects.create(user=self.user, name='Homer')
#         self.note1 = dict(name='BACS 200',
#                                      title='UNC BACS 200',
#                                      subtitle='Subtitle UNC BACS 200',
#                                      author=self.author1,
#                                      description='description',
#                                      doc_path='Documents/note/bacs200',
#                                      num_projects=14,
#                                      num_lessons=42)
#         self.note2 = dict(name='BACS 350',
#                                      title='UNC BACS 350',
#                                      subtitle='Subtitle UNC BACS 350',
#                                      author=self.author1,
#                                      description='None',
#                                      doc_path='Documents/note/bacs350',
#                                      num_projects=14,
#                                      num_lessons=42)

#     def test_home(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, reverse('note_list'))

#     def test_note_list_view(self):
#         self.assertEqual(reverse('note_list'), '/note/')
#         Note.objects.create(**self.note1)
#         Note.objects.create(**self.note2)
#         response = self.client.get('/note/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'note_list.html')
#         self.assertTemplateUsed(response, 'theme.html')
#         self.assertContains(response, '<tr>', count=3)

#     def test_note_detail_view(self):
#         Note.objects.create(**self.note1)
#         self.assertEqual(reverse('note_detail', args='1'), '/note/1')
#         self.assertEqual(reverse('note_detail', args='2'), '/note/2')
#         response = self.client.get(reverse('note_detail', args='1'))
#         self.assertContains(response, 'BACS 200')

#     def test_note_add_view(self):

#         # Add without Login
#         response = self.client.post(reverse('note_add'), self.note1)
#         self.assertEqual(response.url, '/accounts/login/?next=/note/add')
#         self.assertEqual(len(Note.objects.all()), 0)

#         # Login to add
#         self.login()
#         response = self.client.post(reverse('note_add'), self.note1)
#         response = self.client.post(reverse('note_add'), self.note2)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/note/2')
#         response = self.client.get('/note/')
#         self.assertEqual(len(Note.objects.all()), 2)
#         response = self.client.get(reverse('note_detail', args='2'))
#         self.assertContains(response, 'BACS 350')

#     def test_note_edit_view(self):

#         # Edit without Login
#         Note.objects.create(**self.note1)
#         self.assertEqual(reverse('note_edit', args='1'), '/note/1/')
#         response = self.client.get('/note/1/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/accounts/login/?next=/note/1/')

#         # Login to edit
#         self.login()
#         response = self.client.post('/note/1/', self.note2)
#         self.assertEqual(response.url, '/note/1')
#         response = self.client.get(response.url)
#         self.assertContains(response, self.note2['title'])
#         self.assertContains(response, self.author1.name)

#         # Check the note object
#         note = Note.objects.get(pk=1)
#         self.assertEqual(note.author, self.author1)
#         self.assertEqual(note.title, 'UNC BACS 350')

#     def test_note_delete_view(self):
#         self.login()
#         Note.objects.create(**self.note1)
#         self.assertEqual(reverse('note_delete', args='1'), '/note/1/delete')
#         response = self.client.get('/note/1/delete')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post('/note/1/delete')
#         self.assertEqual(len(Note.objects.all()), 0)
