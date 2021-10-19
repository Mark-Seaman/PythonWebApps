from django.core.management.base import BaseCommand, no_translations

# from table.table import read_csv_file
from book.models import Chapter
from table.table import import_chapters
from book.models import Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Quick Test")

        # path = 'Documents/objects.csv'
        # print(read_csv_file(path))

        # Chapter.import_record(['Leverage Principle', '1', 'The Leverage Principle', '4866'])
        # print(len(Chapter.objects.all()))

        Chapter.objects.all().delete()

        book = Book.objects.get_or_create(title="The Leverage Principle", author='Mark Seaman')[0]
        import_chapters(book)
        chapters = Chapter.objects.all()
        for c in chapters:
            print(c.export_record())
