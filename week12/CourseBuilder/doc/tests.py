from django.test import TestCase
from markdown import markdown
from os import listdir

from doc.document import document_body, document_html, read_file

from .views import scan_document_files


class DocTest(TestCase):

    def test_markdown(self):
        markdown_text = '# Headline'
        html_text = document_html(markdown_text)
        self.assertEqual(html_text, '<h1>Headline</h1>')

    def test_doc_index_view(self):
        response = self.client.get('/doc/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Course Builder')

    def test_doc_default_view(self):
        response = self.client.get('/doc')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/doc/')

    def test_markdown_file(self):
        path = "Documents/Test/README.md"
        self.assertEqual(len(document_body(read_file(path))), 137)

    def test_document_files(self):
        'scan_document_files() - Disabled'
        # scan_document_files()
