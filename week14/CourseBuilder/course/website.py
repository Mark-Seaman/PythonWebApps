from django.template.loader import render_to_string
from os import listdir, mkdir
from os.path import dirname, exists
from json import loads
from markdown import markdown


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


def create_index_page(md_path, html_path, doc_type, course):
    def link(page):
        lesson = page.replace(".md", "")
        return f'* [Lesson {lesson}]({lesson}.html)\n'

    settings = course_json(course)
    title = f'{course.upper()} Lesson Index'
    index_text = f'# {title}\n\n'
    for p in sorted(listdir(md_path)):
        index_text += link(p)

    md_path = f'{md_path}/index.md'
    html_path = f'{html_path}/index.html'

    open(md_path, 'w').write(index_text)
    save_page(md_path, html_path, title, doc_type, settings)


def create_pages(markdown_path, html_path, directory, doc_type, course):
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

    create_index_page(md_path, html_path, doc_type, course)

    for p in listdir(md_path):
        x = p.replace('.md', '')
        title = f'{doc_type} {x}'
        save_page(f'{md_path}/{p}', f'{html_path}/{x}.html', title, doc_type, settings)


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

    create_pages(markdown_path, website_path, 'lesson', 'Lesson', course)
    create_pages(markdown_path, website_path, 'project', 'Project', course)
    create_pages(markdown_path, website_path, 'docs', 'Document', course)

    # create_doc_pages(markdown_path, website_path, course)
    # create_project_pages(markdown_path, website_path, course)
    # build_slides(markdown_path, website_path, course)
    # create_lecture_pages(course)
    # return count_files(website_path)


def save_page(md, html, page_title, doc_type, settings):

    def write_html_file(path, html):
        if not exists(dirname(path)):
            mkdir(dirname(path))
        open(path, 'w').write(html)

    def render_page(settings):
        return render_to_string('static_theme.html', settings)

    title = page_title
    text = markdown(open(md).read())
    settings.update(dict(page=md, text=text, page_title=title, doc_type=doc_type))
    # print('write_html_file', md, html)
    write_html_file(html, render_page(settings))
