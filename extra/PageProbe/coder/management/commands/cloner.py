from django.core.management.base import BaseCommand, no_translations
from shutil import copyfile

from coder.cloner import generate_clone_code


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('CODE CLONER')

        generate_clone_code()
        # generate_note_code()
