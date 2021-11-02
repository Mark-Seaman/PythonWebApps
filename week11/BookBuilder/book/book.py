from os.path import exists

from django.contrib.auth import get_user_model

from book.models import Author, Book, Chapter
from table.table import read_csv_file, write_csv_file


def create_book(**kwargs):
    title = kwargs.get('title')
    author = kwargs.get('author')
    book = Book.objects.get_or_create(title=title, author=author)[0]
    book.doc_path = kwargs.get('doc_path')
    book.description = kwargs.get('description')
    book.save()
    return book


def create_author(name):
    user = get_user_model().objects.get(pk=1)
    return Author.objects.get_or_create(name=name, user=user)[0]


def export_chapters(book):
    model = Chapter
    chapters = f'{book.doc_path}/chapters.csv'
    records = [o.export_record() for o in model.objects.filter(book=book.title)]
    write_csv_file(chapters, records)


def get_book(title):
    return Book.objects.get(title=title)


def get_author(name):
    return Author.objects.get(name=name)


def get_chapter(book, order):
    return Chapter.objects.get(book=book, order=order)


def import_chapters(book):
    model = Chapter
    chapters = f'{book.doc_path}/chapters.csv'
    # print(chapters)
    assert(exists(chapters))
    if exists(chapters):
        for row in read_csv_file(chapters):
            # print(row)
            model.import_record(book, row)


def import_leverage_book():
    author = create_author('Mark Seaman')
    book = dict(title="The Leverage Principle",
                author=author,
                description="Software Engineering Skills",
                doc_path='Documents/Leverage')
    b = create_book(**book)
    import_chapters(b)


def import_poems_book():
    author = create_author('Mark Seaman')
    book = dict(title="A Seaman's Poems",
                author=author,
                description="From the Edge of Reality",
                doc_path='Documents/Poems')
    b = create_book(**book)
    import_chapters(b)


def import_all_books():
    import_leverage_book()
    import_poems_book()
