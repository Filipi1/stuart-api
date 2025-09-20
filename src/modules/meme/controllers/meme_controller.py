from http import HTTPMethod
from typing import Optional

from fastapi import Header
from modules.meme.dtos.fetch_random_meme.fetch_random_meme_response_dto import (
    FetchRandomMemeResponseDto,
)
from modules.meme.dtos.create_meme.create_meme_request_dto import CreateMemeRequestDto
from modules.meme.dtos.create_meme.create_meme_response_dto import CreateMemeResponseDto
from modules.shared.decorators import API
from modules.shared.adapters import APIController

from containers import containers


@API.controller("meme")
class MemeController(APIController):
    def __init__(self):
        self.__fetch_random_meme = containers.fetch_random_meme
        self.__create_meme = containers.create_meme_application_service

    @API.route("/", method=HTTPMethod.GET, response_model=FetchRandomMemeResponseDto)
    async def get_meme(
        self,
        x_request_token: Optional[str] = Header(
            None, description="The token of the user"
        ),
    ):
        return await self.__fetch_random_meme.process()

    @API.route("/", method=HTTPMethod.POST, response_model=CreateMemeResponseDto)
    async def create_meme(self, request: CreateMemeRequestDto):
        return await self.__create_meme.process(request)
