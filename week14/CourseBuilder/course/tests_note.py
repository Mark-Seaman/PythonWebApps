from django.test import TestCase
from django.urls import reverse

from .models import Author, Course, Note, Chapter
from coder.coder import create_test_user


class NoteDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.book = Course.objects.create(title='Tale of 2 Cities', author=self.author,
                                          description='None', doc_path='Documents')
        self.chapter = Chapter.objects.create(book=self.book, title='Achilles', order='1', document='1.md')
        self.note1 = dict(title='Best note ever', chapter=self.chapter, author=self.author, text='None',)
        self.note2 = dict(title='Worst note ever', chapter=self.chapter, author=self.author, text='None')

    def test_add_note(self):
        self.assertEqual(len(Note.objects.all()), 0)
        Note.objects.create(**self.note1)
        Note.objects.create(**self.note2)
        x = Note.objects.get(pk=2)
        self.assertEqual(str(x), 'Worst note ever - 1 Tale of 2 Cities')
        self.assertEqual(x.author.name, 'Chuck Dickens')
        self.assertEqual(x.title, 'Worst note ever')
        self.assertEqual(len(Note.objects.all()), 2)

    def test_note_edit(self):
        Note.objects.create(**self.note1)
        b = Note.objects.get(pk=1)
        b.title = 'Worst note ever'
        b.save()
        self.assertEqual(b.title, 'Worst note ever')

    def test_note_delete(self):
        Note.objects.create(**self.note1)
        Note.objects.create(**self.note2)
        self.assertEqual(len(Note.objects.all()), 2)
        b = Note.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Note.objects.all()), 1)


class NoteViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.book = Course.objects.create(title='Tale of 2 Cities', author=self.author,
                                          description='None', doc_path='Documents')
        self.chapter = Chapter.objects.create(book=self.book, title='Achilles', order='1', document='1.md')
        self.note1 = dict(title='Best note ever', chapter=self.chapter, author=self.author, text='None',)
        self.note2 = dict(title='Worst note ever', chapter=self.chapter, author=self.author, text='None')

    def test_note_list_view(self):
        self.assertEqual(reverse('note_list'), '/note/')
        Note.objects.create(**self.note1)
        Note.objects.create(**self.note2)
        response = self.client.get('/note/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_note_detail_view(self):
        Note.objects.create(**self.note1)
        self.assertEqual(reverse('note_detail', args='1'), '/note/1')
        self.assertEqual(reverse('note_detail', args='2'), '/note/2')
        response = self.client.get(reverse('note_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_note_add_view(self):

        # Add without Login
        response = self.client.post(reverse('note_add'), self.note1)
        self.assertEqual(response.url, '/accounts/login/?next=/note/add')
        self.assertEqual(len(Note.objects.all()), 0)

        # Login to add
        self.login()
        response = self.client.post(reverse('note_add'), self.note1)
        response = self.client.post(reverse('note_add'), self.note2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/note/')
        response = self.client.get('/note/')
        self.assertEqual(len(Note.objects.all()), 2)

    def test_note_edit_view(self):

        # Edit without Login
        Note.objects.create(**self.note1)
        self.assertEqual(reverse('note_edit', args='1'), '/note/1/')
        response = self.client.get('/note/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/note/1/')

        # Login to edit
        self.login()
        response = self.client.post('/note/1/', self.note2)
        self.assertEqual(response.url, '/note/')
        response = self.client.get(response.url)
        self.assertContains(response, self.note2['title'])
        self.assertContains(response, self.author.name)

        # Check the note object
        note = Note.objects.get(pk=1)
        self.assertEqual(note.author, self.author)
        self.assertEqual(note.title, self.note2['title'])

    def test_note_delete_view(self):
        self.login()
        Note.objects.create(**self.note1)
        self.assertEqual(reverse('note_delete', args='1'), '/note/1/delete')
        response = self.client.get('/note/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/note/1/delete')
        self.assertEqual(len(Note.objects.all()), 0)
