import datetime

from django.shortcuts import render

from .models import AlbumPhoto
from .resources import KEYS
from dataclasses import dataclass


@dataclass
class AlbumPhotoDetail:
    album: str
    dt_publish: datetime.date
    ref_photo: str
    subtitle: str
    description: str
    count: int


def index(request):
    return render(request, 'website/index.html', {"keys": KEYS})


def portfolio(request):
    album_photo_details = []

    albumphotos = AlbumPhoto.objects.select_related('photo', 'album').filter(is_ref=True)

    for ap in albumphotos:
        nb_photo: int = AlbumPhoto.objects.filter(album=ap.album).count()
        album_photo_details.append(
            AlbumPhotoDetail(
                album=ap.album.title,
                dt_publish=ap.album.dt_publish,
                ref_photo=ap.photo.image.url,
                subtitle=ap.album.subtitle,
                description=ap.album.description,
                count=nb_photo
            )
        )
    return render(request, 'website/portfolio.html', {"keys": KEYS, "collections": album_photo_details})
