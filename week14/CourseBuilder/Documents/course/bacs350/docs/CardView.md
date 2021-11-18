# Card View Design Pattern

## Overview

### Goals

Build a common way to display content on web pages organized as cards.

Provide one place in code for each feature.

Encapsulate all common logic for reuse.

Build views without thinking (up and running in 5 minutes).

Use Bootstrap to create high visual impact.

Use Partial Template "cards.html" to organize your code logic.

Pass in data as a dictionary.


### Steps
* Gather the page data
* Pass dictionary with all info for page
* Use a generic template to display the info
* Allow for display of multiple cards



## Data

Single card

```python
def card_data(title, body, color='', width='', link=None):
    html = markdown(body)
    return dict(title=title, body=html, color=color, width=width)
```

Multiple Cards

```python
def cards_data():
    return [
        card_data("Card One",   text1),
        card_data("Card Two",   text2),
        card_data("Card Three", text3),
    ]
```


## Template

### Document Template
* Add variable to view
* Use autoescape in template
* Iterate over all "cards"

templates/cards.html

```html
{% for card in cards %}

    <div class="card">
        <div class="card-header">
            <h2>{{ card.title }}</h2>
        </div>
        <div class="card-body">

            {% autoescape off %}
            <p>{{ card.body }}</p>
            {% endautoescape %}

        </div>
    </div>

{% endfor %}
```


## Views

workshop/views.py

```python
class CardView(TemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        return dict(cards=cards_data())

```


## URL Routes

workshop/urls.py

```python
    urlpatterns = [
        path('card',  CardView.as_view(), name='card'),
    ]
```


## Tests

workshop/tests.py

```python
from django.test import TestCase

class ViewTest(TestCase):

    def test_card_view(self):
        response = self.client.get('card/')
        self.assertContains(response, 'Card One')
```

