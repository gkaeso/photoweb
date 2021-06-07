from django.db import models

from .apps import WebsiteConfig


class Photo(models.Model):
    image = models.ImageField(upload_to=f'{WebsiteConfig.name}/images/')
    dt_shot = models.DateField(default=None, blank=True, null=True)
