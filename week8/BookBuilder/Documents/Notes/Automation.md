# Automation commands

## Goal

Provide commands that do all frequent operations so that they
do not take any mindshare or typing.


## Command Set
All commands are defined in .bashrc

To load the commands into a Linux shell (use bash terminal on Windows)

    $ source .bashrc

Start in the correct directory for the current project

Automatically pull code

* Automation
    * b -- Load the shell environment for BACS 350
    * l -- List the files
    * u -- Go up one directory
    * d -- Go to any directory
* Git
    * s -- Git Status
    * c -- Git Commit and Push
    * pull -- Git Pull
    * push -- Git Push
* Django
    * pm -- Run Django command (python manage.py)
    * serve -- Run Django server
    * dt -- Run Django tests
    * qt -- Run quick test Django command
    * migrate -- Migrate the database

