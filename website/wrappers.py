import datetime

from dataclasses import dataclass


@dataclass
class AlbumDetail:
    id: int
    title: str
    dt_publish: datetime.date
    ref_photo: str
    subtitle: str
    description: str
    count: int


@dataclass
class PhotoDetail:
    id: int
    url: str
    title: str
    model: str
    dt_shot: datetime.date
