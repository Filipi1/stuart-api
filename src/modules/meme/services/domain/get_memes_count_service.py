import asyncio
from typing import Tuple, Optional

from modules.meme.entities.meme import MemeEntity
from modules.meme.repositories.meme_repository import MemeRepository
from modules.shared.adapters import DomainService


class GetMemesCountDomainService(DomainService):
    def __init__(self, meme_repository: MemeRepository):
        self.__meme_repository = meme_repository

    async def process(self) -> int:
        return await self.__meme_repository.count_total_memes()

    async def get_meme_status_info(
        self,
    ) -> Tuple[int, Optional[str], int, Optional[MemeEntity]]:
        """Retorna informações completas sobre o status dos memes"""
        total_memes, oldest_unsorted_date, unsorted_count, most_sorted_meme = (
            await asyncio.gather(
                self.__meme_repository.count_total_memes(),
                self.__meme_repository.get_oldest_unsorted_meme_date(),
                self.__meme_repository.count_unsorted_memes(),
                self.__meme_repository.get_most_sorted_meme(),
            )
        )
        return (total_memes, oldest_unsorted_date, unsorted_count, most_sorted_meme)
