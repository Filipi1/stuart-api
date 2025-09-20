from modules.album.dtos.build_album_slots.build_album_slots_request_dto import (
    BuildAlbumSlotsRequestDto,
)
from modules.album.services.domain.build_album_slots_service import (
    BuildAlbumSlotsDomainService,
)
from modules.meme.dtos.get_earned_memes_by_user import GetEarnedMemesByUserRequestDto
from modules.meme.services.domain.get_earned_memes_by_user_service import (
    GetEarnedMemesByUserDomainService,
)
from modules.album.dtos.fetch_album import FetchAlbumRequestDto, FetchAlbumResponseDto
from modules.meme.repositories.meme_repository import MemeRepository

from modules.shared.adapters import ApplicationService
from modules.user.dtos.get_user_by_token import GetUserByTokenRequestDto
from modules.user.exceptions.user_not_found_exception import UserNotFoundException
from modules.user.services.domain.get_user_by_token_service import (
    GetUserByTokenDomainService,
)


class FetchAlbumApplicationService(ApplicationService):
    def __init__(
        self,
        get_user_by_token: GetUserByTokenDomainService,
        get_earned_memes_by_user: GetEarnedMemesByUserDomainService,
        build_album_slots: BuildAlbumSlotsDomainService,
        meme_repository: MemeRepository,
    ):
        self.__get_user_by_token = get_user_by_token
        self.__get_earned_memes_by_user = get_earned_memes_by_user
        self.__build_album_slots = build_album_slots
        self.__meme_repository = meme_repository
        super().__init__(FetchAlbumApplicationService.__name__)

    async def process(self, input: FetchAlbumRequestDto) -> FetchAlbumResponseDto:
        self.logger.info(f"Fetching album for user: {input.token}...")
        user = await self.__get_user_by_token.process(
            GetUserByTokenRequestDto(token=input.token)
        )
        if not user:
            raise UserNotFoundException()

        self.logger.info(f"User found: {user.id} - <green>{user.username}</green>.")
        self.logger.info(
            f"Fetching memes for page {input.page} with {input.items_per_page} items per page."
        )
        total_memes = await self.__meme_repository.count_total_memes()
        total_pages = (total_memes + input.items_per_page - 1) // input.items_per_page
        paginated_memes = await self.__meme_repository.get_memes_paginated(
            page=input.page, items_per_page=input.items_per_page
        )

        self.logger.info(
            f"Memes fetched {len(paginated_memes)} for page {input.page} / Total memes: {total_memes}."
        )

        earned_memes = await self.__get_earned_memes_by_user.process(
            GetEarnedMemesByUserRequestDto(user_id=user.id)
        )

        slots = self.__build_album_slots.process(
            BuildAlbumSlotsRequestDto(
                user_earned_memes=earned_memes, paginated_memes=paginated_memes
            )
        )

        return FetchAlbumResponseDto(
            page=input.page,
            total_pages=total_pages,
            items_per_page=input.items_per_page,
            is_last_page=input.page >= total_pages,
            content=slots,
        )
