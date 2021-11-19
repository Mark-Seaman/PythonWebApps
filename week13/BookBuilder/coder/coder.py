from django.contrib.auth import get_user_model

from book.book import import_all_books
from book.models import Book
from pprint import pformat


def create_test_user():
    args = dict(username='seaman', email='me@here.com', password='secret')
    user = get_user_model().objects.filter(username='seaman')
    if user:
        user = user[0]
    else:
        user = get_user_model().objects.create_user(**args)
    return user, args


def quick_test():
    print("QUICK TEST")
    # initialize_database()


def initialize_database():
    create_test_user()
    import_all_books()


def test_values():
    # Query for books
    books = Book.objects.all()

    # Convert to values list
    for book in books.values_list():
        print(book)

    # Convert to dictionary
    for book in books.values():
        print(book)

    # Print with indents
    print(pformat(book, indent=4))
