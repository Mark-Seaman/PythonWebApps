# Web Apps Demo Code  - Chapter 4

This demo code illustrates the concepts from "Building Web Apps - Chapter 4".

* [Course Website](https://shrinking-world.com/course/bacs350)
* [Chapter 4](https://shrinking-world.com/course/bacs350/chapter/4)


## Gallery

This code shows the structure of a simple Django application that uses visual
inheritance to eliminate code duplication.  

There is a Django App Module that displays photos.  

There are two URL Routes:

* URL:  /,  View: PhotoListView, Template: templates/photos.html
* URL:  <filename>, View: PhotoDetailView, Template: templates/photo.html

The list view finds all images in the static images directory on the server.
It shows a small view of the image.

When the user selects an image all of the details are displayed.

A static server must be configured to load the photos.


## Running the App

To run the code do the following steps.

* Start Visual Studio
* Open "week3/Pages"
* Run menu, Start Debugging
* Browse to http://127.0.0.1:8000/

Visit all views for testing.


### Build Project Code

Build the project

    $ cd week4/Gallery
    $ django-admin startproject config .

Run the server

    $ python manage.py migrate
    $ python manage.py runserver

Browse to web page

    http://localhost:8000

Set up static server that is used locally

config/settings.py

    # On Digital Ocean it will use the Static Server
    # Locally you need to enable the static media server (Images, CSS, Javascript)
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / "static"]

    # Handle all URL requests made to web server
    ALLOWED_HOSTS = ['*']


### Create a new app

Start a new Django app

    $ python manage.py startapp gallery
   

### Configure URL Routes
   
photos.urls.py

    from django.urls import path
    from photos.views import PhotoDetailView, PhotoListView

    urlpatterns = [
        path('', PhotoListView.as_view()),
        path('<int:id>', PhotoDetailView.as_view()),
    ]


### Create Views

photos/views.py

    from pathlib import Path
    from django.views.generic import TemplateView


    def photo_list():
        def photo_details(i, f):
            caption = f'Caption for Photo {i}' if i == 1 else None
            return dict(id=i, file=f, caption=caption)

        photos = Path('static/images').iterdir()
        photos = [photo_details(i, f) for i, f in enumerate(photos)]
        return photos


    class PhotoListView(TemplateView):
        template_name = 'photos.html'

        def get_context_data(self, **kwargs):
            return dict(photos=photo_list())


    class PhotoDetailView(TemplateView):
        template_name = 'photo.html'

        def get_context_data(self, **kwargs):
            i = kwargs['id']
            photos = photo_list()
            p = photos[i]
            return dict(photo=p)


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


templates/photos.html

    {% extends 'theme.html' %}

    {% block content %}
        <div class="container">

            <p>
                <img class="photo" src="{{ photo.file }}">
            </p>
            <p>
                {{ photo.caption }}
            </p>
            <p>
                FILE PATH: {{ photo.file }}
            </p>

        </div>

    {% endblock content %}


templates/photo.html

    {% extends 'theme.html' %}

    {% block content %}

        {% for photo in photos %}

            <a href="{{ photo.id }}">
                <img class="photo" src="{{ photo.file }}">
            </a>

        {% endfor %}

    {% endblock content %}


## Settings

config/settings.py

    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'photos',
    ]

    # Enable the templates for the 'templates' directory
    TEMPLATES = [
        {
            ...
            'DIRS': [BASE_DIR / 'templates'],
            ...
        },
    ]

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]



### Digital Ocean Setup

Prep for App Platform

runtime.txt

    python-3.10.4

requirements.txt

    Django
    gunicorn
    psycopg2-binary

