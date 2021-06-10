from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('album/<int:album_id>/', views.album, name='album'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
