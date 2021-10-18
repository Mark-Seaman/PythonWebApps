from django.test import TestCase
from markdown import markdown


class DocTest(TestCase):

    def test_markdown(self):
        markdown_text = '# Headline'
        html_text = markdown(markdown_text)
        self.assertEqual(html_text, '<h1>Headline</h1>')
