from modules.meme.dtos.get_meme_by_id.get_meme_by_id_response_dto import (
    GetMemeByIdResponseDto,
)
from modules.meme.repositories.meme_repository import MemeRepository
from modules.meme.dtos.get_meme_by_id import GetMemeByIdRequestDto
from modules.shared.adapters import DomainService


class GetMemeByIdDomainService(DomainService):
    def __init__(self, meme_repository: MemeRepository):
        self.__meme_repository = meme_repository

    async def process(self, input: GetMemeByIdRequestDto) -> GetMemeByIdResponseDto:
        meme = await self.__meme_repository.get_meme_by_id(input.meme_id)
        return GetMemeByIdResponseDto(meme=meme)
