from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    first_name = None
    last_name = None
    name = CharField(max_length=255)
    surname = CharField(max_length=255)
