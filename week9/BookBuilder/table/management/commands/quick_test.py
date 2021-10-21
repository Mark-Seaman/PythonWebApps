from django.core.management.base import BaseCommand, no_translations

# from table.table import read_csv_file
from book.models import Chapter
from book.book import export_chapters, import_chapters
from book.models import Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Quick Test")

        create_chapter_code()


def create_chapter_code():
    print('Create chapter code')
    file_list = '''book/views_book.py
book/tests_book.py
templates/book_add.html
templates/book_delete.html
templates/book_detail.html
templates/book_edit.html
templates/book_list.html'''
    for f in file_list.split('\n'):
        new_file = f.replace('book', 'chapter').replace('chapter/', 'book/')
        text = open(f).read()
        text = text.replace('book', 'chapter')
        text = text.replace('Book', 'Chapter')
        open(new_file, 'w').write(text)
        print(f, new_file)
