from modules.meme.entities.meme import MemeEntity
from modules.meme.repositories.meme_repository import MemeRepository
from modules.shared.adapters import DomainService


class GetMemesPaginatedDomainService(DomainService):
    def __init__(self, meme_repository: MemeRepository):
        self.__meme_repository = meme_repository
        super().__init__(GetMemesPaginatedDomainService.__name__)

    async def process(
        self, page: int, items_per_page: int
    ) -> tuple[list[MemeEntity], int]:
        total_memes = await self.__meme_repository.count_total_memes()
        total_pages = (total_memes + items_per_page - 1) // items_per_page
        paginated_memes = await self.__meme_repository.get_memes_paginated(
            page=page, items_per_page=items_per_page
        )
        return paginated_memes, total_pages
