from modules.album.dtos.fetch_album import FetchAlbumRequestDto, FetchAlbumResponseDto
from modules.album.entities.album import AlbumEntity
from modules.album.enums.album_cache_keys_enum import AlbumCacheKeysEnum
from modules.album.services.domain.get_album_by_user_service import (
    GetAlbumByUserDomainService,
)
from modules.shared.adapters import ApplicationService
from modules.shared.services.cache.cache_service import CacheService
from modules.user.exceptions.user_not_found_exception import UserNotFoundException
from modules.user.services.domain.get_user_by_token_service import (
    GetUserByTokenDomainService,
)


class FetchAlbumApplicationService(ApplicationService):
    def __init__(
        self,
        get_user_by_token: GetUserByTokenDomainService,
        get_album_by_user: GetAlbumByUserDomainService,
        cache: CacheService,
    ):
        self.__get_user_by_token = get_user_by_token
        self.__get_album_by_user = get_album_by_user
        self.__cache = cache
        super().__init__(FetchAlbumApplicationService.__name__)

    def __get_cache_key(self, user_id: int, page: int, items_per_page: int) -> str:
        return AlbumCacheKeysEnum.ALBUM.value.format(
            user_id=user_id, page=page, items_per_page=items_per_page
        )

    async def process(self, input: FetchAlbumRequestDto) -> FetchAlbumResponseDto:
        self.logger.info(f"Fetching album for user: <yellow>{input.token}</yellow>...")
        user = await self.__get_user_by_token.process(input.token)
        if not user:
            raise UserNotFoundException()
        self.logger.info(f"User found: {user.id} - <green>{user.username}</green>.")

        cache_key = self.__get_cache_key(user.id, input.page, input.items_per_page)

        async def compute_album() -> AlbumEntity:
            album = await self.__get_album_by_user.process(
                user_id=user.id,
                page=input.page,
                items_per_page=input.items_per_page,
            )
            expire = 300 if album.is_last_page and len(album.content) == 0 else 1800
            self.__cache.set_model(cache_key, album, expire)
            return album

        album = await self.__cache.get_or_compute_model(
            key=cache_key,
            compute_func=compute_album,
            model_class=AlbumEntity,
        )

        return (
            FetchAlbumResponseDto.from_entity(album)
            if album
            else FetchAlbumResponseDto(
                page=input.page,
                total_pages=1,
                items_per_page=input.items_per_page,
                is_last_page=True,
                content=[],
            )
        )
