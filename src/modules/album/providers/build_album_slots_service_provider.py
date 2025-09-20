from typing import Annotated

from fastapi import Depends

from modules.album.services.domain.build_album_slots_service import (
    BuildAlbumSlotsDomainService,
)


def build_album_slots_service_provider():
    return BuildAlbumSlotsDomainService()


BuildAlbumSlotsServiceProvider = Annotated[
    BuildAlbumSlotsDomainService, Depends(build_album_slots_service_provider)
]
