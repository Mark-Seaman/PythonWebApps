from django.template.loader import render_to_string
from os import listdir
from os.path import exists

# from course.lecture import course_lectures
# from course.slides import build_slides
# from course.view_data import project_data, weekly_lessons
# from tool.document import doc_path, file_to_html
# from tool.files import count_files, read_json, write_file
# from views.mybook import page_settings


# def course_json(course, filename="page_settings.json"):
#     json = doc_path(f'course/{course}/{filename}')
#     assert (exists(json))
#     settings = read_json(json)
#     assert (settings)
#     return settings


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
#     def make_title(t): return f"Lesson #{int(t[-2:])}"
#     create_pages(markdown_path, html_path, directory, make_title, course)


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


# def create_pages(markdown_path, html_path, directory, make_title, course):
#     md_path = f'{markdown_path}/{directory}'
#     assert (exists(md_path))

#     html_path = f'{html_path}/{directory}'
#     assert (exists(html_path))

#     settings = course_json(course)
#     for p in listdir(md_path):
#         x = p.replace('.md', '')
#         title = make_title(x)
#         save_page(f'{md_path}/{p}', f'{html_path}/{x}.html', title, settings)


def create_static_site(course):
    markdown_path = f'static/pages/{course}/markdown'
    website_path = f'static/pages/{course}'
    print(f'Build course {course}')
    # create_index_page(course)
    # create_lesson_pages(markdown_path, website_path, course)
    # create_doc_pages(markdown_path, website_path, course)
    # create_project_pages(markdown_path, website_path, course)
    # build_slides(markdown_path, website_path, course)
    # create_lecture_pages(course)
    # return count_files(website_path)


# def save_page(md, html, page_title, settings):
#     title = page_title
#     text = file_to_html(md, '../images')
#     settings.update(dict(page=md, text=text, page_title=title))
#     write_file(html, render_to_string('static_theme.html', settings))
