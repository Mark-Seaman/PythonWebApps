# Accordion View Design Pattern

## Overview

### Goals

Display an accordion with collapsible panels.

Encapsulate common logic for reuse to build views in 5 minutes.

Use Bootstrap to create consistent appearance.

Use Partial Template "accordion.html" to organize your code logic.

Pass in data as a dictionary.


### Steps
* Gather the panel data
* Pass dictionary with all info for page
* Use a generic template to display the info
* Select the initial panel to show



## Data

Reading a Data

```python
def accordion_data():

    def create_card(i):
        return f'<h2>Lessons (week {i})</h2><p>Lesson {i*3-2}</p><p>Lesson {i*3-1}</p><p>Lesson {i*3}</p>'

    def card_content(i, active):
        card = card_data(f'Week {i+1}', create_card(i+1))
        if i == active:
            card.update(dict(id=i, collapsed='', show='show', aria='true'))
        else:
            card.update(dict(id=i, collapsed='collapsed', show='', aria='false'))
        return card

    return [card_content(i, 3) for i in range(12)]
```


## Template

templates/_ accordion.html

```html
<div class="accordion" id="theAccordion">

    {% for card in accordion %}

    <div class="accordion-item">

        <h2 class="accordion-header" id="heading-{{ card.id }}">

            <button class="accordion-button {{ card.collapsed }}" 
                type="button" 
                data-bs-toggle="collapse"
                data-bs-target="#collapse-{{ card.id }}" 
                aria-expanded="{{ card.aria }}"
                aria-controls="collapse-{{ card.id }}">

                {{ card.title }}

            </button>

        </h2>

        <div id="collapse-{{ card.id }}" 
            class="accordion-collapse collapse {{ card.show }}"
            aria-labelledby="heading-{{ card.id }}" 
            data-bs-parent="#theAccordion">

            <div class="accordion-body">
                {% autoescape off %}
                {{ card.body }}
                {% endautoescape %}
            </div>

        </div>

    </div>

    {% endfor %}
</div>
```


## Views

workshop/views.py

```python
class AccordionView(TemplateView):
    template_name = 'accordion.html'

    def get_context_data(self, **kwargs):
        return dict(accordion=accordion_data())

```


## URL Routes

workshop/urls.py

```python
    urlpatterns = [
        path('accordion',  AccordionView.as_view(), name='accordion'),
    ]
```


## Tests

workshop/tests.py

```python
from django.test import TestCase

class ViewTest(TestCase):

    def test_accordion_view(self):
        response = self.client.get('/accordion')
        self.assertContains(response, 'Index')
```

