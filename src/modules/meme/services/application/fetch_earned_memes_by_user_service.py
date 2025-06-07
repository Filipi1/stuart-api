from modules.meme.dtos.get_earned_memes_by_user.get_earned_memes_by_user_request_dto import (
    GetEarnedMemesByUserRequestDto,
)
from modules.meme.services.domain.get_earned_memes_by_user_service import (
    GetEarnedMemesByUserDomainService,
)
from modules.meme.dtos.fetch_earned_memes_by_user import (
    FetchEarnedMemesByUserRequestDto,
    FetchEarnedMemesByUserResponseDto,
)

from modules.shared.adapters import ApplicationService


class FetchEarnedMemesByUserApplicationService(ApplicationService):
    def __init__(self, get_earned_memes_by_user: GetEarnedMemesByUserDomainService):
        self.__get_earned_memes_by_user = get_earned_memes_by_user

    async def process(
        self, input: FetchEarnedMemesByUserRequestDto
    ) -> FetchEarnedMemesByUserResponseDto:
        earned_memes = await self.__get_earned_memes_by_user.process(
            GetEarnedMemesByUserRequestDto(user_id=input.user_id)
        )
        return FetchEarnedMemesByUserResponseDto(earned_memes=earned_memes)
