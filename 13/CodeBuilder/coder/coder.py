from asyncio import tasks
from shutil import copyfile, copytree
from pathlib import Path
from os import system
from django.shortcuts import render


def build_code():
    print('build_code()')
    # generate_software_planner()
    # generate_static_site
    # generate_course()
    # generate_messenger()
    # generate_blog()
    # generate_book()
    generate_hero()


def generate_hero():
    project_path = Path('/Users/seaman/Github/PythonWebApps/')
    project_name = 'Superhero'
    project_app = 'hero'
    project_path = create_new_project(project_path, project_name)
    generate_data_type(project_path, project_app, 'Superhero', "hero")


def generate_book():
    project_path = Path('/Users/seaman/Github/PythonWebApps/11')
    project_name = 'Book'
    project_app = 'book'
    project_path = create_new_project(project_path, project_name)
    generate_data_type(project_path, project_app, 'Author', "author")
    generate_data_type(project_path, project_app, 'Book', "book")
    generate_data_type(project_path, project_app, 'Chapter', "chapter")


def generate_blog():
    project_path = Path('/Users/seaman/Github/PythonWebApps/08')
    project_name = 'Blog'
    project_app = 'blog'
    project_path = create_new_project(project_path, project_name)
    generate_data_type(project_path, project_app, 'Blog', "blog")
    generate_data_type(project_path, project_app, 'Article', "article")


def generate_messenger():
    project_path = Path('/Users/seaman/Github/PythonWebApps/08')
    project_name = 'Messenger'
    project_app = 'messenger'
    project_path = create_new_project(project_path, project_name)
    # create_new_app(project_path, project_app)
    generate_data_type(project_path, project_app, 'Person', "person")
    generate_data_type(project_path, project_app, 'Message', "message")
    system(f'tree {project_path}')


def generate_static_site():
    project_path = Path('/Users/seaman/Github/PythonWebApps/12')
    project_name = 'StaticSite'
    project_app = 'course'
    project_path = create_new_project(project_path, project_name)
    # create_new_app(project_path, project_app)
    generate_data_type(project_path, project_app, 'Lesson', "lesson")
    system(f'tree {project_path}')


def generate_software_planner():
    project_path = Path('/Users/seaman/Github/PythonWebApps/14')
    project_name = 'SoftwarePlanner'
    project_app = 'plan'
    project_path = create_new_project(project_path, project_name)
    # create_new_app(project_path, project_app)
    # generate_data_type(project_path, project_app, 'Milestone', "milestone")
    generate_data_type(project_path, project_app, 'Task', "task")
    system(f'tree {project_path}')


def generate_course():
    project_path = Path('/Users/seaman/Github/PythonWebApps/15')
    project_name = 'Course'
    project_app = 'course'
    project_path = create_new_project(project_path, project_name)
    generate_data_type(project_path, project_app, 'Student', "student")
    system(f'tree {project_path}')


def clone_code(project, object_name, class_name, module_name):

    def prototypes_list():
        prototypes = Path('prototype').rglob('*')
        prototypes = [p for p in prototypes if not ('project' in str(p))]
        prototypes = [p for p in prototypes if p.is_file()]
        return prototypes

    def create_file_protoype(f1):
        f1 = f'{f1}'
        f2 = f1.replace('object_instance', object_name)
        if not 'xxx' in f2:
            base = 'prototype'
            f2 = f2.replace(base, module_name)
            f2 = f'{project}/{f2}'
            convert_file(f1, f2, module_name, object_name, class_name)

    def convert_file(f1, f2, module2, object2, class2):
        print(f'   {f1}  -->  {f2}')
        if not Path(f2).exists():

            object1 = 'object_instance'
            class1 = 'ClassName'
            module1 = 'prototype'

            text = open(f1).read()
            text = text.replace(object1, object2)
            text = text.replace(class1, class2)
            text = text.replace(module1, module2)
            open(f2, 'w').write(text)

    print(f'\n\nGenerating code\n    Class: {class_name}\n    Object: {module_name}\n')

    for f1 in prototypes_list():
        create_file_protoype(f1)


def create_directory(path):
    if not path.exists():
        if not path.parent.exists():
            path.parent.mkdir()
            print('Create ', path.parent)
        path.mkdir()
        print('Create ', path)
    return path


def create_new_project(project_path, project_name):

    def create_config(project_path):
        create_directory(project_path)
        if not (project_path/'config').exists():
            print(f'cd {project_path} && django-admin startproject config .')
            system(f'cd {project_path} && django-admin startproject config .')
            print(f'Create {project_path/"config"}')
        return project_path

    def clone_project_files(path):
        prototypes = Path('prototype/project').glob('*')
        for p in prototypes:
            if not ('config' in str(p)):
                path_name = path / p.name
                if p.is_dir() and not path_name.exists():
                    copytree(p, path_name)
                if p.is_file() and not path_name.exists():
                    copyfile(p, path_name)

        prototypes = Path('prototype/project/config').glob('*')
        for p in prototypes:
            path_name = path / 'config' / p.name
            if p.is_file() and not path_name.exists():
                copyfile(p, path_name)

    project_path = project_path / project_name
    create_config(project_path)
    clone_project_files(project_path)
    return project_path


def create_new_app(path, app):
    if not (path / app).exists():
        system(f'cd {path} && python manage.py startapp {app}')
        print(f'Create app {path / app}')
    return path


def generate_data_type(project_path, project_app, class_name='Xxx', object_name='xxx'):
    create_new_app(project_path, project_app)
    create_directory(project_path / project_app / 'templates')
    create_directory(project_path / project_app / 'templates' / object_name)
    clone_code(project_path, object_name, class_name, project_app)
