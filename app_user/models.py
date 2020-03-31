from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):

    nickname = models.CharField(
        default="",
        max_length=64,
    )