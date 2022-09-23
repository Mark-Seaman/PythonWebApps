from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to = "static/images")

    def __str__(self):
        return f'{self.name}'
