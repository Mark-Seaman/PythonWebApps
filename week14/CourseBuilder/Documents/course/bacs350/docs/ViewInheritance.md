# View Inheritance Design Pattern

## Overview

### Goals

Build a common theme that is used on all pages on a website.

Provide one place for each feature.

Encapsulate all common logic for reuse.

Build views without thinking.

Use Bootstrap to create high visual impact.

Use Partial Templates to organize your code logic.

Use Template Blocks to override default behavior.

Provide useful default behavior.


### Steps

Create a series of templates
    
    theme.html
    _header.html
    _footer.html
    _navbar.html
    _user.html

Define blocks for page composition

    title
    navbar
    user
    header
    content
    footer
    

## Template


### Theme

theme.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{% block title %}NO TITLE{% endblock title %}</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"></script>
    <link href="/static/style.css" rel="stylesheet">
</head>

<body>

    {% block navbar %}
    {% include '_navbar.html' %}
    {% endblock navbar %}


    {% block header %}
    {% include '_header.html' %}
    {% endblock header %}


    {% block content %}
    <div class="bg-danger text-light text-center">
        <h1>Workshop Theme Page</h1>
        <p>This is a demo of a base theme page with no content or inheritance.</p>
    </div>
    {% endblock content %}


    {% block footer %}
    {% include '_footer.html' %}
    {% endblock footer %}

</body>

</html>
```
    

### Header

header.html

```html
<header class="container-fluid p-5 bg-primary text-white text-center">
    <a href="/" class="text-white">
        <h1>View Workshop</h1>
    </a>
</header>
```
    

### Footer

footer.html

```html
<footer class="bg-primary p-3 text-center text-light">
    &copy;2020 -
    <b><a href="https://shrinking-world.com" class="text-light">Shrinking World</a></b>
    - Practical Software Engineering
</footer>
```
    

### Navbar

navbar.html

```html
<nav class="navbar navbar-expand-sm navbar-dark bg-dark text-light">
    <div class="container">

        <a class="navbar-brand text-light" href="/">View Workshop</a>

        <ul class="navbar-nav ml-auto">
            {% for i in menu.menu_items %}
                <li class="nav-item {{ i.active }}">
                    <a href="{{ i.url }}" class="nav-link">{{ i.label }}</a>
                </li>
            {% endfor %}
        </ul>

    </div>
</nav>
```


### User Info

user.html

```html
{% if user.is_authenticated %}
    <li class="nav-item active">
        <span class="nav-link p-2 m-2">Welcome {{ user.username }}</span>
    </li>
    <li class="nav-item">
        <a href="{% url 'logout' %}" class=" nav-link p-2 m-2">
            <i class="fas fa-sign-out-alt"></i> Log out
        </a>
    </li>
{% else %}
    <li class="nav-item">
        <span class="nav-link p-2 m-2">You are not logged in.</span>
    </li>

    <li class="nav-item active">
        <a href="{% url 'login' %}" class="nav-link p-2 m-2">
            <i class="fas fa-sign-in-alt"></i> Log In
        </a>
    </li>
{% endif %}
```



## Views

views.py

```python
class HtmlView(TemplateView):
    template_name = 'home.html'
```

## URL Routes

urls.py

```python
urlpatterns = [
    path('', HtmlView.as_view(), name='home'),
    path('theme.html', HtmlView.as_view(template_name='theme.html'), name='theme'),
]

```

    