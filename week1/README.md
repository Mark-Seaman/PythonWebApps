# Web Apps Demo Code  - Chapter 1

This demo code illustrates the concepts from "Building Web Apps - Chapter 1".

* [Course Website](https://shrinking-world.com/course/bacs350)
* [Chapter 1](https://shrinking-world.com/course/bacs350/chapter/1)
* [Github Source Code](https://github.com/Mark-Seaman/BACS350/tree/main/week1)

The following Design Patterns are illustrated by this demo

* [Skill 1 - VS Code & Github](https://shrinking-world.com/course/bacs350/skill/1)
* [Skill 2 - Setup Python Environment](https://shrinking-world.com/course/bacs350/skill/2)
* [Skill 3 - Running a Django Application](https://shrinking-world.com/course/bacs350/skill/3)



## Profile Page

This code demo shows the construction of a simple static website.

* Single directory
* Single HTML file "index.html"
* CSS file "style.css"
* Image file "Mark-Seaman.jpg"

To view the web page open the index file by double-clicking to run the 
default browser.

### Files

These files are used to build the static web page.

├── Mark-Seaman.jpg
├── index.html
└── style.css


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
* Open "week1/ProfileApp"
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
