from django.db import models

# Create your models here.


class AppTestModels(models.Model):

    name = models.CharField(
        default="",
        max_length=64,
    )