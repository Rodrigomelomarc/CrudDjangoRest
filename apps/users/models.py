import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    registered_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']
    is_anonymous = False
    is_authenticated = True

    def __str__(self):
        return f'Name: {self.name}, Member since: {self.registered_at}.'
