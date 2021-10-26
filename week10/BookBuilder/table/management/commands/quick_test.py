from django.core.management.base import BaseCommand, no_translations

# from table.table import read_csv_file
from book.models import Chapter
from book.book import export_chapters, import_chapters
from book.models import Book
from coder.coder import generate_code


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Quick Test")

        generate_code()
