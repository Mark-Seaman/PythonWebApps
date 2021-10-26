def quick_test():
    print("QUICK TEST")
    print("Do nothing")
    # generate_code()


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
