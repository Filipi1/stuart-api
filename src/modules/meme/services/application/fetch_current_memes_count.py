from modules.meme.dtos.fetch_current_memes_count import (
    FetchCurrentMemesCountResponseDto,
)
from modules.meme.services.domain.get_memes_count_service import (
    GetMemesCountDomainService,
)
from modules.shared.adapters import ApplicationService


class FetchCurrentMemesCountApplicationService(ApplicationService):
    def __init__(self, get_memes_count: GetMemesCountDomainService):
        self.__get_memes_count = get_memes_count

    async def process(self) -> FetchCurrentMemesCountResponseDto:
        total_memes, oldest_unsorted_date, unsorted_count, most_sorted_meme = (
            await self.__get_memes_count.get_meme_status_info()
        )

        return FetchCurrentMemesCountResponseDto(
            total_memes=total_memes,
            oldest_unsorted_meme_date=oldest_unsorted_date,
            unsorted_memes_count=unsorted_count,
            most_sorted_meme=most_sorted_meme,
        )
