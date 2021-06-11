from django.contrib import admin

from .models import Photo, Album, AlbumPhoto, Tag, PhotoTag


admin.site.register(Photo)
admin.site.register(Album)
admin.site.register(AlbumPhoto)
admin.site.register(Tag)
admin.site.register(PhotoTag)
