from django.contrib.auth import get_user_model

from book.book import import_all_books


def create_test_user():
    args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
    user = get_user_model().objects.filter(username='TEST_DUDE')
    if user:
        user = user[0]
    else:
        user = get_user_model().objects.create_user(**args)
    return user, args


def quick_test():
    print("QUICK TEST")

    initialize_database()

    # print("Do nothing")
    # generate_code()


def initialize_database():
    create_test_user()
    import_all_books()


def generate_code():
    class_name = "Author"
    object_name = "author"
    old_class = 'Book'
    old_object = 'book'
    clone_code(class_name, object_name, old_class, old_object)


def clone_code(class_name, object_name, old_class, old_object):

    def file_list():
        return f'''{old_object}/urls_{old_object}.py
{old_object}/views_{old_object}.py
{old_object}/tests_{old_object}.py
templates/{old_object}_add.html
templates/{old_object}_delete.html
templates/{old_object}_detail.html
templates/{old_object}_edit.html
templates/{old_object}_list.html'''

    print(f'Generating code \nClass: {class_name}, Object: {object_name}')
    for f in file_list().split('\n'):
        new_file = f.replace(old_object, object_name).replace(f'{object_name}/', f'{old_object}/')
        text = open(f).read()
        text = text.replace(old_object, object_name)
        text = text.replace(old_class, class_name)
        open(new_file, 'w').write(text)
        print(f'Create {new_file} from {f}')
