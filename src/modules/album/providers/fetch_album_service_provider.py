from modules.album.services.application.fetch_album_service import (
    FetchAlbumApplicationService,
)

from typing import Annotated
from fastapi import Depends

from modules.user.providers import GetUserByTokenServiceProvider
from modules.album.providers import BuildAlbumSlotsServiceProvider
from modules.meme.providers import (
    MemeRepositoryProvider,
    GetEarnedMemesByUserServiceProvider,
)


def fetch_album_service_provider(
    get_user_by_token: GetUserByTokenServiceProvider,
    get_earned_memes_by_user: GetEarnedMemesByUserServiceProvider,
    build_album_slots: BuildAlbumSlotsServiceProvider,
    meme_repository: MemeRepositoryProvider,
):
    return FetchAlbumApplicationService(
        get_user_by_token=get_user_by_token,
        get_earned_memes_by_user=get_earned_memes_by_user,
        build_album_slots=build_album_slots,
        meme_repository=meme_repository,
    )


FetchAlbumServiceProvider = Annotated[
    FetchAlbumApplicationService, Depends(fetch_album_service_provider)
]
