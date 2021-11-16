# Design of Book Builder

## Data

### Book

    class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=200)
        description = models.TextField(default='None')

        def __str__(self):
            return f'{self.pk} - {self.title} by {self.author}'

        def get_absolute_url(self):
            return reverse_lazy('book_detail', args=[str(self.id)])

Future Book data model

* author - convert from name to Author object


### Chapter

**Not defined yet**

Future Chapter data model

* book - points to book object
* order - chapter order
* title - title text of chapter
* markdown - markdown text 
* document - path to markdown file


### Author

**Not defined yet**

Future Author data model

* name - name of Author
* profile - url of author website
* title - job title
* bio - markdown text of bio
* document - path to markdown file for about page


### Accounts

Accounts are represented by the User data model in Django

from django.contrib.auth.models import User


---

## Views

### Book
* List
* Detail
* Add
* Edit
* Delete

### Chapter
* List
* Detail
* Add
* Edit
* Delete

### Author
* List
* Detail
* Add
* Edit
* Delete

### Accounts
* Login
* Logout
* Sign Up
* User Info
* List
* Detail
* Add
* Edit
* Delete

---

## Design Patterns

Document Reusable Design Patterns

* Data Views
* CRUD operations
* CRUD Test
* Data Views Test


### Data Views Design Pattern

#### Views

book/views.py

```python
    class BookView(RedirectView):
        url = '/book/'

    class BookListView(ListView):
        template_name = 'book_list.html'
        model = Book

    class BookDetailView(DetailView):
        template_name = 'book_detail.html'
        model = Book

    class BookCreateView(LoginRequiredMixin, CreateView):
        template_name = "book_edit.html"
        model = Book
        fields = ['title', 'author']

    class BookUpdateView(LoginRequiredMixin, UpdateView):
        template_name = "book_edit.html"
        model = Book
        fields = ['title', 'author']

    class BookDeleteView(LoginRequiredMixin, DeleteView):
        model = Book
        template_name = 'book_delete.html'
        success_url = reverse_lazy('book_list')
```


#### Templates

templates/book_list.html

```html
    {% for book in object_list %}
        <h3><a href="{% url 'book_detail' book.pk %}">{{ book.title }}</a></h3>
        <p>by {{ book.author }}</p>
    {% endfor %}
```   

templates/book_detail.html

```html  
    <h2>{{ book.title }}</h2>
    <p>{{ book.author }}</p>
    
    <a href="{% url 'book_edit' book.pk %}">Edit Book Book</a>
    <a href="{% url 'book_delete' book.pk %}">Delete Book Book</a>
``` 

templates/book_new.html

```html

    <form action="" method="book">{% csrf_token %}
       {{ form.as_p }}
       <input type="submit" value="Save">
    </form>
```

templates/book_edit.html

```html
    <form action="" method="book">{% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Update">
    </form>
```

templates/book_delete.html

```html
    <h1>Delete Book</h1>
    <form action="" method="post">{% csrf_token %}
      <p>Are you sure you want to delete "{{ book.title }}"?</p>
      <input type="submit" value="Confirm">
    </form>
```


#### URL Routes

book/urls.py

```python
from django.urls import path
from .views_book import BookView, BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView

urlpatterns = [
    path('book/',                       BookListView.as_view(),    name='book_list'),
    path('book/<int:pk>',               BookDetailView.as_view(),  name='book_detail'),
    path('book/add',                    BookCreateView.as_view(),  name='book_add'),
    path('book/<int:pk>/',              BookUpdateView.as_view(),  name='book_edit'),
    path('book/<int:pk>/delete',        BookDeleteView.as_view(),  name='book_delete'),
]

```

#### Tests

book/tests_book.py

```python
from django.test import TestCase

class BookViewsTest(TestCase):

    def setUp(self):
        pass

    def test_book_list_view(self):
        pass

    def test_book_detail_view(self):
        pass

    def test_book_add_view(self):
        pass

    def test_book_edit_view(self):
        pass

    def test_book_delete_view(self):
        pass
```