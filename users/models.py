from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']

