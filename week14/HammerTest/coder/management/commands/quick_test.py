from django.core.management.base import BaseCommand, no_translations
from coder.coder import quick_test


class Command(BaseCommand):

    def handle(self, *args, **options):
        quick_test()
