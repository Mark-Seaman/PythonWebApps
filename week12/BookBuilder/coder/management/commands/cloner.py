from django.core.management.base import BaseCommand, no_translations
from shutil import copyfile


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('CODE CLONER')
        print(file_list('book'))

        generate_code()


def file_list(old_object):
    return f'''{old_object}/urls_{old_object}.py
{old_object}/views_{old_object}.py
{old_object}/tests_{old_object}.py
templates/{old_object}_add.html
templates/{old_object}_delete.html
templates/{old_object}_detail.html
templates/{old_object}_edit.html
templates/{old_object}_list.html'''


def generate_code():
    class_name = "Note"
    object_name = "note"
    old_class = 'Book'
    old_object = 'book'
    clone_code(class_name, object_name, old_class, old_object)


def clone_code(class_name, object_name, old_class, old_object):
    print(f'\n\nGenerating code \nClass: {class_name}, Object: {object_name}\n')
    copyfile(f'{old_object}/urls.py', f'{old_object}/urls_{old_object}.py')
    for f in file_list(old_object).split('\n'):
        new_file = f.replace(old_object, object_name).replace(f'{object_name}/', f'{old_object}/')
        convert_file(f, new_file, old_object, object_name, old_class, class_name)


def convert_file(f1, f2, object1, object2, class1, class2):
    text = open(f1).read()
    text = text.replace(object1, object2)
    text = text.replace(class1, class2)
    open(f2, 'w').write(text)
    print(f'{f1}  -->  {f2}')
