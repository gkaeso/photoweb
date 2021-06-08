from django.contrib import admin

from .models import Photo, Album, AlbumPhoto


admin.site.register(Photo)
admin.site.register(Album)
admin.site.register(AlbumPhoto)
