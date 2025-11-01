from typing import Annotated

from fastapi import Depends

from modules.album.providers.get_album_by_user_service_provider import (
    GetAlbumByUserServiceProvider,
)
from modules.album.services.application.fetch_album_service import (
    FetchAlbumApplicationService,
)
from modules.shared.providers import CacheServiceProvider
from modules.user.providers import GetUserByTokenServiceProvider


def fetch_album_service_provider(
    get_user_by_token: GetUserByTokenServiceProvider,
    get_album_by_user: GetAlbumByUserServiceProvider,
    cache: CacheServiceProvider,
):
    return FetchAlbumApplicationService(
        get_user_by_token=get_user_by_token,
        get_album_by_user=get_album_by_user,
        cache=cache,
    )


FetchAlbumServiceProvider = Annotated[
    FetchAlbumApplicationService, Depends(fetch_album_service_provider)
]
