from django.db import models
from apps.users.models import User


class Book(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    genre = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
