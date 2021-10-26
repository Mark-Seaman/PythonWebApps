from book.models import Chapter
from book.book import export_chapters, import_chapters
from book.models import Book


def generate_code():
    class_name = "Author"
    object_name = "author"
    print(f'Generating code \nClass: {class_name}, Object: {object_name}')
    # create_chapter_code()


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
