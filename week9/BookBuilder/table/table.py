from csv import reader, writer

from os.path import exists

from book.models import Chapter


def export_chapters(book):
    model = Chapter
    chapters = f'{book.doc_path}/chapters.csv'
    records = [o.export_record() for o in model.objects.filter(book=book.title)]
    write_csv_file(chapters, records)


def import_chapters(book):
    model = Chapter
    chapters = f'{book.doc_path}/chapters.csv'
    if exists(chapters):
        with open(chapters) as f:
            for row in reader(f):
                model.import_record([book.title] + row)


def read_csv_file(path):
    with open(path) as f:
        return [row for row in reader(f)]


def write_csv_file(path, table):
    with open(path, 'w', newline='') as f:
        writer(f).writerows(table)
