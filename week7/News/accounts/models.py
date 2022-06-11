from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


# class UserAccount(AbstractUser):
#     bio = models.TextField(null=True, blank=True)

#     @property
#     def name(self):
#         return self.first_name + ' ' + self.last_name

#     def __str__(self):
#         return f'{self.username}'

#     def get_absolute_url(self):
#         return reverse_lazy('account_list')
