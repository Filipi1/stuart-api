from typing import Annotated

from fastapi import Depends

from modules.album.providers.get_album_by_user_service_provider import (
    GetAlbumByUserServiceProvider,
)
from modules.album.services.application.fetch_album_service import (
    FetchAlbumApplicationService,
)
from modules.user.providers import GetUserByTokenServiceProvider


def fetch_album_service_provider(
    get_user_by_token: GetUserByTokenServiceProvider,
    get_album_by_user: GetAlbumByUserServiceProvider,
):
    return FetchAlbumApplicationService(
        get_user_by_token=get_user_by_token,
        get_album_by_user=get_album_by_user,
    )


FetchAlbumServiceProvider = Annotated[
    FetchAlbumApplicationService, Depends(fetch_album_service_provider)
]
