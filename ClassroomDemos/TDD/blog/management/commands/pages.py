from django.core.management.base import BaseCommand

from requests import get


class Command(BaseCommand):

    def handle(self, *args, **options):

        response = get('https://shrinking-world.com')
        print(response)
        msg = f'Shrinking World: {len(response.text)} characters'
        print(msg)
