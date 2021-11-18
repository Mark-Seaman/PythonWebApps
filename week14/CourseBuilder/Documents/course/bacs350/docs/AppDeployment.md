# Deploy App on Python Anywhere

### Setup Python Anywhere Web App
* Follow steps in [Setup Python Anywhere](PythonAnywhere.md)

### Create Book Builder App
* Create [Book Builder Repo](GithubRepo.md)
* Create application code
* Commit to [Book-Builder](https://github.com/Mark-Seaman/Book-Builder)


### Clone Repo at PythonAnywhere
* Run Console at [PythonAnywhere](https://www.pythonanywhere.com/user/markseaman/)
* Clone the repo

    cd
    git clone https://github.com/Mark-Seaman/Book-Builder
    

### Allowed Hosts

Allow connection at Python Anywhere

settings.py

    ALLOWED_HOSTS = ['markseaman.pythonanywhere.com']


### Git Pull

    cd Book-Builder
    git pull   # Brings in new code
    
### Reload Server

    Visit page https://www.pythonanywhere.com/user/markseaman/
    
    View error logs
    

