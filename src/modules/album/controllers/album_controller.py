from http import HTTPMethod
from modules.album.dtos.fetch_album.fetch_album_request_dto import FetchAlbumRequestDto
from modules.shared.decorators import API
from modules.shared.adapters import APIController

from fastapi import Query

from modules.album.providers import FetchAlbumServiceProvider


@API.controller("album")
class AlbumController(APIController):
    @API.route("/", method=HTTPMethod.GET)
    async def get_album(
        self,
        fetch_album: FetchAlbumServiceProvider,
        token: str = Query(..., description="The token of the user"),
        page: int = Query(1, description="The page number"),
        items_per_page: int = Query(10, description="The number of items per page"),
    ):
        return await fetch_album.process(
            FetchAlbumRequestDto(token=token, page=page, items_per_page=items_per_page)
        )
