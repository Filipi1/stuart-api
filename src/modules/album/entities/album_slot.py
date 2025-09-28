from typing import Optional

from pydantic import BaseModel

from modules.album.entities.album_figure import AlbumFigureEntity


class AlbumSlotEntity(BaseModel):
    slot: str
    figure: Optional[AlbumFigureEntity]
