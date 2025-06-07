from modules.meme.entities.earned_meme import EarnedMemeEntity
from modules.meme.repositories.earned_meme_repository import EarnedMemeRepository
from modules.meme.dtos.get_earned_memes_by_user.get_earned_memes_by_user_request_dto import (
    GetEarnedMemesByUserRequestDto,
)

from modules.shared.adapters import DomainService


class GetEarnedMemesByUserDomainService(DomainService):
    def __init__(self, earned_meme_repository: EarnedMemeRepository):
        self.__earned_meme_repository = earned_meme_repository

    async def process(
        self, input: GetEarnedMemesByUserRequestDto
    ) -> list[EarnedMemeEntity]:
        memes = await self.__earned_meme_repository.get_earned_memes_with_meme_info(
            input.user_id
        )
        return memes
