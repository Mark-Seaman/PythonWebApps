from django.core.management.base import BaseCommand
from json import loads
from pathlib import Path

from hero.models import Superhero


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data()


def load_data():
    # Delete the old objects
    Superhero.objects.all().delete()

    # Read the JSON file
    path = Path('hero_objects.json')
    if path.exists():
        objects = loads(path.read_text())

    # Create new objects
    for o in objects:
        Superhero.objects.get_or_create(**o)

    # Show the objects
    for hero in Superhero.objects.all().values():
        print(hero)
