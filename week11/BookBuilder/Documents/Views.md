# Building Views in Django

Creating views involves many different levels of understanding.  Throughout this course
we have been building different types of views.  This section of the book looks at all
of the different ways that we can build views with Django.


View types

* Template View
* Custom View using Template
* Django ListView
* Django DetailView
* Django UpdateView
* Django CreateView
* Django DeleteView
* HTML File
* Document File
* Directory View
* Markdown Document



## Template View

The easiest way to build a view in Django is to define a template using HTML.  
This template is automatically loaded by setting a value is "settings.py".   To
see a demo of this go to 
[week 2 demo](https://github.com/Mark-Seaman/BACS350/blob/main/week2/Pages/config/settings.py) and
look for the TEMPLATES variable.


templates/index.html

    <h1>Index Page</h1>


urls.py

    urlpatterns = [
        path('', TemplateView.as_view(template_name="index.html")),
    ]



### Custom View using Template

views.py

    from django.views.generic import TemplateView

    class IndexView(TemplateView):
        template_name = 'index.html'


urls.py

    urlpatterns = [
        path('', IndexView.as_view()),
    ]


tests.py

    from django.test import SimpleTestCase

    class SimpleTests(SimpleTestCase):
        def test_home_page_status_code(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)


Run all tests

    $ python manage.py test



### Django Data Views

All code is illustrated with the Book code implementation.

views.py

    class BookListView(ListView):
        template_name = 'book_list.html'
        model = Book


    class BookDetailView(DetailView):
        template_name = 'book_detail.html'
        model = Book


    class BookCreateView(LoginRequiredMixin, CreateView):
        template_name = "book_add.html"
        model = Book
        fields = ['title', 'author', 'description']


    class BookUpdateView(LoginRequiredMixin, UpdateView):
        template_name = "book_edit.html"
        model = Book
        fields = ['title', 'author', 'description']


    class BookDeleteView(LoginRequiredMixin, DeleteView):
        model = Book
        template_name = 'book_delete.html'
        success_url = reverse_lazy('book_list')


urls.py

    urlpatterns = [
        path('book/',                   BookListView.as_view(),    name='book_list'),
        path('book/<int:pk>',           BookDetailView.as_view(),  name='book_detail'),
        path('book/add',                BookCreateView.as_view(),  name='book_add'),
        path('book/<int:pk>/',          BookUpdateView.as_view(),  name='book_edit'),
        path('book/<int:pk>/delete',    BookDeleteView.as_view(),  name='book_delete'),
    ]


tests.py

    from django.test import TestCase

    class TestBookView(TestCase):
        def test_home_page_status_code(self):
            response = self.client.get('/book/')
            self.assertEqual(response.status_code, 200)


Run all tests

    $ python manage.py test