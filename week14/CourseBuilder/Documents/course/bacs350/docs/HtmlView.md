# HTML Page View Design Pattern

## Overview

### Goals

Build a common way to display content of pure HTML pages on web server.

Provide one place in code for each feature.

Encapsulate all common logic for reuse.

Build views without thinking (up and running in 5 minutes).

Use view inheritance in templates.

Pass the template selector on the URL and load the correct template.


### Steps
* Pass the template selector the URL
* Select the template for the page
* Add extra context when needed
* Allow for view inheritance
     
            

## Data

This design pattern is used when rendering static web pages.  This means that 
data is rarely provided when rendering the view.



## Template

### Page Template

templates/page.html

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Generic HTML Page</title>
    </head>
    <body>
        <h1>Generic HTML Page</h1>
    </body>
</html>
```

### Visual Inheritance Template

templates/home.html

```html
{% extends 'theme.html' %}

{% block content%}

    <h1>Page with Visual Inheritance</h1>

{% endblock content%}
```



## Views

workshop/views.py

```python
class PageView(TemplateView):
            
    def get_template_names(self):
        page = self.kwargs.get('page', 'index')
        return f'{page}.html'

```


## URL Routes


### Select the HTML template

With static web pages every page is implemented by a different HTML file.  This type
of customization is available with Django templates.  Unique HTML content can be provided
by building files in the "templates" directory and them tying them to URL routes.  This 
requires you to provide a route and view code for each template that you wish to use.

Example

    URL:    path('page.html', PageView.as_view())
    
    View:  
            class PageView(TemplateView):
                template_name = 'page.html'

workshop/urls.py

```python
    urlpatterns = [
        path('<str:page>.html', PageView.as_view()),
    ]
```



## Tests

workshop/tests.py

```python
from django.test import TestCase

class ViewTest(TestCase):

    def test_html_page_view(self):
        response = self.client.get('/')
        self.assertContains(response, 'home')

        response = self.client.get('/home.html')
        self.assertContains(response, 'Home Page')

        response = self.client.get('/theme.html')
        self.assertContains(response, 'Workshop Theme Page')

        response = self.client.get('/page.html')
        self.assertContains(response, 'Generic HTML Page')
```

