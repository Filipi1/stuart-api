from http import HTTPMethod
from typing import Optional

from fastapi import Header
from modules.meme.dtos.fetch_random_meme.fetch_random_meme_response_dto import (
    FetchRandomMemeResponseDto,
)
from modules.meme.dtos.create_meme.create_meme_request_dto import CreateMemeRequestDto
from modules.meme.dtos.create_meme.create_meme_response_dto import CreateMemeResponseDto
from modules.meme.providers import FetchRandomMemeProvider, CreateMemeProvider
from modules.shared.decorators import API
from modules.shared.adapters import APIController


@API.controller("meme")
class MemeController(APIController):
    @API.route("/", method=HTTPMethod.GET, response_model=FetchRandomMemeResponseDto)
    async def get_meme(
        self,
        fetch_random_meme: FetchRandomMemeProvider,
        x_request_token: Optional[str] = Header(
            None, description="The token of the user"
        ),
    ):
        return await fetch_random_meme.process()

    @API.route("/", method=HTTPMethod.POST, response_model=CreateMemeResponseDto)
    async def create_meme(
        self, request: CreateMemeRequestDto, create_meme: CreateMemeProvider
    ):
        return await create_meme.process(request)
