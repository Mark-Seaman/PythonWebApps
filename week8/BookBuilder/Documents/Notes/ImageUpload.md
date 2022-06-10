# Image Upload Design Pattern

## How To Video
by John Elder

This is the fastest way to build an image upload utility.

<iframe width="996" height="560" src="https://www.youtube.com/embed/ygzGr51dbsY" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen>
</iframe>


## Code For Image Upload
Django model ImageField is used to upload images

book/models.py

```python
class Image(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField(max_length=200)
```


## Settings for Storage
Set upload directory and URL

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
```


## Generate Code for Image
* Run the code cloner to produce image files.
* Delete views and templates for Detail and Edit


## Form For Image Upload
Django model ImageField is used to upload images

templates/image_add.html

```html
<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.media }}
    {{ form.as_p }}
    <button type="submit">Save Record</button>
</form>
```


## Views For Image Upload
Django model ImageField is used to upload images

book/models.py

```python
class ImageListView(ListView):
    template_name = 'image_list.html'
    model = Image

class ImageCreateView(LoginRequiredMixin, CreateView):
    template_name = "image_add.html"
    model = Image
    fields = ['image', 'title']

class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'image_delete.html'
    success_url = reverse_lazy('image_list')
```


## Views For Image Display
Django model ImageField is used to upload images

templates/image_list.html

```html
{% for image in object_list %}
    <tr>
        <td><img src="{{ image.image.url }}" alt="{{ image.title }}" width='200'></td>
        <td>{{ image.image.url }}</td>
        <td><a href="/image/{{ image.pk }}/delete">Delete</a></td>
    </tr>
{% endfor %}
```
