from typing import Annotated

from fastapi import Depends

from modules.album.providers import BuildAlbumSlotsServiceProvider
from modules.album.services.application.fetch_album_service import (
    FetchAlbumApplicationService,
)
from modules.meme.providers import (
    GetEarnedMemesByUserServiceProvider,
    GetMemesPaginatedServiceProvider,
)
from modules.user.providers import GetUserByTokenServiceProvider


def fetch_album_service_provider(
    get_user_by_token: GetUserByTokenServiceProvider,
    get_earned_memes_by_user: GetEarnedMemesByUserServiceProvider,
    build_album_slots: BuildAlbumSlotsServiceProvider,
    get_memes_paginated: GetMemesPaginatedServiceProvider,
):
    return FetchAlbumApplicationService(
        get_user_by_token=get_user_by_token,
        get_earned_memes_by_user=get_earned_memes_by_user,
        build_album_slots=build_album_slots,
        get_memes_paginated=get_memes_paginated,
    )


FetchAlbumServiceProvider = Annotated[
    FetchAlbumApplicationService, Depends(fetch_album_service_provider)
]
