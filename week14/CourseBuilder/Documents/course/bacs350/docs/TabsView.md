# Tabs View Design Pattern

## Overview

### Goals

Reusable code to show tabs with multiple panels of information.

Build views without thinking (up and running in 5 minutes).

Use Bootstrap to create high visual impact.

Use Partial Template "tabs.html" to organize your code logic.

Pass in data as a dictionary.


### Steps
* Gather data for the page structure
* Pass dictionary with all info for page
* HTML Template shows the data using Bootstrap tabs
* Use a generic template to display the info



## Data

Reading Card Data

```python
def tabs_data():

    def options(i, tab, selected):
        data = dict(name=f'tab{i}', header=tab['title'], body=tab['body'])
        if selected:
            data.update(dict(active='active', show='show', selected='true'))
        else:
            data.update(dict(active='', show='', selected='false'))
        return data

    def set_options(tabs):
        return [options(i, tab, i==0) for i, tab in enumerate(tabs)]

    return set_options(cards_data())
```


## Template

templates/_ tabs.html

```html
<ul class="nav nav-tabs" role="tablist">

    {% for t in tabs %}
        <li class="nav-item">
            <a class="nav-link {{ t.active }}" id="{{ t.name }}-tab" data-bs-toggle="tab" href="#{{ t.name }}">
                {{ t.header }}
            </a>
        </li>
    {% endfor %}

</ul>

<div class="tab-content">

    {% for t in tabs %}

        <div class="tab-pane bg-light text-dark p-5 {{ t.active }} {{ t.show }} fade" id="{{ t.name }}">

            <h2>{{ t.header }}</h2>

            {% autoescape off %}
            {{ t.body }}
            {% endautoescape %}

        </div>

    {% endfor %}

</div>
```


## Views

workshop/views.py

```python
class TabsView(TemplateView):
    template_name = 'tabs.html'

    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs)
```


## URL Routes

workshop/urls.py

```python
urlpatterns = [
    path('tabs',  TabsView.as_view(), name='tabs'),
]
```


## Tests

workshop/tests.py

```python
from django.test import TestCase

class ViewTest(TestCase):

    def test_tabs_view(self):
        response = self.client.get('/tabs')
        self.assertContains(response, 'Card Four')
```

