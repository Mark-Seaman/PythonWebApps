from django.template.loader import render_to_string
from os import listdir, mkdir
from os.path import dirname, exists
from json import loads
from markdown import markdown

# from course.lecture import course_lectures
# from course.slides import build_slides
# from course.view_data import project_data, weekly_lessons
# from tool.document import doc_path, file_to_html
# from tool.files import count_files, read_json, write_file
# from views.mybook import page_settings


def course_json(course, filename="page_settings.json"):
    def read_json(filename):
        if exists(filename):
            return loads(open(filename).read())
        return {}

    json = f'Documents/course/{course}/{filename}'
    assert (exists(json))
    settings = read_json(json)
    assert (settings)
    return settings


# def create_doc_pages(markdown_path, html_path, course):
#     directory = 'docs'
#     def make_title(t): return t
#     create_pages(markdown_path, html_path, directory, make_title, course)


# def create_index_page(course):
#     settings = course_json(course)
#     weekly = weekly_lessons(course)
#     projects = project_data(course)
#     settings.update(dict(css='unc.css',
#                          logo='images/Bear.png',
#                          site_url='index.html',
#                          weekly=weekly,
#                          projects=projects))

#     template_name = 'course_website.html'
#     html_path = f'static/pages/{course}/index.html'

#     html = render_to_string(template_name, settings)
#     write_file(html_path, html)


# def create_lesson_pages(markdown_path, html_path, course):
#     directory = 'lesson'
#     print('\ncreate_pages', markdown_path, html_path, directory, course)
#     print()
#     # def make_title(t): return f"Lesson #{int(t[-2:])}"
#     # create_pages(markdown_path, html_path, directory, make_title, course)


# def create_lecture_pages(course):
#     settings = course_json(course)
#     for lecture in course_lectures(course):
#         url = '../index.html'
#         page = f'Lecture {lecture.lesson.lesson}'
#         settings.update(page_settings(page=page, course=course, url=url, lecture=lecture))

#         template_name = 'course_website.html'
#         html_path = f'static/pages/{course}/lecture/{lecture.lesson.lesson:02d}.html'
#         settings['cover'] = None

#         html = render_to_string(template_name, settings)
#         write_file(html_path, html)


# def create_project_pages(markdown_path, html_path, course):
#     directory = 'project'
#     def make_title(t): return f"Project #{int(t[-2:])}"
#     create_pages(markdown_path, html_path, directory, make_title, course)


def create_pages(markdown_path, html_path, directory, course):
    md_path = f'{markdown_path}/{directory}'
    assert (exists(md_path))

    html_path = f'{html_path}/{directory}'
    if not exists(html_path):
        mkdir(html_path)
    assert (exists(html_path))

    print('\ncreate_pages', markdown_path, html_path, directory, course)
    print()

    settings = course_json(course)
    print(settings)
    print()

    for p in listdir(md_path):
        x = p.replace('.md', '')
        title = f'Lesson {x}'
        save_page(f'{md_path}/{p}', f'{html_path}/{x}.html', title, settings)


def create_static_site(course):
    markdown_path = f'Documents/course/{course}'
    website_path = f'Documents/Pages/course/{course}'
    print(f'Build course {course}')

    # Make directories
    print('    ', markdown_path)
    print('    ', website_path)
    if not exists(f'Documents/Pages/course'):
        mkdir(f'Documents/Pages/course')
    if not exists(f'Documents/Pages/course/{course}'):
        mkdir(f'Documents/Pages/course/{course}')
    if not exists(website_path):
        mkdir(website_path)

    # create_index_page(course)
    create_pages(markdown_path, website_path, 'lesson', course)
    # create_doc_pages(markdown_path, website_path, course)
    # create_project_pages(markdown_path, website_path, course)
    # build_slides(markdown_path, website_path, course)
    # create_lecture_pages(course)
    # return count_files(website_path)


def save_page(md, html, page_title, settings):
    # def file_to_html(path, image_path=None):
    #     if exists(path):
    #         # return text_to_html(fix_images(read_markdown(path), image_path))
    #     else:
    #         return 'No file found, ' + path

    def write_html_file(path, html):
        if not exists(dirname(path)):
            mkdir(dirname(path))
        open(path, 'w').write(html)

    title = page_title
    text = markdown(open(md).read())
    settings.update(dict(page=md, text=text, page_title=title))
    print('write_html_file', md, html)
    write_html_file(html, render_to_string('static_theme.html', settings))
