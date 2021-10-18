# Manual Test Script


Run Django tests


Run Server and Browse


## Accounts

* List
* Detail
* Add
* Edit
* Delete


## Book

* List
* Detail
* Add
* Edit
* Delete



---


# Automated Tests

## Common Tests for Data

Start with these tests for any new object model

    from django.test import TestCase
    from .models import Object


    class ObjectDataTest(TestCase):

        def create_object(self, title):
            return Object.objects.create(title=title)

        def setUp(self):
            self.create_object('Title for Object')

        def test_add_object(self):
            self.assertTrue(True)

        def test_delete_object(self):
            self.assertTrue(True)

        def test_detail_object(self):
            self.assertTrue(True)

        def test_edit_object(self):
            self.assertTrue(True)

        def test_list_object(self):
            self.assertTrue(True)


## Common Tests for Views

    class ObjectViewsTest(TestCase):

        def login(self):
            args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
            user = get_user_model().objects.create_user(**args)
            response = self.client.login(username='TEST_DUDE', password='secret')
            self.assertEqual(response, True)

        def setUp(self):
            self.object = Object.objects.create(title='Object Title')

        def test_object_list_view(self):
            self.assertTrue(True)

        def test_object_detail_view(self):
            self.assertTrue(True)

        def test_object_add_view(self):
            self.assertTrue(True)

        def test_object_edit_view(self):
            self.assertTrue(True)

        def test_object_delete_view(self):
            self.assertTrue(True)

---

## Tests for Accounts, Book, Chapter

* [accounts/test.py]()
* [book/tests_book.py]()
* [book/tests_chapter.py]()
