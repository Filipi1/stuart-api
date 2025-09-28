from pydantic import BaseModel

from modules.album.entities.album_slot import AlbumSlotEntity


class FetchAlbumResponseDto(BaseModel):
    page: int
    total_pages: int
    items_per_page: int
    is_last_page: bool
    content: list[AlbumSlotEntity]
