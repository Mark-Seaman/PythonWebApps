from django.test import TestCase
from django.urls import reverse

from .models import Author, Course, Lesson
from coder.coder import create_test_user


class CourseDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.course1 = dict(name='Dickens', title='Tale of 2 Cities', author=self.author1,
                            description='None', doc_path='Documents')
        self.course2 = dict(name='Homer', title='Iliad', author=self.author2,
                            description='None', doc_path='Documents')

    def test_add_course(self):
        self.assertEqual(len(Course.objects.all()), 0)
        Course.create(**self.course1)
        Course.create(**self.course2)
        x = Course.objects.get(pk=2)
        self.assertEqual(str(x), '2 - Homer by 2 - Homer')
        self.assertEqual(x.author.name, 'Homer')
        self.assertEqual(x.title, 'Iliad')
        self.assertEqual(len(Course.objects.all()), 2)

    def test_course_edit(self):
        Course.create(**self.course1)
        b = Course.objects.get(pk=1)
        b.author = self.author2
        b.title = 'Iliad'
        b.description = 'No description'
        b.save()
        self.assertEqual(b.title, 'Iliad')
        self.assertEqual(b.author.name, 'Homer')
        self.assertEqual(b.description, 'No description')

    def test_course_delete(self):
        Course.objects.create(**self.course1)
        b = Course.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Course.objects.all()), 0)


class CourseViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.course1 = dict(name='BACS 200',
                            title='UNC BACS 200',
                            subtitle='Subtitle UNC BACS 200',
                            author=self.author1,
                            description='description',
                            doc_path='Documents/course/bacs200',
                            num_projects=14,
                            num_lessons=42)
        self.course2 = dict(name='BACS 350',
                            title='UNC BACS 350',
                            subtitle='Subtitle UNC BACS 350',
                            author=self.author1,
                            description='None',
                            doc_path='Documents/course/bacs350',
                            num_projects=14,
                            num_lessons=42)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('course_list'))

    def test_course_list_view(self):
        self.assertEqual(reverse('course_list'), '/course/')
        Course.objects.create(**self.course1)
        Course.objects.create(**self.course2)
        response = self.client.get('/course/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_course_detail_view(self):
        Course.objects.create(**self.course1)
        self.assertEqual(reverse('course_detail', args='1'), '/course/1')
        self.assertEqual(reverse('course_detail', args='2'), '/course/2')
        response = self.client.get(reverse('course_detail', args='1'))
        self.assertContains(response, 'BACS 200')

    def test_course_add_view(self):

        # Add without Login
        response = self.client.post(reverse('course_add'), self.course1)
        self.assertEqual(response.url, '/accounts/login/?next=/course/add')
        self.assertEqual(len(Course.objects.all()), 0)

        # Login to add
        self.login()
        response = self.client.post(reverse('course_add'), self.course1)
        response = self.client.post(reverse('course_add'), self.course2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/course/2')
        response = self.client.get('/course/')
        self.assertEqual(len(Course.objects.all()), 2)
        response = self.client.get(reverse('course_detail', args='2'))
        self.assertContains(response, 'BACS 350')

    def test_course_edit_view(self):

        # Edit without Login
        Course.objects.create(**self.course1)
        self.assertEqual(reverse('course_edit', args='1'), '/course/1/')
        response = self.client.get('/course/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/course/1/')

        # Login to edit
        self.login()
        response = self.client.post('/course/1/', self.course2)
        self.assertEqual(response.url, '/course/1')
        response = self.client.get(response.url)
        self.assertContains(response, self.course2['title'])
        self.assertContains(response, self.author1.name)

        # Check the course object
        course = Course.objects.get(pk=1)
        self.assertEqual(course.author, self.author1)
        self.assertEqual(course.title, 'UNC BACS 350')

    def test_course_delete_view(self):
        self.login()
        Course.objects.create(**self.course1)
        self.assertEqual(reverse('course_delete', args='1'), '/course/1/delete')
        response = self.client.get('/course/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/course/1/delete')
        self.assertEqual(len(Course.objects.all()), 0)


# class CourseFixtureTest(TestCase):
#     fixtures = ['Documents/Test/data.json']

#     def test_with_data(self):
#         self.assertEqual(len(Author.objects.all()), 0)
#         self.assertEqual(len(Course.objects.all()), 0)
#         self.assertEqual(len(Lesson.objects.all()), 0)

    # def test_import_courses(self):
    #     import_all_courses()
    #     # print(Author.objects.all())
    #     # print(course.objects.all())
    #     # print(Chapter.objects.all())
    #     self.assertEqual(len(Author.objects.all()), 3)
    #     self.assertEqual(len(Course.objects.all()), 2)
    #     self.assertEqual(len(Lesson.objects.all()), 70)
