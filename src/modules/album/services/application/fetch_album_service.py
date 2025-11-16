from modules.album.dtos.fetch_album import FetchAlbumRequestDto, FetchAlbumResponseDto
from modules.album.services.domain.get_album_by_user_service import (
    GetAlbumByUserDomainService,
)
from modules.shared.adapters import ApplicationService
from modules.user.exceptions.user_not_found_exception import UserNotFoundException
from modules.user.services.domain.get_user_by_token_service import (
    GetUserByTokenDomainService,
)


class FetchAlbumApplicationService(ApplicationService):
    def __init__(
        self,
        get_user_by_token: GetUserByTokenDomainService,
        get_album_by_user: GetAlbumByUserDomainService,
    ):
        self.__get_user_by_token = get_user_by_token
        self.__get_album_by_user = get_album_by_user
        super().__init__(FetchAlbumApplicationService.__name__)

    async def process(self, input: FetchAlbumRequestDto) -> FetchAlbumResponseDto:
        self.logger.info(f"Fetching album for user: <yellow>{input.token}</yellow>...")
        user = await self.__get_user_by_token.process(input.token)
        if not user:
            raise UserNotFoundException()
        self.logger.info(f"User found: {user.id} - <green>{user.username}</green>.")

        album = await self.__get_album_by_user.process(
            user_id=user.id,
            page=input.page,
            items_per_page=input.items_per_page,
        )

        self.logger.info(f"Album fetched: <green>{album.page}/{album.total_pages}</green> with {len(album.content)} items.")

        return FetchAlbumResponseDto.from_entity(album)
