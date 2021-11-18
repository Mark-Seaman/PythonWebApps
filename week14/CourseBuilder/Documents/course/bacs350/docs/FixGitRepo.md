# Fix Your Git Repo

## Detecting the Problem
 
Your Git repo cannot have the Virtual Environment committed.  There are about 1000 files that
are built into this one directory.  Committing them to Git WILL cause problems for you.

Python 3 creates cached files when it runs a program.  These files cannot be committed to Git
or they WILL cause problems.


### Do you have the problem?

Go to the Github Website.  Click through all directories in your repo.  

Look for the Virtual Env (env, venv,  etc.)

Look for __pycache__ 

If you have either then you have the problem.


### .gitignore

Now look for .gitignore anywhere in the directory structure.

You must have this file to tell git to ignore certain files.

If you are missing .gitignore then copy the file from my repo and put it in your root.

Now venv and __pycache__ will not be committed.


### Remove Old Cache files

cd into the directory where __pycache__ lives.

Remove all the files from git.

    git pull

    git rm -r __pycache__
    
    git commit -m 'Remove cache files'
       
    git push
    
Clean up remote files

    # Throw away changes
    git checkout .

    # Bring in deletions
    git pull


### Remove Venv Code

cd into the directory where __pycache__ lives.

Remove all the files from git.

    git pull

    git rm -r Venv
    
    git commit -m 'Remove Venv files'
    
    git push


### Rebuild your Local Venv

Reinstall Venv

    pipenv install django
    
    pipenv shell


### Rebuild your Remote Venv

Create an isolated python environment

    mkvirtualenv --python=/usr/bin/python3.8 .venv

Install Django in the environment
    
    pip install django