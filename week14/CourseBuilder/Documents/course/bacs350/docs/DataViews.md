# Data Views Design Pattern


### Development Process
* Create a project
* Edit settings.py
* Add an app
* Define Templates
* Define Views
* Define Routes


### Django View Classes
* TemplateView
* ListView
* DetailView
* CreateView
* UpdateView
* DeleteView


### Create a new Django project
* The default view should contain a list of link to superheroes
* An add button will let users add a new record


### ListView
* Create a table or divs that show a list of records
* Each hero should have a link that goes to the details page


### DetailView
* Display all info from the Database records
* Show the image as a thumbnail with a link to the large image
* Add a button to Edit the record


### CreateView
* Create new records with a view
* You can cheat by loading the image file into a directory
* Add the image as a URL pointing to this file


### UpdateView
* Make sure that you can edit the records
* Make sure that the page is redirected after save


### DeleteView
* Delete the records after confirmation
* Go to the list after a delete


### View Inheritance
* Create a base page template
* Style all pages without duplicating any code

---


## Code for Design Pattern

### Data

book/models.py

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse_lazy('book_detail', args=[str(self.id)])
```


### Views

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


### Templates

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


### URL Routes

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


### Tests

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
