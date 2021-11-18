from django.contrib.auth import get_user_model
from os.path import exists
from markdown import markdown

from .models import Author, Course, Lesson
from table.table import read_csv_file, write_csv_file


# def create_book(**kwargs):
#     name = kwargs.get('name')
#     author = kwargs.get('author')
#     book = Course.objects.get_or_create(name=name, author=author)[0]
#     book.doc_path = kwargs.get('doc_path')
#     book.title = kwargs.get('title')
#     book.description = kwargs.get('description')
#     book.save()
#     return book


def create_author(name):
    user = get_user_model().objects.get(pk=1)
    return Author.objects.get_or_create(name=name, user=user)[0]


def export_all_books():
    for b in Course.objects.all():
        export_chapters(b)


def export_chapters(book):
    model = Lesson
    chapters = f'{book.doc_path}/chapters.csv'
    records = [o.export_record() for o in model.objects.filter(book=book.title)]
    write_csv_file(chapters, records)


def get_author(name):
    return Author.objects.get(name=name)


def get_book(title):
    return Course.objects.get(title=title)


def get_chapter(book, order):
    c = Lesson.objects.get(book=book, order=order)
    c.markdown = open(f'{book.doc_path}/{c.document}').read()
    c.html = markdown(c.markdown)
    c.save()
    return c


def import_all_books():
    author = create_author('Mark Seaman')
    import_book("The Leverage Principle", author, 'Documents/Leverage', "Software Engineering Skills")
    description = 'Mark shares his insights and irony about the absurdity of life.'
    import_book("From the Edge of Reality", author, 'Documents/Poems', "A Seaman's Poems", description)


def import_book(title, author, doc_path, subtitle='None', description='None'):
    args = dict(title=title, author=author, subtitle=subtitle, description=description, doc_path=doc_path)
    book = create_book(**args)
    import_chapters(book)


def import_chapters(book):
    model = Lesson
    chapters = f'{book.doc_path}/chapters.csv'
    # print(chapters)
    assert(exists(chapters))
    if exists(chapters):
        for row in read_csv_file(chapters):
            # print(row)
            model.import_record(book, row)
