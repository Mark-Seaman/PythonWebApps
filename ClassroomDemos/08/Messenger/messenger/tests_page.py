from requests import get

from django.test import SimpleTestCase


class PageTest(SimpleTestCase):

    def get_page(self, page):
        digital_ocean = 'https://octopus-app-bndcn.ondigitalocean.app/person/1'
        response = get(f'{digital_ocean}/{page}')

    def test_default(self):
        self.get_page('')
        self.get_page('person/')
