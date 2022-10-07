from django.core.management.base import BaseCommand
from requests import get


def get_web_page(url):
    response = get(url)
    p = f"URL: {url},"
    s = f"Status Code: {response.status_code},"
    t = response.text
    c = f"Text: {len(t)} characters"
    print(p, s, c)


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_web_page("https://shrinking-world.com")
        get_web_page("http://google.com")
