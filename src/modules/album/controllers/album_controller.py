from http import HTTPMethod
from modules.album.dtos.fetch_album.fetch_album_request_dto import FetchAlbumRequestDto
from modules.shared.decorators import API
from modules.shared.adapters import APIController

from fastapi import Query

from containers import containers


@API.controller("album")
class AlbumController(APIController):
    def __init__(self):
        self.__fetch_album = containers.fetch_album

    @API.route("/", method=HTTPMethod.GET)
    async def get_album(
        self, token: str = Query(..., description="The token of the user"), 
        page: int = Query(1, description="The page number")
    ):
        return await self.__fetch_album.process(FetchAlbumRequestDto(token=token, page=page))
