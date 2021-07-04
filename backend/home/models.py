from django.conf import settings
from django.db import models


class CustomText(models.Model):
    "Generated Model"
    breakinh = models.CharField(
        max_length=150,
        blank=True,
    )
    videos = models.TextField(
        null=True,
        blank=True,
    )


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()
