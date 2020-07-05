# Create your models here.
from django.db import models


class Aulas(models.Model):
    titulo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    data = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    palestrante = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    objects = models.Manager()
