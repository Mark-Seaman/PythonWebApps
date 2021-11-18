# Python Anywhere 

## Account Setup

### Why use Python Anywhere 
* simple & intermediate site and free
* [Python Anywhere](https://www.pythonanywhere.com)
* [Plans & Pricing](https://www.pythonanywhere.com/pricing/)
* Sign up for free account


### How to set up Django Hosting at Python Anywhere 
* [Watch video tutorial](https://www.youtube.com/watch?v=Y4c4ickks2A)  (7 steps)


### Learn Linux Commands
* Master a few command line basics
* Read [Command Line](CommandLine)
* Essential commands: pwd, cs, ls, rm


### Run Terminal Window
*  Select "Consoles, New console, Bash"
    * pwd
    * cd
    * ls


### Clone your git repository
* Visit your [Github Repo](https://github.com/Mark-Seaman/Book-Builder.git)
* Clone the repo
    
    git clone https://github.com/Mark-Seaman/Book-Builder.git


### Create Virtual Environment
* Create an isolate python environment

    mkvirtualenv --python=/usr/bin/python3.8 .venv

* Install Django in the environment
    
    pip install django



## Create Web App
* Visit your main page
* Login to [Python Anywhere account](https://www.pythonanywhere.com)
* Bookmark this page on your bookmark toolbar
* Select Web tab in top menu


### Configure Your Web App
* Your Python Anywhere account support one free Web App
* Free accounts must be enabled every three months
* Click on "Run until 3 months from today" button
* This is not a problem for when you are actively developing code

### Python Anywhere Server

![](img/pa-server.png)


### Configure WSGI Python File
* Edit Config file for app runner
* WSGI - Web Server Gateway Interface


/var/www/markseaman_pythonanywhere_com_wsgi.py

    # +++++++++++ DJANGO +++++++++++
    import os
    import sys

    path = '/home/markseaman/Book-Builder/bookbuilder'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'bookbuilder.settings'

    ## then:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()


### Configure Code Settings

![](img/pa-code.png)


### Python Anywhere Static Files

![](img/pa-static.png)


### Python Anywhere Database
* Start with MySQL, switch to PostGres if needed

![](img/pa-db.png)


### Startup the Server

Reload http://markseaman.pythonanywhere.com/

Browse to http://markseaman.pythonanywhere.com/


