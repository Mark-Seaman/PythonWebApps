from django.core.management.base import BaseCommand

from course.website import create_website


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_website()
