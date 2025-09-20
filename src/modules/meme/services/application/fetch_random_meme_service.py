from modules.meme.exceptions.meme_not_found_exception import MemeNotFoundException
from modules.meme.services.domain.get_random_meme_service import (
    GetRandomMemeDomainService,
)
from modules.meme.dtos.fetch_random_meme import FetchRandomMemeResponseDto

from modules.shared.adapters import ApplicationService


class FetchRandomMemeApplicationService(ApplicationService):
    def __init__(self, get_random_meme: GetRandomMemeDomainService):
        self.__get_random_meme = get_random_meme

    async def process(self) -> FetchRandomMemeResponseDto:
        meme = await self.__get_random_meme.process()
        if not meme:
            raise MemeNotFoundException("Meme not found")

        return FetchRandomMemeResponseDto(
            id=meme.id,
            title=meme.title,
            description=meme.description,
            image=meme.image,
            earned_times=meme.earned_times,
            created_at=meme.created_at,
            updated_at=meme.updated_at,
        )
