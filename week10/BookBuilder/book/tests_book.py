from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from book.models import Author, Book, Chapter
from book.book import import_poems_book, import_leverage_book


def create_test_user():
    # args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
    # user = get_user_model().objects.create_user(**args)
    # return user, args
    args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
    return get_user_model().objects.create_user(**args)


class BookDataTest(TestCase):

    def setUp(self):
        self.user = create_test_user()
        # self.user, self.user_args = create_test_user()

        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.book1 = dict(title='Tale of 2 Cities', author=self.author1)
        self.book2 = dict(title='Iliad', author=self.author2)

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

    def test_import_leverage(self):
        import_leverage_book()
        # print(Author.objects.all())
        # print(Book.objects.all())
        # print(Chapter.objects.all())
        self.assertEqual(len(Author.objects.all()), 3)
        self.assertEqual(len(Book.objects.all()), 1)
        self.assertEqual(len(Chapter.objects.all()), 14)

    def test_import_poems(self):
        import_poems_book()
        # print(Author.objects.all())
        # print(Book.objects.all())
        # print(Chapter.objects.all())
        self.assertEqual(len(Author.objects.all()), 3)
        self.assertEqual(len(Book.objects.all()), 1)
        self.assertEqual(len(Chapter.objects.all()), 56)


class BookViewsTest(TestCase):

    def login(self):
        # response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        response = self.client.login(username='TEST_DUDE', password='secret')

        self.assertEqual(response, True)

    def setUp(self):
        self.user = create_test_user()
        # self.user, self.user_args = create_test_user()

        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.book1 = dict(title='Iliad', author_id=self.author1.pk, description='description', doc_path='Documents')
        self.book2 = dict(title='Odyssey', author_id=self.author2.pk, description='None', doc_path='Documents')

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
        # Book.objects.create(**self.book1)

        # Add without Login
        response = self.client.post(reverse('book_add'), self.book2)
        self.assertEqual(response.url, '/accounts/login/?next=/book/add')

        # Login to add
        # self.login()
        response = self.client.login(username='TEST_DUDE', password='secret')
        self.assertEqual(response, True)

        response = self.client.post(reverse('book_add'), self.book1)
        response = self.client.post(reverse('book_add'), self.book2)
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response.url, '/book/2')

        # # List the books
        response = self.client.get('/book/')
        self.assertContains(response, '<tr>', count=3)

#     def test_book_edit_view(self):
#         Book.objects.create(**self.book1)

#         # Edit without Login
#         self.assertEqual(reverse('book_edit', args='1'), '/book/1/')
#         response = self.client.get('/book/1/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/accounts/login/?next=/book/1/')

#         # Login to edit
#         self.login()
#         response = self.client.post('/book/1/', self.book2)

#         # Check the redirect
#         self.assertEqual(response.url, '/book/1')
#         response = self.client.get(response.url)
#         self.assertContains(response, 'Darth Vadar')

#         # Check the book object
#         book = Book.objects.get(pk=1)
#         self.assertEqual(book.author, 'Darth Vadar')
#         self.assertEqual(book.title, 'Star Wars')

#     def test_book_delete_view(self):
#         Book.objects.create(**self.book1)

#         self.login()
#         self.assertEqual(reverse('book_delete', args='1'), '/book/1/delete')
#         response = self.client.get('/book/1/delete')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post('/book/1/delete')
#         self.assertEqual(len(Book.objects.all()), 0)
