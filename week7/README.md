# Web Apps Demo Code  - Chapter 7

This demo code illustrates the concepts from "Building Web Apps - Chapter 7".

* [Course Website](https://shrinking-world.com/course/bacs350)
* [Chapter 7](https://shrinking-world.com/course/bacs350/chapter/7)
* [Github Source Code](https://github.com/Mark-Seaman/BACS350/tree/main/week7)

The following Design Patterns are illustrated by this demo

* [](https://shrinking-world.com/course/bacs350/skill/)
* [](https://shrinking-world.com/course/bacs350/skill/)
* [](https://shrinking-world.com/course/bacs350/skill/)


## News

This code shows the structure of a Django application that has user accounts.  Multiple data types are 
defined along with the views required to edit the data records.  This app has been left intentionally
simple to make it easy to understand all of the code.


Multiple data types are 
defined along with the views required to edit the data records.  This app has unique user accounts
for authors.  Every data object is tied to a specific author.

Each author is able to log in in order to create new articles or modify existing ones.

New users can register directly on the website to get a new user login.  The Author records in the
database use the built-in data models and views for Users.

I custom registration form and login form follow the style of the application by extending "theme.html".

Any author can read all articles but only the author of an article can modify the contents.


## Running the App

To run the code do the following steps.

* Start Visual Studio
* Open "week7/News"
* Run menu, Start Debugging
* Browse to http://127.0.0.1:8000/

Visit all views for testing.


### Build Project Code

Build the project & start a new Django app

    $ cd week7/News
    $ django-admin startproject config .
    $ python manage.py startapp doc

Modify config/settings.py
   
Configure the settings 

    ALLOWED_HOSTS
    INSTALLED_APPS
    TEMPLATES
    STATICFILES_DIRS
    STATIC_ROOT = BASE_DIR / "static_assets"

Collect static assets

    $ python manage.py collectstatic
    $ mv static_assets/* static
    $ echo "<h1>App Platform Static Server</h1>" > static/index.html


### Configure URL Routes

config.urls.py

    urlpatterns = [
        # Admin
        path('admin/', admin.site.urls),

        # Blog
        path('', BlogListView.as_view()),
        path('blog/', include('blog.urls_blog')),
        path('article/', include('blog.urls_article')),
    ]
 
blog.urls_blog.py

    urlpatterns = [

        # Blog
        path('',                BlogListView.as_view(),    name='blog_list'),
        path('<int:pk>',        BlogDetailView.as_view(),  name='blog_detail'),
        path('add',             BlogCreateView.as_view(),  name='blog_add'),
        path('<int:pk>/',       BlogUpdateView.as_view(),  name='blog_edit'),
        path('<int:pk>/delete', BlogDeleteView.as_view(),  name='blog_delete'),

    ]

blog.urls_article.py

    urlpatterns = [

        # Article
        path('',                 ArticleListView.as_view(),    name='article_list'),
        path('<int:pk>',         ArticleDetailView.as_view(),  name='article_detail'),
        path('add',              ArticleCreateView.as_view(),  name='article_add'),
        path('<int:pk>/',        ArticleUpdateView.as_view(),  name='article_edit'),
        path('<int:pk>/delete',  ArticleDeleteView.as_view(),  name='article_delete'),

    ]

### Create Views

blog/views.py

    class BlogListView(ListView):
        template_name = 'blog_list.html'
        model = Blog

    class BlogDetailView(DetailView):
        template_name = 'blog_detail.html'
        model = Blog

    class BlogCreateView(LoginRequiredMixin, CreateView):
        template_name = "blog_add.html"
        model = Blog
        fields = '__all__'

    class BlogUpdateView(LoginRequiredMixin, UpdateView):
        template_name = "blog_edit.html"
        model = Blog
        fields = '__all__'

    class BlogDeleteView(LoginRequiredMixin, DeleteView):
        model = Blog
        template_name = 'blog_delete.html'
        success_url = reverse_lazy('blog_list')


Build templates

    theme.html
    article_add.html
    article_delete.html
    article_detail.html
    article_edit.html
    article_list.html
    blog_add.html
    blog_delete.html
    blog_detail.html
    blog_edit.html
    blog_list.html


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

Deploy with config/app.yaml

