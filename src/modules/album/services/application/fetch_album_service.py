from modules.album.dtos.build_album_slots.build_album_slots_request_dto import BuildAlbumSlotsRequestDto
from modules.album.services.domain.build_album_slots_service import BuildAlbumSlotsDomainService
from modules.meme.dtos.get_earned_memes_by_user import GetEarnedMemesByUserRequestDto
from modules.meme.services.domain.get_earned_memes_by_user_service import (
    GetEarnedMemesByUserDomainService,
)
from modules.album.dtos.fetch_album import FetchAlbumRequestDto, FetchAlbumResponseDto

from modules.shared.adapters import ApplicationService
from modules.user.dtos.get_user_by_token import GetUserByTokenRequestDto
from modules.user.services.domain.get_user_by_token_service import (
    GetUserByTokenDomainService,
)


class FetchAlbumApplicationService(ApplicationService):

    def __init__(
        self,
        get_user_by_token: GetUserByTokenDomainService,
        get_earned_memes_by_user: GetEarnedMemesByUserDomainService,
        build_album_slots: BuildAlbumSlotsDomainService
    ):
        self.__get_user_by_token = get_user_by_token
        self.__get_earned_memes_by_user = get_earned_memes_by_user
        self.__build_album_slots = build_album_slots

    async def process(self, input: FetchAlbumRequestDto) -> FetchAlbumResponseDto:
        user = await self.__get_user_by_token.process(
            GetUserByTokenRequestDto(token=input.token)
        )
        memes = await self.__get_earned_memes_by_user.process(
            GetEarnedMemesByUserRequestDto(user_id=user.id)
        )
        slots = self.__build_album_slots.process(
            BuildAlbumSlotsRequestDto(user_earned_memes=memes)
        )
        return FetchAlbumResponseDto(
            page=input.page,
            total_pages=1,
            items_per_page=10,
            is_last_page=True,
            content=slots
        )
