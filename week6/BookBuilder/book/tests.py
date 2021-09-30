from book.models import Book
from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_num_book(self):
        self.assertEqual(len(Book.objects.all()), 0)

    def test_add_book(self):
        Book.objects.create(title='Tale of 2 Cities', author='Chuck Dickens')
        Book.objects.create(title='Iliad', author='Homer')
        self.assertEqual(len(Book.objects.all()), 2)

    def test_book_title(self):
        Book.objects.create(title='Iliad', author='Homer')
        b = Book.objects.get(pk=1)
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author, 'Homer')

    def test_book_edit(self):
        Book.objects.create(title='Iliad', author='Homer')
        b = Book.objects.get(pk=1)
        b.author = 'Mark Seaman'
        b.save()
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author, 'Mark Seaman')

    def test_book_edit(self):
        Book.objects.create(title='Iliad', author='Homer')
        b = Book.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Book.objects.all()), 0)

    def test_string_representation(self):
        book = Book.objects.create(title='Iliad', author='Homer')
        self.assertEqual(
            str(book), 'Iliad by Homer')


class BookViewsTests(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_get_absolute_url(self):
        book = Book.objects.create(title='Iliad', author='Homer')
        self.assertEqual(book.get_absolute_url(), '/book/1')

    def test_book_list_view(self):
        book = Book.objects.create(title='Iliad', author='Homer')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)


#from django.contrib.auth import get_user_model


# # -----------------------------------------------------
# #   B o o k

# class BookTests(TestCase):

#     def check_book_author(self, pk, name):
#         b = Book.objects.get(pk=pk)
#         self.assertEqual(b.author.name, name)

#     def check_book_title(self, pk, title):
#         b = Book.objects.get(pk=pk)
#         self.assertEqual(b.title, title)

#     def check_description(self, pk, text):
#         b = Book.objects.get(pk=pk)
#         self.assertEqual(b.description, text)

#     def check_num_books(self, num):
#         self.assertEqual(len(list_books()), num)

#     def setUp(self):
#         self.user = create_test_user()
#         author = add_author(self.user, 'Charles Dickens')
#         self.book = add_book('Tale of Two Cities', author)

#     def test_string_representation(self):
#         book = Book.objects.get(pk=1)
#         self.assertEqual(
#             str(book), '1 - Tale of Two Cities by Charles Dickens')

#     def test_book_content(self):
#         self.assertEqual(f'{self.book.title}', 'Tale of Two Cities')
#         self.assertEqual(f'{self.book.author.name}', 'Charles Dickens')
#         self.assertEqual(f'{self.book.description}', 'None')

#     def test_book_model(self):
#         self.check_num_books(1)
#         self.check_book_title(1, 'Tale of Two Cities')
#         self.check_book_author(1, 'Charles Dickens')

#     def test_create_book(self):
#         self.check_num_books(1)
#         author = get_author('Charles Dickens')
#         add_book('Christmas Carol', author)
#         self.check_num_books(2)
#         self.check_book_title(2, 'Christmas Carol')

#     def test_create_author(self):
#         jack = add_author(self.user, 'Jack London')
#         add_book('Sea Wolf', jack)
#         self.check_num_books(2)
#         self.check_book_author(2, 'Jack London')
#         self.check_book_title(2, 'Sea Wolf')

#     def test_list_books(self):
#         add_book('Sea Wolf', add_author(self.user, 'Jack London'))
#         add_book('1984', add_author(self.user, 'George Orwell'))
#         self.check_num_books(3)

#     def test_update_book(self):
#         self.check_num_books(1)
#         a = get_book('Tale of Two Cities')
#         a.title = 'Christmas Carol'
#         a.save()
#         self.check_book_title(1, 'Christmas Carol')
#         self.check_book_author(1, 'Charles Dickens')

#     def test_description(self):
#         self.check_description(1, None)
#         a = get_book('Tale of Two Cities')
#         a.description = 'This is a book description'
#         a.save()
#         self.check_description(1, 'This is a book description')

#     def test_delete_book(self):
#         delete_book('Tale of Two Cities')
#         self.check_num_books(0)


# # -----------------------------------------------------
# #   B o o k    V i e w s

# class BookViewsTests(TestCase):

#     def create_test_user(self):
#         args = dict(username='TEST_DUDE',
#                     email='me@here.com', password='secret')
#         self.user = get_user_model().objects.create_user(**args)

#     def login(self):
#         response = self.client.login(username='TEST_DUDE', password='secret')
#         self.assertEqual(response, True)

#     def setUp(self):
#         self.create_test_user()
#         self.author = add_author(self.user, 'Charles Dickens')
#         self.book = add_book('Tale of Two Cities', self.author)
#         self.login()

#     def test_get_absolute_url(self):
#         self.assertEqual(self.book.get_absolute_url(), '/book/1')

#     def test_book_list_view(self):
#         response = self.client.get(reverse('book_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Tale of Two Cities')
#         self.assertContains(response, '<li>', count=1)
#         self.assertTemplateUsed(response, 'book_list.html')
#         self.assertTemplateUsed(response, 'book_theme.html')

#     def test_book_detail_view(self):
#         response = self.client.get('/book/1')
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Charles Dickens')
#         self.assertContains(response, 'Tale of Two Cities')
#         self.assertContains(response, 'No description')
#         self.assertTemplateUsed(response, 'book_detail.html')
#         no_response = self.client.get('/book/100000')
#         self.assertEqual(no_response.status_code, 404)

#     def test_book_create_view(self):
#         new_book = dict(title="Sea Wolf", description='No big deal')
#         response = self.client.post(reverse('book_add'), new_book)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(len(Book.objects.all()), 2)
#         book = Book.objects.last()
#         self.assertEqual(book.author.name, 'Charles Dickens')
#         self.assertEqual(book.title, 'Sea Wolf')
#         self.assertEqual(book.description, 'No big deal')

#     def test_book_update_view(self):
#         kwargs = dict(title='Lord of the Rings', description='Great story')
#         response = self.client.post(reverse('book_edit', args='1'), kwargs)
#         self.assertEqual(response.status_code, 302)
#         b = Book.objects.get(pk=1)
#         self.assertEqual(b.title, 'Lord of the Rings')

#     # def test_book_delete_view(self):
#     #     response = self.client.post(reverse('book_delete', args='1'))
#     #     self.assertEqual(response.status_code, 302)
