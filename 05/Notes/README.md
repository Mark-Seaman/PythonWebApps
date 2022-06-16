# Web Apps Demo Code  - Chapter 5

This demo code illustrates the concepts from "Building Web Apps - Chapter 5".

* [Course Website](https://shrinking-world.com/course/bacs350)
* [Chapter 5](https://shrinking-world.com/course/bacs350/chapter/5)
* [Github Source Code](https://github.com/Mark-Seaman/BACS350/tree/main/week4)

The following Design Patterns are illustrated by this demo

* [Skill 13 - Models & Database](https://shrinking-world.com/course/bacs350/skill/)
* [Skill 14 - CRUD Operations](https://shrinking-world.com/course/bacs350/skill/)
* [Skill 15 - Admin Views](https://shrinking-world.com/course/bacs350/skill/)


## NotePad

This code shows the structure of a simple Django application that uses a database.  

### Files

These files are used to build the Django application.

    ├── Documents
    │   ├── DataCascade.md
    │   ├── Document.md
    │   ├── Index.md
    │   ├── Note.md
    │   └── ToDo.md
    ├── config
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    ├── manage.py
    ├── note
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── static
    │   ├── admin
    │   │   ├── css
    │   │   ├── fonts
    │   │   ├── img
    │   │   ├── js
    └── templates
        ├── document.html
        ├── note.html
        ├── notes.html
        └── theme.html

## Running the App

To run the code do the following steps.

* Start Visual Studio
* Open "week5/NotePad"
* Run menu, Start Debugging
* Browse to http://127.0.0.1:8000/

Visit all views for testing.


### Build Project Code

Build the project

    $ cd week5/NotePad
    $ django-admin startproject config .


Start a new Django app

    $ python manage.py startapp note
   

### Configure URL Routes
   
note.urls.py

    from django.urls import path
    from .views import NoteDetailView, NoteListView

    urlpatterns = [
        path('', NoteListView.as_view()),
        path('<int:id>', NoteDetailView.as_view()),
    ]


### Create Views

note/views.py

    from pathlib import Path
    from django.views.generic import TemplateView 


    class NoteListView(TemplateView):
        template_name = 'notes.html'


    class NoteDetailView(TemplateView):
        template_name = 'note.html'


templates/theme.html

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"></script>
        <title>Photos by Mark</title>
        <link rel="stylesheet" href="/static/gallery.css">
    </head>

    <body class=" bg-dark text-light">
        <h1 class="header">Photos by Mark</h1>

        {% block content %}
        <h2>No Block Defined</h2>
        {% endblock content %}

    </body>

    </html>


templates/note.html

    {% extends 'theme.html' %}

    {% block content %}

        <h1>
            {{ note.title }}
        </h1>
        <p>
            {{ note.author }}
        </p>
        <p>
            {{ note.body }}
        </p> 

    {% endblock content %}


templates/notes.html

    {% extends 'theme.html' %}

    {% block content %}

        {% for note in object_list %}

            <a href="{{ note.pk }}">
                {{ note.title }} by {{ note.author }}
            </a>

        {% endfor %}

    {% endblock content %}


## Settings

Configure the settings 

* ALLOWED_HOSTS
* INSTALLED_APPS
* TEMPLATES
* STATICFILES_DIRS


config/settings.py

    # Handle all URL requests made to web server
    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'note',
    ]

    # Enable the templates for the 'templates' directory
    TEMPLATES = [
        {
            ...
            'DIRS': [BASE_DIR / 'templates'],
            ...
        },
    ]

    # On Digital Ocean it will use the Static Server
    # Locally you need to enable the static media server (Images, CSS, Javascript)
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]


## Run the local server

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver

Browse to web page

    http://localhost:8000

Set up static server that is used locally



### Digital Ocean Setup

Prep for App Platform

runtime.txt

    python-3.10.4

requirements.txt

    Django
    gunicorn
    psycopg2-binary

