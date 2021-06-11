import os.path

from django.db import models

from .apps import WebsiteConfig


def rename_and_upload(instance, filename) -> str:
    upload_to = os.path.join(WebsiteConfig.name, 'images')
    return os.path.join(upload_to, filename)


class Photo(models.Model):
    image = models.FileField(upload_to=rename_and_upload)
    title = models.CharField(max_length=50, default=None, blank=True, null=True)
    model = models.CharField(max_length=50, default=None, blank=True, null=True)
    dt_shot = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.image.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    dt_publish = models.DateField()
    subtitle = models.CharField(max_length=100, default=None, blank=True, null=True)
    description = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.title


class AlbumPhoto(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.RESTRICT)
    is_ref = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'{self.album} - {self.photo}'
