from django.test import TestCase


class ViewTest(TestCase):

    def test_html_page_view(self):
        response = self.client.get('/')
        self.assertContains(response, 'home')

        response = self.client.get('/home.html')
        self.assertContains(response, 'Home Page')

        response = self.client.get('/theme.html')
        self.assertContains(response, 'View Workshop Demo App')

        response = self.client.get('/page.html')
        self.assertContains(response, 'Generic HTML Page')

    def test_card_view(self):
        response = self.client.get('/card')
        self.assertContains(response, 'Card Four')

    def test_document_view(self):
        response = self.client.get('/doc/')
        self.assertContains(response, 'Doc Index')

    def test_tabs_view(self):
        response = self.client.get('/tabs')
        self.assertContains(response, 'Card Four')

    def test_accordion_view(self):
        response = self.client.get('/accordion')
        self.assertContains(response, 'Week 12')

    def test_carousel_view(self):
        response = self.client.get('/carousel')
        self.assertContains(response, 'Ocean')
