from django.test import TestCase
from django.urls import reverse

from book.models import Author, Book, Chapter
from book.book import import_all_books
from coder.coder import create_test_user


class BookDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.book1 = dict(title='Tale of 2 Cities', author=self.author1, description='None', doc_path='Documents')
        self.book2 = dict(title='Iliad', author=self.author2, description='None', doc_path='Documents')

    def test_add_book(self):
        self.assertEqual(len(Book.objects.all()), 0)
        Book.objects.create(**self.book1)
        Book.objects.create(**self.book2)
        x = Book.objects.get(pk=2)
        self.assertEqual(str(x), '2 - Iliad by 2 - Homer')
        self.assertEqual(x.author.name, 'Homer')
        self.assertEqual(x.title, 'Iliad')
        self.assertEqual(len(Book.objects.all()), 2)

    def test_book_edit(self):
        Book.objects.create(**self.book1)
        b = Book.objects.get(pk=1)
        b.author = self.author2
        b.title = 'Iliad'
        b.description = 'No description'
        b.save()
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author.name, 'Homer')
        self.assertEqual(b.description, 'No description')

    def test_book_delete(self):
        Book.objects.create(**self.book1)
        b = Book.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Book.objects.all()), 0)

    def test_import_books(self):
        import_all_books()
        # print(Author.objects.all())
        # print(Book.objects.all())
        # print(Chapter.objects.all())
        self.assertEqual(len(Author.objects.all()), 3)
        self.assertEqual(len(Book.objects.all()), 2)
        self.assertEqual(len(Chapter.objects.all()), 70)


class BookFixtureTest(TestCase):
    fixtures = ['Documents/Test/data.json']

    def test_with_data(self):
        self.assertEqual(len(Author.objects.all()), 1)
        self.assertEqual(len(Book.objects.all()), 2)
        self.assertEqual(len(Chapter.objects.all()), 70)


class BookViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.book1 = dict(title='Iliad',   author=self.author1, description='description', doc_path='Documents')
        self.book2 = dict(title='Odyssey', author=self.author1, description='None', doc_path='Documents')

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('book_list'))

    def test_book_list_view(self):
        self.assertEqual(reverse('book_list'), '/book/')
        Book.objects.create(**self.book1)
        Book.objects.create(**self.book2)
        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_book_detail_view(self):
        Book.objects.create(**self.book1)
        self.assertEqual(reverse('book_detail', args='1'), '/book/1')
        self.assertEqual(reverse('book_detail', args='2'), '/book/2')
        response = self.client.get(reverse('book_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_book_add_view(self):

        # Add without Login
        response = self.client.post(reverse('book_add'), self.book1)
        self.assertEqual(response.url, '/accounts/login/?next=/book/add')
        self.assertEqual(len(Book.objects.all()), 0)

        # Login to add
        self.login()
        response = self.client.post(reverse('book_add'), self.book1)
        response = self.client.post(reverse('book_add'), self.book2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/book/2')
        response = self.client.get('/book/')
        self.assertEqual(len(Book.objects.all()), 2)

    def test_book_edit_view(self):

        # Edit without Login
        Book.objects.create(**self.book1)
        self.assertEqual(reverse('book_edit', args='1'), '/book/1/')
        response = self.client.get('/book/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/book/1/')

        # Login to edit
        self.login()
        response = self.client.post('/book/1/', self.book2)
        self.assertEqual(response.url, '/book/1')
        response = self.client.get(response.url)
        self.assertContains(response, self.book2['title'])
        self.assertContains(response, self.author1.name)

        # Check the book object
        book = Book.objects.get(pk=1)
        self.assertEqual(book.author, self.author1)
        self.assertEqual(book.title, 'Odyssey')

    def test_book_delete_view(self):
        self.login()
        Book.objects.create(**self.book1)
        self.assertEqual(reverse('book_delete', args='1'), '/book/1/delete')
        response = self.client.get('/book/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/book/1/delete')
        self.assertEqual(len(Book.objects.all()), 0)
