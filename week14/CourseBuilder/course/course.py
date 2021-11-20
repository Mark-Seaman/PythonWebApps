from django.contrib.auth import get_user_model
from os.path import exists
from markdown import markdown

from .models import Author, Course, Lesson
from table.table import read_csv_file, write_csv_file


def create_author(name):
    user = get_user_model().objects.get(pk=1)
    return Author.objects.get_or_create(name=name, user=user)[0]


def export_all_courses():
    for b in Course.objects.all():
        export_lessons(b)


def export_lessons(course):
    model = Lesson
    lessons = f'{course.doc_path}/lessons.csv'
    records = [o.export_record() for o in model.objects.filter(course=course.title)]
    write_csv_file(lessons, records)


def get_author(name):
    return Author.objects.get(name=name)


def get_course(title):
    return Course.objects.get(title=title)


def get_lesson(course, order):
    c = Lesson.objects.get(course=course, order=order)
    c.markdown = open(f'{course.doc_path}/{c.document}').read()
    c.html = markdown(c.markdown)
    c.save()
    return c


def create_bacs200():
    author = create_author('Mark Seaman')
    c = Course.create(name='bacs200',
                      title='UNC BACS 200 - Intro to Web Development',
                      subtitle='Intro to Web Development for Small Business',
                      author=author,
                      doc_path='Documents/Course/bacs200',
                      description='None',
                      num_projects=14,
                      num_lessons=42)
    return c


def create_bacs350():
    author = create_author('Mark Seaman')
    c = Course.create(name='bacs350',
                      title='UNC BACS 350 - Web Apps with Python',
                      subtitle='Intermediate Web Development',
                      author=author,
                      doc_path='Documents/Course/bacs350',
                      description='None',
                      num_projects=14,
                      num_lessons=42)
    return c


def import_all_courses():
    author = create_author('Mark Seaman')
    import_course(create_bacs200())
    import_course(create_bacs350())


def import_course(course):
    print(f'Importing course "{course.title}"')


# def import_lessons(course):
#     model = Lesson
#     lessons = f'{course.doc_path}/lessons.csv'
#     # print(lessons)
#     assert(exists(lessons))
#     if exists(lessons):
#         for row in read_csv_file(lessons):
#             # print(row)
#             model.import_record(course, row)
