""" Company model """

from django.db import models
from django.contrib.postgres.fields import ArrayField

from .base import AbstractBase


class Drink(AbstractBase):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    image = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=50, null=False, blank=False)
    is_alcoholic = models.BooleanField(null=True)
    instructions = models.TextField(max_length=500, null=True, blank=True)
    ingredients = ArrayField(
        models.CharField(max_length=500, blank=True, null=True),
        blank=True, null=True
    )

    def __str__(self):
        return self.name
