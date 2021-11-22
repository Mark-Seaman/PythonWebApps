from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from book.book import import_all_books
from book.models import Author, Book, Chapter


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("IMPORT BOOKS")
        create_test_user()
        import_all_books()
        show_book_content()


def create_test_user():
    args = dict(username='seaman', email='me@here.com', password='secret')
    user = get_user_model().objects.filter(username='seaman')
    if user:
        user = user[0]
    else:
        user = get_user_model().objects.create_user(**args)
    return user, args


def show_book_content():
    for x in Author.objects.all():
        print(x)
    for x in Book.objects.all():
        print(x)
    for x in Chapter.objects.all():
        print(x)
    assert(len(Author.objects.all()) == 1)
    assert(len(Book.objects.all()) == 2)
    assert(len(Chapter.objects.all()) == 70)
