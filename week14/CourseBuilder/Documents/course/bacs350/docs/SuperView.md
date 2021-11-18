# Super View Design Pattern

## Overview

### Goals

Encapsulate common logic for reuse to build views in 5 minutes.

Use Bootstrap to create consistent appearance.

Build a complex view by compositing partial view templates.

Pass in data as a dictionary for structured pages.


### Steps
* Gather the page data
* Pass dictionary with all info for page
* Use a generic template to display the info
* Allow for display of layers of data



## Data
* The superview is a single view with a large number of subviews directly
built into it.
* The desired data is passed into the template for display
* Components 
    * Documents
    * Cards
    * Table
    * Carousel
    * Tabs
    * Accordion

Reading Data for View

```python
def super_data():
    return dict(document=document_data('README'),
                table=table_data('Documents/lessons.csv'),
                carousel=carousel_data(),
                tabs=tabs_data())
```


## Template
* Components supported by partial templates
    * Documents
    * Cards
    * Table
    * Carousel
    * Tabs
    * Accordion

templates/document.html

```html
{% extends 'theme.html' %}

{% block content %}

    <h2>Super View</h2>

    {% include '_documents.html' %}
    {% include '_cards.html' %}
    {% include '_table.html' %}
    {% include '_carousel.html' %}
    {% include '_accordion.html' %}
    {% include '_tabs.html' %}

{% endblock content %}
```


## Views

workshop/views.py

```python
class SuperView(TemplateView):
    template_name = 'super.html'

    def get_context_data(self, **kwargs):
        return super_data()
```


## URL Routes

workshop/urls.py

```python
    urlpatterns = [
        path('super', SuperView.as_view()),
    ]
```


## Tests

workshop/tests.py

```python
from django.test import TestCase

class ViewTest(TestCase):

    def test_super_view(self):
        response = self.client.get('super')
        self.assertContains(response, 'Week 12')
```

