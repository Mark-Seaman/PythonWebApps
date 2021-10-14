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

