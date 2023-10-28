from django.core.management.base import BaseCommand
from blog.page import get_web_page


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_web_page("https://shrinking-world.com")
        get_web_page("http://google.com")
