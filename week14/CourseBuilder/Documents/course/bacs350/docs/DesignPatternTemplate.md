# Document View Design Pattern

## Overview

### Goals

Build a common way to display Markdown documents on web pages.

Provide one place in code for each feature.

Encapsulate all common logic for reuse.

Build views without thinking (up and running in 5 minutes).

Use Bootstrap to create high visual impact.

Use Partial Template "documents.html" to organize your code logic.

Pass in data as a dictionary.


### Steps
* Gather the markdown and page data
* Convert the markdown to HTML
* Pass dictionary with all info for page
* Use a generic template to display the info
* Allow for display of multiple documents



## Data

Reading a Data

```python
```


## Template

### Document Template

templates/document.html

```html
{% extends 'theme.html' %}

{% block content %}

    {% for card in documents %}

        <div class="card">
            <div class="card-header">
                <div class="row">
                    DOCUMENT: {{ card.file }}
                </div>
            </div>
            <div class="card-body">

                {% autoescape off %}
                <p>{{ card.body }}</p>
                {% endautoescape %}

            </div>
        </div>

    {% endfor %}
    
{% endblock content %}
```


## Views

doc/views.py

```python
class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('doc', 'Index')
        return document_data(document)
```


## URL Routes

doc/urls.py

```python
    urlpatterns = [
        path('doc/', DocumentView.as_view(), name='document'),
        path('doc/<str:doc>', DocumentView.as_view()),
    ]
```


## Tests

doc/tests.py

```python
from django.test import TestCase

class DocViewTest(TestCase):

    def test_doc_view(self):
        response = self.client.get('doc/')
        self.assertContains(response, 'Index')
```

