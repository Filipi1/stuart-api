from typing import Annotated

from fastapi import Depends

from modules.album.providers import BuildAlbumSlotsServiceProvider
from modules.album.services.domain.get_album_by_user_service import (
    GetAlbumByUserDomainService,
)
from modules.meme.providers import (
    GetEarnedMemesByUserServiceProvider,
    GetMemesPaginatedServiceProvider,
)


def get_album_by_user_service_provider(
    get_earned_memes_by_user: GetEarnedMemesByUserServiceProvider,
    build_album_slots: BuildAlbumSlotsServiceProvider,
    get_memes_paginated: GetMemesPaginatedServiceProvider,
):
    return GetAlbumByUserDomainService(
        get_earned_memes_by_user=get_earned_memes_by_user,
        build_album_slots=build_album_slots,
        get_memes_paginated=get_memes_paginated,
    )


GetAlbumByUserServiceProvider = Annotated[
    GetAlbumByUserDomainService, Depends(get_album_by_user_service_provider)
]

