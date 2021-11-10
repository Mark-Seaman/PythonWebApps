from django.test import TestCase


class ViewTest(TestCase):

    def test_html_page_view(self):
        response = self.client.get('/')
        self.assertContains(response, 'home')

        response = self.client.get('/home.html')
        self.assertContains(response, 'Home Page')

        response = self.client.get('/theme.html')
        self.assertContains(response, 'Workshop Theme Page')

        response = self.client.get('/page.html')
        self.assertContains(response, 'Generic HTML Page')
