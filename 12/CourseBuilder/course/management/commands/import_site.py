from django.core.management.base import BaseCommand

from course.website import import_course


class Command(BaseCommand):

    def handle(self, *args, **options):
        import_course()
