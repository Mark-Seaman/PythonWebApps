from django.contrib.auth.models import User
from django.db import models
from django.urls.base import reverse_lazy


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse_lazy('person_detail', args=[str(self.id)])

    @property
    def messages(self):
        return Message.objects.filter(author=self)

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @staticmethod
    def get_me(user):
        return Person.objects.get_or_create(user=user)[0]


class Message(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, editable=False, related_name='messages_sent')
    recipient = models.ForeignKey(Person, on_delete=models.CASCADE,
                                  related_name='messages_received', default='1')
    title = models.CharField(max_length=100)
    text = models.TextField()

    @property
    def messages(self):
        return Message.objects.filter(author=self.author)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('message_detail', args=[str(self.id)])
