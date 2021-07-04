from django.conf import settings
from django.db import models


class CustomText(models.Model):
    "Generated Model"
    breaking = models.CharField(
        blank=True,
        max_length=150,
    )
    videos = models.TextField(
        null=True,
        blank=True,
    )
    local = models.TextField(
        null=True,
        blank=True,
    )


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()
