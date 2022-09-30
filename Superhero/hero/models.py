from email.policy import default
from django.db import models
from django.urls import reverse_lazy

class Hero(models.Model):
    name = models.CharField(max_length=200, default="None")
    identity = models.CharField(max_length=200, default="None")
    description = models.TextField(default="None")
    image = models.CharField(max_length=200, default="None")
    strengths = models.CharField(max_length=200, default="None")
    weaknesses = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')
