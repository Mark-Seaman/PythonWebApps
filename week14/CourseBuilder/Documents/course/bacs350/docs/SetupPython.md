# Install Python 3 & Django

Before you can have any fun then you must create a Python Environment that allows you
to write code.

Essential Setup Steps:

* Install update of Python 3
* Create a Virtual Environment
* Install Django code libraries

There are perhaps hundreds of ways to do this setup and what works for you will rely
heavily on your existing computer setup.  This cookbook is the way that I find works 
for most people.  Try this first and if you can't make it work then read the materials
at the end of this document.

If all else fails then come to the interactive work sessions during our regular class 
period.
 

### Python Version 

Check to make sure that you have the latest version of python installed.

Terminal window

    python --version 
    
    python3 --version
    Python 3.7.6
    
Run Python 3

    python3
    
    Python 3.7.6
    >>> print('I win')
    I win
    
### Install new version

Visit [https://python.org](https://python.org)

Download the Installer file [Python 3.8.4](https://www.python.org/downloads/release/python-384/)


### Virtual Env

Create a virtual environment

    cd UNC-BACS-350
    python3 -m venv .venv
    
Activate the virtual environment

    source .venv/bin/activate

    python3 --version
    Python 3.8.6
    
    # Any other version before 3.8 is bad

Install python packages

    pip list
    
    Package    Version
    ---------- -------
    pip        20.1.1
    setuptools 47.1.0
    
    pip freeze
    
    pip install django pillow markdown django-crispy-forms requests
    
    Collecting django
      Using cached Django-3.0.8-py3-none-any.whl (7.5 MB)
    Collecting pillow
      Downloading Pillow-7.2.0-cp38-cp38-macosx_10_10_x86_64.whl (2.2 MB)
         |████████████████████████████████| 2.2 MB 2.1 MB/s 
    Collecting markdown
      Using cached Markdown-3.2.2-py3-none-any.whl (88 kB)
    Collecting pytz
      Using cached pytz-2020.1-py2.py3-none-any.whl (510 kB)
    Collecting sqlparse>=0.2.2
      Using cached sqlparse-0.3.1-py2.py3-none-any.whl (40 kB)
    Collecting asgiref~=3.2
      Using cached asgiref-3.2.10-py3-none-any.whl (19 kB)
    Installing collected packages: pytz, sqlparse, asgiref, django, pillow, markdown
    Successfully installed asgiref-3.2.10 django-3.0.8 markdown-3.2.2 pillow-7.2.0 pytz-2020.1 sqlparse-0.3.1

Check the installation

    pip freeze
    
    asgiref==3.2.10
    Django==3.1.2
    Markdown==3.3.1
    Pillow==8.0.0
    pytz==2020.1
    sqlparse==0.4.1
    
    which python
    
    /Users/seaman/Sensei-2020/.venv/bin/python

Exit the virtual environment

    deactivate
    
    
### Debugging Your Install

Try the easy recipe above but if you get stuck don't give up.  Dive in deeper to solve the
problems that are associated with the different variations of computer setups.
Consult these simple tutorials if you get stuck.  The last one is a website that teaches you 
many alternatives.

* [Install Python3 on Mac](https://wsvincent.com/install-python3-mac/)
* [Install Python3 on Windows](https://wsvincent.com/install-python3-windows/)
* [Install Python3 on Chromebook](https://wsvincent.com/install-python3-chromebook/)
* [Install Python3](https://installpython3.com)
    