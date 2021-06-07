from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='images')
    dt_shot = models.DateField(default=None)
