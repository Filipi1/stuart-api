from modules.album.dtos.build_album_slots.build_album_slots_request_dto import (
    BuildAlbumSlotsRequestDto,
)
from modules.album.entities.album import AlbumEntity
from modules.album.services.domain.build_album_slots_service import (
    BuildAlbumSlotsDomainService,
)
from modules.meme.dtos.get_earned_memes_by_user import GetEarnedMemesByUserRequestDto
from modules.meme.services.domain.get_earned_memes_by_user_service import (
    GetEarnedMemesByUserDomainService,
)
from modules.meme.services.domain.get_memes_paginated_service import (
    GetMemesPaginatedDomainService,
)
from modules.shared.adapters import DomainService


class GetAlbumByUserDomainService(DomainService):
    def __init__(
        self,
        get_earned_memes_by_user: GetEarnedMemesByUserDomainService,
        build_album_slots: BuildAlbumSlotsDomainService,
        get_memes_paginated: GetMemesPaginatedDomainService,
    ):
        self.__get_earned_memes_by_user = get_earned_memes_by_user
        self.__build_album_slots = build_album_slots
        self.__get_memes_paginated = get_memes_paginated
        super().__init__(GetAlbumByUserDomainService.__name__)

    async def process(
        self, user_id: int, page: int, items_per_page: int
    ) -> AlbumEntity:
        self.logger.info(
            f"Fetching memes for page {page} with {items_per_page} items per page."
        )
        paginated_memes, total_pages = await self.__get_memes_paginated.process(
            page=page, items_per_page=items_per_page
        )

        if page > total_pages:
            self.logger.warning(
                f"Page {page} does not exist. Total pages: {total_pages}"
            )
            return AlbumEntity(
                page=page,
                total_pages=total_pages,
                items_per_page=items_per_page,
                is_last_page=True,
                content=[],
            )

        self.logger.info(
            f"Memes fetched {len(paginated_memes)} for page {page} / Total pages: {total_pages}."
        )

        earned_memes = await self.__get_earned_memes_by_user.process(
            GetEarnedMemesByUserRequestDto(user_id=user_id)
        )

        slot_offset = (page - 1) * items_per_page
        slots = self.__build_album_slots.process(
            BuildAlbumSlotsRequestDto(
                user_earned_memes=earned_memes,
                paginated_memes=paginated_memes,
                slot_offset=slot_offset,
            )
        )

        return AlbumEntity(
            page=page,
            total_pages=total_pages,
            items_per_page=items_per_page,
            is_last_page=page >= total_pages,
            content=slots,
        )

