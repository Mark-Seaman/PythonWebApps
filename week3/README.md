# Web Apps Demo Code  - Chapter 3

This demo code illustrates the concepts from "Building Web Apps - Chapter 3".

* [Course Website](https://shrinking-world.com/course/bacs350)
* [Chapter 3](https://shrinking-world.com/course/bacs350/chapter/3)
* [Github Source Code](https://github.com/Mark-Seaman/BACS350/tree/main/week3)

The following Design Patterns are illustrated by this demo

* [Skill 7 - Create a Django App](https://shrinking-world.com/course/bacs350/skill/7)
* [Skill 8 - Create Template View](https://shrinking-world.com/course/bacs350/skill/8)
* [Skill 9 - Add Variables to View](https://shrinking-world.com/course/bacs350/skill/9)


## Pages

This code shows the structure of a simple Django application.  There are several
HTML templates that are displayed.  Unique URLs route to specific views.
Each view loads a template with some views containing hard coded content and
others using variables to display custom data.

* URL:  /,     View: IndexView, Template: templates/index.html
* URL:  home,  View: HomeView, Template: templates/home.html
* URL:  about, View: AboutView, Template: templates/about.html

### Files

These files are used to build the Django application.

    ├── config
    │   ├── app.yaml
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── hero
    │   ├── models.py
    │   ├── templates
    │   │   ├── hero.html
    │   │   └── heroes.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── pages
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── requirements.txt
    ├── runtime.txt
    ├── static
    │   ├── images
    │   │   ├── black_widow.jpg
    │   │   ├── hulk.jpg
    │   │   └── iron_man.jpg
    │   └── index.html
    └── templates
        ├── about.html
        ├── home.html
        └── index.html


## Superheroes

This code is a Django App Module that displays information about superheroes.
It contains two types of views and support four URL routes.

* URL:  hero/,     View: IndexView, Template: templates/heroes.html
* URL:  hero/hulk,  View: HulkView, Template: templates/hero.html
* URL:  hero/blackwidow,  View: BlackWidow, Template: templates/hero.html
* URL:  hero/ironman,  View: IronManView, Template: templates/hero.html

Each view loads a static image of the superhero.

A static server must be configured to load the photos.

To run the code do the following steps.

* Start Visual Studio
* Open "week3/Pages"
* Run menu, Start Debugging
* Browse to http://127.0.0.1:8000/

Visit all views for testing.


### Build Project Code

Build the project

    $ mkdir week3/Pages
    $ cd week3/Pages
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

    $ python manage.py startapp pages
    $ python manage.py startapp hero
   
config/settings.py

    # Enable data the Profile app
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'hero',
        'pages',
    ]


### Configure URL Routes
   
config.urls.py

    from django.urls import path
    from django.urls.conf import include

    from pages.views import IndexView, HomeView, AboutView

    urlpatterns = [
        path('', IndexView.as_view()),
        path('about', AboutView.as_view()),
        path('home', HomeView.as_view()),
        path('hero/', include('hero.urls')),
    ]


hero.urls.py

    from django.urls import path
    from .views import BlackWidow, HulkView, IndexView, IronManView

    urlpatterns = [
        path('', IndexView.as_view()),
        path('hulk', HulkView.as_view()),
        path('ironman', IronManView.as_view()),
        path('blackwidow', BlackWidow.as_view()),
    ]


### Create a View

hero/views.py
    from django.views.generic import TemplateView

    class IndexView(TemplateView):
        template_name = 'heroes.html'

    class HulkView(TemplateView):
        template_name = 'hero.html'

        def get_context_data(self, **kwargs):
            return {
                'title': 'Hulk',
                'body': 'My name is Bruce Banner',
                'image': '/static/images/hulk.jpg'
            }




templates/heroes.html

    <h1>My Superhero Page</h1>
    <ul>
        <li><a href="hulk">Hulk</a></li>
        <li><a href="blackwidow">Black Widow</a></li>
        <li><a href="ironman">Iron Man</a></li>
    </ul>

templates/hero.html

    <h1>{{ title }}</h1>
    <p>{{ body }}</p>
    <img src="{{ image }}" alt="{{ image }}" width="300">
    <p>
        <a href=".">Show all heroes</a>
    </p>


Enable Templates

config/settings.py

    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'hero',
        'pages',
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

    