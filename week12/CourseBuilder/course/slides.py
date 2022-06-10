from os import listdir
from os.path import exists

from django.template.loader import render_to_string

from tool.document import fix_images, read_markdown
from tool.files import write_file, read_json
from tool.text import text_join, text_lines


def build_slides(markdown_path, website_path, course):

    def build_slide_deck(slides_file, markdown_file, **kwargs):
        text = read_markdown(markdown_file)
        text = render_slides(text, **kwargs)
        template_name = 'course_slides.html'
        kwargs['text'] = text
        html = render_to_string(template_name, kwargs)
        write_file(slides_file, html)

    markdown = f'{markdown_path}/lesson'
    assert (exists(markdown))

    slides = f'{website_path}/slides'
    assert (exists(slides))

    json = f'Documents/course/{course}/slides_settings.json'
    assert (exists(json))
    settings = read_json(json)
    assert (settings)

    for s in listdir(markdown):
        lesson = s.replace('.md', '')
        settings['lesson'] = lesson
        markdown_file = f'{markdown}/{s}'
        slides_file = f'{slides}/{lesson}.html'
        build_slide_deck(slides_file, markdown_file, **settings)


def render_slides(text, **kwargs):

    def slides_text(text):
        slides = ['### ' + s for s in text.split('### ')[1:]]
        return slides

    def create_slide_section(title, body):
        return dict(title=title, text=body, slides=slides_text(body))

    def render_sections(markdown_text):
        output = []
        sections = markdown_text.split("\n## ")
        for text in sections:
            body = fix_images(text, '../images')
            title = text_lines(text)[0]
            settings = create_slide_section(title, body)
            output.append(settings)
        return output

    def render_section(section, kwargs):
        kwargs.update(section)
        return render_to_string("slides_section.html", kwargs)

    return text_join([render_section(s, kwargs) for s in render_sections(text)][1:])


def slides_view_data(kwargs):
    course = kwargs.get('course')
    lesson = kwargs.get('lesson')
    json = f'Documents/course/{course}/slides_server.json'
    settings = read_json(json)
    kwargs.update(settings)
    page = f'Documents/course/{course}/lesson/{lesson:02}'
    title = f'{course} - Lesson {lesson} - Slides'
    md_path = f'static/pages/{course}/markdown/lesson/{lesson:02}.md'
    text = render_slides(read_markdown(md_path), **kwargs)
    kwargs.update(dict(server=True, page=page, title=title, text=text))
    return kwargs
