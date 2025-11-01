from enum import Enum


class AlbumCacheKeysEnum(str, Enum):
    ALBUM = "album:{user_id}:{page}:{items_per_page}"