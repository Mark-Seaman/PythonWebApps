# Add Data to Django Views

There are a set of design patterns that can be used to quickly build full custom views in 
Django.


### Simple File Viewer

urls.py

    from django.urls import path
    from .views import MyStoryView

    urlpatterns = [
        path('story', MyStoryView.as_view()),
    ]
    
views.py

    from django.views.generic import TemplateView

    class MyStoryView(TemplateView):
        template_name = "story.html"
        
        def get_context_data(self, **kwargs):
            return {
                'title': 'Three Pigs', 
                'body': 'Once upon a time ...',
            }
     
templates/story.html

    <h1>{{ title }}</h1>
    <p>
        {{ body}}
    </p>

        