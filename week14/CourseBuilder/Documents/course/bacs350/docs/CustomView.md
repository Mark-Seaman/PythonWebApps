# Custom Django Views

There are a set of design patterns that can be used to quickly build full custom views in 
Django.


## Degrees of Freedom - How to customize

Django views can be customized in a wide variety of ways.  But choosing to the correct
method can be tricky for beginners.  Here are the common ways that you can implement the
look an feel that you want.  Apply these in priority order.


### Select the HTML template

With static web pages every page is implemented by a different HTML file.  This type
of customization is available with Django templates.  Unique HTML content can be provided
by building files in the "templates" directory and them tying them to URL routes.  This 
requires you to provide a route and view code for each template that you wish to use.

Example

    URL:    path('page.html', PageView.as_view())
    
    View:  
            class PageView(TemplateView):
                template_name = 'page.html'
    

### Template Selector View

A single view function can be used to serve many different page templates.  An argument 
supplied with the URL route can be used to select from a number of possible templates.

Example:

    URL:    path('<str:page>', PageView.as_view())
    
    View:  
            class PageView(TemplateView):
            
                def get_template_names(self):
                    return self.kwargs.get('page')
                    

### Inject Data Variables into View

Templates can contain placeholders for data that is supplied by the view.  Data is provided
as a Python dictionary.

templates/page.html
    
    <h1>{{ title }}</h1>
    
views.py
    
    class PageView(TemplateView):
        template_name = 'page.html'
    
        def get_context_data(self, **kwargs):
            return {'title': 'My Page Title'}
    

### Entire Templates Can be Included

One template can be included within another template file.  This lets you reuse pieces of
code without redefining the logic.  For example, there may be a complex header at the top
of every page.  Define the header content once and include the file in every page.  Designate
files that do not define complete HTML with names that start with " _ ".

templates/header.html

    <div>
        <h1>{{ title }}</h1>
        <img src="my_logo.png">
    </div>

templates/page.html

    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{{ title }}</title>
        </head>
        <body>
            {% include '_header.html' %}
            <p>This is my text</p>
        <body>
    </html>


### Inherit from a Base View

A base view template may define extensive HTML content that can be shared by all of the
views. The logic can be defined once and used by inheriting from the base view.  Variables
provided to the derived view will be applied to the base view.

templates/page_theme.html

    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{{ title }}</title>
        </head>
        <body>
            <h1>{{ title }}</h1>
            <p>This is a paragraph</p>
        </body>
    </html>
 
templates/page.html
   
    {% extends 'page_theme.html' %}


### Override Blocks

Blocks of HTML content can be defined in the base template.  These can be overridden in
each derived page.  If the block is not defined then a default answer can be provided by
the base template.

templates/page_theme.html

    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{{ title }}</title>
        </head>
        <body>
            {% block content %}
                <h1>No CONTENT</h1>
            {% endblock content %}
        </body>
    </html>    
    
templates/page.html
   
    {% extends 'page_theme.html' %}
   
    {% block content %}
        <h1>{{ title }}</h1>
        <p>This is a paragraph</p>
    {% endblock content %}
            
