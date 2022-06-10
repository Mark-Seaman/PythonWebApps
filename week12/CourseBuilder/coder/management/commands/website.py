from django.core.management.base import BaseCommand
from traceback import format_exc

from course.website import create_static_site


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            build_course_websites()
        except:
            self.stdout.write(format_exc())


def build_course_websites():
    print('Build course websites')
    create_static_site('bacs200')
    create_static_site('bacs350')
