import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError("email must be set")
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser, models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    registered_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']
    is_anonymous = False
    is_authenticated = True
    objects = UserManager()

    def __str__(self):
        return f'Name: {self.name}, Member since: {self.registered_at}.'
