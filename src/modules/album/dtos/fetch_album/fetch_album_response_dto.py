from pydantic import BaseModel

from modules.album.entities import AlbumEntity
from modules.album.entities.album_slot import AlbumSlotEntity


class FetchAlbumResponseDto(BaseModel):
    page: int
    total_pages: int
    items_per_page: int
    is_last_page: bool
    content: list[AlbumSlotEntity]

    @classmethod
    def from_entity(cls, entity: AlbumEntity) -> "FetchAlbumResponseDto":
        return cls(
            page=entity.page,
            total_pages=entity.total_pages,
            items_per_page=entity.items_per_page,
            is_last_page=entity.is_last_page,
            content=entity.content,
        )
