from pathlib import Path
from django.views.generic import TemplateView


def photo_list():
    def photo_details(i, f):
        if(i == 0):
            caption = 'Batman, AKA Bruce Wayne, is a rich sad man' if i == 0 else None 
            return dict(id=i, file=f, caption=caption)
        if(i == 1):
            caption = 'Flash, Barry Allen is the fastest man alive' 
            return dict(id=i, file=f, caption=caption)
        if(i == 2):
            caption = 'The Green Lantern, Hal Jordan has the universes most powerful weapon' 
            return dict(id=i, file=f, caption=caption)
        if(i == 3):
            caption = 'SuperMan, Clark Kent thinks glasses can hid an identity' 
            return dict(id=i, file=f, caption=caption)
        if(i == 4):
            caption = 'Wonder Woman, Princess Diana weilds the lasso of truth' 
            return dict(id=i, file=f, caption=caption)
        else:
            return None 
    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos





class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        return dict(photo=p)
