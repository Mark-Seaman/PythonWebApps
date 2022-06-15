# Web Apps Demo Code  - Chapter 2

This demo code illustrates the concepts from "Building Web Apps - Chapter 2".

* [Course Website](https://shrinking-world.com/course/bacs350)
* [Chapter 2](https://shrinking-world.com/course/bacs350/chapter/2)
* [Github Source Code](https://github.com/Mark-Seaman/BACS350/tree/main/week2)

The following Design Patterns are illustrated by this demo

* [Skill 4 - Deploy a Static Web Server](https://shrinking-world.com/course/bacs350/skill/4)
* [Skill 5 - Deploy to Development Server](https://shrinking-world.com/course/bacs350/skill/5)
* [Skill 6 - Deploy to Production Server](https://shrinking-world.com/course/bacs350/skill/6)


## Profile App

This code is a simple Django application that shows the same content as the 
Profile Page.  But this app code is more general purpose and is easily extended.

The code helps you test if all the development tools are set up properly.

* Python environment
* Django code libraries
* Visual Studio Code
* Github Repo

To run the code do the following steps.

* Start Visual Studio
* Open "week2/ProfileApp"
* Run menu, Start Debugging
* Browse to http://127.0.0.1:8000/

If this does not look like the Profile Page then your tools are not configured
properly.

### Files

These files are used to build the Django application.

    ├── config
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── pages
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── templates
    │   │   └── index.html
    │   ├── tests.py
    │   └── views.py
    └── static
        ├── Mark-Seaman.jpg
        ├── index.html
        └── style.css


### Build Project Code

Build the project

    $ mkdir week2/ProfileApp
    $ cd week2/ProfileApp
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

    $ python manage.py startapp profile
   
config/settings.py

    # Enable data the Profile app
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'profile',
    ]


### Configure URL Route
   
urls.py

    from django.urls import path
    from pages.views import ProfileView
    
    urlpatterns = [
        path('', ProfileView.as_view()),
    ]
  

### Create a View

hero/views.py

    from django.views.generic import TemplateView
    
    class ProfileView(TemplateView):
        template_name = 'profile.html'


templates/profile.html

    <h1>Profile Page</h1>
    <p>
        This is the profile page.  Wow ... it is beautiful.
    </p>


Enable Templates

config/settings.py

    # Enable the templates for the 'templates' directory
    TEMPLATES = [
        {
            ...
            'DIRS': [BASE_DIR / 'templates'],
            ...
        },
    ]


### Digital Ocean Setup

Prep for App Platform

runtime.txt

    python-3.10.4

requirements.txt

    Django
    gunicorn
    psycopg2-binary

    