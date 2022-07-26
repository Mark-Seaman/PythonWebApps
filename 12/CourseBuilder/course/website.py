from pathlib import Path
from django.template.loader import render_to_string
from shutil import copyfile

from .models import Lesson
from .views import get_document


def create_website():

    def render_page(page):
        template = 'lesson/detail.html'
        data = dict(lesson=page.pk, lessons=Lesson.objects.all(), body=get_document(page))
        return render_to_string(template, data)

    print('create the website')
    p = Path('Website')
    if not p.exists():
        p.mkdir()
    copyfile('static/style.css', p/'style.css')
    for page in Lesson.objects.all():
        print(page.title)
        output_path = str(page.document).replace('Documents', 'Website').replace('.md', '.html')
        print(output_path)
        Path(output_path).write_text(render_page(page))


def import_course():

    def get_lesson(i, path):
        lesson = Lesson.objects.get_or_create(pk=i+1)[0]
        lesson.title = get_title(path)
        lesson.save()
        return lesson

    def get_title(doc):
        if not doc.exists():
            return f'Document not found, {doc}'
        return doc.read_text().split('\n')[0][10:]

    print('import the course')
    for i, doc in enumerate(sorted(Path('Documents/').iterdir())):
        lesson = get_lesson(i, doc)
        print(lesson)
