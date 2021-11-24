from shutil import copyfile


def clone_code(object1, object2, class1, class2, module1, module2):
    print(f'\n\nGenerating code \nClass: {class2}, Object: {object2}\n')
    # copyfile(f'{module1}/urls_{object1}.py', f'{module1}/urls_{old_object}.py')
    for f1 in file_list(object1).split('\n'):
        f2 = f1.replace(object1, object2)
        f2 = f2.replace(module1, module2)
        f2 = f2.replace(f'{module2}/templates', f'templates')
        convert_file(f1, f2, object1, object2, class1, class2, module1, module2)


def convert_file(f1, f2, object1, object2, class1, class2, module1, module2):
    text = open(f1).read()
    text = text.replace(object1, object2)
    text = text.replace(class1, class2)
    text = text.replace(module1, module2)
    open(f2, 'w').write(text)
    print(f'{f1}  -->  {f2}')
    # print(text)


def file_list(old_object):
    return f'''coder/prototype/urls_{old_object}.py
coder/prototype/views_{old_object}.py
coder/prototype/tests_{old_object}.py
coder/prototype/templates/{old_object}_add.html
coder/prototype/templates/{old_object}_delete.html
coder/prototype/templates/{old_object}_detail.html
coder/prototype/templates/{old_object}_edit.html
coder/prototype/templates/{old_object}_list.html'''


def generate_clone_code():

    class_name = "DataFactory"
    object_name = "factory"
    module_name = 'coder'

    old_class = 'ClassName'
    old_object = 'object_instance'
    old_module = 'coder/prototype'

    clone_code(old_object, object_name, old_class, class_name, old_module, module_name)


def generate_image_code():
    class_name = "Image"
    object_name = "image"
    old_class = 'Book'
    old_object = 'book'
    clone_code(class_name, object_name, old_class, old_object)
