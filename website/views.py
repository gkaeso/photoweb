from django.shortcuts import render

from .models import AlbumPhoto
from .resources import KEYS
from .wrappers import AlbumDetail, PhotoDetail


def index(request):
    return render(request, 'website/index.html', {"keys": KEYS})


def portfolio(request):
    album_details = []

    album_photos = AlbumPhoto.objects.select_related('photo', 'album').filter(is_ref=True)
    for ap in album_photos:
        nb_photo: int = AlbumPhoto.objects.filter(album=ap.album).count()
        album_details.append(
            AlbumDetail(
                id=ap.album.id,
                title=ap.album.title,
                dt_publish=ap.album.dt_publish,
                ref_photo=ap.photo.image.url,
                subtitle=ap.album.subtitle,
                description=ap.album.description,
                count=nb_photo,
            )
        )

    return render(request, 'website/portfolio.html', {"keys": KEYS, "collections": album_details})


def album(request, album_id):
    photo_details = []

    album_photos = AlbumPhoto.objects.select_related('photo', 'album').filter(album=album_id)
    for ap in album_photos:
        photo_details.append(
            PhotoDetail(
                id=ap.photo.id,
                url=ap.photo.image.url,
                title=ap.photo.title,
                dt_shot=ap.photo.dt_shot,
            )
        )

    return render(
        request, 'website/album.html',
        {"keys": KEYS, "album_title": album_photos[0].album.title, "photo_details": photo_details}
    )
