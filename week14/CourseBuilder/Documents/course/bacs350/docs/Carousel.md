# Carousel View Design Pattern

## Overview

### Goals

Add an image carousel to web pages.

Encapsulate common logic for reuse to build views in 5 minutes.

Use Bootstrap to create consistent appearance.

Use Partial Template "carousel.html" to organize your code logic.

Pass in data as a dictionary for images and labels.


### Steps
* Gather the image data and labels
* Pass dictionary with all info for page
* Use a generic template to display the info
* Select the initial photo to be active



## Data

Reading a Data

```python
def carousel_data():
    return [
        dict(image_url="https://source.unsplash.com/random/1200x800?bear", label="Bear", active="active"),
        dict(image_url="https://source.unsplash.com/random/1200x800?forest", label="Forest"),
        dict(image_url="https://source.unsplash.com/random/1200x800?ocean", label="Ocean"),
        dict(image_url="https://source.unsplash.com/random/1200x800?flower", label="Flower"),
    ]
```


## Template

templates/carousel.html

```html
<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">

    <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"
            aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
            aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
            aria-label="Slide 3"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3"
            aria-label="Slide 4"></button>
    </div>

    <div class="carousel-inner">
        {% for image in carousel %}
        <div class="carousel-item {{ image.active }}">
            <img class="d-block w-100" src="{{ image.image_url }}" alt="{{ image.label }}">
        </div>
        {% endfor %}
    </div>

    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
        data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
        data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div>
```


## Views

workshop/views.py

```python
class CarouselView(TemplateView):
    template_name = 'carousel.html'

    def get_context_data(self, **kwargs):
        carousel = carousel_data()
        return dict(title='Carousel View', carousel=carousel)
```


## URL Routes

workshop/urls.py

```python
    urlpatterns = [
        path('carousel',  CarouselView.as_view(), name='carousel'),
    ]
```


## Tests

workshop/tests.py

```python
from django.test import TestCase

class ViewTest(TestCase):

    def test_carousel_view(self):
        response = self.client.get('/carousel')
        self.assertContains(response, 'Ocean')
```

